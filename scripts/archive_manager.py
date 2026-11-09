# -*- coding: utf-8 -*-
"""
계층형 브리핑 보존 및 자동 승격(Roll-up) 아카이브 매니저 (archive_manager.py)
- 1단계 (최근 7일): 12시간마다 생성된 브리핑 원본 전체를 그대로 보존 (최대 14회차, 6일 뒤에도 전체 열람 가능)
- 2단계 (7일 단위 합산): 7일이 경과해 걸러지는 에디션에서 중요 안건(CRITICAL / 시사점 전환·신규·강화)만 추출하여 7일 단위로 합산
- 3단계 (30일 단위 합산): 7일 단위 중요 브리핑 중에서 핵심 구조적 변화 안건만 다시 뽑아 30일 단위로 합산
- 4단계 (120일/1분기 합산): 30일 단위 브리핑들을 모아 120일(1분기) 최중요 브리핑으로 통합 보존
"""
import os
import json
import datetime


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def score_agenda_importance(ag):
    """안건의 보존·승격 우선순위 점수를 산출합니다."""
    score = 0
    imp = ag.get("importance", "CORE")
    if imp == "CRITICAL":
        score += 50
    elif imp == "HIGH":
        score += 30
    else:
        score += 15

    delta = ag.get("deltaStatus", "MAINTAINED")
    if delta == "CHALLENGED":     # 기존 시사점 약화/전환 (가장 중요한 변곡점)
        score += 35
    elif delta == "NEW":          # 신규 시사점 등장
        score += 30
    elif delta == "REINFORCED":   # 기존 시사점 강력 강화
        score += 20
    else:
        score += 5

    return score


def parse_edition_datetime(edition_id):
    """'YYYY-MM-DD_0800' 형식의 ID에서 datetime 객체를 반환합니다."""
    try:
        date_part, slot_part = edition_id.split("_")
        hour = int(slot_part[:2])
        dt = datetime.datetime.strptime(date_part, "%Y-%m-%d")
        return dt.replace(hour=hour, minute=0, second=0)
    except Exception:
        return datetime.datetime.now()


def seed_historical_editions_if_needed(base_dir, current_edition):
    """
    최초 구축 시에도 최근 7일간의 회차 전환 및 7일/30일/120일 계층형 합산 기능을
    즉시 확인하고 이어갈 수 있도록 기준 아카이브 구조를 초기화합니다.
    이후 12시간마다 새 에디션이 생성되면 실제 시간 경과에 따라 누적 및 자동 승격됩니다.
    """
    editions_dir = os.path.join(base_dir, "data", "editions")
    rollups_dir = os.path.join(base_dir, "data", "rollups")
    ensure_dir(editions_dir)
    ensure_dir(rollups_dir)

    # 현재 에디션 저장 확인
    cur_id = current_edition["editionId"]
    cur_path = os.path.join(editions_dir, f"{cur_id}.json")
    with open(cur_path, "w", encoding="utf-8") as f:
        json.dump(current_edition, f, ensure_ascii=False, indent=2)


def process_tiered_archives(base_dir, current_edition):
    """
    전체 에디션을 스캔하여:
    1) 최근 7일 이내(14회차) 원본 에디션 리스트 유지
    2) 7일 단위 중요 브리핑 합산 (weekly_7d.json)
    3) 30일 단위 최중요 브리핑 합산 (monthly_30d.json)
    4) 120일(1분기) 단위 최중요 브리핑 합산 (quarterly_120d.json)
    을 생성 및 갱신합니다.
    """
    editions_dir = os.path.join(base_dir, "data", "editions")
    rollups_dir = os.path.join(base_dir, "data", "rollups")
    ensure_dir(editions_dir)
    ensure_dir(rollups_dir)

    now = parse_edition_datetime(current_edition["editionId"])
    cutoff_7d = now - datetime.timedelta(days=7)

    # 저장된 모든 에디션 로드
    all_editions = []
    for fname in sorted(os.listdir(editions_dir), reverse=True):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(editions_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                ed = json.load(f)
                all_editions.append(ed)
        except Exception as e:
            print(f"[WARN] 에디션 로드 실패 ({fname}): {e}")

    # 1. 최근 7일치 원본 에디션 (그대로 보존하여 6일 뒤에도 열람 가능)
    recent_7d_editions = []
    older_editions = []
    for ed in all_editions:
        ed_dt = parse_edition_datetime(ed["editionId"])
        if ed_dt >= cutoff_7d and len(recent_7d_editions) < 14:
            recent_7d_editions.append(ed)
        else:
            older_editions.append(ed)

    # 기존 롤업 데이터 로드
    weekly_path = os.path.join(rollups_dir, "weekly_7d.json")
    monthly_path = os.path.join(rollups_dir, "monthly_30d.json")
    quarterly_path = os.path.join(rollups_dir, "quarterly_120d.json")

    def load_rollup(path, default_title, default_desc):
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "title": default_title,
            "description": default_desc,
            "updatedAt": now.strftime("%Y-%m-%d %H:%M:%S KST"),
            "agendas": []
        }

    weekly_rollup = load_rollup(
        weekly_path,
        "📌 7일 단위 최중요 브리핑 합산 (Weekly Core)",
        "7일마다 만료되는 일별 브리핑 중에서 중요도가 높은 핵심 안건(CRITICAL 및 시사점 전환·신규·강화)만 걸러내어 합산한 주간 핵심 아카이브입니다."
    )
    monthly_rollup = load_rollup(
        monthly_path,
        "🏆 30일 단위 최중요 브리핑 합산 (Monthly Core)",
        "7일 단위 중요 브리핑들 중에서도 시장의 구조적 방향성을 바꾼 최중요 안건만 다시 추려 합산한 30일 단위 핵심 아카이브입니다."
    )
    quarterly_rollup = load_rollup(
        quarterly_path,
        "🏛️ 120일(1분기) 단위 최중요 브리핑 합산 (Quarterly 120-Day Core)",
        "30일 단위 최중요 브리핑들을 모아 120일(1분기) 동안의 거시경제·반도체·금·비트코인·한국 부동산 대세 흐름을 집대성한 분기 아카이브입니다."
    )

    # 승격 헬퍼: 중복 안건(같은 제목 또는 ID)은 최신 시사점 상태로 병합·업데이트
    def merge_promoted_agendas(existing_list, candidate_agendas, min_score, max_items, tier_tag):
        by_key = {a["id"]: a for a in existing_list}
        for ag in candidate_agendas:
            sc = score_agenda_importance(ag)
            if sc >= min_score:
                promoted = dict(ag)
                promoted["importanceScore"] = sc
                promoted["archiveTier"] = tier_tag
                promoted["promotedAt"] = now.strftime("%Y-%m-%d")
                by_key[ag["id"]] = promoted

        merged = list(by_key.values())
        merged.sort(key=lambda x: x.get("importanceScore", score_agenda_importance(x)), reverse=True)
        return merged[:max_items]

    # 7일이 지난 에디션(older_editions) 및 현재 누적된 에디션에서 주간(7일) 핵심 안건 추출·합산
    # (7일 경과 에디션 파일은 주간 롤업에 중요 안건을 남긴 뒤 디스크 정리를 수행하여 무한 증식을 방지)
    source_for_weekly = []
    for ed in older_editions:
        for ag in ed.get("agendas", []):
            ag_copy = dict(ag)
            ag_copy["sourceEdition"] = ed.get("displayDate", "") + " " + ed.get("slotLabel", "")
            source_for_weekly.append(ag_copy)
        # 7일 경과 원본 파일 정리 (중요 안건은 이미 source_for_weekly에 추출됨)
        old_file = os.path.join(editions_dir, f"{ed['editionId']}.json")
        if os.path.exists(old_file):
            try:
                os.remove(old_file)
            except Exception:
                pass

    # 최근 7일 에디션에서도 핵심 안건을 실시간으로 주간/월간/분기 합산 뷰에 미리 반영하여 언제든 계층별 요약 열람 가능
    for ed in recent_7d_editions:
        for ag in ed.get("agendas", []):
            ag_copy = dict(ag)
            ag_copy["sourceEdition"] = ed.get("displayDate", "") + " " + ed.get("slotLabel", "")
            source_for_weekly.append(ag_copy)

    # 1) 7일 단위 중요 브리핑: 점수 50점 이상 (약 상위 14~16개 핵심 안건)
    weekly_rollup["agendas"] = merge_promoted_agendas(
        weekly_rollup.get("agendas", []),
        source_for_weekly,
        min_score=50,
        max_items=16,
        tier_tag="7일 주간 핵심"
    )
    weekly_rollup["updatedAt"] = now.strftime("%Y-%m-%d %H:%M:%S KST")

    # 2) 30일 단위 최중요 브리핑: 7일 단위 브리핑에 모인 안건 중 점수 70점 이상 (CRITICAL + 시사점 전환/신규/강화, 약 상위 10~12개)
    monthly_rollup["agendas"] = merge_promoted_agendas(
        monthly_rollup.get("agendas", []),
        weekly_rollup["agendas"],
        min_score=70,
        max_items=12,
        tier_tag="30일 월간 최중요"
    )
    monthly_rollup["updatedAt"] = now.strftime("%Y-%m-%d %H:%M:%S KST")

    # 3) 120일(1분기) 단위 최중요 브리핑: 30일 단위 브리핑들을 모아 최상위 구조적 변화 안건 보존 (점수 80점 이상 또는 월간 핵심 전체 통합)
    quarterly_rollup["agendas"] = merge_promoted_agendas(
        quarterly_rollup.get("agendas", []),
        monthly_rollup["agendas"],
        min_score=75,
        max_items=15,
        tier_tag="120일(1분기) 빅픽처"
    )
    quarterly_rollup["updatedAt"] = now.strftime("%Y-%m-%d %H:%M:%S KST")

    # 롤업 JSON 파일 저장
    with open(weekly_path, "w", encoding="utf-8") as f:
        json.dump(weekly_rollup, f, ensure_ascii=False, indent=2)
    with open(monthly_path, "w", encoding="utf-8") as f:
        json.dump(monthly_rollup, f, ensure_ascii=False, indent=2)
    with open(quarterly_path, "w", encoding="utf-8") as f:
        json.dump(quarterly_rollup, f, ensure_ascii=False, indent=2)

    return {
        "recent7dEditions": recent_7d_editions,
        "weeklyRollup": weekly_rollup,
        "monthlyRollup": monthly_rollup,
        "quarterlyRollup": quarterly_rollup,
    }

# -*- coding: utf-8 -*-
"""
노트북 부팅/깨어남 시 누락된 08:00 / 20:00 브리핑 자동 보충 실행기 (check_and_catchup.py)
- 08:00 또는 20:00에 노트북이 꺼져 있다가 나중에(예: 09:00, 10:30 등) 켜졌을 때,
  현재 시간대의 목표 에디션이 해당 정각 이후에 생성되었는지 확인하고 누락 시 즉시 생성합니다.
"""
import os
import sys
import json
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from generate_briefing import get_target_edition_slot, build_briefing_edition


def needs_catchup(now=None):
    if now is None:
        now = datetime.datetime.now()

    slot = get_target_edition_slot(now)
    edition_id = slot["editionId"]
    edition_file = os.path.join(BASE_DIR, "data", "editions", f"{edition_id}.json")

    if not os.path.exists(edition_file):
        return True, f"목표 에디션 파일({edition_id}.json)이 아직 존재하지 않음"

    # 파일이 존재하더라도, 해당 슬롯의 기준 정각(08:00 또는 20:00) 이전에 미리 만들어진 파일이라면
    # 정각 이후 데이터로 새로고침이 필요함
    try:
        date_str, slot_code = edition_id.split("_")
        slot_hour = int(slot_code[:2])
        slot_start_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").replace(
            hour=slot_hour, minute=0, second=0
        )

        # 현재 시각이 슬롯 정각 이후인데, 파일 내 generatedAt이 슬롯 정각 이전이면 보충 실행 필요
        if now >= slot_start_dt:
            with open(edition_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            gen_str = data.get("generatedAt", "")[:19]
            if gen_str:
                gen_dt = datetime.datetime.strptime(gen_str, "%Y-%m-%d %H:%M:%S")
                if gen_dt < slot_start_dt:
                    return True, f"에디션({edition_id})이 정각({slot_start_dt}) 이전에 생성됨 (생성시각: {gen_dt})"
    except Exception as e:
        return True, f"에디션 상태 확인 중 예외 발생: {e}"

    return False, f"현재 시간대 목표 에디션({edition_id})이 이미 최신 상태임"


if __name__ == "__main__":
    required, reason = needs_catchup()
    print(f"[CATCH-UP CHECK] {reason}")
    if required or "--force" in sys.argv:
        print("[CATCH-UP RUN] 누락된 브리핑 작업을 즉시 보충 실행합니다...")
        build_briefing_edition()
    else:
        print("[CATCH-UP SKIP] 추가 작업이 필요하지 않습니다.")

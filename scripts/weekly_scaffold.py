import os
import datetime
from pathlib import Path

# Weekly Scaffolding Script
# 매주 새로운 주간 리포트 파일을 템플릿으로부터 생성함.

BASE_DIR = Path(__file__).parent.parent
WEEKLY_DIR = BASE_DIR / "weekly"
TEMPLATE_FILE = BASE_DIR / "_templates" / "weekly.md"

def get_week_info():
    today = datetime.date.today()
    # 일요일 23:00에 실행된다고 가정하면, 다음 주는 내일(월요일)부터 시작
    # 하지만 보통 해당 주차 리포트를 미리 만들어두는 것이 좋음.
    # ISO 주차 계산
    isocal = today.isocalendar()
    year = isocal[0]
    week = isocal[1]
    
    # 해당 주 월요일/일요일 계산
    monday = today - datetime.timedelta(days=today.weekday())
    sunday = monday + datetime.timedelta(days=6)
    
    return {
        "year": str(year),
        "week": str(week).zfill(2),
        "start": monday.strftime("%Y-%m-%d"),
        "end": sunday.strftime("%Y-%m-%d"),
        "today": today.strftime("%Y-%m-%d")
    }

def get_inbox_items():
    inbox_file = BASE_DIR / "raw" / "inbox.md"
    if not inbox_file.exists():
        return ""
    
    content = inbox_file.read_text(encoding="utf-8")
    # "## 미분류 항목" 이후부터 "## 처리된 항목" 이전까지의 섹션 추출
    match = re.search(r"## 미분류 항목(.*?)(## 처리된 항목|---|_마지막 Dream Cycle|_generated)", content, re.DOTALL | re.IGNORECASE)
    if not match:
        return ""
    
    inbox_text = match.group(1).strip()
    if not inbox_text or "새 항목 추가 형식" in inbox_text:
        return ""
    
    # 각 항목을 [ ] 형식의 리스트로 변환 (날짜/태그 기반 헤더 추출)
    items = re.findall(r"### (.*?)\n(.*?)(?=###|---|$)", inbox_text, re.DOTALL)
    formatted_items = []
    for header, body in items:
        clean_body = body.strip().replace("\n", " ")[:100] # 너무 길면 생략
        formatted_items.append(f"- [ ] **{header}**: {clean_body}...")
        
    return "\n".join(formatted_items)

def scaffold():
    if not TEMPLATE_FILE.exists():
        print(f"Template not found: {TEMPLATE_FILE}")
        return
    
    info = get_week_info()
    file_name = f"{info['year']}-W{info['week']}.md"
    target_path = WEEKLY_DIR / file_name
    
    if target_path.exists():
        print(f"File already exists: {target_path}")
        return
    
    template_content = TEMPLATE_FILE.read_text(encoding="utf-8")
    inbox_list = get_inbox_items()
    
    # 치환
    content = template_content.replace("{{YEAR}}", info['year'])
    content = content.replace("{{WEEK}}", info['week'])
    content = content.replace("{{START_DATE}}", info['start'])
    content = content.replace("{{END_DATE}}", info['end'])
    content = content.replace("{{TODAY}}", info['today'])
    
    # 이번 주 핵심 활동 섹션에 inbox 아이템 삽입 (템플릿에 {{INBOX_ITEMS}} 플레이스홀더가 있다고 가정하거나 특정 위치에 삽입)
    if inbox_list:
        content = content.replace("- [ ] \n- [ ]", "- [ ] (Inboxed Items)\n" + inbox_list)
    
    WEEKLY_DIR.mkdir(exist_ok=True)
    target_path.write_text(content, encoding="utf-8")
    print(f"Created weekly report: {target_path}")

if __name__ == "__main__":
    import re
    scaffold()

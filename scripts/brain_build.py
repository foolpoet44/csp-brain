import os
import glob
import json
from datetime import datetime

# CSP Brain Build System - v1.0
# 지식 베이스의 무결성을 점검하고 인덱스(CONVERSATION_MAP.md)를 최신화합니다.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
CONV_DIR = os.path.join(BASE_DIR, "raw", "archive", "conversations").replace('\\', '/')
MAP_FILE = os.path.join(BASE_DIR, "raw", "archive", "CONVERSATION_MAP.md").replace('\\', '/')

def build_index():
    print("Building Knowledge Index...")
    all_conversations = []
    
    # 모든 샤딩된 JSON 파일 검색
    json_files = glob.glob(os.path.join(CONV_DIR, "**", "*.json"), recursive=True)
    
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
                # 데이터가 리스트일 수도 있고 단일 객체일 수도 있음
                if isinstance(data, list):
                    for item in data:
                        extract_meta(item, file_path, all_conversations)
                else:
                    extract_meta(data, file_path, all_conversations)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # 최신순 정렬 (updated_at 또는 created_at 기준)
    all_conversations.sort(key=lambda x: x.get('date', ''), reverse=True)

    # 인덱스 파일 작성
    with open(MAP_FILE, 'w', encoding='utf-8-sig') as f:
        f.write("# Conversation Knowledge Map Index\n\n")
        f.write("> 이 지표는 114MB의 과거 데이터를 분할하여 관리하는 마스터 인덱스입니다.\n")
        f.write("> **최신순**으로 정렬되어 있으며, 에이전트가 필요한 시점에 특정 파일만 읽어 지식을 복원합니다.\n\n")
        f.write("| 날짜 | 제목 | UUID | 경로 |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        
        for conv in all_conversations:
            # 절대 경로를 상대 경로로 변환 (CI 환경 호환성)
            conv_path = conv['path'].replace('\\', '/')
            try:
                # 윈도우에서 드라이브가 다른 경우 os.path.relpath가 ValueError를 일으킴
                rel_path = os.path.relpath(conv_path, BASE_DIR).replace('\\', '/')
            except ValueError:
                # 드라이브가 다르면 절대 경로 유지 (file:/// 형식 권장)
                rel_path = f"file:///{conv_path}" if conv_path.startswith('/') or ':' in conv_path else conv_path
            
            # 마크다운 상대 경로 링크 작성
            f.write(f"| {conv['date']} | {conv['title']} | `{conv['id']}` | [{conv['id']}]({rel_path}) |\n")

    print(f"Successfully indexed {len(all_conversations)} conversations.")

def extract_meta(item, path, target_list):
    # Sharding 방식에 따라 메타데이터 추출 방식이 다를 수 있음
    conv_id = item.get('id', 'unknown')
    title = item.get('title', 'No Title').replace('|', 'ㅣ') # 테이블 깨짐 방지
    created_at = item.get('created_at', '')
    date = created_at[:10] if created_at else 'unknown'
    
    target_list.append({
        'id': conv_id,
        'title': title,
        'date': date,
        'path': path
    })

def check_integrity():
    print("Checking knowledge integrity...")
    # 주요 폴더 존재 확인
    essential_dirs = ["projects", "people", "concepts", "raw/archive"]
    for d in essential_dirs:
        full_path = os.path.join(BASE_DIR, d)
        if not os.path.exists(full_path):
            print(f"Warning: Essential directory missing: {d}")
    
    # Inbox 체크
    inbox_path = os.path.join(BASE_DIR, "raw", "inbox.md")
    if os.path.exists(inbox_path):
        size = os.path.getsize(inbox_path)
        if size > 1024 * 50: # 50KB 이상이면 정리 필요 알림
            print(f"Tip: raw/inbox.md size is {size} bytes. Consider a Dream Cycle to clean it up.")

def sync_zavis_brain():
    print("Syncing Zavis Brain Knowledge...")
    script_path = os.path.join(BASE_DIR, "scripts", "build_knowledge_json.py")
    if os.path.exists(script_path):
        import subprocess
        try:
            subprocess.run(["python", script_path], check=True)
        except Exception as e:
            print(f"Error during Zavis Brain sync: {e}")
    else:
        print("Warning: build_knowledge_json.py not found.")

if __name__ == "__main__":
    check_integrity()
    build_index()
    sync_zavis_brain()

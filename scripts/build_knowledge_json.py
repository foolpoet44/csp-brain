import json
import os
import re
import glob
from datetime import datetime

# 설정
SOURCE_MANIFEST = r"D:\2026\4월\markit\Zavis_Brain\manifest.json"
SOURCE_DIR = r"D:\2026\4월\markit\Zavis_Brain"
TARGET_JSON = r"d:\2026\4월\MYKM_1\projects\llm-knowledge-base\data\zavis_knowledge_summary.json"
SUMMARY_LIMIT = 1000

def get_summary(md_path):
    """마크다운 파일에서 요약 내용을 추출합니다."""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # YAML Frontmatter 제거
            content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL)
            # 불필요한 공백 제거
            content = content.strip()
            # 1000자 요약
            return content[:SUMMARY_LIMIT] + "..." if len(content) > SUMMARY_LIMIT else content
    except Exception as e:
        print(f"Error reading {md_path}: {e}")
        return None

def build_knowledge():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting Knowledge Sync...")
    
    if not os.path.exists(SOURCE_MANIFEST):
        print(f"Error: Manifest not found at {SOURCE_MANIFEST}")
        return

    # 기존 데이터 로드 (증분 업데이트용)
    existing_data = {}
    if os.path.exists(TARGET_JSON):
        try:
            with open(TARGET_JSON, 'r', encoding='utf-8') as f:
                old_list = json.load(f)
                existing_data = {item['id']: item for item in old_list if 'id' in item}
            print(f"Loaded {len(existing_data)} existing entries for incremental update.")
        except Exception as e:
            print(f"Warning: Could not load existing JSON: {e}")

    with open(SOURCE_MANIFEST, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 모든 .md 파일 인덱싱
    print("Indexing available markdown files...")
    all_md_files = glob.glob(os.path.join(SOURCE_DIR, "**", "*.md"), recursive=True)
    md_map = {os.path.basename(p).lower(): p for p in all_md_files}

    knowledge_base = []
    found_count = 0
    skipped_count = 0
    
    for original_path, meta in manifest.items():
        original_filename = os.path.basename(original_path)
        item_hash = meta.get('hash', 'unknown')
        
        # 증분 업데이트 체크: 해시가 같으면 기존 데이터 재사용
        if item_hash in existing_data:
            knowledge_base.append(existing_data[item_hash])
            skipped_count += 1
            continue

        # 시도 1: 원본 파일명 + .md
        target_name = f"{original_filename}.md".lower()
        md_path = md_map.get(target_name)
        
        # 시도 2: 확장자 제외한 파일명 + .md
        if not md_path:
            name_without_ext = os.path.splitext(original_filename)[0]
            target_name_legacy = f"{name_without_ext}.md".lower()
            md_path = md_map.get(target_name_legacy)

        if md_path and os.path.exists(md_path):
            summary = get_summary(md_path)
            if summary:
                entry = {
                    "id": item_hash,
                    "title": original_filename,
                    "category": meta.get('category', 'Uncategorized'),
                    "tags": meta.get('tags', []),
                    "summary": summary,
                    "original_path": original_path,
                    "last_updated": meta.get('converted_at', datetime.now().isoformat())
                }
                knowledge_base.append(entry)
                found_count += 1
        else:
            pass

    # 결과 저장
    os.makedirs(os.path.dirname(TARGET_JSON), exist_ok=True)
    with open(TARGET_JSON, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, indent=2, ensure_ascii=False)

    print(f"Sync Complete: {len(knowledge_base)} total, {found_count} new/updated, {skipped_count} skipped.")

if __name__ == "__main__":
    build_knowledge()

import os
import re
import sys
from pathlib import Path

# CSP Brain Validation Script
# 원칙: 모든 프로젝트/개념 파일은 'Compiled Truth'와 'Timeline' 섹션을 포함해야 함.

BASE_DIR = Path(__file__).parent.parent
PROJECTS_DIR = BASE_DIR / "projects"
CONCEPTS_DIR = BASE_DIR / "concepts"
PEOPLE_DIR = BASE_DIR / "people"
CLAUDE_MD = BASE_DIR / "CLAUDE.md"

def check_file_structure(file_path):
    """파일 내 필수 섹션 존재 여부 확인"""
    content = file_path.read_text(encoding="utf-8")
    
    # 필수 섹션 체크 (대소문자 구분 없이)
    has_truth = re.search(r"##.*(Compiled Truth|핵심 개념|아키텍처)", content, re.IGNORECASE)
    has_timeline = re.search(r"##.*Timeline", content, re.IGNORECASE)
    
    issues = []
    if not has_truth:
        issues.append("Missing 'Compiled Truth' section")
    if not has_timeline:
        issues.append("Missing 'Timeline' section")
        
    return issues

def validate_links(file_path):
    """깨진 내부 링크 확인"""
    content = file_path.read_text(encoding="utf-8")
    # [link text](file:///...) 또는 [[Link]] 형식의 링크 추출 (여기서는 file:/// 패턴 위주)
    file_links = re.findall(r"file:///([^)\s]+)", content)
    
    is_ci = os.environ.get("GITHUB_ACTIONS") == "true"
    issues = []
    for link in file_links:
        # URL 디코딩 및 OS 경로 변환
        from urllib.parse import unquote
        link_path_str = unquote(link)
        
        # 윈도우 경로 처리 (d:/... 및 /d:/... 대응)
        clean_path = re.sub(r'^/([a-zA-Z]:)', r'\1', link_path_str)
        potential_path = Path(clean_path)

        # 1. 파일 시스템에 직접 존재하는가? (로컬 환경)
        if potential_path.exists():
            continue
            
        # 2. 레포지토리 루트 기준 상대 경로인가?
        repo_relative = BASE_DIR / clean_path
        if repo_relative.exists():
            continue
            
        # 3. 예외 조건 (CI 환경에서 외부 드라이브 링크 건너뛰기)
        # 윈도우가 아니거나 CI 환경이면 모든 알파벳 드라이브 문자로 시작하는 경로는 무시
        if (sys.platform != "win32" or is_ci) and re.match(r'^[a-zA-Z]:', clean_path):
            continue

        # 4. 경로 구분자 혼용 처리 (리눅스에서 \ 가 포함된 경우 / 로 치환하여 재검사)
        if (sys.platform != "win32" or is_ci) and "\\" in clean_path:
            alt_path = BASE_DIR / clean_path.replace("\\", "/")
            if alt_path.exists():
                continue

        issues.append(f"Broken link: {link_path_str}")
                
    return issues

def main():
    errors_found = False
    
    # 1. 문서 파일 스캔
    target_dirs = [PROJECTS_DIR, CONCEPTS_DIR, PEOPLE_DIR]
    for directory in target_dirs:
        if not directory.exists():
            continue
            
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".md") and file.lower() != "readme.md":
                    file_path = Path(root) / file
                    
                    # 구조 체크
                    # extracted-*.md 파일은 파편화된 조각이므로 구조 검증 제외
                    is_extracted = file.startswith("extracted-")
                    
                    if not is_extracted:
                        struct_issues = check_file_structure(file_path)
                        if struct_issues:
                            print(f"[STRUCT] {file_path.relative_to(BASE_DIR)}: {', '.join(struct_issues)}")
                            errors_found = True
                    
                    # 링크 체크
                    # extracted-*.md 파일의 링크 오류는 경고만 출력하고 빌드 실패로 간주하지 않음
                    link_issues = validate_links(file_path)
                    if link_issues:
                        for issue in link_issues:
                            level = "[WARN]" if is_extracted else "[LINK]"
                            print(f"{level} {file_path.relative_to(BASE_DIR)}: {issue}")
                        
                        if not is_extracted:
                            errors_found = True

    # 2. CLAUDE.md 프로젝트 테이블 검증
    if CLAUDE_MD.exists():
        content = CLAUDE_MD.read_text(encoding="utf-8")
        # 프로젝트 경로 패턴 추출: `projects/name/`
        project_paths = re.findall(r"`projects/([^/`]+)/?`", content)
        for p in project_paths:
            p_path = PROJECTS_DIR / p
            if not p_path.exists():
                print(f"[SYNC] CLAUDE.md references non-existent project: projects/{p}")
                errors_found = True

    if errors_found:
        print("\nValidation FAILED.")
        sys.exit(1)
    else:
        print("Validation PASSED.")
        sys.exit(0)

if __name__ == "__main__":
    main()

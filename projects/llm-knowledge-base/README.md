# Project: LLM Knowledge Base

> 조직 내 흩어진 지식 자산(Zavis Brain)을 LLM이 즉각적으로 활용할 수 있도록 구조화된 형태로 관리하는 프로젝트입니다.

---

## Compiled Truth

### 📋 Overview
- **Status**: Active (Syncing)
- **Primary Source**: `D:\2026\4월\markit\Zavis_Brain\`
- **Integrated Data**: [zavis_knowledge_summary.json](data/zavis_knowledge_summary.json)
- **Sync Method**: Dream Cycle (`scripts/brain_build.py`) 호출 시 자동 동기화 (증분 업데이트 지원)

### 🧠 Knowledge Structure
현재 약 250여 개의 고침투성 지식 자산이 다음과 같은 형태로 통합되어 있습니다:
- **Metadata**: 원본 경로, 카테고리, 태그, 해시, 업데이트 일시
- **Summary**: 문서의 핵심 내용 (상위 1000자 내외)

### 🛠 Tech Stack
- Python (Sync Script)
- JSON (Knowledge Store)

---

## Timeline

### 2026-04-14
- **[Feature]** `scripts/build_knowledge_json.py` 구현 및 드림 사이클 연동 완료.
- **[Data]** Zavis Brain으로부터 251개의 지식 엔트리 초기 동기화 완료.
- **[Guide]** 에이전트 지식 소스 활용 가이드 작성.

---

## How to used by Agent
에이전트(사용자 포함)는 `data/zavis_knowledge_summary.json` 파일을 읽어 특정 주제(예: AX, HR, 리더십)에 대한 핵심 내용을 검색하거나, 원본 마크다운 파일의 경로를 파악하여 더 상세한 분석을 수행할 수 있습니다.

**Prompt 예시**:
> "`data/zavis_knowledge_summary.json`에서 'AX 역량' 관련 항목을 찾아 핵심 내용을 브리핑해줘."

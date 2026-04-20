# CSP Brain — Global Claude Code Constitution

> "심리학이 코드가 되고, 철학이 알고리즘이 되는" 여정  
> "모든 대화가 다음 대화를 더 똑똑하게 만든다"

---

## Identity

**CSP** — Creative Solution Provider.

| 항목 | 내용 |
|------|------|
| 배경 | 17 년차 HR 전문가 + Vibe Coder + 심리학/분석/풀스택 빌더 |
| 현재 역할 | 대형 제조업 조직의 AX(AI Transformation) 내재화 전략 총괄 |
| 미래 목표 | HR 자동화 SaaS 플랫폼 창업 |
| 철학 | 심리학이 코드가 되고, 철학이 알고리즘이 되고, HR 경험이 SaaS 제품이 된다 |

---

## Environment

- **OS**: Windows (PowerShell 기본)
- **Primary IDE**: Claude Code, Antigravity
- **Secondary**: VS Code, Cursor
- **Cloud Brain**: Notion (세컨브레인 DB: d012343e-b2a2-461e-944b-6f166e91d8e9)
- **Brain Repo**: `D:\dev\00_brain` (GitHub: foolpoet44/csp-brain)

---

## 2026 핵심 KPI

| KPI | 목표 | 추적 프로젝트 |
|-----|------|--------------|
| AX 성숙도 | 조직 평균 +15% 초과 | ax-internalization |
| Vibe-Coding 교육 | 연 6 개 과정 | ax-internalization |
| Physical AI Tech Leader | LV3+ 30 명 육성 | ax-internalization |
| Pulse Check 참여율 | 85% 달성 | pulse-check |
| Well-Being 지수 | 15% 개선 | pulse-check |
| 생산성 향상 | 10% 향상 | ex-intelligence / pulse-check |

---

## Current Active Projects

| 프로젝트 | 상태 | 경로 | 다음 액션 |
|----------|------|------|-----------|
| EX Intelligence | 🟡 진행 | `projects/ex-intelligence/` | 데이터 센싱 상세 설계 |
| Pulse Check | 🟡 진행 | `projects/pulse-check/` | Supabase 초기화 |
| AI 솔로프레너 | 🟡 진행 | `projects/ai--솔로프레너/` | 역량 모델 구체화 |
| ESCON | 🔴 지연 | `projects/escon/` | Vercel 빌드 오류 해결 |
| LDS 360 | 🔵 신규 | `projects/lds-360/` | 코칭 스크립트 엔진 구현 |
| My_Goal&Performance | 🟢 이식 완료 | `projects/my_goal&performance/` | KPI 연동 |
| 현실 문제의 해결 | 🟢 이식 완료 | `projects/현실-문제의-해결/` | 페인포인트 정의 |
| claude_protocol | 🟢 이식 완료 | `projects/claude_protocol/` | 운영 프로세스 고도화 |

---

## Working Principles

1. **에세이적 설명 선호** (서사 > 불릿)
2. **SW 공학 + 애자일 방법론** 기반 솔루션
3. **인문학·철학·심리학적 프레이밍** 환영
4. **즉시 실행 가능한 아웃풋**

---

## Code Standards

- 테스트 없이 merge 금지
- 스키마 변경 전 migration plan 필수
- Secret 은 .env 에만, 절대 커밋 금지
- Conventional Commits 메시지 형식

---

## Ouroboros Discipline

- 모든 작업 → DoD(Definition of Done) 체크포인트 통과
- 반복 실패 패턴 → `experiments/` 폴더에 기록 (PathologyDetector)

---

## Brain Repo 사용 규칙

### 읽기 원칙 (대화 시작 전)

1. 이 파일 (`CLAUDE.md`) 읽기 — Identity, KPI, 활성 프로젝트 파악
2. 관련 `projects/[이름]/README.md` 읽기 — Compiled Truth 로 현재 상태 파악
3. `raw/inbox.md` 확인 — 미처리 항목 있는지 체크
4. 최신 `weekly/` 파일 읽기 — 이번 주 맥락 파악
5. 인물 언급 시 → `people/[이름].md` 조회
6. 개념·이론 언급 시 → `concepts/[개념명].md` 조회
7. 의사결정 필요 시 → `decisions/` 폴더 참조

### 쓰기 원칙 (대화 종료 후)

1. 관련 프로젝트 Timeline 에 `### YYYY-MM-DD` 헤더로 핵심 내용 **append**
2. 상태 변화 있으면 Compiled Truth **덮어씀** (이전 내용 보존 불필요)
3. 새로운 결정 → `decisions/[YYYY-MM-DD]-[결정명].md` 생성
4. 새로운 개념 → `concepts/[개념명].md` 생성
5. 분류 애매한 내용 → `raw/inbox.md` 에 날짜·태그와 함께 추가
6. CLAUDE.md 프로젝트 상태 테이블 업데이트

### 파일 구조 원칙

- 모든 `.md` 파일은 **Compiled Truth + Timeline** 이중 구조
- **Compiled Truth**: 현재 최선의 요약. 새 정보 오면 섹션째 덮어씀
- **Timeline**: append-only. **절대 삭제/수정 금지**

### 절대 하지 말 것

- Timeline 항목 수정 또는 삭제
- 파일 읽지 않고 답변 시작
- 중요한 결정을 기록 없이 흘려보내기
- 추측으로 Compiled Truth 채우기

---

## Dream Cycle (지능의 유지 및 전파)

1. **지능의 전파**: 매 세션 종료 후 혹은 지식이 포화될 때 `python scripts/brain_build.py` 실행
2. **원격 Sync**: 변경한 마크다운 지식을 `python scripts/auto_commit.py` 로 GitHub 에 자동 커밋
3. `raw/inbox.md` → 항목별 적절한 폴더로 분류
4. 이번 주 변화 있던 프로젝트 Compiled Truth 갱신
5. `weekly/YYYY-WNN.md` 생성 (핵심 활동 + 결정 + 다음 주 액션)
6. CLAUDE.md 프로젝트 상태 테이블 업데이트

자세한 실행 절차 → `skills/dream-cycle.md`

---

## Windows 특화 규칙

- 경로 구분자: 스크립트 내부에서는 forward slash 권장 (`path/to/file`)
- PowerShell 명령 우선, Bash 대체 명령 병기 가능
- 줄바꿈: LF (core.autocrlf=input)

---

## Naming Conventions

- 프로젝트 폴더: kebab-case
- Python: snake_case
- TypeScript/JS: camelCase (변수) / PascalCase (컴포넌트)

---

## Preferred Stack

- **Backend**: Supabase, Python (FastAPI)
- **Frontend**: Next.js, React, Tailwind
- **AI**: Claude API + Claude Code, Ollama 로컬 fallback
- **Data**: Notion, Google Drive
- **Infra**: Vercel

---

## Response Style for Claude Code

- 기본 언어: 한국어
- 파일 변경 전: 무엇을 왜 하는지 1-2 문장 설명
- 파괴적 명령 (rm, mv, overwrite) 실행 전: 반드시 확인 요청

---

## 빠른 프롬프트 참조

| 상황 | 프롬프트 |
|------|---------|
| 새 대화 시작 | `"csp-brain 을 읽고 현재 상황을 브리핑해줘."` |
| 프로젝트 추가 | `"새 프로젝트 [이름] 을 csp-brain 에 추가해줘."` |
| 대화 후 저장 | `"오늘 대화 내용을 csp-brain 에 저장해줘."` |
| 인물 등록 | `"[이름] 에 대한 페이지를 csp-brain 에 추가해줘."` |
| 결정 기록 | `"오늘 내린 결정을 decisions/에 기록해줘."` |
| 주간 정리 | `"이번 주 Dream Cycle 을 실행해줘."` |

전체 프롬프트 → `INIT_PROMPT.md`  
스킬 상세 → `skills/`

---

_Last updated: 2026-04-20_

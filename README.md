# 🧠 CSP Brain — Global Claude Code Hub

> "심리학이 코드가 되고, 철학이 알고리즘이 되는" 여정  
> "모든 대화가 다음 대화를 더 똑똑하게 만든다"

CSP 의 글로벌 Claude Code 설정 허브이자 AI 에이전트 메모리 레포지토리입니다.  
**4-Zone 로컬 아키텍처의 Zone 00(영원 지대)**로, 모든 프로젝트가 상속하는 전역 헌법과 지식을 관리합니다.

---

## 📁 4-Zone 로컬 아키텍처

```
~/
├── 00_brain/           # 🧠 영원 지대 — 지식과 도구의 원천 (이 레포지토리)
├── 10_work/            # 💼 업무 지대 — 회사 프로젝트 (EX Intelligence, Pulse Check...)
├── 20_build/           # 🛠️ 빌드 지대 — 개인/창업 프로젝트 (ESCON, HR SaaS...)
├── 30_lab/             # 🧪 실험 지대 — 휘발성 스크래치 (30 일 규칙)
└── 99_archive/         # 📦 아카이브 — 완료되거나 중단된 것들
```

### Zone 별 책임

| Zone | 수명 | Git 계정 | 예시 |
|------|------|----------|------|
| **00_brain** | 영구 | 개인 | 전역 헌법, 스킬, 프롬프트 |
| **10_work** | 프로젝트 기간 | 회사 | EX Intelligence, Pulse Check |
| **20_build** | 영구 (창업 준비) | 개인 | ESCON, CSP-OS |
| **30_lab** | 30 일 휘발 | 혼용 | 5 분 실험, 프로토타입 |
| **99_archive** | 영구 (참조용) | 보존 | 완료된 프로젝트 |

---

## 📂 00_brain 폴더 구조

```
00_brain/
├── CLAUDE.md                   # 🧭 전역 헌법 — 모든 프로젝트가 상속
├── README.md                   # 이 파일
├── MANUAL.md                   # 상세 사용 매뉴얼
├── INIT_PROMPT.md              # 초기 구현 프롬프트 모음
├── LICENSE.md                  # 라이선스
├── .gitignore                  # Git 제외 패턴
│
├── .claude/                    # Claude Code 설정 (Junction 으로 연결)
│   ├── agents/                 # AI Agent 정의
│   ├── commands/               # 사용자 정의 명령
│   ├── skills/                 # 재사용 가능한 스킬
│   └── settings.json           # 권한 설정
│
├── knowledge/                  # 지식 저장소 (Zettelkasten)
│   ├── moc/                    # Map of Content (지식 인덱스)
│   ├── permanent/              # 영구 지식
│   ├── references/             # 참고 자료
│   ├── concepts/               # 개념·이론 (Compiled Truth + Timeline)
│   ├── people/                 # 인물 지식
│   ├── decisions/              # 의사결정 로그
│   ├── weekly/                 # 주간 컨텍스트 (Dream Cycle 결과물)
│   ├── raw/
│   │   └── inbox.md            # 미분류 수신함
│   └── skills/                 # 에이전트 스킬 문서
│
├── prompts/                    # 프롬프트 라이브러리
│   ├── patterns/               # 검증된 프롬프트 패턴
│   └── snippets/               # 재사용 블록
├── dotfiles/                   # 설정 파일 템플릿 (.zshrc, .gitconfig...)
├── scripts/                    # 자동화 스크립트
│   ├── brain_build.py          # 지식 맵 빌드
│   ├── auto_commit.py          # GitHub 자동 커밋
│   ├── validate_brain.py       # 무결성 검증
│   └── weekly_scaffold.py      # 주간 스캐폴드
└── _templates/                 # 재사용 템플릿 (10_work 용)
    ├── project.md
    ├── person.md
    ├── concept.md
    └── decision.md
```

---

## 🚀 빠른 시작

### 1. 사전 요구사항

- **OS**: Windows 10/11
- **Git**: [GitHub Desktop](https://desktop.github.com/) 또는 [Git for Windows](https://gitforwindows.org/)
- **Claude Code**: `npm install -g @anthropic-ai/claude-code`
- **Python 3.8+**: 스크립트 실행용 (선택)

### 2. 설치 (Windows)

```powershell
# 1. 레포지토리 클론
cd C:\dev
git clone https://github.com/foolpoet44/csp-brain.git 00_brain

# 2. Junction 생성 (관리자 권한 불필요)
cmd /c mklink /J "%USERPROFILE%\.claude" "C:\dev\00_brain\.claude"

# 또는 PowerShell 5.0+
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude" -Target "C:\dev\00_brain\.claude"
```

### 3. 검증

```powershell
# Junction 확인
Get-Item "$env:USERPROFILE\.claude" | Select-Object Name, Target, LinkType

# Claude Code 재시작 후 테스트
claude
# "CLAUDE.md 의 내용을 요약해줘" 라고 입력
```

---

## 🔧 핵심 패턴

### Compiled Truth + Timeline

모든 지식 파일 (`knowledge/concepts/*.md`, `10_work/*/CLAUDE.md`) 은 이 구조를 따릅니다.

```markdown
## Compiled Truth
현재 알고 있는 최선의 요약. 새 정보 오면 이 섹션만 덮어씀.

---

## Timeline
append-only 증거 기록. 절대 삭제/수정 금지.

### YYYY-MM-DD
- 오늘 배운 것, 결정한 것, 변화한 것
```

### 프로젝트 CLAUDE.md 상속

모든 프로젝트의 `CLAUDE.md` 맨 위에는 다음을 명시합니다:

```markdown
> 이 프로젝트는 `~/00_brain/CLAUDE.md` 의 모든 원칙을 상속한다.
> 아래는 이 프로젝트 고유의 컨텍스트만 기술한다.
```

---

## 🔄 운영 주기

| 주기 | 작업 | 설명 |
|------|------|------|
| **매 대화** | 시작 전 읽기 → 종료 후 Timeline append | 컨텍스트 유지 |
| **매주 금요일** | Dream Cycle | inbox 정리 + Compiled Truth 갱신 + weekly 생성 |
| **월 1 회** | 스크립트 실행 | `python scripts/brain_build.py`로 지식 맵 최신화 |
| **매월 말** | 30_lab 정리 | 30 일 규칙에 따라 승격/이동/아카이브 |

---

## 📚 주요 기능

| 기능 | 설명 |
|------|------|
| **전역 헌법** | `CLAUDE.md` 에 정의된 Identity, 원칙이 모든 프로젝트에 적용됨 |
| **Junction 링크** | `%USERPROFILE%\.claude` 가 `00_brain\.claude` 를 가리켜 설정 동기화 |
| **Compiled Truth + Timeline** | 빠른 복원과 기록 보존을 동시에 |
| **Dream Cycle** | 주간 정리 루틴으로 지식 정제 |
| **자동화 스크립트** | GitHub 자동 커밋, 지식 맵 빌드, 무결성 검증 |
| **4-Zone 아키텍처** | 영구/업무/빌드/실험 분리로 IP 분쟁 방지 |

---

## ⚡ 빠른 시작 프롬프트

| 상황 | 프롬프트 |
|------|---------|
| 새 대화 시작 | `"csp-brain 을 읽고 현재 상황을 브리핑해줘."` |
| 프로젝트 추가 | `"새 프로젝트 [이름] 을 10_work/에 추가해줘."` |
| 대화 후 저장 | `"오늘 대화 내용을 csp-brain 에 저장해줘."` |
| 인물 등록 | `"[이름] 에 대한 페이지를 knowledge/people/에 추가해줘."` |
| 결정 기록 | `"오늘 내린 결정을 knowledge/decisions/에 기록해줘."` |
| 주간 정리 | `"이번 주 Dream Cycle 을 실행해줘."` |
| 실험 시작 | `"30_lab/에 새 실험 폴더를 생성해줘."` |

자세한 프롬프트는 [INIT_PROMPT.md](./INIT_PROMPT.md) 를 참고하세요.

---

## 📄 라이선스

MIT

---

**Maintained by** CSP (Creative Solution Provider)  
**GitHub** [@foolpoet44](https://github.com/foolpoet44)

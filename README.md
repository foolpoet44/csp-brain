# 🧠 CSP Brain — Global Claude Code Hub

> "심리학이 코드가 되고, 철학이 알고리즘이 되는" 여정  
> "모든 대화가 다음 대화를 더 똑똑하게 만든다"

CSP 의 글로벌 Claude Code 설정 허브이자 AI 에이전트 메모리 레포지토리입니다.  
gbrain(Garry Tan) 패턴을 CSP 워크플로우에 맞게 구현하였으며, 어느 프로젝트에서 `claude` 를 실행하든 일관된 설정과 지식 컨텍스트가 적용됩니다.

---

## 📁 폴더 구조

```
00_brain/
├── CLAUDE.md                   # 전역 헌법 + 에이전트 진입점 (Identity, KPI, 규칙)
├── README.md                   # 이 파일
├── MANUAL.md                   # 상세 사용 매뉴얼
├── INIT_PROMPT.md              # 초기 구현 프롬프트 모음
├── LICENSE.md                  # 라이선스
├── .gitignore                  # Git 제외 패턴
│
├── .claude/                    # Claude Code 설정 (Junction 으로 연결됨)
│   ├── agents/                 # AI Agent 정의
│   ├── commands/               # 사용자 정의 명령
│   ├── skills/                 # 재사용 가능한 스킬
│   └── settings.json           # 권한 설정
│
├── projects/                   # 프로젝트별 컨텍스트 메모리
│   ├── ex-intelligence/        # EX 진단 플랫폼
│   ├── pulse-check/            # 조직 웰빙 체크
│   ├── escon/                  # ESCON 스킬 온톨로지
│   ├── ai--솔로프레너/         # AI 솔로프레너 역량모델
│   ├── lds-360/                # 리더십 코칭
│   └── ...
│
├── people/                     # 인물 지식
├── concepts/                   # 개념·이론 (Compiled Truth + Timeline)
├── decisions/                  # 의사결정 로그
├── weekly/                     # 주간 컨텍스트 (Dream Cycle 결과물)
├── raw/
│   └── inbox.md                # 미분류 수신함
├── skills/                     # 에이전트 스킬 문서
│   ├── context-restore.md
│   ├── dream-cycle.md
│   └── memory-save.md
├── _templates/                 # 재사용 템플릿
│   ├── project.md
│   ├── person.md
│   ├── concept.md
│   └── decision.md
├── scripts/                    # 자동화 스크립트
│   ├── brain_build.py          # 지식 맵 빌드
│   ├── auto_commit.py          # GitHub 자동 커밋
│   └── weekly_scaffold.py      # 주간 스캐폴드
├── prompts/                    # 프롬프트 라이브러리
├── dotfiles/                   # 설정 파일 템플릿
└── knowledge/                  # 지식 저장소 (Zettelkasten)
    ├── moc/
    ├── permanent/
    └── references/
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
cd C:\dev  # 또는 선호하는 경로
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

## 🔧 핵심 패턴: Compiled Truth + Timeline

CSP Brain 의 모든 지식 파일은 이 구조를 따릅니다.

```markdown
## Compiled Truth
현재 알고 있는 최선의 요약. 새 정보 오면 이 섹션만 덮어씀.

---

## Timeline
append-only 증거 기록. 절대 삭제/수정 금지.

### YYYY-MM-DD
- 오늘 배운 것, 결정한 것, 변화한 것
```

---

## 🔄 운영 주기

| 주기 | 작업 | 설명 |
|------|------|------|
| **매 대화** | 시작 전 읽기 → 종료 후 Timeline append | 컨텍스트 유지 |
| **매주 금요일** | Dream Cycle | inbox 정리 + Compiled Truth 갱신 + weekly 생성 |
| **월 1 회** | 스크립트 실행 | `python scripts/brain_build.py`로 지식 맵 최신화 |

---

## 📚 주요 기능

| 기능 | 설명 |
|------|------|
| **전역 헌법** | `CLAUDE.md` 에 정의된 Identity, 원칙이 모든 프로젝트에 적용됨 |
| **Junction 링크** | `%USERPROFILE%\.claude` 가 `00_brain\.claude` 를 가리켜 설정 동기화 |
| **Compiled Truth + Timeline** | 빠른 복원과 기록 보존을 동시에 |
| **Dream Cycle** | 주간 정리 루틴으로 지식 정제 |
| **자동화 스크립트** | GitHub 자동 커밋, 지식 맵 빌드 |

---

## ⚡ 빠른 시작 프롬프트

| 상황 | 프롬프트 |
|------|---------|
| 새 대화 시작 | `"csp-brain 을 읽고 현재 상황을 브리핑해줘."` |
| 프로젝트 추가 | `"새 프로젝트 [이름] 을 csp-brain 에 추가해줘."` |
| 대화 후 저장 | `"오늘 대화 내용을 csp-brain 에 저장해줘."` |
| 인물 등록 | `"[이름] 에 대한 페이지를 csp-brain 에 추가해줘."` |
| 결정 기록 | `"오늘 내린 결정을 decisions/에 기록해줘."` |
| 주간 정리 | `"이번 주 Dream Cycle 을 실행해줘."` |

자세한 프롬프트는 [INIT_PROMPT.md](./INIT_PROMPT.md) 를 참고하세요.

---

## 📄 라이선스

MIT

---

**Maintained by** CSP (Creative Solution Provider)  
**GitHub** [@foolpoet44](https://github.com/foolpoet44)

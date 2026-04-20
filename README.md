# 🧠 CSP Brain — Global Claude Code Hub

> "심리학이 코드가 되고, 철학이 알고리즘이 되는" 여정

CSP 의 글로벌 Claude Code 설정 허브입니다.  
어느 프로젝트에서 `claude` 를 실행하든 일관된 헌법과 설정이 적용됩니다.

---

## 📁 폴더 구조

```
00_brain/
├── CLAUDE.md                   # 전역 헌법 (Identity, Working Principles, Code Standards)
├── README.md                   # 이 파일
├── MANUAL.md                   # 상세 사용 매뉴얼
├── .gitignore                  # Git 제외 패턴
│
├── .claude/                    # Claude Code 설정 (Junction 으로 연결됨)
│   ├── agents/                 # AI Agent 정의
│   ├── commands/               # 사용자 정의 명령
│   ├── skills/                 # 재사용 가능한 스킬
│   └── settings.json           # 권한 설정
│
├── knowledge/                  # 지식 저장소
│   ├── moc/                    # Map of Content (지식 맵)
│   ├── permanent/              # 영구 지식 (Permanent Notes)
│   └── references/             # 참고 자료
│
├── prompts/                    # 프롬프트 라이브러리
├── dotfiles/                   # 설정 파일 템플릿
└── scripts/                    # 자동화 스크립트
```

---

## 🚀 빠른 시작

### 1. 사전 요구사항

- **OS**: Windows 10/11
- **Git**: [GitHub Desktop](https://desktop.github.com/) 또는 [Git for Windows](https://gitforwindows.org/)
- **Claude Code**: `npm install -g @anthropic-ai/claude-code`

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
# 1. Junction 확인
Get-Item "$env:USERPROFILE\.claude" | Select-Object Name, Target, LinkType

# 2. Claude Code 재시작 후 테스트
claude
# "CLAUDE.md 의 내용을 요약해줘" 라고 입력
```

---

## 🔧 설정

### settings.json

```json
{
  "permissions": {
    "allow": [
      "Bash(*)",
      "Read(*)",
      "Write(*)",
      "Edit(*)",
      "Glob(*)",
      "Grep(*)"
    ]
  }
}
```

### .gitignore

Claude Code 자동 생성 폴더는 Git 에서 제외됩니다:
- `.claude/backups/`, `.claude/cache/`, `.claude/sessions/`
- `.claude/history.jsonl`, `.claude/telemetry/`

---

## 📚 주요 기능

| 기능 | 설명 |
|------|------|
| **전역 헌법** | `CLAUDE.md` 에 정의된 Identity, Working Principles 가 모든 프로젝트에 적용됨 |
| **Junction 링크** | `%USERPROFILE%\.claude` 가 `00_brain\.claude` 를 가리켜 설정 동기화 |
| **지식 저장소** | `knowledge/` 폴더에 영구 지식과 참고 자료 축적 |
| **프롬프트 라이브러리** | 재사용 가능한 프롬프트 템플릿 보관 |

---

## 🔄 업데이트

```powershell
cd 00_brain
git pull origin main
```

---

## 📝 기여

이 레포지토리는 CSP 의 개인 설정 허브입니다.  
공유하고 싶은 기능이 있다면 이슈 또는 PR 을 열어주세요.

---

## 📄 라이선스

MIT

---

**Maintained by** CSP (Creative Solution Provider)  
**GitHub** [@foolpoet44](https://github.com/foolpoet44)

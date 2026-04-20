# CSP Brain — 사용 매뉴얼

> Claude Code 글로벌 설정 허브 + AI 에이전트 메모리 완전 가이드

---

## 목차

1. [개요](#1-개요)
2. [설치 가이드](#2-설치-가이드)
3. [구조 설명](#3-구조-설명)
4. [핵심 패턴: Compiled Truth + Timeline](#4-핵심-compiled-truth--timeline)
5. [운영 주기](#5-운영-주기)
6. [Dream Cycle 가이드](#6-dream-cycle-가이드)
7. [Junction 관리](#7-junction-관리)
8. [문제 해결](#8-문제-해결)

---

## 1. 개요

### 1.1 CSP Brain 이란?

CSP Brain 은 **두 가지 핵심 기능**을 가진 통합 허브입니다:

1. **글로벌 Claude Code 설정**: 어느 폴더에서 `claude` 실행하든 일관된 헌법 적용
2. **AI 에이전트 메모리**: gbrain(Garry Tan) 패턴 기반 지식 저장소

> "심리학이 코드가 되고, 철학이 알고리즘이 되는"  
> "모든 대화가 다음 대화를 더 똑똑하게 만든다"

### 1.2 핵심 가치

- **일관성**: 모든 프로젝트에서 동일한 응답 스타일과 원칙 적용
- **기억 축적**: 대화 내용이 지식으로 축적되어 다음 세션을 더 똑똑하게 만듦
- **재사용성**: 프롬프트, 스킬, 템플릿 자산화
- **투명성**: Timeline(append-only) 로 변화의 증거 보존

---

## 2. 설치 가이드

### 2.1 사전 요구사항

| 항목 | 필수 여부 | 확인 방법 |
|------|-----------|-----------|
| Windows 10/11 | 필수 | `winver` |
| Git | 필수 | `git --version` |
| Claude Code | 필수 | `claude --version` |
| Python 3.8+ | 권장 (스크립트용) | `python --version` |
| PowerShell 5.0+ | 권장 | `$PSVersionTable.PSVersion` |

### 2.2 단계별 설치

#### 단계 1: 레포지토리 클론

```powershell
cd C:\dev  # 또는 선호하는 경로
git clone https://github.com/foolpoet44/csp-brain.git 00_brain
```

#### 단계 2: Junction 생성

**방법 A: CMD 사용 (권장 — 관리자 권한 불필요)**
```powershell
cmd /c mklink /J "C:\dev\.claude" "C:\dev\00_brain\.claude"
```

**방법 B: PowerShell 사용**
```powershell
New-Item -ItemType Junction -Path "C:\dev\.claude" -Target "C:\dev\00_brain\.claude"
```

#### 단계 3: 기존 `.claude` 백업 (있는 경우)

```powershell
if (Test-Path "C:\dev\.claude") {
    $backup = "C:\dev\.claude.backup." + (Get-Date -Format "yyyyMMdd-HHmmss")
    Rename-Item "C:\dev\.claude" $backup
}
```

#### 단계 4: 검증

```powershell
# Junction 확인
Get-Item "C:\dev\.claude" | Select-Object Name, Target, LinkType

# Claude Code 테스트
cd C:\temp
claude
# "CLAUDE.md 내용을 요약해줘"
```

---

## 3. 구조 설명

### 3.1 4-Zone 로컬 아키텍처

```
~/
├── 00_brain/           # 🧠 영원 지대 — 지식과 도구의 원천 (이 레포지토리)
├── 10_work/            # 💼 업무 지대 — 회사 프로젝트 (EX Intelligence, Pulse Check...)
├── 20_build/           # 🛠️ 빌드 지대 — 개인/창업 프로젝트 (ESCON, HR SaaS...)
├── 30_lab/             # 🧪 실험 지대 — 휘발성 스크래치 (30 일 규칙)
└── 99_archive/         # 📦 아카이브 — 완료되거나 중단된 것들
```

### 3.2 00_brain 상세 구조

```
00_brain/
├── CLAUDE.md                   # 🧭 전역 헌법 — 모든 프로젝트가 상속
├── README.md                   # 프로젝트 소개
├── MANUAL.md                   # 이 매뉴얼
├── INIT_PROMPT.md              # 초기 구현 프롬프트 모음
├── .gitignore                  # Git 제외 패턴
│
├── .claude/                    # Claude Code 설정 (Junction 연결)
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
│   └── raw/
│       └── inbox.md            # 미분류 수신함
│
├── prompts/                    # 프롬프트 라이브러리
├── scripts/                    # 자동화 스크립트
├── dotfiles/                   # 설정 파일 템플릿
└── _templates/                 # 재사용 템플릿 (10_work 용)
```

### 3.3 Zone 별 책임

| Zone | 수명 | Git 계정 | 예시 |
|------|------|----------|------|
| **00_brain** | 영구 | 개인 | 전역 헌법, 스킬, 프롬프트 |
| **10_work** | 프로젝트 기간 | 회사 | EX Intelligence, Pulse Check |
| **20_build** | 영구 (창업 준비) | 개인 | ESCON, CSP-OS |
| **30_lab** | 30 일 휘발 | 혼용 | 5 분 실험, 프로토타입 |
| **99_archive** | 영구 (참조용) | 보존 | 완료된 프로젝트 |

### 3.4 주요 폴더 상세 (00_brain 기준)

| 폴더 | 파일 수 | 설명 |
|------|---------|------|
| `knowledge/concepts/` | 100+ | 추출된 지식 노트 (UUID 명명) + 수동 작성 개념 |
| `knowledge/weekly/` | 주간 생성 | Dream Cycle 결과물 (YYYY-WNN.md 형식) |
| `knowledge/people/` | 인물별 | 인물별 컨텍스트 (Compiled Truth + Timeline) |
| `knowledge/decisions/` | 결정별 | 의사결정 로그 (append-only) |
| `scripts/` | 5 개 | brain_build, auto_commit, validate_brain, weekly_scaffold |
| `_templates/` | 4 개 | project.md, person.md, concept.md, decision.md |

---

## 4. 핵심: Compiled Truth + Timeline

모든 지식 파일 (`knowledge/concepts/*.md`, `knowledge/people/*.md`, `10_work/*/CLAUDE.md`) 은 이 구조를 따릅니다.

```markdown
## Compiled Truth
현재 알고 있는 최선의 요약. 새 정보 오면 이 섹션만 덮어씀.

---

## Timeline
append-only 증거 기록. 절대 삭제/수정 금지.

### YYYY-MM-DD
- 오늘 배운 것, 결정한 것, 변화한 것
```

### 작성 규칙

| 섹션 | 규칙 |
|------|------|
| **Compiled Truth** | 새 정보 오면 섹션 전체 덮어씀 (이전 내용 보존 불필요) |
| **Timeline** | **절대 삭제/수정 금지** — 날짜 헤더만 추가하며 append |

---

## 5. 운영 주기

| 주기 | 작업 | 설명 |
|------|------|------|
| **매 대화 시작 전** | 파일 읽기 | CLAUDE.md → 10_work/[프로젝트]/CLAUDE.md → knowledge/weekly → inbox |
| **매 대화 종료 후** | Timeline append | 관련 프로젝트에 `### YYYY-MM-DD` 헤더로 기록 |
| **매주 금요일** | Dream Cycle | inbox 정리 → Compiled Truth 갱신 → weekly 생성 |
| **월 1 회** | 스크립트 실행 | `python scripts/brain_build.py`로 지식 맵 최신화 |

---

## 6. Dream Cycle 가이드

### 6.1 Dream Cycle 이란?

매주 금요일 실행하는 **지식 정제 루틴**입니다.  
뇌의 수면 중 기억 강화 (memory consolidation) 에서 영감을 받았습니다.

### 6.2 실행 절차

```powershell
# 1. raw/inbox.md 확인 → 각 폴더로 분류
# 2. 변화 있던 프로젝트 Compiled Truth 갱신
# 3. weekly 파일 생성
python scripts/weekly_scaffold.py

# 4. GitHub 에 푸시
git add -A
git commit -m "weekly: Dream Cycle - YYYY-WNN"
git push
```

### 6.3 자동화 (GitHub Actions)

`.github/workflows/weekly-scaffold.yml` 이 매주 금요일 자동 실행합니다.

---

## 7. Junction 관리

### 7.1 상태 확인

```powershell
Get-Item "C:\dev\.claude" | Select-Object Name, Target, LinkType
```

### 7.2 제거 및 재생성

```powershell
# 제거
Remove-Item "C:\dev\.claude"

# 재생성
cmd /c mklink /J "C:\dev\.claude" "C:\dev\00_brain\.claude"
```

---

## 8. 문제 해결

### 8.1 "CLAUDE.md 가 로드되지 않아요"

1. Junction 확인: `Get-Item "C:\dev\.claude" | Format-List *`
2. 파일 존재 확인: `Test-Path "C:\dev\CLAUDE.md"`
3. Claude Code 재시작

### 8.2 "프로젝트 파일을 못 읽어요"

1. `10_work/[이름]/CLAUDE.md` 존재 확인
2. Compiled Truth 섹션에 현재 상태가 있는지 확인
3. CLAUDE.md 프로젝트 상태 테이블 업데이트

### 8.3 "Dream Cycle 을 깜빡했어요"

1. `weekly/` 폴더에 누락된 주 확인
2. `python scripts/weekly_scaffold.py` 실행
3. 수동으로 `weekly/YYYY-WNN.md` 생성

### 8.4 "Git 이 `.claude` 파일을 추적해요"

`.gitignore` 에 다음 패턴이 있는지 확인:

```gitignore
.claude/backups/
.claude/cache/
.claude/sessions/
.claude/history.jsonl
.claude/settings.local.json
```

---

## 부록: 빠른 프롬프트 참조

| 상황 | 프롬프트 |
|------|---------|
| 새 대화 시작 | `"csp-brain 을 읽고 현재 상황을 브리핑해줘."` |
| 프로젝트 추가 | `"새 프로젝트 [이름] 을 10_work/에 추가해줘."` |
| 대화 후 저장 | `"오늘 대화 내용을 csp-brain 에 저장해줘."` |
| 인물 등록 | `"[이름] 에 대한 페이지를 knowledge/people/에 추가해줘."` |
| 결정 기록 | `"오늘 내린 결정을 knowledge/decisions/에 기록해줘."` |
| 주간 정리 | `"이번 주 Dream Cycle 을 실행해줘."` |
| 실험 시작 | `"30_lab/에 새 실험 폴더를 생성해줘."` |

---

**Last Updated**: 2026-04-20  
**Maintained by**: CSP (Creative Solution Provider)

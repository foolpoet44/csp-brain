# CSP Brain — 사용 매뉴얼

> Claude Code 글로벌 설정 허브 완전 가이드

---

## 목차

1. [개요](#1-개요)
2. [설치 가이드](#2-설치-가이드)
3. [구조 설명](#3-구조-설명)
4. [CLAUDE.md 작성 가이드](#4-claudemd-작성-가이드)
5. [Junction 관리](#5-junction-관리)
6. [문제 해결](#6-문제-해결)
7. [베스트 프랙티스](#7-베스트-프랙티스)

---

## 1. 개요

### 1.1 CSP Brain 이란?

CSP Brain 은 Claude Code 의 **전역 설정 허브**입니다.  
Windows 환경에서 어느 폴더에서 `claude` 명령을 실행하든 일관된 설정과 헌법이 적용되도록 합니다.

### 1.2 핵심 가치

- **일관성**: 모든 프로젝트에서 동일한 응답 스타일과 원칙 적용
- **재사용성**: 프롬프트, 스킬, 명령어 자산 축적 및 공유
- **지식 축적**: knowledge 폴더에 영구 지식 저장

---

## 2. 설치 가이드

### 2.1 사전 요구사항

| 항목 | 필수 여부 | 확인 방법 |
|------|-----------|-----------|
| Windows 10/11 | 필수 | `winver` |
| Git | 필수 | `git --version` |
| Claude Code | 필수 | `claude --version` |
| PowerShell 5.0+ | 권장 | `$PSVersionTable.PSVersion` |

### 2.2 단계별 설치

#### 단계 1: 레포지토리 클론

```powershell
# 선호하는 개발 폴더로 이동
cd C:\dev

# 클론 (경로에 공백 없어야 함)
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

> ⚠️ **주의**: `%USERPROFILE%\.claude` 가 아닌 **프로젝트 루트**에 Junction 을 생성합니다.

#### 단계 3: 기존 `.claude` 백업 (있는 경우)

```powershell
# 기존 폴더가 있다면 백업
if (Test-Path "C:\dev\.claude") {
    $backup = "C:\dev\.claude.backup." + (Get-Date -Format "yyyyMMdd-HHmmss")
    Rename-Item "C:\dev\.claude" $backup
}
```

#### 단계 4: 검증

```powershell
# Junction 확인
Get-Item "C:\dev\.claude" | Format-List Name, Target, LinkType

# 예상 출력:
# Name     : .claude
# Target   : C:\dev\00_brain\.claude
# LinkType : Junction

# Claude Code 재시작
claude
```

---

## 3. 구조 설명

### 3.1 루트 폴더

| 폴더/파일 | 설명 |
|-----------|------|
| `CLAUDE.md` | 전역 헌법 — Identity, 원칙, 코드 표준 |
| `.claude/` | Claude Code 설정 (Junction 으로 연결) |
| `knowledge/` | 지식 저장소 (Zettelkasten 방식) |
| `prompts/` | 재사용 프롬프트 라이브러리 |
| `dotfiles/` | 설정 파일 템플릿 |
| `scripts/` | 자동화 스크립트 |

### 3.2 `.claude` 하위 폴더

| 폴더 | 설명 |
|------|------|
| `agents/` | 특수화된 AI Agent 정의 |
| `commands/` | 사용자 정의 `/command` |
| `skills/` | 재사용 가능한 스킬 |
| `backups/` | 자동 백업 (gitignore) |
| `cache/` | 캐시 데이터 (gitignore) |
| `sessions/` | 세션 기록 (gitignore) |

### 3.3 `knowledge` 하위 폴더

| 폴더 | 설명 |
|------|------|
| `moc/` | Map of Content — 지식 맵 (인덱스) |
| `permanent/` | Permanent Notes — 영구 지식 |
| `references/` | 외부 참고 자료 |

---

## 4. CLAUDE.md 작성 가이드

### 4.1 필수 섹션

```markdown
# [프로젝트명] Claude Code Constitution

## Identity
[당신의 역할과 정체성]

## Environment
- OS: [Windows/macOS/Linux]
- Primary IDE: [Claude Code, VS Code, etc.]
- Cloud Brain: [Notion, Obsidian, etc.]

## Working Principles
1. [원칙 1]
2. [원칙 2]

## Code Standards
- [코드 표준 1]
- [코드 표준 2]

## Response Style
- [응답 스타일 1]
- [응답 스타일 2]
```

### 4.2 프로젝트별 상속

로컬 프로젝트 `CLAUDE.md`:

```markdown
# My Project CLAUDE.md

이 프로젝트는 [전역 헌법](../00_brain/CLAUDE.md) 을 상속합니다.

## Project-Specific Context
- 프로젝트 목적: [간단한 설명]
- 사용 스택: [React, Supabase, etc.]
- 특수 규칙: [프로젝트 고유 규칙]
```

---

## 5. Junction 관리

### 5.1 Junction 상태 확인

```powershell
# 심볼릭 링크 확인
Get-Item "C:\dev\.claude" | Select-Object Name, Target, LinkType

# 실제 폴더 내용 확인
Get-ChildItem "C:\dev\.claude" -Force
```

### 5.2 Junction 제거

```powershell
# Junction 만 삭제 (실제 폴더는 유지)
Remove-Item "C:\dev\.claude"

# 또는 CMD
cmd /c rmdir "C:\dev\.claude"
```

### 5.3 Junction 재생성

```powershell
# 1. 기존 Junction 제거
Remove-Item "C:\dev\.claude"

# 2. 새 Junction 생성
cmd /c mklink /J "C:\dev\.claude" "C:\dev\00_brain\.claude"
```

---

## 6. 문제 해결

### 6.1 "CLAUDE.md 가 로드되지 않아요"

**확인할 사항:**
1. Junction 이 올바른지 확인
   ```powershell
   Get-Item "C:\dev\.claude" | Format-List *
   ```
2. `CLAUDE.md` 파일 존재 확인
   ```powershell
   Test-Path "C:\dev\CLAUDE.md"
   ```
3. Claude Code 재시작

### 6.2 "Junction 이 작동하지 않아요"

**해결 방법:**
1. Junction 제거 후 재생성
2. 대상 폴더가 존재하는지 확인
3. 경로에 공백이 없는지 확인

### 6.3 "Git 이 `.claude` 파일을 추적해요"

`.gitignore` 에 다음 패턴이 있는지 확인:

```gitignore
.claude/backups/
.claude/cache/
.claude/sessions/
.claude/history.jsonl
.claude/settings.local.json
```

### 6.4 "권한 오류가 발생해요"

`settings.json` 에 적절한 권한이 있는지 확인:

```json
{
  "permissions": {
    "allow": [
      "Bash(*)",
      "Read(*)",
      "Write(*)"
    ]
  }
}
```

---

## 7. 베스트 프랙티스

### 7.1 CLAUDE.md 관리

- ✅ **간결하게**: 핵심 원칙만 기록 (10-20 줄)
- ✅ **버전 관리**: 변경사항은 git 커밋으로 기록
- ✅ **상속 활용**: 프로젝트별 CLAUDE.md 는 전역 헌법 참조

### 7.2 Knowledge 관리

- ✅ **moc/ 에 인덱스**: 지식 맵 먼저 작성
- ✅ **하나의 아이디어 = 하나의 파일**: 재사용성 향상
- ✅ **링크 활용**: `[[파일명]]` 으로 지식 연결

### 7.3 Git 관리

- ✅ **자동 생성 폴더 제외**: `.gitignore` 철저히
- ✅ **정기적 푸시**: 로컬만 사용하지 말고 GitHub 에 백업
- ✅ **의미 있는 커밋 메시지**: Conventional Commits 준수

### 7.4 백업 전략

- ✅ **`.claude.backup`**: Junction 재생성 전 백업
- ✅ **GitHub 동기화**: `git push` 로 클라우드 백업
- ✅ **정기 export**: 중요한 세션은 수동 백업

---

## 부록: PowerShell 유틸리티

### A.1 Junction 상태 한 번에 확인

```powershell
function Test-ClaudeJunction {
    $junction = Get-Item "$env:USERPROFILE\.claude" -ErrorAction SilentlyContinue
    if ($junction -and $junction.LinkType -eq "Junction") {
        Write-Host "✅ Junction 정상: $($junction.Target)" -ForegroundColor Green
    } else {
        Write-Host "❌ Junction 없음 또는 오류" -ForegroundColor Red
    }
}
```

### A.2 빠른 백업

```powershell
function Backup-Claude {
    $backup = ".claude.backup." + (Get-Date -Format "yyyyMMdd-HHmmss")
    if (Test-Path ".claude") {
        Rename-Item ".claude" $backup
        Write-Host "백업 완료: $backup"
    }
}
```

---

**Last Updated**: 2026-04-20  
**Maintained by**: CSP (Creative Solution Provider)

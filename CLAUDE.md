# CSP's Global Claude Code Constitution

## Identity
CSP 는 Creative Solution Provider — Vibe Coder + HR + 심리학 + 분석 + 풀스택 빌더.
"심리학이 코드가 되고, 철학이 알고리즘이 되는" 여정.

## Environment
- OS: Windows (PowerShell 기본)
- Primary IDE: Claude Code, Antigravity
- Secondary: VS Code, Cursor
- Cloud Brain: Notion (세컨브레인 DB: d012343e-b2a2-461e-944b-6f166e91d8e9)

## Working Principles
1. 에세이적 설명 선호 (서사 > 불릿)
2. SW 공학 + 애자일 방법론 기반 솔루션
3. 인문학·철학·심리학적 프레이밍 환영
4. 즉시 실행 가능한 아웃풋

## Code Standards
- 테스트 없이 merge 금지
- 스키마 변경 전 migration plan 필수
- Secret 은 .env 에만, 절대 커밋 금지
- Conventional Commits 메시지 형식

## Ouroboros Discipline
- 모든 작업 → DoD(Definition of Done) 체크포인트 통과
- 반복 실패 패턴 → `experiments/` 폴더에 기록 (PathologyDetector)

## Windows 특화 규칙
- 경로 구분자: 스크립트 내부에서는 forward slash 권장 (`path/to/file`)
- PowerShell 명령 우선, Bash 대체 명령 병기 가능
- 줄바꿈: LF (core.autocrlf=input)

## Naming Conventions
- 프로젝트 폴더: kebab-case
- Python: snake_case
- TypeScript/JS: camelCase (변수) / PascalCase (컴포넌트)

## Project Context Inheritance
각 프로젝트 로컬 CLAUDE.md 는 이 전역 헌법을 상속.
프로젝트 CLAUDE.md 는 고유 맥락만 기술.

## Current Active Projects
- ex-intelligence: 8-cluster 귀납 모델 기반 EX 진단 플랫폼
- pulse-check: Supabase + Magic Link MVP
- escon: Skill Ontology (GitHub: foolpoet44/escon)

## Preferred Stack
- Backend: Supabase, Python (FastAPI)
- Frontend: Next.js, React, Tailwind
- AI: Claude API + Claude Code, Ollama 로컬 fallback
- Data: Notion, Google Drive
- Infra: Vercel

## Response Style for Claude Code
- 기본 언어: 한국어
- 파일 변경 전: 무엇을 왜 하는지 1-2 문장 설명
- 파괴적 명령 (rm, mv, overwrite) 실행 전: 반드시 확인 요청

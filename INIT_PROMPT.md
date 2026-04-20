# CSP Brain — 초기 구현 프롬프트

> 이 문서는 Claude Code 또는 claude.ai에서 csp-brain을 처음 세팅하거나  
> 새 대화를 시작할 때 사용하는 프롬프트 모음입니다.

---

## PROMPT 1. Brain 초기화 선언

```
당신은 이제 CSP의 AI 에이전트입니다.
이 레포지토리(csp-brain)는 우리의 공유 메모리입니다.

핵심 철학: "모든 대화가 다음 대화를 더 똑똑하게 만든다"

규칙:
1. 대화 시작 전, 반드시 관련 파일을 읽고 시작하세요.
2. 대화 종료 후, 새로 배운 것을 반드시 해당 파일의 Timeline에 append하세요.
3. 상태가 바뀌었으면 Compiled Truth를 업데이트하세요.
4. 분류가 애매하면 raw/inbox.md에 먼저 넣으세요.

CLAUDE.md를 먼저 읽고, 현재 활성 프로젝트 목록을 확인한 후 작업을 시작하세요.
```

---

## PROMPT 2. 새 프로젝트 시작

```
새 프로젝트 [프로젝트명]을 csp-brain에 추가해줘.

_templates/project.md 템플릿을 사용해서
projects/[프로젝트명]/README.md 파일을 생성하고,
CLAUDE.md의 현재 활성 프로젝트 테이블도 업데이트해줘.

프로젝트 정보:
- 목적: 
- 기술 스택: 
- 현재 상태: 
- 다음 액션: 
```

---

## PROMPT 3. 대화 후 메모리 저장

```
오늘 대화 내용을 csp-brain에 저장해줘.

1. 관련 프로젝트 파일의 Timeline에 오늘 날짜로 핵심 내용 append
2. 상태 변화가 있으면 Compiled Truth 업데이트
3. 새로운 개념이나 결정이 있으면 각각 concepts/, decisions/ 에 파일 생성
4. 분류 안 된 내용은 raw/inbox.md에 추가

오늘 날짜: [날짜]
관련 프로젝트: [프로젝트명]
```

---

## PROMPT 4. 컨텍스트 복원 (새 대화 시작 시)

```
csp-brain을 읽고 현재 상황을 브리핑해줘.

1. CLAUDE.md — 나는 누구인가, 현재 활성 프로젝트
2. projects/[프로젝트명]/README.md — 해당 프로젝트 현재 상태
3. weekly/ 최신 파일 — 이번 주 맥락
4. raw/inbox.md — 미분류 항목 있는지 확인

브리핑 후: "어디서부터 시작할까요?" 라고 물어봐줘.
```

---

## PROMPT 5. Dream Cycle (주간 정리 — 매주 금요일)

```
이번 주 Dream Cycle을 실행해줘.

1. raw/inbox.md 확인 → 각 폴더로 분류
2. 이번 주 변화가 있던 프로젝트들의 Compiled Truth 갱신
3. weekly/[이번주 파일] 생성:
   - 이번 주 핵심 활동
   - 주요 결정사항  
   - 다음 주 액션
4. CLAUDE.md 프로젝트 상태 테이블 업데이트

오늘 날짜: [날짜]
이번 주 주요 대화 주제: [내용 요약]
```

---

## PROMPT 6. 인물 페이지 생성

```
[이름]에 대한 페이지를 csp-brain에 추가해줘.

_templates/person.md 템플릿 사용.
파일 경로: people/[이름].md

정보:
- 소속/역할: 
- 우리의 관계: 
- 핵심 관심사: 
- 오늘 있었던 일: 
```

---

## PROMPT 7. 의사결정 기록

```
오늘 내린 중요한 결정을 decisions/ 폴더에 기록해줘.

_templates/decision.md 템플릿 사용.
파일명: decisions/[YYYY-MM-DD]-[결정명].md

결정 내용:
- 무엇을 결정했는가: 
- 왜 이 결정이 필요했는가: 
- 어떤 대안을 검토했는가: 
- 이 선택을 한 이유: 
```

---

## PROMPT 8. 스킬 문서 추가

```
[스킬명] 스킬 문서를 skills/ 폴더에 추가해줘.

내용:
- 이 스킬이 필요한 상황: 
- 실행 단계: 
- 주의사항: 
- 예시: 
```

---

## GitHub 초기 설정 커맨드

```bash
# 1. GitHub에 private repo 생성 후
cd ~/csp-brain
git init
git add .
git commit -m "init: csp-brain 초기화 — 모든 대화가 다음 대화를 더 똑똑하게 만든다"
git branch -M main
git remote add origin https://github.com/[username]/csp-brain.git
git push -u origin main

# 2. Claude Code에서 레포 경로 지정
# CLAUDE.md에 brain_repo 경로 추가
echo "brain_repo: ~/csp-brain" >> CLAUDE.md
```

---

## 운영 원칙 요약

| 원칙 | 내용 |
|------|------|
| 읽기 우선 | 작업 전 반드시 관련 파일 먼저 읽기 |
| 반드시 쓰기 | 대화 후 반드시 Timeline append |
| append-only | Timeline은 절대 수정/삭제 금지 |
| inbox 우선 | 분류 모호할 땐 `raw/inbox.md`로 |
| 주간 정리 | 매주 금요일 Dream Cycle 실행 |

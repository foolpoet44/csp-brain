# Pulse Check

> 조직 구성원의 실시간 Well-Being·몰입도를 측정하고 개선하는 HR 펄스 서베이 플랫폼.

---

## Compiled Truth

| 항목 | 내용 |
|------|------|
| 상태 | 🟡 MVP 아키텍처 정의 완료 |
| 기술 스택 | Supabase + Magic Link (Consent-based) |
| 레포 | — |
| 배포 URL | — |
| 다음 액션 | Supabase 환경 구축 및 Auth Flow 연동 |
| 핵심 결정사항 | MS Forms/SharePoint 기반에서 Supabase 독립 스택으로 전환 |

---

## 목적 & 배경

- **왜 이 프로젝트를 시작했는가**: 연 1~2회 정기 설문만으로는 조직의 실시간 맥박을 파악할 수 없어 상시 측정 체계 필요
- **해결하려는 문제**: 
  - 직원 Well-Being 악화 신호를 사전에 감지하지 못함
  - 참여자의 익명성 보장과 동시에 명시적 동의(Explicit Consent) 기반의 참여 트래킹 필요
- **아키텍처 전환**: 기존 Microsoft Forms 중심에서 Supabase 모바일/웹 스택으로 전환하여 데이터 통제권 확보

---

## 핵심 KPI 연결

| KPI | 목표 |
|-----|------|
| 참여율 | 85% (명시적 동의 기준) |
| Well-Being 지수 | +15% (상시 트래킹) |

---

## 주요 파일 & 경로

| 파일/경로 | 역할 |
|----------|------|
| `decisions/2026-04-14-supabase-stack-selection.md` | 기술 스택 전환 사유 (계획 중) |

---

## 알려진 이슈 & 제약

- [ ] MVP 구현 미착수 상태
- [ ] Supabase 프로젝트 초기화 및 DB Schema 설계 대기

---

---

## 관련 문서

- 결정: `decisions/`
- 개념: `concepts/`
- 관련 인물: `people/`

## Timeline (append-only — 절대 수정/삭제 금지)

### 2026-04-14
- 프로젝트 폴더 초기 생성 (csp-brain 구조화)
- 상태: MVP 아키텍처 정의 완료
- Compiled Truth 초기 작성 (CLAUDE.md 정보 기반)
- 다음 액션: MVP 구현 착수

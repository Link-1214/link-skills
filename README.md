# link-skills

**만들기 전에 정하는 스킬 모음.**

AI로 일하다 "이건 절차로 굳혀두는 게 낫겠다" 싶은 것들을 스킬로 만들어 모읍니다.
공통점은 하나입니다. **정해지지 않은 걸 대신 정하지 않고, 물어보고 멈춥니다.**

모든 스킬은 무엇을 왜 정했는지를 평문 마크다운으로 남깁니다. 보드나 목업은 사람이 보는 것이고,
그 기록은 다음 세션이 읽는 것입니다.

---

## 빠른 시작

```bash
claude plugin marketplace add Link-1214/link-skills
```

```bash
claude plugin install link@link-skills
```

```bash
/reload-plugins
```

끝입니다. `link`는 전체 설치용이라 이후 스킬이 추가돼도 `update`만 하면 따라옵니다.

---

## 용어

이 저장소는 Claude Code 공식 용어를 그대로 씁니다.

| 용어 | 뜻 | 예 |
|---|---|---|
| **마켓플레이스** | 저장소. `add` 하는 대상 | `link-skills` |
| **플러그인** | **설치 단위.** 스킬 여러 개를 담음 | `link-design-pitch` |
| **스킬** | **호출 단위** | `link-design-pitch:link-design-pitch` |

포인트는 하나입니다. **설치는 플러그인 단위이고, 그 안의 스킬은 쪼갤 수 없습니다.**
서로 없으면 의미가 없는 스킬을 한 플러그인에 넣는 이유가 이것입니다.

---

## 스킬 목록

### 🎨 link-design-pitch

**시각 방향을 고르고, 정해진 뒤 적용한다.** 스킬 2개.

```bash
claude plugin install link-design-pitch@link-skills
```

| 순서 | 호출 | 하는 일 |
|---|---|---|
| 1 | `link-design-pitch:link-design-pitch` | 질문 5개 → 시안 10개 → 추천 → **멈추고 선택을 물음** |
| — | *직접 만드는 단계* | 기능과 내용을 직접 또는 다른 AI로 |
| 2 | `link-design-pitch:link-design-pitch-detail` | 모든 화면에 적용 → 인터랙션 선택지 제시 |

**왜 둘로 나뉘어 있나.** 사이에 "실제로 만드는" 단계가 끼기 때문입니다. 한 번에 하려면 내용이
나올 때까지 멈춰 있거나, 없는 내용을 지어내야 합니다.

**어디에 쓰나.** 웹·데스크톱 앱, 모바일, 발표 자료, 스프레드시트, 문서, 인쇄물.
질문 2번이 "무엇을 만드는가"라서, 스프레드시트와 웹앱은 애초에 다른 후보를 받습니다.

**무엇이 나오나.** 프로젝트가 문서를 두는 곳(`docs/design/` 또는 `design/`)에:

- `01-directions.html` · `.png` — 시안 10개 보드
- `02-detail-<방향>.html` · `.png` — 선택한 방향의 모든 화면
- `DECISION.md` — 답변·판정·측정값·토큰. 다음 세션과 다른 AI가 읽는 기록

[**사용법 자세히 →**](plugins/link-design-pitch/README.md)

---

> 앞으로 추가되는 스킬도 여기에 같은 형식으로 붙습니다.
> `link` 를 설치해 두면 `claude plugin update link@link-skills` 만으로 따라옵니다.

---

## 설치

### 전부 설치

```bash
claude plugin marketplace add Link-1214/link-skills
```

```bash
claude plugin install link@link-skills
```

`link` 는 스킬이 없는 플러그인입니다. 나머지를 의존성으로 가리키기만 해서, 한 번 설치로 전부
들어오고 새 스킬도 업데이트에 딸려옵니다.

### 하나만 설치

마켓플레이스를 추가한 뒤 원하는 것만 고릅니다.

```bash
claude plugin install link-design-pitch@link-skills
```

### 확인

```bash
claude plugin list
```

문제가 있으면 `/plugin` 의 **Errors** 탭에 뜹니다.

### 갱신과 제거

```bash
claude plugin update link@link-skills
```

```bash
claude plugin uninstall link-design-pitch
```

자동 갱신은 Anthropic 외 마켓플레이스에서 기본 꺼짐입니다. `/plugin` 에서 켤 수 있습니다.

### 설치 범위

기본은 사용자 범위(모든 프로젝트). 팀 저장소에 커밋하려면 `--scope project`,
내 체크아웃에만 두려면 `--scope local`.

### Codex 등 다른 AI

스킬은 Claude 전용 도구를 쓰지 않는 평범한 마크다운입니다. **설치할 것이 없습니다.**

```bash
git clone https://github.com/Link-1214/link-skills.git
```

프로젝트의 `AGENTS.md` 에 경로만 적어 둡니다.

```markdown
시각 방향이 안 정해졌다면
<경로>/link-skills/plugins/link-design-pitch/skills/link-design-pitch/SKILL.md 를 따른다

방향이 정해졌고 실제로 만들어졌다면
<경로>/link-skills/plugins/link-design-pitch/skills/link-design-pitch-detail/SKILL.md 를 따른다
```

저장소의 [`AGENTS.md`](AGENTS.md) 가 이 용도로 쓰였습니다.

---

## 어떻게 만드는가

무엇을 설치하는지 알려면 필요한 내용이라 적어 둡니다.

**이유가 살아 있는 산문으로 씁니다.** 체크리스트가 아닙니다. 이유를 아는 모델은 지시문이 예상하지
못한 상황도 처리합니다. 유난히 구체적인 규칙은 전부 그게 없어서 뭔가 잘못됐던 것들입니다.

**참조 파일은 필요할 때만 읽힙니다.** 항상 읽히는 건 `SKILL.md` 뿐입니다. 긴 것은 앞에 색인을 붙여
전부가 아니라 실제로 쓰는 부분만 읽습니다. 이것만으로 한 번 실행의 입력이 29% 줄었습니다.

**결정 지점에서 멈춥니다.** 지나쳐서 만든 결과물은 버려질 수 있는 작업이고, 동시에 주인에게서
빼앗은 결정입니다.

**특정 AI 전용 기능에 기대지 않습니다.** 더 나은 수단이 있으면 쓰고, 없으면 없는 대로 됩니다.
Codex가 그냥 clone해서 쓸 수 있는 이유입니다.

**변경은 실사용 실패에서만 나옵니다.** 좋아 보여서 넣은 것은 없습니다.

새 스킬 추가는 [`AUTHORING.md`](AUTHORING.md) 를 보세요.

---

## 운영 방식

**제 도구를 공개한 것입니다.** 제가 하는 일에 맞춰 만들었습니다. 그래서 의견이 뚜렷하고, 같은
이유로 안 맞을 수 있습니다. 돌리기 전에 읽어 보세요.

**버전은 손으로 올립니다.** 릴리스할 때만 움직입니다. 고침은 patch, 새 동작은 minor, 호출 이름이나
산출물 계약이 바뀌면 major. [`CHANGELOG.md`](CHANGELOG.md)

**이슈·PR 환영, 답장은 약속 못 합니다.** 버그 제보는 읽습니다. 기능 요청은 제가 그 필요를 겪지
않으면 아마 안 만듭니다. 포크는 마음껏.

**아무것도 밖으로 보내지 않습니다.** 외부 서비스를 부르지 않고, 수집하지 않고, 전송하지 않습니다.

---

## 언어

사람이 읽는 문서는 한국어입니다.

`SKILL.md` 와 `references/` 는 영어입니다. **독자가 사람이 아니라 모델**이고, 같은 내용이 영어일 때
토큰을 덜 먹기 때문입니다. 출력은 영어로 나오지 않습니다 — 스킬 안에 "사용자가 쓰는 언어로 답하라"가
들어 있어서, 한국어로 물으면 한국어로 답합니다.

---

MIT — [LICENSE](LICENSE)

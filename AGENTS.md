# link-skills — Codex와 다른 에이전트를 위한 안내

이 저장소는 스킬 모음입니다. 스킬은 어떤 코딩 에이전트든 따라갈 수 있는 **글로 쓴 절차**입니다.
Claude 전용인 것은 하나도 없고, 마크다운 지시문과 참조 파일이 전부입니다. 설치할 필요 없이
`SKILL.md` 를 읽고 그대로 따르면 됩니다.

## 용어

| 용어 | 뜻 |
|---|---|
| 마켓플레이스 | 이 저장소. `add` 하는 대상 |
| 플러그인 | **설치 단위.** 스킬 여러 개를 담음 |
| 스킬 | **호출 단위.** `SKILL.md` 하나 |

설치는 플러그인 단위이고 그 안의 스킬은 쪼갤 수 없습니다. 서로 없으면 의미가 없는 스킬을 한
플러그인에 넣는 이유입니다.

## 이 저장소의 스킬

| 스킬 | 진입점 | 언제 |
|---|---|---|
| link-design-pitch | `plugins/link-design-pitch/skills/link-design-pitch/SKILL.md` | 산출물의 시각 방향이 안 정해졌을 때 — UI, 리스타일, 테마, 색 체계, 발표 자료, 보고서, 스프레드시트, 또는 지금 것이 밋밋하거나 뻔하다는 말이 나왔을 때. 시안 열 개 중 어느 것으로 갈지 묻고 끝납니다. |
| link-design-pitch-detail | `plugins/link-design-pitch/skills/link-design-pitch-detail/SKILL.md` | 방향이 이미 정해졌고 **실제 물건이 만들어졌을 때**. 모든 화면에 적용하고 인터랙션 선택지를 제시합니다. 정해진 방향이 기록에 없으면 실행을 거부합니다. |

둘은 하나의 흐름이고, 그 사이에 사람이 만드는 단계가 있습니다.

```
질문 다섯 → 시안 열 개 → 추천 → [주인이 고름]
                                      ↓
                    [주인이 실제 기능과 내용을 만듦]
                                      ↓
      모든 화면에 적용 → [인터랙션 선택지 제시] → [주인이 고름]
```

각 스킬 폴더에 자체 `AGENTS.md` 가 있고, 단계별 상세와 어떤 참조 파일을 언제 읽는지가 적혀 있습니다.
전체 트리를 훑지 말고 그것부터 읽으세요.

## 프로젝트에 붙이는 법

받아 둔 경로를 가리켜 프로젝트의 `AGENTS.md` 에 적습니다.

```markdown
시각 방향이 안 정해졌다면
<받은경로>/link-skills/plugins/link-design-pitch/skills/link-design-pitch/SKILL.md 를 따른다

방향이 정해졌고 실제로 만들어졌다면
<받은경로>/link-skills/plugins/link-design-pitch/skills/link-design-pitch-detail/SKILL.md 를 따른다
```

## 반드시 지켜야 하는 두 가지

**여기 스킬은 전부 대상 프로젝트에 평문 마크다운 결정 기록을 남깁니다.** HTML 보드와 목업은 사람이
보는 것이고, 그 기록은 맥락 없이 나중에 오는 당신이 읽는 것입니다.

- **다시 하기 전에 기록을 읽으세요.** 프로젝트에 이미 기록이 있다면, 당신이 한 세션을 쓰려던 그
  질문에 이미 답이 있을 수 있습니다.
- **기록을 정확하게 유지하세요.** 낡은 기록은 없느니만 못합니다. 다음 에이전트가 그걸 믿기 때문입니다.
  계획으로 적힌 것을 구현했다면 구현했다고 표시하세요. 실제로 이것 때문에 중복 작업이 한 번 났습니다.

**정해지지 않은 것을 만들지 말고 선택지를 제시하세요.** 두 스킬 모두 주인이 버릴 수 있는 결과물을
만드는 대신 결정 지점에서 멈춥니다. 주인이 모델을 고르기 전에 쓴 전체 인터랙션 명세는 나머지 전부를
합친 것보다 비싸고, 제시하지 않았던 답이 나오는 순간 버려집니다 — 실제로 한 번 그랬습니다.

## 저장소 구조

```
link-skills/
├── .claude-plugin/marketplace.json     Claude Code 마켓플레이스 카탈로그
└── plugins/
    ├── link/                           전체 설치용 — 의존성만 있고 스킬은 없음
    └── link-design-pitch/              플러그인 하나, 스킬 둘
        ├── .claude-plugin/plugin.json
        ├── README.md                   사용법과 예시
        └── skills/
            ├── link-design-pitch/            SKILL.md · AGENTS.md · references/
            └── link-design-pitch-detail/     SKILL.md · AGENTS.md · references/
```

`.claude-plugin/` 디렉터리와 `plugins/` 중첩은 Claude Code 설치기를 위한 것입니다. 다른 에이전트라면
무시하고 위의 `SKILL.md` 경로로 바로 가세요.

## 언어

이 문서와 README·AUTHORING·CHANGELOG는 한국어입니다. `SKILL.md` 와 `references/` 는 영어인데, 독자가
모델이고 영어가 토큰을 덜 먹기 때문입니다. **출력은 영어로 나오지 않습니다** — 스킬 안에 사용자가
쓰는 언어로 답하라는 지시가 있습니다.

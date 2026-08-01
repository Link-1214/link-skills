# link-skills — for Codex and other agents

This repository is a set of skills: written procedures any coding agent can follow. Nothing here is
Claude-specific — it is Markdown instructions plus reference files. No installation is required to
use them; read the `SKILL.md` and follow it.

## Skills in this repo

| Skill | Entry point | Use when |
|---|---|---|
| link-design-pitch | `plugins/link-design-pitch/skills/link-design-pitch/SKILL.md` | The visual direction of a deliverable is undecided — a UI, a restyle, a theme, a deck, a report, a spreadsheet, or someone saying it looks bland or generic. Ends by asking which of ten directions they want. |
| link-design-pitch-detail | `plugins/link-design-pitch/skills/link-design-pitch-detail/SKILL.md` | A direction is already chosen **and the real thing is built**. Applies it to every surface, then presents interaction options. Refuses to run without a chosen direction on record. |

The two are one workflow with the build in between:

```
five questions → ten directions → recommend → [owner chooses]
                                                     ↓
                          [owner builds the real features and content]
                                                     ↓
              apply to every surface → [present interaction options] → [owner chooses]
```

Each skill folder carries its own `AGENTS.md` with the phase detail and which reference files to
load at which point. Read that before starting, not the whole tree.

## Wiring into a project

Add to the project's own `AGENTS.md`, pointing at wherever you cloned this repo:

```markdown
Design direction undecided?
Follow <path-to>/link-skills/plugins/link-design-pitch/skills/link-design-pitch/SKILL.md

Direction chosen and the thing is built? Apply it with
<path-to>/link-skills/plugins/link-design-pitch/skills/link-design-pitch-detail/SKILL.md
```

## The two conventions that matter

**Every skill here writes a plain-Markdown decision record into the target project.** HTML boards
and mockups are for humans; the record is for you, in a later session, with none of this context.

- **Read the record before redoing the work.** If a project already has one, it may already answer
  the question you were about to spend a session on.
- **Keep it accurate.** A stale record is worse than none, because the next agent will believe it.
  If you implement what it described as planned, mark it implemented. This has already caused one
  round of duplicated work in practice.

**Present options; do not build what has not been chosen.** Both skills stop at a decision point
rather than producing work the owner may discard. A full interaction specification written before
the owner picks a model costs more than everything else combined and is thrown away the moment they
name something you did not offer — which has already happened once.

## Repo layout

```
link-skills/
├── .claude-plugin/marketplace.json     Claude Code marketplace catalog
└── plugins/
    ├── link/                           bundle — dependencies only, ships no skills
    └── link-design-pitch/              one plugin, two skills
        ├── .claude-plugin/plugin.json
        ├── README.md                   usage and worked example
        └── skills/
            ├── link-design-pitch/            SKILL.md · AGENTS.md · references/
            └── link-design-pitch-detail/     SKILL.md · AGENTS.md · references/
```

The `.claude-plugin/` directories and the `plugins/` nesting exist for Claude Code's installer. If
you are a different agent, ignore them and go straight to the `SKILL.md` paths above.

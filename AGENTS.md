# link-skills — for Codex and other agents

This repository is a set of skills: written procedures any coding agent can follow. Nothing here is
Claude-specific — it is Markdown instructions plus reference files. No installation is required to
use them; read the `SKILL.md` and follow it.

## Skills in this repo

| Skill | Entry point | Use when |
|---|---|---|
| design-pitch | `plugins/link-design-pitch/skills/design-pitch/SKILL.md` | The visual direction of an interface is undecided or under question — a new UI, a restyle, a theme, a color scheme, or someone saying it looks bland or generic. Works before the code exists, midway through, and on software that already ships. |

Each skill folder carries its own `AGENTS.md` with the phase-by-phase detail and which reference
files to load at which point. Read that before starting, not the whole tree.

## Wiring a skill into a project

Add a line to the project's own `AGENTS.md` so the skill is discoverable from where the work
happens, pointing at wherever you cloned this repo:

```markdown
Design direction undecided or under review?
Follow <path-to>/link-skills/plugins/link-design-pitch/skills/design-pitch/SKILL.md
```

## The one convention that matters

**Every skill here writes a plain-Markdown decision record into the target project.** HTML boards
and mockups are for humans; the record is for you, in a later session, with none of this context.

Two rules follow from that:

- **Read the record before redoing the work.** If a project already has one, it may already answer
  the question you were about to spend a session on.
- **Keep it accurate.** A stale decision record is worse than no record, because the next agent will
  believe it. If you implement what it described as planned, mark it implemented. This has already
  caused one round of duplicated work in practice.

## Repo layout

```
link-skills/
├── .claude-plugin/marketplace.json     Claude Code marketplace catalog
└── plugins/
    ├── link/                           bundle — dependencies only, ships no skills
    └── link-design-pitch/
        ├── .claude-plugin/plugin.json
        ├── README.md                   usage and worked example
        └── skills/design-pitch/
            ├── SKILL.md                the procedure
            ├── AGENTS.md               agent-facing entry point
            └── references/             loaded on demand
```

The `.claude-plugin/` directories and the `plugins/` nesting exist for Claude Code's installer. If
you are a different agent, ignore them and go straight to the `SKILL.md` paths above.

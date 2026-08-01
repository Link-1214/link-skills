# link-skills

**Decide it before you build it.**

Agent skills for the part of the work that happens before the code: surveying the options, arguing
the trade-offs out loud, checking what your platform can actually do, and writing the decision down
somewhere the next session can read it.

Every skill here leaves a plain-Markdown record of what was decided and why. Boards and mockups are
for people; the record is for the next agent — including you, three weeks later with none of the
context.

---

## Install

### Claude Code — everything

```bash
claude plugin marketplace add Link-1214/link-skills
```

```bash
claude plugin install link@link-skills
```

`link` ships nothing itself. It lists the other plugins as dependencies, so one install gets all of
them and new skills arrive on update without another install step.

From inside a session, the same two steps are:

```bash
/plugin marketplace add Link-1214/link-skills
```

```bash
/plugin install link@link-skills
```

Then reload so the skills register:

```bash
/reload-plugins
```

### Claude Code — one skill only

Add the marketplace once with the command above, then install just what you want:

```bash
claude plugin install link-design-pitch@link-skills
```

### Codex and other agents

Skills here are plain Markdown with no Claude-specific tooling, so any coding agent can follow them.
Clone the repo:

```bash
git clone https://github.com/Link-1214/link-skills.git
```

Then point at the skill from your project's `AGENTS.md`:

```markdown
Design direction undecided or under review?
Follow <path-to>/link-skills/plugins/link-design-pitch/skills/design-pitch/SKILL.md
```

Each skill folder carries its own `AGENTS.md` describing when to reach for it and which reference
files to load at which point.

### Staying current

```bash
claude plugin update link@link-skills
```

Auto-update is off by default for non-Anthropic marketplaces. Turn it on for this one in `/plugin`,
or run the command above.

---

## Skills

### link-design-pitch

```bash
claude plugin install link-design-pitch@link-skills
```

Pitches visual design directions the way a studio does, instead of guessing at a single comp. Ten
directions on the wall rendered with **your** real content and data, trade-offs argued in a table,
technical feasibility checked *before* anyone falls for something the platform cannot render, one
recommendation with the strongest objection to it answered — then you pick, and only then the
detailed screen-by-screen spec.

It opens with five questions: who this is for, what kind of screen it is, the core color, the
layout, and the single action the screen has to drive. That last answer sets the visual hierarchy
for everything downstream.

Runs before the code exists, midway through, or on software that already ships.

**[Usage and worked example →](plugins/link-design-pitch/README.md)**

---

## How this repo is run

Written down so you know what to expect before you depend on it.

**These are my tools, published.** They are built for work I actually do and shaped by what breaks
in it. That is why they are opinionated enough to be useful, and also why they may not fit your
situation. Read a skill before you run it — it is a few hundred lines of Markdown and it tells you
exactly what it will do.

**Changes come from use, not from planning.** Every revision so far came from a skill failing on a
real task. I do not add capability speculatively, because guessing at needs I have not hit produces
instructions that read well and do nothing.

**Versions are explicit and bumped by hand.** Each plugin pins a `version`, so you only move when I
publish. Patch for corrections, minor for new behavior, major if an invocation name or an output
contract changes. What ships is what passed a real run, not a draft.

**Skills stay tool-agnostic.** No skill depends on a feature only one agent has. Where a harness
offers something better, the skill uses it when present and works without it when absent. That is
what keeps the clone path above viable for Codex and others.

**Issues and PRs are welcome; a reply is not promised.** Bug reports naming what you ran and what
happened are genuinely useful and I will read them. Feature requests I will read too, but will
probably not build unless I hit the need myself — see the second point. Fork freely; that is what
the MIT license is for.

**Nothing here phones home.** Skills are instructions. They call no external service, collect
nothing, and send nothing anywhere.

---

## License

MIT — see [LICENSE](LICENSE).

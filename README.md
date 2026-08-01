# link-skills

**Decide it before you build it.**

Agent skills for the part of the work that happens before the code: surveying the options, arguing
the trade-offs out loud, checking what your platform can actually do, and writing the decision down
somewhere the next session can read it.

Every skill here leaves a plain-Markdown record of what was decided and why. Boards and mockups are
for people; the record is for the next agent — including you, three weeks later with none of the
context.

---

## Skills

### link-design-pitch

```bash
claude plugin install link-design-pitch@link-skills
```

**Two skills, one install.** Choosing a visual direction and applying it are separate runs, because
building the actual thing sits between them.

| | Invoked as | Does |
|---|---|---|
| **1** | `link-design-pitch:link-design-pitch` | Five questions — including what you are actually producing, since a spreadsheet and a web app deserve different options — then ten directions rendered with **your** real content, trade-offs argued in a table, feasibility checked against your platform, one recommendation with the strongest objection to it answered. **Stops for your choice.** |
| | *you build the features and content* | by hand or with another agent |
| **2** | `link-design-pitch:link-design-pitch-detail` | Applies the chosen direction to every surface with hierarchy and contrast *measured* rather than asserted, lists what has to change in the code, then lays out the interaction options and asks. Refuses to run without a direction on record. |

Works for any deliverable: web and desktop apps, mobile, slide decks, spreadsheets, documents,
printed reports.

**[Usage and worked example →](plugins/link-design-pitch/README.md)**

---

## Install

### Claude Code

Add the marketplace once:

```bash
claude plugin marketplace add Link-1214/link-skills
```

Then install. `link` is a bundle that ships nothing itself — it lists the others as dependencies, so
one install gets everything and new skills arrive on update without another install step:

```bash
claude plugin install link@link-skills
```

Or install a single plugin instead:

```bash
claude plugin install link-design-pitch@link-skills
```

Then reload so the skills register in the current session:

```bash
/reload-plugins
```

**A plugin is the install unit, not a skill.** `link-design-pitch` carries two skills and they always
arrive together. That is deliberate — the second is meaningless without the first.

The same steps work from inside a session as `/plugin marketplace add …` and `/plugin install …`.

### Check it worked

```bash
claude plugin list
```

You should see the plugin and its skills. Problems appear in the `/plugin` **Errors** tab, and
`claude plugin list --json` adds an `errors` field to anything that failed to load.

### Update and remove

```bash
claude plugin update link@link-skills
```

Auto-update is off by default for marketplaces that are not Anthropic's. Turn it on for this one in
`/plugin`, or run the command above.

```bash
claude plugin uninstall link-design-pitch
```

### Scope

Installs are user-scoped by default — available in every project. Add `--scope project` to commit the
choice to a repository your team shares, or `--scope local` to keep it to your own checkout.

### Codex and other agents

The skills are plain Markdown with no Claude-specific tooling, so any coding agent can follow them.
Nothing needs installing — clone and point at the file:

```bash
git clone https://github.com/Link-1214/link-skills.git
```

Then add to your project's `AGENTS.md`:

```markdown
Design direction undecided?
Follow <path-to>/link-skills/plugins/link-design-pitch/skills/link-design-pitch/SKILL.md

Direction chosen and the thing is built? Apply it with
<path-to>/link-skills/plugins/link-design-pitch/skills/link-design-pitch-detail/SKILL.md
```

[`AGENTS.md`](AGENTS.md) at the repo root is written for exactly this — which skill handles what,
and which reference files to load at which point.

---

## How these are built

Not a style guide for its own sake — knowing this tells you what you are installing.

**A skill is a procedure written as prose, with its reasoning intact.** Not a checklist. Where a step
matters the file says *why*, because a model that understands the reason handles the case the
checklist did not anticipate. Every rule in here that reads oddly specific is there because
something went wrong without it.

**Reference files load on demand, and the long ones are indexed.** `SKILL.md` is what always gets
read; anything lengthy sits in `references/` and is pulled in only for the phase that needs it. The
two catalogs open with an index so a run reads the ten entries it uses rather than all twenty-four —
that alone is 29% of a run's input.

**Skills stop at decisions rather than guessing past them.** Both of these end a run by asking. It is
the most important property here: work produced past a decision point is work the owner may throw
away, and it is also a decision quietly taken away from them.

**Nothing depends on a feature only one agent has.** Where a harness offers something better — a
structured question prompt, a hosted preview — the skill uses it when present and works without it
when absent. That is what keeps the clone path above viable.

**Changes come from use, not from planning.** Every revision so far came from a skill failing on a
real task: a pause that got skipped, a measurement taken against the wrong element, a bias baked into
the instructions. Nothing here was added because it seemed like a good idea.

Adding a skill to this repo: see [`AUTHORING.md`](AUTHORING.md).

---

## How this repo is run

Written down so you know what to expect before you depend on it.

**These are my tools, published.** They are built for work I actually do and shaped by what breaks in
it. That is why they are opinionated enough to be useful, and also why they may not fit your
situation. Read a skill before you run it — it is a few hundred lines of Markdown and it tells you
exactly what it will do.

**Versions are explicit and bumped by hand.** Each plugin pins a `version`, so you only move when I
publish. Patch for corrections, minor for new behavior, major if an invocation name or an output
contract changes. What ships is what passed a real run, not a draft. See [`CHANGELOG.md`](CHANGELOG.md).

**Issues and PRs are welcome; a reply is not promised.** Bug reports naming what you ran and what
happened are genuinely useful and I will read them. Feature requests I will read too, but will
probably not build unless I hit the need myself. Fork freely; that is what the MIT license is for.

**Nothing here phones home.** Skills are instructions. They call no external service, collect
nothing, and send nothing anywhere.

---

## License

MIT — see [LICENSE](LICENSE).

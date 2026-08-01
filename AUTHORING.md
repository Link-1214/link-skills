# Adding a skill to this repo

Written for me on a different machine, and for anyone forking this. Everything here came from
something breaking, not from a style preference.

## Where files go

```
plugins/<plugin>/
├── .claude-plugin/plugin.json      name · description · version · author · license
├── README.md                       usage, for humans browsing GitHub
└── skills/<skill>/
    ├── SKILL.md                    the procedure — always loaded when the skill triggers
    ├── AGENTS.md                   entry point for Codex and other agents
    └── references/*.md             loaded on demand, per phase
```

A plugin can hold several skills. **Put skills in the same plugin when one is meaningless without the
other** — installing a plugin installs all of its skills, so that is how you guarantee they travel
together. Separate plugins when someone might genuinely want one and not the other.

Register the plugin in `.claude-plugin/marketplace.json`, and add it to `plugins/link/`'s
`dependencies` array so the bundle install picks it up.

## Naming

The invocation is `<plugin>:<skill>`. Two constraints pull against each other:

- The plugin prefix already namespaces the skill, so short skill names read better.
- Anyone cloning the repo instead of installing gets the **folder name** with no prefix. A skill
  folder called `detail/` becomes `/detail` on their machine, which is a name nobody should own.

So: name skill folders for what they are in full, even when it repeats the plugin. `link-design-pitch`
and `link-design-pitch-detail` are verbose as `link-design-pitch:link-design-pitch-detail`, and they
are unambiguous on both install paths. Verbosity costs less than a collision.

## Writing the SKILL.md

**Frontmatter.** `name` must equal the folder name. `description` is the only thing the model sees
when deciding whether to invoke — write what it does *and* when to reach for it, and be a little
pushy, because skills under-trigger more often than they over-trigger.

**No `: ` inside the description.** An unquoted YAML scalar containing a colon-space parses as a
mapping and the frontmatter is silently dropped — the skill then loads with no metadata and never
triggers. Use an em dash. This has happened here, and `claude plugin validate` is what caught it.

**Explain why, not just what.** A model that knows the reason handles the case the instruction did
not anticipate. `"Compute rendered areas, confirm the hero is largest"` is a checklist item;
`"dominance is a claim about area and it inverts silently when an element spans two rows"` is
something the model can reason from.

**Every mandatory pause needs a reason attached.** Steps that stop and ask are the highest-value and
most-skipped instruction type. Say what running past it costs — the decision taken away from the
owner, and the work thrown out — or it will get run past.

**Keep an eye on what you are biasing.** A phrase like *"the answer is often a combination"* produced
a combination in two consecutive runs, from two different projects. If every run of a skill ends the
same way, look for the sentence that caused it.

## Reference files

Anything long goes in `references/` and gets loaded only for its phase. `SKILL.md` should name the
file and the phase that needs it.

**Index anything read partially.** A catalog of twenty-four that gets read whole so ten can be
chosen is paying three times over. Put an index at the top with exactly what selection needs, keep
the rest below, and **tell the skill to read the index first** — otherwise the file changes shape and
the read stays the same size.

**Split by what the information is for.** Selection needs "good at / where it breaks". Rendering
needs the palette and the type stance. Those are different readers at different moments, so they
belong in different places, and neither should repeat the other.

**Write indexes by hand.** Auto-summarising cuts mid-sentence, and what gets cut is the decisive
clause — *"contrast to ground is near zero by construction"*, *"perspective distorts perceived
magnitude"*. Those phrases are the whole reason an entry is in the index at all.

## Before committing

```bash
claude plugin validate ./plugins/<plugin> --strict
claude plugin validate .
```

The first checks the plugin manifest and every skill's frontmatter. The second checks the
marketplace catalog and that each `source` path resolves. Both must pass; `--strict` treats warnings
as errors.

Then check by hand:

- Does every `references/*.md` the SKILL.md names actually exist?
- Does `name` in frontmatter match the folder?
- If the skill writes files into a user's project, is the path named for **what is in it** rather
  than for the skill? A folder called `design-pitch/` at the root of someone else's repo says who
  made it, not what it holds. That one had to be moved after the fact.

## Versioning

`version` in `plugin.json` is explicit and bumped by hand, so users only move when you publish.

| Bump | For |
|---|---|
| patch | corrections, clearer wording, token reductions with no behavior change |
| minor | new phases, new reference files, new behavior |
| major | an invocation name changes, or the output contract changes |

Record it in `CHANGELOG.md`. If you want version constraints to resolve between plugins, tag the
release as `<plugin>--v<version>` — `claude plugin tag --push` derives the tag from the manifest.

## Testing a skill

There is no substitute for running it on something real. Three things that only show up that way:

1. **Whether it stops where it should.** Reading the instruction is not evidence; the first run of
   `link-design-pitch` blew past its own pause and produced detail nobody had asked for.
2. **Whether its measurements measure the right thing.** Two separate wrong findings came from
   comparing a highlighted element in one case against a plain element in another, and from a
   contrast helper that read `#FFFFFF` as black because it only parsed `rgb()`.
3. **Whether the output is the shape you expected.** Look at the rendered result, not only the
   numbers. A card with no visible boundary reads as broken long before anyone computes its contrast.

Run it on a project you do not already know the answer for. A skill you exercise on the project you
just designed by hand will appear to work because you are supplying the judgment, not the skill.

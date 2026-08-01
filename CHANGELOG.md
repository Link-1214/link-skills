# Changelog

Versions are pinned in each plugin's manifest and bumped by hand, so you only move when a release is
published. Patch for corrections, minor for new behavior, major if an invocation name or an output
contract changes.

## link-design-pitch

### 1.0.0

First release. Two skills in one plugin, because the second is meaningless without the first.

**`link-design-pitch`** — five questions, ten directions rendered with the project's real content,
trade-offs and feasibility argued in a table, one recommendation with the strongest objection to it
answered, then it stops for the owner's choice.

**`link-design-pitch-detail`** — applies the chosen direction to every surface, measures hierarchy
and contrast rather than asserting them, lists what has to change in the code, then presents the
interaction options and asks. Refuses to run without a chosen direction on record.

Shaped by two real runs — a PySide6 dashboard and a web kanban board — which between them produced
every rule that reads oddly specific:

- **The pauses are mandatory and stated twice.** The first run wrote a full detail spec before anyone
  had chosen a direction. Work past a decision point is work the owner may discard, and a decision
  taken from them.
- **A combination is never one of the ten.** Both early runs ended in a combination because the
  instructions said *"the answer is often a combination"*. Spending a slot on one covers nine ideas
  with ten panels, and what drops out is the stretch option that teaches the most.
- **Hierarchy is measured, and so is the channel it uses.** Three of four tabs in the first run had
  their hierarchy silently inverted by an element spanning two rows. In the second run the same rule
  nearly flagged a working design, because that one carried hierarchy in contrast rather than area.
- **Contrast is measured after opacity compositing.** Dimming other people's content to 50% reads as
  tasteful and lands at 3.5:1. Two accessibility failures were caught this way, one of them in a
  design already shipping.
- **Phase 5 presents options; it does not build them.** A full behavior spec written around
  "optimistic or confirmed" was invalidated in one sentence by a third answer nobody had offered.
- **Output goes where the project keeps its docs**, never in a folder named after the skill.

Also in this release: both catalogs open with a hand-written index so a run reads the ten entries it
uses rather than all twenty-four, cutting 29% of the input; the board is captured as a PNG so agents
with vision can see the styles rather than read markup; and `DECISION.md` is plain Markdown so the
decision survives the session that made it.

## link

### 1.0.0

Bundle plugin. Ships no skills — lists the others as dependencies so one install gets everything and
new skills arrive on update.

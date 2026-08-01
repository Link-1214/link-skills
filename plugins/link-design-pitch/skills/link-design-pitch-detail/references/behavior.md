# Behavior and states

Loaded in Phase 5, and only when the deliverable moves. A printed report, a deck, a spreadsheet
handed over as a file — none of these have states, and a table of them is noise.

**This file is a menu, not a specification to write out.** Phase 5 presents options and their
trade-offs and asks; it does not draw states or write behavior specs. Use the tables below to pick
the two or three forks worth putting to the owner, and to produce the states *checklist* — a line
each saying which apply and which do not.

The reason for the limit is cost. A full behavior specification runs longer than everything else in
both skills combined, and it is thrown away the moment the owner names a model you did not offer.
That has already happened: a complete spec was written around "optimistic vs confirmed", and the
answer was a third model — stage the moves, apply them together — which invalidated the failure
screens, the empty states, and the undo affordance in one sentence.

## The states that actually occur — as a checklist

Go through the list and mark which apply here, one line each. Marking one "does not occur" is a real
answer; the point is that someone checked. **Do not draw them.** Whoever builds this needs to know
the list exists and which entries are live — they do not need mockups of each.

The third column is why the entry is on the list at all: it names the failure it prevents, which is
what makes the checklist worth reading rather than skipping.

| State | The question it answers | Where it usually goes wrong |
|---|---|---|
| **Empty — first run** | Nothing exists yet | Shown as a blank rectangle. This is the one moment you have the user's full attention and a chance to say what the thing is for. |
| **Empty — filtered to nothing** | Data exists, this view has none | Rendered identically to first-run empty, so the user thinks their data is gone rather than that a filter is on. These two are different states with different copy and different exits. |
| **Loading — first paint** | Nothing on screen yet | A centered spinner tells the user nothing about what is coming. A skeleton in the shape of the result sets the expectation and stops the layout jumping. |
| **Loading — refreshing** | Something is already on screen | Replacing content with a spinner throws away what the user was reading. Keep the stale content and mark it as updating. |
| **Error — the whole view** | Nothing can be shown | "Something went wrong" with no exit. Say what failed and give the retry. |
| **Error — one item** | The rest is fine | One bad row taking down the page. Scope failures to the smallest thing that failed. |
| **Partial** | Some of it loaded | Silently showing 40 of 200 as if that were all of it. If the data is incomplete the screen has to say so, or every number on it is a lie. |
| **Overflow** | More than fits | Designed with five; production has ninety. Decide now: scroll, paginate, virtualize, or truncate with a count. |
| **Long content** | Text longer than the mockup's | The label that was one word is a long compound noun. Decide wrap, clamp, or ellipsis-with-tooltip per field, and pick the longest realistic value when you draw it. |
| **Zero-ish values** | 0, null, and "not applicable" | All three rendered as `0`, or all as `—`. They mean different things and at least the first two usually need to look different. |
| **Read-only / no permission** | The user cannot act here | Controls shown then failing on click. Absent or visibly disabled beats a lie. |
| **Stale / offline** | The data is old | Showing old numbers as if live. Timestamp it. |
| **In flight** | The user acted, it has not landed | No feedback, so they click again. See optimistic updates below. |

## Per-control states

Resting, hover, focus, active/pressed, disabled, selected, and where it applies, error and loading.

Two are skipped constantly and both matter more than hover:

- **Focus.** Anyone navigating by keyboard is lost without a visible focus ring. Removing the outline
  because it looks untidy makes the product unusable for them. Style it; do not delete it.
- **Disabled.** If a control is disabled, something has to say why, or the user just concludes the
  product is broken. Adjacent text, a tooltip, or an inline reason.

Hit targets stay comfortable — roughly 44px on touch. A drag handle that is hard to grab makes a
drag-first product feel broken no matter how it looks.

## Decisions to put to the owner

**These are choices, not deductions. Ask them.** Each is a fork with real consequences, and
defaulting silently is how a product ends up inconsistent with itself — one screen optimistic and
another confirmed, one autosaving and another not, and nobody remembers deciding either.

Do not ask all of them. Pick the **two or three that actually bite for this artifact**, give each a
recommendation with the reason, and let the owner answer. A read-mostly dashboard does not need the
autosave question; a form-heavy tool does not need the drag question.

The record's **one action** tells you which matter: whichever forks sit on that path are the ones to
ask about. The rest are noise, and asking about all of them makes the owner do work you were
supposed to do.

**Expect answers off your axis.** The forks below are the common shapes, not the space of possible
answers. When an owner describes a model you did not offer, that is the fork being framed too
narrowly — record their model in their words and list what it newly leaves undecided, rather than
pushing it back onto your two options.

**Optimistic or confirmed?** Optimistic — show the result immediately, reconcile later — makes the
product feel instant and suits high-frequency, low-stakes actions. It obliges you to design the
rollback: what the user sees when it fails, and how they learn it failed after they already moved
on. Confirmed suits anything where being wrong is expensive. *Recommend optimistic when the Phase 1
action is repeated many times a day; confirmed when it moves money, sends something, or is hard to
undo.*

**Undo or confirm?** A confirm dialog on every destructive action trains people to click through it,
at which point it protects nothing. *Recommend undo by default, with confirmation reserved for the
genuinely irreversible* — and say which actions those are, so the answer is concrete.

**Inline, panel, or modal?** Modals block everything and remove the context the user was comparing
against. A side panel keeps the surroundings visible. Inline editing is fastest and hardest to make
discoverable. *Recommend by whether the user needs to see the rest while acting* — if they do, a
modal is the wrong answer no matter how standard it looks.

**Autosave or explicit save?** Autosave needs a visible "saved" signal or users do not trust it.
Explicit save needs unsaved-change protection on navigate away. *Recommend one and hold to it
everywhere* — mixing both in one product is how people lose work.

**The keyboard path.** Not really a fork — for anything used daily this is required, so state it
rather than asking. Name the keyboard route through the Phase 1 action. Daily users build muscle
memory, and a mouse-only tool caps how fast they can ever get. Where the primary action is drag,
a keyboard equivalent is not optional: drag is unavailable to keyboard users entirely.

**Drag affordance.** If something is draggable, the resting state has to say so — a handle, a cursor
change, a lift on hover. Ask only whether drag is the primary path or a convenience; the answer
changes how much of the interaction budget it earns.

## Motion

Motion is for orientation: where a thing went, what changed, what is now loading. Motion as
decoration is cost without return, and on data screens it delays the read.

Keep transitions short — roughly 150–250ms for state changes, and let entrances be a touch slower
than exits. Animate transform and opacity where the platform is doing real compositing; animating
layout properties on a long list is how a smooth design becomes a janky build.

Two hard constraints:

- **Honor reduced-motion.** Where the platform exposes the preference, respect it, and make the
  reduced path still communicate the change — an instant swap, not a silent one.
- **Never let motion be the only carrier.** If the sole signal that something saved is a fade, then
  for anyone who never sees the fade, nothing saved.

And check Phase 0 before specifying any of it. A toolkit without transitions will silently ignore
every duration you write. Specify the instant version instead and say why.

## Feedback

For each action in the Phase 1 path, name what tells the user it worked. Silence is the most common
bug in otherwise finished software: the button was pressed, something happened somewhere, and the
user has no idea.

The strongest feedback is the interface simply showing the new truth — the card is in the new
column, the count went up. A toast is the fallback for when nothing visible changed. If your answer
to "what tells them it worked" is only a toast, look again at whether the screen could just show it.

## What to record

Into `DECISION.md`, not into a spec document:

1. **The forks you put to the owner and what they chose** — so the next person knows these were
   decided, not assumed. An interaction choice with no recorded owner is one that gets quietly
   reversed.
2. **If they answered outside the options**, their model in their words, and what it newly leaves
   undecided.
3. **Which states apply**, one line each. A checklist, not drawings.
4. **What is deliberately out of scope**, and why. "Offline is not handled in v1" is a decision;
   leaving it unmentioned is an omission someone finds in production.

Motion, durations, and per-state screens are for whoever builds it, working from these answers.

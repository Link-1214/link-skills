# Behavior and states

Loaded in Phase 4b, and only when the deliverable moves. A printed report has no states.

A mockup shows one moment: full data, nothing loading, nothing wrong, labels the length you happened
to type. Everything that sinks a build lives outside that moment. This file is the list of moments
you have to draw too.

## The states that actually occur

Not every screen has every one. Go through the list, mark which apply, and say what the screen looks
like in each. Marking one "does not occur here" is a real answer — the point is that you checked.

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

## Interaction decisions worth making explicitly

Each of these is a fork with real consequences, and defaulting silently is how a product ends up
inconsistent with itself.

**Optimistic or confirmed.** Optimistic (show the result immediately, reconcile later) makes the app
feel instant and is right for high-frequency, low-stakes actions like moving a card. It obliges you
to design the rollback: what the user sees when it fails, and how they learn it failed after they
already moved on. Confirmed (wait for the server) is right where being wrong is expensive.

**Undo or confirm.** A confirm dialog on every destructive action trains people to click through it,
which means it stops protecting anything. Undo after the fact is usually better and always faster.
Reserve confirmation for the genuinely irreversible.

**Inline, panel, or modal.** Modals block everything and lose the context the user was comparing
against. A side panel keeps the surrounding state visible. Inline editing is fastest and hardest to
make discoverable. Pick per task, then hold to it.

**Autosave or explicit save.** Autosave needs a visible "saved" signal or users do not trust it.
Explicit save needs unsaved-change protection on navigate away. Mixing both in one product is how
people lose work.

**The keyboard path.** For anything used daily, name the keyboard route through the primary action.
Daily users build muscle memory and a mouse-only tool caps how fast they can ever get.

**Drag affordance.** If something is draggable, the resting state has to say so — a handle, a cursor
change, a lift on hover. And drag needs a non-drag equivalent, because drag is unavailable to
keyboard users and awkward on touch.

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

## What to write down

In the spec, per screen:

1. Which states from the table apply, and what the screen looks like in each
2. The Phase 1 action's full path: resting → in-flight → success, and → failure
3. The keyboard route to that action
4. Motion, with durations, or an explicit "instant, platform has no transitions"
5. Anything deliberately not handled, and why

Point 5 matters as much as the rest. "Offline is out of scope for v1" is a decision. Leaving it
undrawn is an omission someone discovers in production.

# SVSI Flow Walkthrough

Step-by-step walkthrough of the **Supplier Voluntary Self-Inspection (SVSI)** task flow on ICW,
built for internal review of the design before the platform work starts.

**Live:** https://marconip2023.github.io/svsi-flow/

## What it covers

Seven steps, four roles, in the order a real task runs:

| Step | Owner |
| --- | --- |
| 00 · Before the task | Buyer |
| 01 · Application | Supplier, then Buyer |
| 02 · Invoice | Buyer → Supplier |
| 03 · Lab Audit | Lab (UL / BV) |
| 04 · QT Review | Buyer · WBA QT |
| 05 · Ethical Check | Buyer |
| 06 · SVSI Team Review | SVSI Team |
| 07 · Approve & Sign | Buyer, Supplier, SVSI Team |

## Clickable prototype

The page opens with links that play the Figma prototype:

- **End-to-end, everything approved** — one factory from *Set SVSI factory* through
  Application, Invoice, Lab Audit, QT Review, Ethical Check and SVSI Team Review to the
  supplier signing and *Complete task*. Switch role with the Lab / Buyer / Supplier chips
  in the top bar, or press → on a hand-off screen.
- **Per-role flows** — 8 Buyer, 7 Supplier, 3 Lab, plus Ethical and SVSI Team. These
  cover the alternatives the end-to-end path skips: return, reject, revise report,
  filters and detail tabs.

Every screen carries a Lab / Buyer / Supplier switch showing whose screen it is; clicking
a role goes to that role's home page.

Every screenshot and every list item links straight back to its frame in the
[SVSI Figma file](https://www.figma.com/design/aJIs39okLTRsQMwk96NWrC/SVSI?node-id=0-1),
so you can jump into the board wherever the discussion goes.

The Reference section at the bottom covers the Bronze/Silver/Gold ladder, what the
Agreement v6 and Addendum v3.1 documents actually ask for, and the open questions
that still need a decision from the team.

## Notes

- Screenshots are a snapshot of the Figma board at build time — the board keeps moving.
- Single static page: `index.html` plus `shots/`. Arrow keys ← → move between steps.
- `src/gen.py` + `src/tpl.html` generate the page body (frame ids, flows, card copy).
  Edit those, run `python3 src/gen.py` from `src/`, then wrap the output with the
  `<head>` used in `index.html`.

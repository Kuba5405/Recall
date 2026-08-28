# Recall — Plan

> Running record of Phase 1 (Discovery & Planning) decisions. Product only —
> tech stack, architecture and visual design are deliberately out of scope here.
> Sections marked **OPEN** have not been decided yet.

## Team & Complexity Calibration

Agreed in Phase 0, and it governs everything downstream:

- **Team size:** small team (2–5 people).
- **Complexity ambition:** commit to the fuller vision from the start, accepting
  a slower pace. Architecture decisions are not to be held back to keep things
  minimal.
- **Testing rigor:** professional / rigorous — high coverage expectations and
  strict CI gates that block merges.

## Core purpose

Recall is a **database of a person's brain**.

Things get into it in whatever form they arrive — photos, written notes, voice
notes, or content shared out of other apps such as Instagram, WhatsApp and
Facebook. An AI then transcribes, catalogs and tags what came in, so that it can
be found again later.

Retrieval works two ways: by specific detail (a name, a place), and by plain
language question — for example *"what restaurant did Marc send me on Instagram
last week?"*.

The product exists to solve forgetting. Everything else in this document should
trace back to that.

## Who it is for

Built **for the author first**, with the possibility that other people use it
later. It is not being designed for an external audience today, but that
possibility should not be architected out.

## What happens today, without it

Information arrives and is then effectively lost:

- It gets **forgotten** outright, or
- It still exists somewhere, but recovering it means **a lot of time searching**
  — scrolling back through message threads across different apps to find the one
  thing that was mentioned.

The cost is not storage. It is retrieval.

## Still open

Not yet discussed — each will be covered before this phase ends:

- Target platform(s)
- Core capture flow and how content actually enters the app
- Primary retrieval interface
- MVP feature scope: what is explicitly IN and explicitly OUT for v1
- Offline vs online requirements
- Privacy & security: data sensitivity, encryption at rest, where data may live,
  who else may ever access it
- Data retention & deletion, including whether anything needs a
  "permanently gone" guarantee
- Data export / backup capability
- Budget and cost constraints
- What "done" looks like for v1

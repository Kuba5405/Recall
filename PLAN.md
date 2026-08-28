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

## Platforms

- **Mobile is the primary target.** Which mobile operating systems — iOS,
  Android, or both — is **OPEN**.
- **A web app is also wanted**, alongside mobile rather than instead of it. Its
  role in v1 is **OPEN**.
- **An Electron desktop app is explicitly later**, once the project has scaled.
  Out of scope for v1.

## How content gets in

**Explicit capture, plus an automatic photo library scan.**

- Explicit: photos, written notes, voice notes, and content shared out of other
  apps through the operating system's share sheet.
- Automatic: scanning the camera roll for screenshots and photos, which is where
  saved recommendations tend to accumulate.

### Constraint accepted here

Instagram, WhatsApp and Facebook provide **no way for an app to read your
messages**. Content from those apps can only enter Recall when it is actively
shared into it, or captured as a screenshot. Recall can only recall what was
captured — it cannot reach back into a conversation that was never shared.

Passive capture of incoming message notifications — technically possible on
Android, impossible on iOS — was **considered and not chosen**.

## How content gets out

**A search box with filters** is the primary retrieval interface: search across
everything, narrowed by person, source app, date and content type.

Whether plain-language question answering (*"what restaurant did Marc send me on
Instagram last week?"*) is part of v1, layered on later, or dropped, is **OPEN** —
it is how the core purpose was originally described, so it needs settling
explicitly rather than by omission.

## Still open

Not yet discussed — each will be covered before this phase ends:

- Which mobile operating system(s), and whether the web app is in v1
- Whether plain-language question answering is in v1
- MVP feature scope: what is explicitly IN and explicitly OUT for v1
- Offline vs online requirements
- Privacy & security: data sensitivity, encryption at rest, where data may live,
  who else may ever access it
- Data retention & deletion, including whether anything needs a
  "permanently gone" guarantee
- Data export / backup capability
- Budget and cost constraints
- What "done" looks like for v1

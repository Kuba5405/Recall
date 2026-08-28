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

- **iOS and Android, both from the start.** The author uses Android today and
  switches to iPhone within three weeks, so a single-platform v1 would leave the
  primary user unsupported.
- **A web app is in v1, for search and review only.** Capture stays on the phone;
  the browser is for finding and reading things on a big screen.
- **An Electron desktop app is explicitly later**, once the project has scaled.
  Out of scope for v1.

### Distribution constraints, acknowledged

- iOS requires the **Apple Developer Program at $99/year** for any usable build.
  A free Apple ID expires the app every 7 days and, more importantly, cannot use
  **App Groups** — which a Share Extension needs to hand captured content to the
  main app. The free tier therefore removes the core capture feature, not just
  convenience. **This cost is accepted in principle and deferred**; it is not
  yet paid or scheduled.
- **Switzerland is not in the EU or EEA**, so the DMA routes — alternative app
  marketplaces and web distribution — are unavailable. TestFlight or the App
  Store are the only iOS distribution paths.
- **Android has no equivalent constraints**: no fee, no review, no expiry.

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

**v1 is deliberately bare-bones: a search box with filters, and nothing more.**
Search across everything, narrowed by person, source app, date and content type.

**Plain-language question answering is explicitly deferred to a later version.**
It is how the core purpose was originally described, so this is a conscious
staging decision rather than an omission: prove capture, transcription and
tagging first.

## Offline behaviour

**Capture works offline; processing happens when back online.** Content can
always be added with no connection; transcription, tagging and indexing run once
connectivity returns.

## AI approach — bring your own model

Recall does **not** ship its own hosted AI. Each user supplies the model:

- an **on-device model**, for users who want nothing leaving the phone, or
- an **API key** to a provider of their choice.

Consequences accepted: AI quality varies per user and is outside the product's
control, and the app must hold a user-supplied API key securely. Which of the
two modes v1 must support — one or both — is **OPEN**.

## Still open

- Privacy & security: data sensitivity, encryption at rest, where data may live,
  and whether anyone besides the author ever has access
- Data retention & deletion, including whether anything needs a
  "permanently gone" guarantee
- Data export / backup capability
- Hosting and storage budget — bring-your-own-AI removes the AI running cost,
  but not storage or sync costs
- MVP feature scope: the explicit IN / OUT list for v1
- What "done" looks like for v1

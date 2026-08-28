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

## Privacy & security

The content is as sensitive as personal data gets — photos, voice notes and
private messages. The decisions reflect that:

- **Storage:** the device is primary. An **encrypted copy syncs** so the web app
  and other devices can reach it, and so a lost phone is not a lost brain.
- **Encryption:** **end-to-end**. Keys never leave the user's devices and the
  server stores ciphertext it cannot decrypt.
- **Web search under E2EE:** the **browser downloads and decrypts the index**
  itself. The server is never given readable content or readable tags, at the
  cost of an initial sync into the browser and a decryption key held in the tab.
- **Access:** single user for now. Sharing an individual item with someone else
  is a plausible later feature and should not be designed out, but there are no
  accounts, no shared collections and no multi-user model in v1.

### Limits of the guarantee, accepted

**End-to-end encryption does not protect content from the AI provider.** When a
user supplies an API key, their photos and transcripts are sent to that provider
in readable form — unavoidable for a cloud model. E2EE protects the sync server,
not the model. Only the on-device mode keeps content private end to end.

## Data retention & deletion

- **Soft delete by default**, into a recoverable trash, so a mis-tap cannot
  destroy something irreplaceable.
- **Plus an explicit "permanently gone" action** for anything genuinely
  sensitive, guaranteeing removal from every copy including backups.
- E2EE strengthens this materially: destroying the key renders every encrypted
  copy unreadable, including copies no longer under the user's control.

## Data export & backup

**Wanted, but post-MVP.** Recorded as planned scope rather than forgotten. The
accepted risk in the meantime is that the only copy of this data lives inside an
application that is still proving itself.

## AI processing in v1

- **Both bring-your-own modes ship in v1**: an on-device model and a
  user-supplied API key. This doubles the processing pipeline and its tests, and
  is accepted deliberately under the "fuller vision" calibration.
- **No text extraction of any kind in v1.** Not a dedicated OCR pipeline, and not
  text read incidentally by a vision model — images are indexed by inferred tags
  and description only. Deferred to a later version.
- **Person attribution is manual in v1.** Automatic inference depends on reading
  the sender's name out of a screenshot's chat header, which requires text
  extraction; it arrives together with it in a later version.

Consequence accepted: a screenshot of a conversation is findable as an image
with inferred tags, not by the words inside it. The originating example —
*"what restaurant did Marc send me"* — is not answerable by v1, by design.

## Still open

- MVP feature scope: the explicit IN / OUT list for v1
- Hosting and storage budget — **deliberately deferred**, to revisit before
  Phase 2 makes architecture decisions that depend on it
- What "done" looks like for v1

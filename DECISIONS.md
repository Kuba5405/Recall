# Decision Log

A dated trail of *changes* to decisions already recorded in `PLAN.md`,
`ARCHITECTURE.md`, `DESIGN.md`, or `CODING_STANDARDS.md`.

Those documents always reflect current reality. This file records how we got
there: whenever a previously recorded decision changes, add a short dated entry
here — what changed, what it was before, and why — rather than silently editing
the original document.

## Entries

<!-- Format:
### YYYY-MM-DD — <short title>
- **Document:** which doc the decision lives in
- **Was:** the previous decision
- **Now:** the new decision
- **Why:** the reason it changed
-->

### 2026-08-28 — Repository is public rather than private

- **Document:** global project rules (Phase 0, step 9)
- **Was:** push the repository to GitHub as a private repository.
- **Now:** the repository is public.
- **Why:** the owning account is on GitHub Free, where branch protection and
  rulesets are rejected on private repositories, and secret scanning is
  unavailable on private repositories below Advanced Security. Going public was
  chosen over paying for GitHub Pro; it also enabled secret scanning, which Pro
  would not have provided on a private repository.

### 2026-08-28 — Version bumps and release tags are automated

- **Document:** global project rules (git workflow — versioning & tags)
- **Was:** `VERSION` and `CHANGELOG.md` updated by hand in each pull request into
  `dev`; tags created only on `main`, only on explicit per-release approval.
- **Now:** a pull request into `dev` bumps patch, into `staging` bumps minor, and
  into `main` bumps major. The base is the highest version across `dev`,
  `staging` and `main`, so the sequence stays correct without back-merges. The
  `[Unreleased]` changelog section is rolled into a dated release section
  automatically, and the `v<VERSION>` tag is created automatically when `main`
  is updated — merging into `main` is the approval.
- **Why:** requested, to remove manual bookkeeping and make the version reflect
  promotion stage. Accepted consequence: MAJOR counts releases to `main` rather
  than signalling breaking changes, so the number no longer carries Semantic
  Versioning's meaning.

### 2026-08-28 — Promotions go through release/vX.Y.Z branches

- **Document:** global project rules (git workflow — branches)
- **Was:** promotion from `dev` to `staging` to `main` happens by pull request
  directly between those branches.
- **Now:** promotions are made from a `release/vX.Y.Z` branch cut off the source
  branch, and that branch is opened as a pull request into the target.
- **Why:** the version bump is committed to the pull request's head branch before
  merge. A direct `dev` -> `staging` pull request would require writing to `dev`,
  which branch protection blocks. The repository is user-owned, so GitHub Actions
  cannot be granted a ruleset bypass to push to protected branches at all.

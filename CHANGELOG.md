# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2026-08-28

### Changed

- Merged pull request branches are now deleted automatically, leaving only
  `main`, `staging`, `dev` and branches with work in progress.

## [0.1.1] - 2026-08-28

### Added

- Initial repository scaffolding: git workflow, versioning, changelog, license,
  environment template, and decision log.
- Automated version bumping: a pull request into `dev`, `staging` or `main`
  bumps the patch, minor or major version respectively, computed from the
  highest version across those three branches.
- Automatic release tagging when `main` is updated.
- A `skip-version` label to exempt trivial or docs-only pull requests from the
  version bump.

## [0.1.0] - 2026-08-28

### Added

- Repository initialized.

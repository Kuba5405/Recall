#!/usr/bin/env python3
"""Compute and apply the next project version for a pull request.

Bump size is decided by the branch the pull request targets:

    dev      -> patch    (0.1.19 -> 0.1.20)
    staging  -> minor    (0.1.19 -> 0.2.0)
    main     -> major    (0.7.0  -> 1.0.0)

The base version is the HIGHEST version found across dev, staging and main
rather than the version on any single branch. That keeps the sequence correct
without back-merges: once staging reaches 0.2.0, the next pull request into dev
continues from 0.2.0 and produces 0.2.1, not 0.1.20.

Writes the new VERSION and rolls CHANGELOG.md's [Unreleased] section into a
dated release section. Committing and pushing is left to the workflow.
"""

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VERSION_FILE = REPO_ROOT / "VERSION"
CHANGELOG_FILE = REPO_ROOT / "CHANGELOG.md"

PERMANENT_BRANCHES = ("dev", "staging", "main")
BUMP_FOR_BASE = {"dev": "patch", "staging": "minor", "main": "major"}
SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def parse(version: str) -> tuple[int, int, int]:
    match = SEMVER_RE.match(version.strip())
    if not match:
        sys.exit(f"::error::'{version}' is not a MAJOR.MINOR.PATCH version")
    return tuple(int(part) for part in match.groups())


def version_on_branch(branch: str) -> tuple[int, int, int] | None:
    """Read VERSION from a remote branch, or None if it isn't readable there."""
    result = subprocess.run(
        ["git", "show", f"origin/{branch}:VERSION"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        return None
    return parse(result.stdout)


def highest_released_version() -> tuple[int, int, int]:
    found = [v for v in (version_on_branch(b) for b in PERMANENT_BRANCHES) if v]
    if not found:
        sys.exit("::error::could not read VERSION from dev, staging or main")
    return max(found)


def bump(version: tuple[int, int, int], kind: str) -> tuple[int, int, int]:
    major, minor, patch = version
    if kind == "major":
        return (major + 1, 0, 0)
    if kind == "minor":
        return (major, minor + 1, 0)
    return (major, minor, patch + 1)


def split_unreleased(text: str) -> tuple[str, str, str]:
    """Split the changelog into (before, unreleased body, after)."""
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.strip().lower().startswith("## [unreleased]"):
            start = index
            break
    else:
        sys.exit("::error::CHANGELOG.md has no '## [Unreleased]' section")

    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break

    return "".join(lines[: start + 1]), "".join(lines[start + 1 : end]), "".join(lines[end:])


def roll_changelog(new_version: str) -> None:
    text = CHANGELOG_FILE.read_text()
    header, body, rest = split_unreleased(text)

    if not body.strip():
        sys.exit(
            "::error::CHANGELOG.md's [Unreleased] section is empty. Describe this "
            "change under [Unreleased], or add the 'skip-version' label if it is "
            "a trivial/docs-only change that needs no version bump."
        )

    today = datetime.date.today().isoformat()
    released = f"## [{new_version}] - {today}\n{body.rstrip()}\n\n"
    CHANGELOG_FILE.write_text(f"{header}\n{released}{rest}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="branch the PR targets")
    args = parser.parse_args()

    if args.base not in BUMP_FOR_BASE:
        print(f"::notice::'{args.base}' is not a versioned branch; nothing to do")
        return

    new_version = ".".join(
        str(part) for part in bump(highest_released_version(), BUMP_FOR_BASE[args.base])
    )
    current = VERSION_FILE.read_text().strip()

    if current == new_version:
        print(f"::notice::VERSION is already {new_version}")
        return

    VERSION_FILE.write_text(f"{new_version}\n")
    roll_changelog(new_version)
    print(f"::notice::bumped {current} -> {new_version} ({BUMP_FOR_BASE[args.base]})")


if __name__ == "__main__":
    main()

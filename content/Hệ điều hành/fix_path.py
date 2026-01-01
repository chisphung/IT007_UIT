"""Utility to reconcile attachment references inside the Hệ điều hành vault section.

This script scans every Markdown file under the requested root directory and looks
for attachment references in the Obsidian-style format `![[filename.ext]]`. When an
attachment is referenced but not present in the destination attachments directory,
the script attempts to locate the file inside the shared `Assets` folder and moves
it into place.

Example usage (defaults already set for the current workspace):

    python fix_path.py                # real move
    python fix_path.py --dry-run      # preview changes only

Use `--help` for the complete list of arguments.
"""

from __future__ import annotations

import argparse
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

try:  # Ensure Windows console can display Unicode paths.
    import sys

    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8")
except Exception:  # pragma: no cover - best-effort fallback only.
    pass

DEFAULT_ROOT = Path(
    r"C:\Users\User\OneDrive - 71205\Documents\Obsidian Vault\Hệ điều hành"
)
DEFAULT_ATTACHMENTS = DEFAULT_ROOT / "attachments"
DEFAULT_ASSETS = Path(
    r"C:\Users\User\OneDrive - 71205\Documents\Obsidian Vault\Assets"
)

ATTACHMENT_PATTERN = re.compile(r"!\[\[([^\]]+)\]\]")


@dataclass
class Stats:
    scanned_files: int = 0
    references_found: int = 0
    already_present: int = 0
    moved: int = 0
    planned: int = 0
    missing: list[tuple[str, Path]] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)

    def report(self) -> str:
        lines = [
            f"Markdown files scanned: {self.scanned_files}",
            f"Unique attachments referenced: {self.references_found}",
            f"Already in attachments: {self.already_present}",
            f"Moved from Assets: {self.moved}",
        ]
        if self.planned:
            lines.append(f"Pending moves (dry-run): {self.planned}")
        if self.missing:
            lines.append(f"Missing attachments: {len(self.missing)} (see details above)")
        if self.failures:
            lines.append(f"Warnings: {len(self.failures)} (see details above)")
        return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Move referenced attachments from the shared Assets folder into "
            "Hệ điều hành/attachments if they are missing."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="Folder that contains the Markdown notes to scan.",
    )
    parser.add_argument(
        "--attachments",
        type=Path,
        default=DEFAULT_ATTACHMENTS,
        help="Destination folder where attachments should live.",
    )
    parser.add_argument(
        "--assets",
        type=Path,
        default=DEFAULT_ASSETS,
        help="Source folder to search for misplaced attachments.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without moving any files.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress verbose logs. Summary is still printed.",
    )
    return parser.parse_args()


def extract_attachment_names(markdown_text: str) -> set[str]:
    """Return the unique file names referenced via Obsidian embeds."""

    names: set[str] = set()
    for match in ATTACHMENT_PATTERN.finditer(markdown_text):
        reference = match.group(1).split("|", 1)[0].strip()
        if not reference:
            continue
        # Only use the terminal name so nested folders don't duplicate hierarchy.
        names.add(Path(reference).name)
    return names


def read_markdown_file(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Retry with UTF-16 for safety.
        try:
            return path.read_text(encoding="utf-16")
        except Exception:
            return None


def build_asset_index(assets_root: Path) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = defaultdict(list)
    if not assets_root.exists():
        return index
    for file_path in assets_root.rglob("*"):
        if file_path.is_file():
            index[file_path.name.casefold()].append(file_path)
    return index


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def log(message: str, quiet: bool) -> None:
    if not quiet:
        print(message)


def relocate_attachments(
    root_dir: Path,
    attachments_dir: Path,
    assets_dir: Path,
    *,
    dry_run: bool = False,
    quiet: bool = False,
) -> Stats:
    stats = Stats()

    if not root_dir.exists():
        raise FileNotFoundError(f"Root directory not found: {root_dir}")
    if not assets_dir.exists():
        raise FileNotFoundError(f"Assets directory not found: {assets_dir}")

    ensure_directory(attachments_dir)
    asset_index = build_asset_index(assets_dir)

    for md_file in root_dir.rglob("*.md"):
        if attachments_dir in md_file.parents:
            # Skip notes that might exist inside the attachments folder.
            continue
        stats.scanned_files += 1
        content = read_markdown_file(md_file)
        if content is None:
            stats.failures.append(f"Could not read {md_file}")
            log(f"⚠️  Skipped unreadable file: {md_file}", quiet)
            continue

        referenced_names = extract_attachment_names(content)
        if not referenced_names:
            continue
        stats.references_found += len(referenced_names)

        for name in referenced_names:
            destination = attachments_dir / name
            if destination.exists():
                stats.already_present += 1
                continue

            key = name.casefold()
            candidates = asset_index.get(key, [])
            if not candidates:
                stats.missing.append((name, md_file))
                log(
                    f"❌  Missing attachment '{name}' referenced in {md_file}",
                    quiet,
                )
                continue

            source = candidates.pop(0)
            if not candidates:
                asset_index.pop(key, None)

            ensure_directory(destination.parent)
            action = "Would move" if dry_run else "Moving"
            log(f"{action}: {source} -> {destination}", quiet)

            if dry_run:
                stats.planned += 1
                continue

            shutil.move(str(source), str(destination))
            stats.moved += 1

    return stats


def main() -> None:
    args = parse_args()
    stats = relocate_attachments(
        args.root.expanduser(),
        args.attachments.expanduser(),
        args.assets.expanduser(),
        dry_run=args.dry_run,
        quiet=args.quiet,
    )
    print("\nSummary\n-------")
    print(stats.report())
    if stats.missing:
        print("\nMissing attachments list:")
        for name, md_file in stats.missing:
            print(f"  - {name} (referenced in {md_file})")
    if stats.failures:
        print("\nWarnings:")
        for message in stats.failures:
            print(f"  - {message}")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Validate the standalone examples without installing a project toolchain."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ("portfolio-tile", "performance-waterfall", "transaction-network")


def main() -> int:
    failures: list[str] = []
    for name in EXAMPLES:
        folder = ROOT / "examples" / name
        html = folder / "index.html"
        preview = folder / "preview.svg"
        if not html.exists():
            failures.append(f"missing {html.relative_to(ROOT)}")
            continue
        if not preview.exists():
            failures.append(f"missing {preview.relative_to(ROOT)}")
        text = html.read_text(encoding="utf-8")
        checks = {
            'English document': 'lang="en"' in text,
            'accessible SVG': 'role="img"' in text and ('aria-labelledby' in text or 'aria-label' in text),
            'declared method': "Method:" in text,
            'no external assets': not re.search(r"(?:src|href)=['\"]https?://", text),
            'no generative image tool': "image_gen" not in text and "Image Generator" not in text,
            'responsive viewport': 'name="viewport"' in text,
        }
        for label, passed in checks.items():
            if not passed:
                failures.append(f"{name}: {label}")

    if failures:
        print("Example validation failed:")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print(f"Validated {len(EXAMPLES)} deterministic examples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Examples

These examples are intentionally small, deterministic, and dependency-free.
They use labeled synthetic data so a reader can open the HTML source, inspect
the rules, and change the data without installing a build toolchain.

| Example | Decision | Source |
|---|---|---|
| [Portfolio comparison tile](portfolio-tile/) | Compare heterogeneous securities with normalized bands and benchmark context | `portfolio-tile/index.html` |
| [Performance waterfall](performance-waterfall/) | Explain how contributions and return components produce a total | `performance-waterfall/index.html` |
| [Transaction network](transaction-network/) | Explore typed relationships while preserving a readable mental map | `transaction-network/index.html` |

## Run locally

Open an example's `index.html` directly, or serve the repository root:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/examples/`.

Run the repository-level smoke check with:

```bash
python3 scripts/validate_examples.py
```

All three examples use the QuantSeras dark Material 2 baseline: neutral dark
surfaces, restrained purple and teal semantic accents, high/medium text roles,
visible labels, and deterministic geometry. No image generator, external font
request, or third-party asset is required.

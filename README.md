# Dataset Lineage Validator

Validates declared data lineage edges for missing nodes, duplicate edges, self-links, and cycles.

## Architecture

```text
JSON payload → domain algorithm → evidence-backed findings → human review
                              └→ OpenAI / CrewAI / Claude Code / Lyzr export surfaces
```

The core implementation is `agent.py` and exposes `analyze(payload)`. Tests include valid, malformed, boundary, and domain-specific cases.

## Run

```bash
python3 agent.py examples/good-input.json
python3 -m unittest discover -s tests -v
python3 tools/audit-dataset-lineage-validator.py examples/good-input.json
```

## Limitations

This checks structural lineage declarations only. It cannot verify that transformations actually ran or that source data is accurate.

#!/usr/bin/env bash
set -euo pipefail
INPUT=${1:-}
OUTPUT=${2:-}
if [[ -z "$INPUT" || -z "$OUTPUT" ]]; then
  echo "usage: render_mermaid.sh <input.mmd> <output.svg|png>" >&2
  exit 1
fi
if command -v mmdc >/dev/null 2>&1; then
  mmdc -i "$INPUT" -o "$OUTPUT"
else
  echo "mmdc not found; install @mermaid-js/mermaid-cli to render Mermaid files" >&2
  exit 2
fi

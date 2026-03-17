#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -eq 0 ]; then
    echo "Usage: $0 file1.gds file2.gds ..."
    exit 1
fi

for g in "$@"; do
    [ -f "$g" ] || { echo "ERROR: file not found: $g" >&2; exit 1; }

    cell=$(basename "$g" .gds)

    echo "=== Processing $g (cell $cell) ==="

    magic -dnull -noconsole -rcfile ~/.ciel/ihp-sg13g2/libs.tech/magic/ihp-sg13g2.magicrc <<EOF
gds read $g
load $cell
lef write ${cell}.lef -hide
quit
EOF
done

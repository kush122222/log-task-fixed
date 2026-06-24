#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
import json
import re
from collections import Counter

paths = Counter()
ips = set()
total = 0

with open("/app/access.log", "r", encoding="utf-8") as f:
    for raw_line in f:
        line = raw_line.strip()
        if not line:
            continue

        total += 1
        ips.add(line.split()[0])

        match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH|OPTIONS) (\S+) HTTP/', line)
        if match:
            paths[match.group(1)] += 1

top_path = sorted(paths.items(), key=lambda item: (-item[1], item[0]))[0][0]

with open("/app/report.json", "w", encoding="utf-8") as f:
    json.dump(
        {
            "total_requests": total,
            "unique_ips": len(ips),
            "top_path": top_path,
        },
        f,
    )
PY

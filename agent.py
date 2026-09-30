
#!/usr/bin/env python3
"""Deterministic, local-only passport implementation."""
import json
import math
import sys
from pathlib import Path

DOMAIN = 'Dataset Lineage Validator'

def _num(value, name, findings):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)):
        findings.append(f"{name}: must be a finite number")
        return 0
    return value

def analyze(payload):
    if not isinstance(payload, dict):
        raise ValueError("payload must be an object")
    findings = []
    nodes=payload.get("nodes"); edges=payload.get("edges")
    if not isinstance(nodes,list) or not isinstance(edges,list): raise ValueError("nodes and edges are required")
    known=set(nodes)
    if len(known)!=len(nodes) or any(not isinstance(n,str) or not n for n in nodes): findings.append("node IDs must be unique non-empty strings")
    graph={n:[] for n in known}; seen=set()
    for e in edges:
        if not isinstance(e,dict): raise ValueError("edges must be objects")
        a=e.get("source"); b=e.get("target")
        if a not in known or b not in known: findings.append(f"edge references undeclared node: {a} -> {b}"); continue
        if a==b: findings.append(f"self-link at {a}")
        if (a,b) in seen: findings.append(f"duplicate edge {a} -> {b}")
        seen.add((a,b)); graph[a].append(b)
    visiting=set(); visited=set()
    def visit(n):
        if n in visiting: return True
        if n in visited: return False
        visiting.add(n)
        cycle=any(visit(child) for child in graph[n])
        visiting.remove(n); visited.add(n)
        return cycle
    if any(visit(n) for n in graph if n not in visited): findings.append("lineage graph contains a directed cycle")
    return {"domain": DOMAIN, "status": "needs-review" if findings else "ready", "findings": findings}

if __name__ == "__main__":
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    payload = json.loads(source.read_text(encoding="utf-8") if source else sys.stdin.read())
    print(json.dumps(analyze(payload), indent=2, sort_keys=True))

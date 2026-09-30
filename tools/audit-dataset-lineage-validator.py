import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agent import analyze
source = Path(sys.argv[1]) if len(sys.argv) > 1 else None
payload = json.loads(source.read_text(encoding="utf-8") if source else sys.stdin.read())
print(json.dumps(analyze(payload), indent=2, sort_keys=True))

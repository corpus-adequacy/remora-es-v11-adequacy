# External CA adapter; upstream checker and suites remain unchanged.
import json, sys
from pathlib import Path
from copy import deepcopy
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'conformance/evidence-sufficiency-v1.1'))
from run_evidence_sufficiency import load_json, assess
mode,vec=sys.argv[1:]
cid=load_json(Path(vec))["id"]
case={c["id"]:c for c in load_json(HERE/'conformance/evidence-sufficiency-v1.1/cases.json')["cases"]}[cid]
v=assess(case["claim"],deepcopy(case["observations"]),scope={"kind":"synthetic_fixture","suite":"evidence-sufficiency-v1.1","bounded":True,"case":cid}).as_dict()
if mode=="verdict":
 print(json.dumps({"status":v["status"],"reason":v["reason"]}))
else:
 print(json.dumps({"missing_evidence":"|".join(v["missing_evidence"]),"decisive_if":v.get("decisive_if") or ""}))

# External CA adapter: only failures is scored, never source hashes.
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'conformance/evidence-sufficiency-v1.1'))
from run_evidence_sufficiency import build_record
print(json.dumps({"failures":"|".join(sorted(build_record()["failures"]))}))

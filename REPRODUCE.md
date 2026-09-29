# Reproduce on new copies, one row at a time

The subject is both upstream directories at `57ee0351a6acd6c1dd865ca933603469ab519cd4`. Preserve the relative `conformance/evidence-sufficiency-v1` and `conformance/evidence-sufficiency-v1.1` paths. Extract them into a new subject directory, then copy adapter contents and the six manifests to that root. Never run against the retained original subject or report files.

Use CA at `5fa2ff587497b00ac684a767335b9068f7e520a6`, Python 3.14.3, stdlib only. For each manifest, sequentially:

```sh
python3 -B ca/corpus_adequacy.py subject/ca_known-row1-verdict.manifest.json --json > new-row1.json
```

Repeat for known-row2-guidance, known-row3-runner, additional-row1-verdict, additional-row2-guidance, additional-row3-runner. Exit 1 can be a completed measurement with survivors; inspect controls and failures before interpretation. Never mix a source-hash snapshot check into the outcome. Full upstream trees, adapters and manifests are bound by RUN-PLAN-FROZEN.json.

The original reports are retained locally. This package contains explicitly derived reports with portable manifest paths; ORIGINAL-TO-DELIVERY.json documents the sole change and both digests. No network isolation is supplied by trusted-local. Obtain source first; the measured checker and adapters use no network calls.

The additional fault manifest was frozen before measurement and publicly committed by hash. Its contents are disclosed in this package, so it is a known set after delivery. Publication of this package is not yet approved; v1.0 publication consent is separate.

# REMORA evidence-sufficiency v1.1 — private result for factual correction

Source: `57ee0351a6acd6c1dd865ca933603469ab519cd4`. Checker remains byte-identical to v1 (`c4ca50aee2b2918b11c6fbde1f8615ca6c6bf1e5b6fa2ac1775f49c5e8c20be0`). Only corpus and runner differ upstream. CA is pinned to `5fa2ff587497b00ac684a767335b9068f7e520a6` (0.7.0), Python 3.14.3, Darwin arm64, local standard-library process execution.

This is not yet a public result. The public v1.0 package remains unchanged apart from a separate README documenting publication and later decisions. No retrospective v1.0 exclusion was applied. Owner's latest scope includes premise typing and semantic guard precedence. The v1.1 corpus was written with the known faults in view.

## Known set — identical mutation definitions and projections

| Projection | v1.0 killed / survived | v1.1 killed / survived | v1.1 crash kills included |
|---|---:|---:|---:|
| row1-verdict | 53 / 27 | 80 / 0 | 2 |
| row2-guidance | 59 / 44 | 90 / 13 | 2 |
| row3-runner | 55 / 48 | 103 / 0 | 2 |

Row 1 retains the original 80-fault selection (guidance class excluded). Rows 2 and 3 retain 103 faults each. Row 2 projects `missing_evidence` and `decisive_if`; row 3 projects the sorted `failures` list, not `--check` or checker identity. The corpus grew from 26 to 50 authored cases. Differences therefore describe this changed corpus/runner against known faults, not an unfitted generalisation test. Counts from the maintainer's own preflight were known in advance and are not an independent expectation oracle.

## Additional set — withheld definitions, not six fresh behavioral faults

The six operators were frozen before our mutation runs at SHA-256 `d07e8d280248d893949749f2fbb61d62608690c42414d4ca340b80bed268edaa`; the complete run plan was `4cdc78bf2fa73e4f39e93268127495700d9be8f008529ba6023b05ad900ebbdd`. Both hashes were published before execution in public commit `f2dac555603269f78099098312cfe4268de1f0d4` of Rul1an/remora-es-v1-adequacy.

The author had seen the public v1.1 design, runner and maintainer's aggregate preflight results before choosing these operators. New case inputs were read after the six-pair file was saved. This is withheld-from-maintainer evidence, not blind or independent selection. No exact known anchor/replacement pair or the owner's `is not True` to `is False` operator is reused, but the adversarial review found two proven behavioral overlaps on the declared JSON adapter path: the admission alias reuses `admission_source_accepted`, already established by the preceding guard, so it is equivalent to the known mutation forcing `admission_matches` true; the postcondition alias reuses `source_accepted`, already established earlier, so it is equivalent to removing the target/predicate guard. Both were killed. They are retained in the six measured rows but are not fresh behavioral evidence. The route alias also overlaps guard-removal behavior, while changing which reason is returned when `outside_required_pep` fails; no independence or entirely new fault-family claim is made for it. After this disclosure these six faults are known and cannot be presented as a fresh held-out set again. No additional-set v1.0 run was made; the before/after comparison above is for the known set only.

| Additional fault | Row 1 | Row 2 | Row 3 |
|---|---|---|---|
| [H] admission match borrows source acceptance | killed | killed | killed |
| [H] route binding borrows route location | killed | killed | killed |
| [H] postcondition binding borrows source acceptance | killed | killed | killed |
| [H] canonical string values case-folded | survived | survived | survived |
| [H] canonical list order erased | survived | survived | survived |
| [H] canonical mapping values ignored | survived | survived | survived |

| Additional projection | Killed / survived | Crash kills included |
|---|---:|---:|
| row1-verdict | 3 / 3 | 0 |
| row2-guidance | 3 / 3 | 0 |
| row3-runner | 3 / 3 | 0 |

These are six selected behavior changes, not six independent samples or a coverage score. A survivor means no distinction on that declared projection under this corpus; it is not a checker defect. The canonical comparison operators affect terminal state comparisons, so guidance-only outcomes can remain unchanged by construction. No missing result is silently reclassified as equivalent or out of scope. Maintainer dispositions should be recorded separately before any subsequent corpus change.

## Controls, crashes and integrity

Every row runs the unchanged positive control (`_unknown` returns ESTABLISHED) and inert docstring control. Positive must be killed; inert must remain unchanged. Original tool verdicts are retained locally. Delivery copies preserve every field except the top-level local `manifest` path, as documented below. For ordinary faults, `killed` means a declared-projection change or an unexpected exit as classified by CA; crash kills are not counted as changes through the declared fields. `survived` means not distinguished on the declared projection. No independent branch-reach proof is claimed for every mutant. Neither healthy controls nor agreement with expected counts proves all mutation sites were exercised.

Crash-kill labels by row:

- known-row1-verdict: [1] postcondition_observed: guard 'state_value_missing' half `"expected_state" not in o` removed; [1] postcondition_observed: guard 'state_value_missing' half `"observed_state" not in o` removed.

- known-row2-guidance: [1] postcondition_observed: guard 'state_value_missing' half `"expected_state" not in o` removed; [1] postcondition_observed: guard 'state_value_missing' half `"observed_state" not in o` removed.

- known-row3-runner: [1] postcondition_observed: guard 'state_value_missing' half `"expected_state" not in o` removed; [1] postcondition_observed: guard 'state_value_missing' half `"observed_state" not in o` removed.

- additional-row1-verdict: none.

- additional-row2-guidance: none.

- additional-row3-runner: none.

Before execution all 50 baseline verdicts matched the authored expectations and the full runner had no failures. Both upstream directories were checked byte for byte against the fixed commit. Every mutation anchor was unique and every replacement parsed. After every row, every pinned source, configuration and adapter byte was rechecked against the frozen plan. No dependencies installed, no hosted experiment, no candidate network operations requested; trusted-local does not provide OS-enforced network isolation.

All rows were sequential on one locked subject tree. Execution logs preserve exit status and elapsed time; reports include their tool and manifest identities. Exit 1 can mean a completed measurement with survivors, not failed execution. Recount reads retained reports without importing the producer or checker. A nonbuilder Codex source review preceded execution; it is not an externally independent review or authenticated maintainer validation. Result review is recorded separately. No production/security/conformance/endorsement claim, no aggregate over projections, and no comparative product score.

Prepared with AI assistance. Candidate source and quoted mutation material retain the original BUSL-1.1 terms and attribution in NOTICE. Private first, per issue #629; publication of this v1.1 result remains separate from permission to publish v1.0.

## Delivery transformation and adversarial correction

This report supersedes the initial private summary solely to correct novelty framing and explain minimal delivery. No measurement was rerun, no fault definition changed, and the six-fault denominator was not reduced after seeing results. Two killed aliases duplicate known behavior; the three surviving canonicalization changes remain named observations for owner classification, not automatically accepted open gaps.

The six files under results/ are **derived delivery copies**, not byte-identical original report.v0 artifacts. Only the top-level manifest string was replaced with the corresponding relative manifests/ path. Every other parsed value, including manifest digest, mutant records, verdicts, controls, tool identity and count, is unchanged. ORIGINAL-TO-DELIVERY.json binds each original SHA-256 to its delivery SHA-256. Original bytes remain retained locally; a reader with delivery copies alone cannot independently verify the originals' digests. Treat delivery copies as transparent projections, not as original signed/attested artifacts. Empty stderr logs and private operator-consent notes are omitted.

The run plan and frozen fault-file bytes are included exactly as precommitted. Baseline and run chronology are producer records. The read-only adversarial/result reviews are by a separate Codex agent, not externally independent or authenticated reviews. They did not rerun the experiment.

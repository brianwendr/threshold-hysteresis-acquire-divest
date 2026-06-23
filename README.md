# Supplementary Material S1: Replication package

This package supports the manuscript **A Finite-State Threshold Policy for Dynamic Acquire-Divest Decisions with Transaction Costs**

## Contents

- `config/capabilities.csv`: capability parameters and prerequisites.
- `config/paths.csv`: budget paths used in the trace examples.
- `src/replicate_hysteresis.py`: Python script for regenerating the main threshold tables and core certificates. The script uses only the Python standard library.
- `output/manuscript_table2_capability_parameters.csv`: values in Table 2.
- `output/manuscript_table3_threshold_verification.csv`: values in Table 3.
- `output/manuscript_table4_algorithmic_trace_certificates.csv`: values in Table 4.
- `output/greedy_acquisition_path.csv`: greedy closure-compatible path for Proposition 2.
- `output/switching_variation_bound.csv`: total-variation switching bound for Lemma 4.
- `output/tightness_switching_bound.csv`: asymptotic tightness construction for Proposition 3.
- `output/reachability_certificate.csv`: bounded-range reachability certificate for Theorem 3.
- `output/chain_decomposable_reachability_complexity.csv`: chain-decomposable polynomial complexity calculation for Corollary 2.
- `output/complementarity_threshold_shift.csv`: threshold-shift calculation for Corollary 3.
- `output/interaction_counterexample.csv`: substitutability counterexample for Theorem 4.
- `output/supplementary_*`: additional trace and decomposition outputs.

## How to run

From the package root, run:

```bash
python src/replicate_hysteresis.py
```

The script regenerates the core output files in the `output/` folder. Additional supplementary CSV files are included as fixed trace certificates because they report specific path and counterexample values used in the manuscript.

## Reproducibility statement

The package is lightweight by design. It contains no confidential or proprietary data, and all values are generated from the normalized illustrative parameters stated in the manuscript.

# Online Resource 1: Replication package

This package supports the manuscript **Threshold Hysteresis in Dynamic Acquire-Divest Decisions with Transaction Costs**.

It contains the configuration files, Python source, and generated CSV outputs used for the numerical trace certificates. The package is deliberately lightweight and uses only the Python standard library.

## Contents

- `config/capabilities.csv`: capability parameters and prerequisites.
- `config/paths.csv`: budget paths used in the trace examples.
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

## Reproducibility statement

The manuscript is theoretical. No external empirical dataset is required. The CSV files here are generated examples used to verify the threshold arithmetic, greedy path, reachability certificate, switching-count bound, tightness construction, complementarity threshold shift, interaction counterexample, and memory traces.

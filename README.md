# Online Resource 1: Replication Package

This anonymized package supports the manuscript **A Finite-State Threshold Decision Model for Path-Dependent Component Adjustment under Transaction Costs**. It provides the configuration files, Python source code, generated CSV outputs, and trace certificates used for the numerical illustration and supplementary checks.

## Contents

- `config/`: input capability and path configuration files.
- `src/replicate_hysteresis.py`: Python script that regenerates the output tables and trace certificates.
- `output/`: generated CSV outputs corresponding to the manuscript tables, greedy path, reachability certificates, switching-count checks, tightness construction, chain-decomposable reachability calculation, threshold-shift calculation, interaction counterexample, and memory traces.

## How to reproduce

From the package root, run:

```bash
python src/replicate_hysteresis.py
```

The script uses only the Python standard library. Running it regenerates the files in `output/`.

## Double-blind note

The package has been anonymized for double-blind review. Public repository details can be supplied after the review process.

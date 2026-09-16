# Klebsiella pneumoniae CTX-M-15 Docking

## Overview
In silico analysis of CTX-M-15 β-lactamase from Klebsiella pneumoniae.

## Workflow
1. Genome annotation (Prokka)
2. AMR detection (AMRFinderPlus)
3. BLAST validation
4. Structure retrieval (PDB: 8R30)
5. Structure preparation
6. Molecular docking (AutoDock Vina)

## Results
| Ligand | Affinity (kcal/mol) |
|--------|---------------------|
| Meropenem | -9.5 |
| Avibactam | -8.1 |
| Clavulanic acid | -7.6 |
| Tazobactam | -7.5 |

## Tools
- Prokka
- AMRFinderPlus
- BLAST
- PyMOL
- AutoDock Vina

## Author
[Sabry Ali Zoghdan]

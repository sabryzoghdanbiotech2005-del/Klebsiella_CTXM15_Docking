# Klebsiella pneumoniae CTX-M-15 Docking

## Overview
In silico analysis of CTX-M-15 β-lactamase from a clinical Klebsiella pneumoniae isolate. The project integrates genome annotation, AMR detection, BLAST validation, and molecular docking.

## Workflow
1. Genome annotation (Prokka)
2. AMR detection (AMRFinderPlus)
3. BLAST validation
4. Structure retrieval (PDB: 8R30)
5. Structure preparation
6. Molecular docking (AutoDock Vina)

## AMR Profile
AMRFinderPlus identified 14 AMR determinants:

### Chromosome (4 genes)
- oqxA (efflux)
- oqxB14 (efflux)
- fosA (fosfomycin)
- blaSHV-75 (β-lactam)

### Plasmid (10 genes)
- aph(6)-Id, aph(3'')-Ib (aminoglycoside)
- sul2 (sulfonamide) - partial
- dfrA14, dfrA50 (trimethoprim)
- blaTEM-1, blaSCO-1 (β-lactam)
- qnrB1 (quinolone)
- tet(A) (tetracycline) - partial
- **blaCTX-M-15 (β-lactam/cephalosporin)**

## Genetic Context of blaCTX-M-15
- Located on plasmid CP129404.1 (317,772 bp)
- Position: 241,865–242,737
- No transposase or insertion sequence identified in the surrounding region
- Flanked by plasmid-associated genes (ssb_2, psiB), suggesting a conjugative plasmid

## Docking Results
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
Sabry Ali Zoghdan

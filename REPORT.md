# Klebsiella pneumoniae CTX-M-15: In Silico Analysis and Covalent Docking

## Author
Sabry Ali Zoghdan

## Date
September 2026

---

## 1. Introduction

CTX-M-15 is an extended-spectrum β-lactamase (ESBL) that confers resistance to cephalosporins and monobactams. It is the most widespread CTX-M variant globally and represents a critical public health threat. This project aimed to:

1. Characterize the genome of a clinical *Klebsiella pneumoniae* isolate
2. Identify antimicrobial resistance (AMR) determinants
3. Validate the identity of *bla*CTX-M-15
4. Perform molecular docking of known inhibitors against CTX-M-15
5. Validate the docking protocol via covalent re-docking

---

## 2. Methods

### 2.1 Genome Annotation
- **Tool:** Prokka
- **Result:** 5,231 genes annotated

### 2.2 AMR Detection
- **Tool:** AMRFinderPlus
- **Result:** 14 AMR determinants (4 chromosomal, 10 plasmid-borne)

### 2.3 BLAST Validation
- **Tool:** NCBI BLAST (blastn + blastp)
- **Result:** 100% identity to CTX-M-15

### 2.4 Structure Retrieval
- **Source:** RCSB PDB
- **Structure:** 8R30 (0.85 Å resolution)

### 2.5 Structure Preparation
- **Tools:** PyMOL + OpenBabel
- Removed water, native ligand (XR3), and ions

### 2.6 Molecular Docking
- **Tool:** AutoDock Vina
- **Ligands:** Avibactam, Clavulanic acid, Tazobactam, Meropenem
- **Grid:** Center (-8.41, -2.76, 10.05), Size (25×25×25 Å)

### 2.7 Covalent Redocking Validation
- **Tool:** GalaxyCDock2-DL
- **Receptor:** 4HBU (CTX-M-15 with Avibactam)
- **Ligand:** Avibactam
- **Covalent residue:** SER70 (OG)
- **Result:** RMSD = 0.83 Å

---

## 3. Results

### 3.1 AMR Profile

| Gene | Class | Location | Coverage | Identity |
|------|-------|----------|----------|----------|
| blaCTX-M-15 | β-lactam | Plasmid | 100% | 100% |
| blaTEM-1 | β-lactam | Plasmid | 100% | 100% |
| blaSHV-75 | β-lactam | Chromosome | 100% | 100% |
| blaSCO-1 | β-lactam | Plasmid | 100% | 100% |
| dfrA14 | Trimethoprim | Plasmid | 100% | 100% |
| dfrA50 | Trimethoprim | Plasmid | 100% | 98.73% |
| sul2 | Sulfonamide | Plasmid | 77.49% | 98.10% |
| tet(A) | Tetracycline | Plasmid | 61.40% | 91.43% |
| qnrB1 | Quinolone | Plasmid | 100% | 100% |
| aph(6)-Id | Aminoglycoside | Plasmid | 100% | 100% |
| aph(3'')-Ib | Aminoglycoside | Plasmid | 100% | 100% |
| oqxA | Efflux | Chromosome | 100% | 100% |
| oqxB14 | Efflux | Chromosome | 100% | 100% |
| fosA | Fosfomycin | Chromosome | 100% | 100% |

### 3.2 Genetic Context of blaCTX-M-15
- Located on plasmid CP129404.1 (317,772 bp)
- Position: 241,865–242,737
- Flanked by hypothetical proteins
- No transposase or insertion sequence detected in the vicinity
- Plasmid-associated genes (ssb_2, psiB) present

### 3.3 Docking Results

| Ligand | Binding Affinity (kcal/mol) |
|--------|----------------------------|
| Meropenem | -9.5 |
| Avibactam | -8.1 |
| Clavulanic acid | -7.6 |
| Tazobactam | -7.5 |

### 3.4 Covalent Redocking Validation

| Parameter | Value |
|-----------|-------|
| Tool | GalaxyCDock2-DL |
| Ligand | Avibactam |
| Receptor | 4HBU |
| Covalent Residue | SER70 |
| RMSD | 0.83 Å |
| Score | 5.549 |

**Interpretation:** RMSD < 2.0 Å confirms the validity of the docking protocol.

---

## 4. Discussion

### 4.1 AMR Profile
The isolate carries 14 AMR determinants, including the clinically critical *bla*CTX-M-15. The presence of multiple β-lactamases (CTX-M-15, TEM-1, SHV-75, SCO-1) indicates a multidrug-resistant phenotype.

### 4.2 Genetic Context
The absence of a transposase immediately upstream of *bla*CTX-M-15 suggests that the gene is stably integrated into the plasmid rather than being part of a mobile transposon. However, the plasmid itself is conjugative (ssb_2, psiB), facilitating horizontal transfer.

### 4.3 Docking Results
- **Meropenem** showed the highest affinity (-9.5 kcal/mol) but is a substrate, not an inhibitor.
- **Avibactam** showed the strongest binding among inhibitors (-8.1 kcal/mol), consistent with its known efficacy.
- **Clavulanic acid** (-7.6) and **Tazobactam** (-7.5) showed moderate binding.

### 4.4 Covalent Redocking
The RMSD of 0.83 Å confirms that the docking protocol is accurate for covalent inhibitors. This validates the docking results and supports the interpretation that Avibactam is the most effective inhibitor among those tested.

---

## 5. Conclusion

This study provides a comprehensive in silico analysis of a clinical *Klebsiella pneumoniae* isolate harboring *bla*CTX-M-15. The combination of genome annotation, AMR detection, BLAST validation, and molecular docking (validated by covalent re-docking) provides a robust framework for understanding and targeting CTX-M-15.

---

## 6. Tools Used
- Prokka
- AMRFinderPlus
- NCBI BLAST
- PyMOL
- OpenBabel
- AutoDock Vina
- GalaxyCDock2-DL
- Linux (WSL)
- Git/GitHub

---

## 7. References
- PDB: 8R30, 4HBU
- NCBI: CP129404.1, WP_000239590.1
- AMRFinderPlus database: 2026-08-07.1

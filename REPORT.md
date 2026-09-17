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

### 2.6 Molecular Docking (Preliminary)
- **Tool:** AutoDock Vina
- **Ligands:** Avibactam, Clavulanic acid, Tazobactam, Meropenem
- **Grid:** Center (-8.41, -2.76, 10.05), Size (25×25×25 Å)

### 2.7 Covalent Redocking Validation
- **Tool:** GalaxyCDock2-DL
- **Reference Ligand:** Avibactam (NXL) from PDB 4HBU
- **Receptor:** 4HBU (CTX-M-15)
- **Covalent Bond:** Avibactam C — Ser70 OG
- **Binding Mode:** Covalent
- **RMSD (heavy atoms):** 0.83 Å
- **Score:** 5.549 (GalaxyCDock2-DL)

---

## 3. Results

### 3.1 AMR Profile

AMRFinderPlus identified 14 AMR determinants:
- **Chromosome (4):** oqxA, oqxB14, fosA, blaSHV-75
- **Plasmid (10):** aph(6)-Id, aph(3'')-Ib, sul2, dfrA14, blaTEM-1, qnrB1, tet(A), blaSCO-1, dfrA50, blaCTX-M-15

Note: sul2 (77.49% coverage) and tet(A) (61.40% coverage) were classified as partial hits.

### 3.2 Genetic Context of blaCTX-M-15
- Located on plasmid CP129404.1 (317,772 bp)
- Position: 241,865–242,737
- Flanked by hypothetical proteins
- No transposase or insertion sequence detected in the vicinity
- Plasmid-associated genes (ssb_2, psiB) present

### 3.3 Preliminary Docking Results (Vina)

| Ligand | Binding Affinity (kcal/mol) |
|--------|----------------------------|
| Meropenem | -9.5 |
| Avibactam | -8.1 |
| Clavulanic acid | -7.6 |
| Tazobactam | -7.5 |

**Note:** These are preliminary results. Meropenem showed the highest docking score, consistent with its role as a substrate rather than a mechanism-based inhibitor.

### 3.4 Covalent Redocking Validation

| Parameter | Value |
|-----------|-------|
| Tool | GalaxyCDock2-DL |
| Reference Ligand | Avibactam (NXL) from 4HBU |
| Receptor | 4HBU (CTX-M-15) |
| Covalent Bond | Avibactam C — Ser70 OG |
| Binding Mode | Covalent |
| RMSD (heavy atoms) | 0.83 Å |
| Score | 5.549 (GalaxyCDock2-DL) |

**Interpretation:** Re-docking of avibactam reproduced the crystallographic binding mode with an RMSD of 0.83 Å (heavy atoms). This is below the 2.0 Å threshold commonly used for docking validation.

### 3.5 Cross-Structure Consistency Check

A second docking run was performed on 4HBU (CTX-M-15 from *E. coli*). Results are shown below:

| Ligand | 8R30 (kcal/mol) | 4HBU (kcal/mol) |
|--------|------------------|------------------|
| Avibactam | -8.1 | -6.8 |
| Clavulanic acid | -7.6 | -6.1 |
| Tazobactam | -7.5 | -6.4 |
| Meropenem | -9.5 | -6.5 |

**Note:** This is a consistency check, not a validation. The ranking of ligands differed between 8R30 and 4HBU, which may reflect differences in pocket geometry, protonation states, or grid box placement.

---

## 4. Discussion

### 4.1 AMR Profile
The isolate carries 14 AMR determinants, including the clinically critical *bla*CTX-M-15. The presence of multiple β-lactamases (CTX-M-15, TEM-1, SHV-75, SCO-1) indicates a multidrug-resistant phenotype.

### 4.2 Prokka vs AMRFinderPlus: A Key Observation

Prokka initially annotated the gene as **CTX-M-1**, while AMRFinderPlus identified it as **CTX-M-15**. BLAST validation confirmed the latter (100% identity to CTX-M-15).

This highlights the importance of using specialized tools for AMR detection. General annotation tools (like Prokka) may misclassify closely related alleles.

### 4.3 Genetic Context
The absence of a transposase immediately upstream of *bla*CTX-M-15 suggests that the gene is stably integrated into the plasmid rather than being part of a mobile transposon. However, the plasmid itself is conjugative (ssb_2, psiB), facilitating horizontal transfer.

### 4.4 Docking Results
- **Meropenem** showed the highest docking score but is a substrate, not an inhibitor.
- **Avibactam** showed the strongest binding among inhibitors, consistent with its known efficacy.
- **Clavulanic acid** and **Tazobactam** showed moderate binding.

### 4.5 Covalent Redocking Validation
The RMSD of 0.83 Å confirms that the covalent docking protocol is accurate for Avibactam. This validates the docking approach for covalent inhibitors.

### 4.6 Limitations
- The consistency check between 8R30 and 4HBU showed different rankings, which may reflect structural differences between the two crystal structures.
- Only Avibactam has a reference crystal pose; Clavulanic acid and Tazobactam do not have crystal structures with CTX-M-15.
- Docking results are preliminary and should be interpreted with caution.

---

## 5. Conclusion

This study provides a comprehensive in silico analysis of a clinical *Klebsiella pneumoniae* isolate harboring *bla*CTX-M-15. The combination of genome annotation, AMR detection, BLAST validation, and molecular docking (with covalent re-docking validation) provides a robust framework for understanding and targeting CTX-M-15.

The key finding is the discrepancy between Prokka (CTX-M-1) and AMRFinderPlus (CTX-M-15), emphasizing the need for specialized tools in AMR detection.

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

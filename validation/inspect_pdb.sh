echo "=== Chains present ==="
awk '$1=="ATOM" {print substr($0,22,1)}' 8R30.pdb | sort -u

echo -e "\n=== HETATM residues (ligands, ions, buffer) ==="
awk '$1=="HETATM" {print substr($0,18,3)}' 8R30.pdb | sort | uniq -c | sort -rn

echo -e "\n=== Alternate location indicators ==="
awk '$1=="ATOM" && substr($0,17,1)!=" " {print substr($0,17,1)}' 8R30.pdb | sort | uniq -c

echo -e "\n=== Residues with altlocs ==="
awk '$1=="ATOM" && substr($0,17,1)!=" " {print substr($0,18,9)}' 8R30.pdb | sort -u

echo -e "\n=== Resolution ==="
grep "RESOLUTION" 8R30.pdb | head -3

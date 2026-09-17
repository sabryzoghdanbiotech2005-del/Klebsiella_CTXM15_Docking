from Bio import SeqIO
from Bio.Seq import Seq

rec = next(SeqIO.parse("validation/03_ctxm15_region.fasta", "fasta"))
dna = rec.seq

print(f"Length (bp): {len(dna)}")
print(f"Divisible by 3: {len(dna) % 3 == 0}")
print(f"Starts with ATG: {str(dna[:3]).upper() == 'ATG'}")

prot_fwd = dna.translate(to_stop=False)
prot_rev = dna.reverse_complement().translate(to_stop=False)

for name, p in [("forward", prot_fwd), ("reverse", prot_rev)]:
    internal = p[:-1].count("*")
    print(f"\n--- {name} strand ---")
    print(f"Protein length: {len(p)}")
    print(f"Internal stop codons: {internal}")
    print(f"Ends with stop: {p.endswith('*')}")
    if internal == 0 and p.startswith("M"):
        print("VALID ORF on this strand")
        print(p)
        with open("validation/03_ctxm15_protein.fasta", "w") as fh:
            fh.write(f">CTXM15_query_{name}\n{str(p).rstrip('*')}\n")

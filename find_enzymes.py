import os
from Bio import SeqIO

def find_enzymes(gbk_files):
    enzyme_sets = {}
    
    for file_path in gbk_files:
        enzymes = set()
        
        for record in SeqIO.parse(file_path, "genbank"):
            for feature in record.features:
                if feature.type in ["CDS", "gene", "PFAM_domain", "aSDomain"]:
                    if "description" in feature.qualifiers:
                        for product in feature.qualifiers.get("description", ["N/A"]):
                            #print(product)
                            enzymes.add(product.strip())
        
        enzyme_sets[file_path] = enzymes
    
    common_enzymes = set.intersection(*enzyme_sets.values())
    return common_enzymes

if __name__ == "__main__":
    gbk_files = ["data/cryptophycin.gbk", "data/hectochlorin.gbk", "data/jamaicamide.gbk", "data/scytophycin.gbk"] 
    
    valid_files = [f for f in gbk_files if os.path.exists(f)]
    if len(valid_files) != len(gbk_files):
        missing = set(gbk_files) - set(valid_files)
        print(f"Warning: Missing files: {missing}")
    
    if len(valid_files) < 2:
        print("Need at least 2 files to compare")
    else:
        common = find_enzymes(valid_files)
        
        print(f"\nAnalyzed {len(valid_files)} files:")
        for f in valid_files:
            print(f"- {f}")
        
        if common:
            print(f"\nEnzymes present in all files ({len(common)}):")
            for enzyme in sorted(common):
                print(f"- {enzyme}")
        else:
            print("\nNo common enzymes found in all files.")
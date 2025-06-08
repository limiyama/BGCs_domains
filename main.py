import glob, os, re
import pandas as pd
from collections import defaultdict
from Bio import SeqIO

def extract_bgcs_from_antismash(gbk_dir):
    data = []
    
    for gbk_file in glob.glob(os.path.join(gbk_dir, "*.gbk*")):
        for record in SeqIO.parse(gbk_file, "genbank"):
            organism = record.annotations.get("organism", "Unknown")
            filename = organism + ".txt"
            features = record.features

            with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"ORGANISM: {organism} \n")
                    
                    for feature in features:
                        if feature.type == "region" and "product" in feature.qualifiers: 
                            products = feature.qualifiers["product"]
                            f.write(f"TYPE: {products} \n")

                        desc = feature.qualifiers.get("description", "N/A")[0].lower()
                        f.write(desc + "\n")

#gbk_file = 'mibig_gbk_4.0/BGC0001000.gbk'  # Replace with your .gbk file
#df = parse_gbk_file(gbk_file)
#print(df.head())

path_gbk = "/Users/Lígia/Desktop/FindBGC/data"
extract_bgcs_from_antismash(path_gbk)
import glob, os, re
import pandas as pd
from collections import defaultdict
from Bio import SeqIO

def extract_bgcs_from_antismash(gbk_dir):
    data = []
    
    for gbk_file in glob.glob(os.path.join(gbk_dir, "*.gbk*")):
        for record in SeqIO.parse(gbk_file, "genbank"):
            organism = record.annotations.get("organism", "Unknown")
            features = record.features

            for feature in features:
                # descriptions - nomes dos domínios e tailoring enzymes
                desc = feature.qualifiers.get("description", "N/A")[0].lower()
                with open("path_to_and_name_of_file","mode") as variable_name:
                    variable_name.write(desc)
                

#gbk_file = 'mibig_gbk_4.0/BGC0001000.gbk'  # Replace with your .gbk file
#df = parse_gbk_file(gbk_file)
#print(df.head())

path_gbk = "/Users/Lígia/Desktop/FindBGC/data"
extract_bgcs_from_antismash(path_gbk)
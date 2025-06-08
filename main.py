import glob, os, re
import pandas as pd
from collections import defaultdict
from Bio import SeqIO

def parse_gbk_file(gbk_file):
    records = list(SeqIO.parse(gbk_file, 'genbank'))
    features = []

    for record in records:
        organism_name = record.annotations.get("organism", "Organism não encontrado")

        for feature in record.features:
            if feature.type == 'CDS':  # Focus on coding sequences
                feature_data = {
                    'organism': organism_name,
                    'gene_kind': feature.qualifiers.get('gene_kind', [''])[0],
                    'product': feature.qualifiers.get('product', [''])[0],
                    'note': feature.qualifiers.get('note', [''])[0]
                }
                features.append(feature_data)

    return pd.DataFrame(features)

def extract_bgcs_from_antismash(gbk_files_dir, output_file):
    data = []
    
    # files com antiSMASH no nome e que terminem em gbk so
    for gbk_file in glob.glob(os.path.join(gbk_files_dir, "*antiSMASH*.gbk")):
        # contagem de dominio completo e incompleto
        with open(gbk_file, 'r') as file:
            file_content = file.read()
            complete_count = len(re.findall(r'/complete\b', file_content))
            incomplete_count = len(re.findall(r'/incomplete\b', file_content))
        
        # dicionario p contagem os gene_kind e descriptions
        for record in SeqIO.parse(gbk_file, "genbank"):
            organism_name = record.annotations.get("organism", "Organism não encontrado")

            gene_kind_counts = defaultdict(int)

            bgc_type = "N/A"
            
            for feature in record.features:
                if feature.type == "protocluster":
                    # pega se eh nrps ou kps
                    bgc_type = feature.qualifiers.get("product", ["N/A"])[0]

            for gene_feature in record.features:
                if gene_feature.type in ["CDS", "gene", "PFAM_domain", "aSDomain"]:
                    
                    # conta gene_kind (biosynthetic, transport, regulatory, etc)
                    gene_kind = gene_feature.qualifiers.get("gene_kind", ["N/A"])[0]
                    if gene_kind != "N/A":
                        gene_kind_counts[gene_kind] += 1

            data.append({
                "Organism": organism_name,
                "BGC_type": bgc_type,
                "Biosynthetic": gene_kind_counts["biosynthetic"],
                "Regulatory": gene_kind_counts["regulatory"],
                "Biosynthetic-additional": gene_kind_counts["biosynthetic-additional"],
                "Transport": gene_kind_counts["transport"],
                "Other": gene_kind_counts["other"],
                "Complete": complete_count,
                "Incomplete": incomplete_count
            })

    df = pd.DataFrame(data)
    
    df_filtered = df[df['BGC_type'].str.contains('NRPS|PKS', case=False, na=False)]
    
    # salva em CSV
    df_filtered.to_csv(output_file, sep='\t', index=False)
    print(f"Tabela de contagens de BGCs salva em: {output_file}")

#gbk_file = 'mibig_gbk_4.0/BGC0001000.gbk'  # Replace with your .gbk file
#df = parse_gbk_file(gbk_file)
#print(df.head())

path_gbk = "/Users/Lígia/Desktop/FindBGC/data"
output = "teste.csv"
extract_bgcs_from_antismash(path_gbk, output)
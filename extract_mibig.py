import tarfile, os

# function to extract only cyanobacterial bgcs from the mibig database (.tar.gz)
def extract_cyano_files(tar_path, output_dir, keyword):
    # make sure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # open the .tar.gz file
    with tarfile.open(tar_path, 'r:gz') as tar:
        for member in tar.getmembers():
            # if its a .gbk file
            if member.name.endswith('.gbk'):
                # extract it!
                file_content = tar.extractfile(member).read().decode('utf-8')
                
                # and if its a cyano .gbk file
                if keyword in file_content:
                    # extract it!
                    tar.extract(member, path=output_dir)

tar_path = 'mibig_gbk_4.0.tar.gz' 
output_dir = 'C:/Users/Lígia/Desktop/FindBGC' 
keyword = 'Cyanobacteriota'

extract_cyano_files(tar_path, output_dir, keyword)
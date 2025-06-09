from collections import Counter

def teste(file_path):
    for file in file_path:
        with open(file, 'r') as f:
            count = Counter(line for line in f)
            lista = count.most_common(20)
            print(f"descriptions: {lista} \n")

if __name__ == "__main__":
    files = ['descriptions/cryptomaldamide.txt', 'descriptions/cryptophycin.txt', 'descriptions/hectochlorin.txt', 'descriptions/jamaicamide.txt', 'descriptions/scytophycin.txt']

    teste(files)
    
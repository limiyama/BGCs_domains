from collections import Counter

with open("Anabaena sp. - scytophycin.txt") as input_file:
    #build a counter from each word in the file
    count = Counter(line for line in input_file)

print(count.most_common(10))
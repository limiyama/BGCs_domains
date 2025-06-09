from collections import Counter

def get_descriptions(file_paths, min_files, top):
    phrase_counts = Counter()
    phrase_files = {} 
    
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            phrases_in_file = set(line.strip().lower() for line in f if line.strip())
            
            for phrase in phrases_in_file:
                if phrase not in phrase_files:
                    phrase_files[phrase] = set()
                phrase_files[phrase].add(file_path)
                phrase_counts[phrase] += 1
    
    common_phrases = {
        phrase: count 
        for phrase, count in phrase_counts.items() 
        if len(phrase_files[phrase]) >= min_files
    }
    
    return Counter(common_phrases).most_common(top)

# Example usage
if __name__ == "__main__":
    files = ['descriptions/cryptomaldamide.txt', 'descriptions/cryptophycin.txt', 'descriptions/hectochlorin.txt', 'descriptions/jamaicamide.txt', 'descriptions/scytophycin.txt']
    min_files = 5
    top = 20

    common_phrases = get_descriptions(files, min_files, top)
    
    print("descriptions que apareceram nos cinco BGCs:")
    for phrase, count in common_phrases:
        print(f"{phrase}: {count} occurrences")
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        cleaned = word.strip(".,!?;:\"'")
        freq[cleaned] = freq.get(cleaned, 0) + 1
    return freq
 
 
if __name__ == "__main__":
    paragraph = "the quick brown fox jumps over the lazy dog. The dog barks at the fox."
    result = word_frequency(paragraph)
    for word, count in sorted(result.items(), key=lambda x: -x[1]):
        print(f"{word}: {count}")
 
def text_statistics(text):
    num_chars = len(text)
    num_words = len(text.split())
    num_sentences = text.count(".") + text.count("!") + text.count("?")
    avg_word_length = (
        sum(len(w.strip(".,!?;:")) for w in text.split()) / num_words
        if num_words > 0 else 0
    )
 
    return {
        "characters": num_chars,
        "words": num_words,
        "sentences": num_sentences,
        "avg_word_length": round(avg_word_length, 2),
    }
 
 
if __name__ == "__main__":
    sample_text = (
        "Python is a great programming language! It is easy to learn. "
        "Many developers love it because of its simplicity and readability."
    )
    stats = text_statistics(sample_text)
    for key, value in stats.items():
        print(f"{key}: {value}")
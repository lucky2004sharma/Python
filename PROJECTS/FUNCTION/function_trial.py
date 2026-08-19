
def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
 
 
if __name__ == "__main__":
    samples = ["Madam", "Hello World", "A man a plan a canal Panama", "Python"]
    for s in samples:
        print(f"'{s}' -> {is_palindrome(s)}")
 
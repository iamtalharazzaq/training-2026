def word_frequency(text, top_n=5):
    # lowercase
    text = text.lower()

    # remove punctuation manually (keep only letters and spaces)
    cleaned = ""
    for ch in text:
        if ch.isalpha() or ch.isspace():
            cleaned += ch

    # split into words - list
    words = cleaned.split()

    # count frequency - dict
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    # sort dictionary by count (descending)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # return top N words
    return sorted_words[:top_n]


# Hardcoded paragraph about World War 2
paragraph = """
World War Two was a global war that lasted from 1939 to 1945.
Many countries were involved in World War Two and millions of people lost their lives.
The war changed the political structure of the world and led to the creation of the United Nations.
After the war many nations worked together to maintain peace and prevent future conflicts.
"""

top_words = word_frequency(paragraph, 5)

# Print top 5 words
print("\nTop 5 Most Common Words\n")
for word, count in top_words:
    print(f"{word:<12} -> {count}")
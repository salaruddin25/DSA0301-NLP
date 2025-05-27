import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize

# Force re-download of essential NLTK data
nltk.download('wordnet', force=True)
nltk.download('punkt', force=True)
nltk.download('omw-1.4', force=True)

# Simplified Lesk algorithm
def lesk(context_sentence, ambiguous_word):
    context = set(word_tokenize(context_sentence.lower(), preserve_line=True))
    best_sense = None
    max_overlap = 0

    for sense in wn.synsets(ambiguous_word):
        signature = set(word_tokenize(sense.definition().lower(), preserve_line=True))
        for example in sense.examples():
            signature |= set(word_tokenize(example.lower(), preserve_line=True))
        overlap = len(context & signature)
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

# Main program
if __name__ == "__main__":
    sentence = input("Enter a sentence with an ambiguous word: ")
    word = input("Enter the ambiguous word: ")

    sense = lesk(sentence, word)

    if sense:
        print(f"\nBest sense: {sense.name()}")
        print(f"Definition: {sense.definition()}")
    else:
        print("No suitable sense found.")

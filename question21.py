import spacy
import neuralcoref

nlp = spacy.load('en_core_web_sm')
coref = neuralcoref.NeuralCoref(nlp.vocab)
nlp.add_pipe(coref, name='neuralcoref')

def resolve_references(text):
    doc = nlp(text)
    return doc._.coref_resolved

def extract_noun_phrases_with_meanings(text):
    doc = nlp(text)
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    meanings = {}
    for phrase in noun_phrases:
        token = nlp(phrase)[0]
        meanings[phrase] = token._.wordnet.synsets() if token.has_vector else []
    return meanings

if __name__ == "__main__":
    sample_text = """
    Mary has a little lamb. She loves it very much. The lamb follows her everywhere.
    """
    resolved_text = resolve_references(sample_text)
    print("Resolved Text:")
    print(resolved_text)

    print("\nNoun Phrases and Their Meanings:")
    noun_meanings = extract_noun_phrases_with_meanings(resolved_text)
    for phrase, meaning in noun_meanings.items():
        print(f"{phrase}: {[syn.name() for syn in meaning]}")

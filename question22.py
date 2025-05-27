import spacy
import neuralcoref

nlp = spacy.load('en_core_web_sm')
coref = neuralcoref.NeuralCoref(nlp.vocab)
nlp.add_pipe(coref, name='neuralcoref')

def resolve_references(text):
    doc = nlp(text)
    return doc._.coref_resolved

if __name__ == "__main__":
    sample_text = """
    Mary has a little lamb. She loves it very much. The lamb follows her everywhere.
    """
    resolved_text = resolve_references(sample_text)
    print("Resolved Text:")
    print(resolved_text)

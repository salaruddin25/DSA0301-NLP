
# english_to_french_translation.py

from transformers import MarianTokenizer, MarianMTModel

def load_model_and_tokenizer(src_lang="en", tgt_lang="fr"):
    """
    Loads the MarianMT model and tokenizer for English to French translation.
    """
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate_text(text, tokenizer, model):
    """
    Translates English text to French.
    """
    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Generate translation
    translated = model.generate(**inputs)

    # Decode the translated tokens
    french_translation = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return french_translation[0]

if __name__ == "__main__":
    # Sample input
    english_text = "Hello, how are you? I hope you're having a good day."

    # Load model and tokenizer
    tokenizer, model = load_model_and_tokenizer()

    # Translate and print result
    french_translation = translate_text(english_text, tokenizer, model)
    print(f"English: {english_text}")
    print(f"French : {french_translation}")
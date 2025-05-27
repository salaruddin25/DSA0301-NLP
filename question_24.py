

# dialog_act_recognizer.py

def recognize_dialog_act(utterance):
    utterance = utterance.lower().strip()

    # Rule-based classification
    if utterance.startswith(("hi", "hello", "hey")):
        return "greeting"
    elif utterance.endswith("?"):
        return "question"
    elif utterance.startswith(("thanks", "thank you")):
        return "thanks"
    elif any(word in utterance for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    elif utterance.startswith(("yes", "no", "okay", "sure", "fine")):
        return "response"
    else:
        return "statement"


def process_conversation(conversation):
    return [(utt, recognize_dialog_act(utt)) for utt in conversation]


if __name__ == "__main__":
    # Sample conversation
    conversation = [
        "Hello!",
        "How are you doing?",
        "I'm fine, thank you.",
        "What can you do?",
        "I can help you with information.",
        "Thanks!",
        "Goodbye!"
    ]

    # Process and print dialog acts
    labeled_conversation = process_conversation(conversation)

    for utterance, act in labeled_conversation:
        print(f"'{utterance}' -> {act}")
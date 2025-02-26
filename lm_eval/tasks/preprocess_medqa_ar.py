def doc_to_choice(doc):
    # Explicitly specify choices
    return ["A", "B", "C", "D", "E"]

def doc_to_text(doc) -> str:
    choices = doc["options"]
    answers = "\n".join([f"{k}. {v}" for k, v in choices.items()])
    return f"السؤال: {doc['question']}\n{answers}\nالإجابة:"

def doc_to_target(doc) -> str:
    return doc["answer_idx"]
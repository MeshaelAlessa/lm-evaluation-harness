def doc_to_text(doc) -> str:
    option_choices = {
        "A": doc["opa"],
        "B": doc["opb"],
        "C": doc["opc"],
        "D": doc["opd"],
    }

    prompt = "السؤال: " + doc["question"] + "\nالخيارات:\n"
    for choice, option in option_choices.items():
        prompt += f"{choice.upper()}. {option}\n"
    prompt += "الإجابة:"
    return prompt

def doc_to_target(doc) -> str:
    return doc["cop"]
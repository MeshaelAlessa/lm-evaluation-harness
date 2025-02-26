def doc_to_text(doc) -> str:
    ctxs = "\n".join(doc["CONTEXTS"])
    return "الملخص: {}\nالسؤال: {}\nالإجابة:".format(
        ctxs,
        doc["QUESTION"],
    )

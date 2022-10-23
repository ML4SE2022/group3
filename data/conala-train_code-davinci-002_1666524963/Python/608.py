def limit_sentences(text, max_sentences):
    sentences = text.split('.')
    if len(sentences) > max_sentences:
        return '.'.join(sentences[:max_sentences]) + '.'
    else:
        return text

limit_sentences('This is a sentence. This is another sentence. This is a third sentence.', 2)
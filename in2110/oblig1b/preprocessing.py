from stopwords import stop_words

# Settings
TRANSLATION_TABLE = dict.fromkeys(map(ord, '\'«»!"#$%&()*+,/:;<=>?@[\]^_`{|}~@.-'), None)


def _preprocess(sentence):
    clean_sentence = sentence.replace('<s>', '').replace('</s>', '').lower().translate(TRANSLATION_TABLE)
    removed_stop_words = [token for token in clean_sentence.split() if token not in stop_words]

    return removed_stop_words



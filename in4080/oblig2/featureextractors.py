
def pos_features(sentence, i, history):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
    return features


def pos_features_2(sentence, i, history):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:],
                "word": sentence[i]
                }
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
    return features


def pos_features_3(sentence, i, history):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:],
                "word": sentence[i]
                }
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]

    features["next-word"] = sentence[i+1] if i < (len(sentence) - 1) else "<END>"

    return features


def pos_features_4(sentence, i, history):
    """
    Added check if first letter of token is Uppercase
    """
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:],
                "word": sentence[i]
                }
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]

    features["next-word"] = sentence[i+1] if i < (len(sentence) - 1) else "<END>"
    features["word-first-upper"] = 1 if sentence[i][0].isupper() else 0
    return features


def pos_features_5(sentence, i, history):
    """
    Added check if all letters of token is Uppercase
    """
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:],
                "word": sentence[i]
                }
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]

    features["next-word"] = sentence[i+1] if i < (len(sentence) - 1) else "<END>"
    features["word-all-upper"] = 1 if sentence[i].isupper() else 0
    return features


def pos_features_6(sentence, i, history):
    """
    Added check if tokens contains hyphen
    """
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:],
                "word": sentence[i]
                }
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]

    features["next-word"] = sentence[i+1] if i < (len(sentence) - 1) else "<END>"
    features["word-hyphen"] = 1 if '-' in sentence[i] else 0
    return features


def pos_features_7(sentence, i, history):
    """
    Added check if tokens contains hyphen
    """
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:],
                "word": sentence[i]
                }
    if i == 0:
        features["prev(1)-word"] = "<START>"
        features["prev(2)-word"] = "<START> <START>"
    elif i == 1:
        features["prev(1)-word"] = sentence[i - 1]
        features["prev(2)-word"] = "<START>"
    else:
        features["prev(1)-word"] = sentence[i - 1]
        features["prev(2)-word"] = sentence[i - 2]

    features["next-word"] = sentence[i+1] if i < (len(sentence) - 1) else "<END>"
    return features

def pos_features_8(sentence, i, history):
    """
    Added check if tokens contains hyphen
    """
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:],
                "word": sentence[i]
                }
    if i == 0:
        features["prev(1)-word"] = "<START>"
        features["prev(2)-word"] = "<START> <START>"
    elif i == 1:
        features["prev(1)-word"] = sentence[i - 1]
        features["prev(2)-word"] = "<START>"
    else:
        features["prev(1)-word"] = sentence[i - 1]
        features["prev(2)-word"] = sentence[i - 2]

    features["next-word"] = sentence[i+1] if i < (len(sentence) - 1) else "<END>"
    features["word-hyphen"] = 1 if '-' in sentence[i] else 0
    features["word-all-upper"] = 1 if sentence[i].isupper() else 0
    features["word-first-upper"] = 1 if sentence[i][0].isupper() else 0
    return features


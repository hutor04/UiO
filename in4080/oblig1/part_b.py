import nltk
import random
import numpy as np
import scipy as sp
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from nltk.corpus import movie_reviews


# Exercise 1.A
raw_movie_docs = [(movie_reviews.raw(fileid), category) for
category in movie_reviews.categories() for fileid in
movie_reviews.fileids(category)]

random.seed(100500)
random.shuffle(raw_movie_docs)
movie_test = raw_movie_docs[:200]
movie_dev = raw_movie_docs[200:]

dev_test_data = movie_dev[:200]
train_data = movie_dev[200:]

train_texts = [text for text, label in train_data]
train_target = [label for text, label in train_data]

dev_test_texts = [text for text, label in dev_test_data]
dev_test_target = [label for text, label in dev_test_data]

# Vectorize data
v = CountVectorizer()
v.fit(train_texts)

train_vectors = v.transform(train_texts)
dev_test_vectors = v.transform(dev_test_texts)

# Train NB
clf = MultinomialNB()
clf.fit(train_vectors, train_target)

# Short test of NB
print(dev_test_texts[14])
print(clf.predict(dev_test_vectors[14]))

# Score on dev test
print(clf.score(dev_test_vectors, dev_test_target))

# Exercise 1.B
print('\nExercise 1.B')

binary = [False, True]
ngram_range = [[1, 1], [1, 2], [1, 3]]


def evaluate_counvectorizer(train_txt, dev_test_txt, train_trg, dev_test_trg, b=False, ngram=(1, 1)):
    vectorizer = CountVectorizer(binary=b, ngram_range=ngram)
    vectorizer.fit(train_txt)

    train_vec = vectorizer.transform(train_txt)
    dev_test_vec = vectorizer.transform(dev_test_txt)

    classifier = MultinomialNB()
    classifier.fit(train_vec, train_trg)

    return classifier.score(dev_test_vec, dev_test_trg)


for i in binary:
    for j in ngram_range:
        r = evaluate_counvectorizer(train_texts, dev_test_texts, train_target, dev_test_target, b=i, ngram=j)
        print(i, j, r)

# Exercise 2.A
print('\nExercise 2.A')

train_texts_all_dev = [text for text, label in movie_dev]
train_target_all_dev = [label for text, label in movie_dev]


def generate_indexes(N, folds):
    stride = N // folds
    start = 0
    end = stride
    idx = []
    for i in range(folds):
        idx.append([start, end])
        start += stride
        end += stride
    return idx


def generate_reverse_slice(data, slice):
    return data[0:slice[0]] + data[slice[1]:]


idxes = generate_indexes(len(train_texts_all_dev), 9)
results = []

for (start, end) in idxes:
    test_txts = train_texts_all_dev[start:end]
    test_lbls = train_target_all_dev[start:end]

    train_txts = generate_reverse_slice(train_texts_all_dev, (start, end))
    train_lbls = generate_reverse_slice(train_target_all_dev, (start, end))

    r = evaluate_counvectorizer(train_txts, test_txts, train_lbls, test_lbls, b=True, ngram=(1, 1))
    results.append(r)

for idx, acc in enumerate(results, start=1):
    print(f'Run No: {idx}, Accuracy: {acc}')

mean = np.mean(results)
std_dev = np.std(results)

print(f'Mean: {mean}, Standard deviation: {std_dev}')

# Exercise 2.B
print('\nExercise 2.B')

for i in binary:
    for j in ngram_range:
        res = []
        for (start, end) in idxes:
            test_txts = train_texts_all_dev[start:end]
            test_lbls = train_target_all_dev[start:end]

            train_txts = generate_reverse_slice(train_texts_all_dev, (start, end))
            train_lbls = generate_reverse_slice(train_target_all_dev, (start, end))
            r = evaluate_counvectorizer(train_txts, test_txts, train_lbls, test_lbls, b=i, ngram=j)
            res.append(r)
        print(i, j, np.mean(res))

# Exercise 3
print('\nExercise 3')


def evaluate_counvectorizer_log_reg(train_txt, dev_test_txt, train_trg, dev_test_trg, b=False, ngram=(1, 1)):
    vectorizer = CountVectorizer(binary=b, ngram_range=ngram)
    vectorizer.fit(train_txt)

    train_vec = vectorizer.transform(train_txt)
    dev_test_vec = vectorizer.transform(dev_test_txt)

    classifier = LogisticRegression(max_iter=1000)
    classifier.fit(train_vec, train_trg)

    return classifier.score(dev_test_vec, dev_test_trg)


settings = [(False, [1, 1]), (True, [1, 2])]

for binary, ngram in settings:
    res = []
    for (start, end) in idxes:
        test_txts = train_texts_all_dev[start:end]
        test_lbls = train_target_all_dev[start:end]

        train_txts = generate_reverse_slice(train_texts_all_dev, (start, end))
        train_lbls = generate_reverse_slice(train_target_all_dev, (start, end))
        r = evaluate_counvectorizer_log_reg(train_txts, test_txts, train_lbls, test_lbls, b=binary, ngram=ngram)
        res.append(r)
    print(binary, ngram, np.mean(res))

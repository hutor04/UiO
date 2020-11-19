import random
import numpy as np
import gensim.downloader as api
import gensim.models
from gensim.test.utils import datapath
from nltk.corpus import brown
from nltk.corpus import movie_reviews
from nltk import word_tokenize
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier


# Exercise 1.A
print('Exercise 1.A')
wv = api.load('word2vec-google-news-300')
vocab = [word for word in wv.vocab]
print(f'Number of words in vocabulary: {len(vocab)}')

# Exercise 1.B
print('Exercise 1.B')


def norm_2(vec):
    squared = np.square(vec)
    summed = np.sum(squared)
    result = np.sqrt(summed)
    return result


def cosine_similarity(vec1, vec2):
    length_1 = norm_2(vec1)
    length_2 = norm_2(vec2)
    cosine_sim = np.dot(vec1, vec2) / (length_1 * length_2)
    return cosine_sim

# Exercise 1.C
print('Exercise 1.C')

sim_1 = wv.similarity('king', 'queen')
king = wv['king']
queen = wv['queen']
sim_2 = cosine_similarity(king, queen)
print(f'Similarity by Gensim:{sim_1}, Similarity by custom functions: {sim_2}')

# Exercise 2.A
print('Exercise 2.A')
print(wv.most_similar(positive=['Oslo', 'Sweden'], negative=['Norway'], topn=5))
print(wv.most_similar(positive=['man', 'queen'], negative = ['king'], topn=5))
print(wv.most_similar(positive=['queen', 'man'], negative=['king'], topn=5))
print(wv.most_similar(positive=['kitten', 'dog'], negative=['cat'], topn=5))

print(wv.most_similar(positive=['infant', 'animal'], negative=['people'], topn=5))
print(wv.most_similar(positive=['apple', 'vegetable'], negative=['fruit'], topn=5))
print(wv.most_similar(positive=['potato', 'fruit'], negative=['vegetable'], topn=5))
print(wv.most_similar(positive=['Minsk', 'Russia'], negative = ['Belarus'], topn=5))

# Exercise 2.B
print('Exercise 2.B')

a = wv['king'] + wv['woman'] - wv['man']

words_1 = ['queen', 'woman', 'man', 'king']
for word in words_1:
    sim_score = cosine_similarity(a, wv[word])
    print(f'Word: {word}. Similarity score: {sim_score}')

wv.similar_by_vector(a)

# Exercise 2.C
print('Exercise 2.C')
print(wv.doesnt_match(['Norway', 'Denmark', 'Finland', 'Sweden', 'Spain', 'Stockholm']))
print(wv.doesnt_match(['fruit', 'potato', 'apple', 'pear', 'cherries', 'watermellon']))
print(wv.doesnt_match(['car', 'train', 'airplane', 'horse', 'ship', 'vessel']))

# Exercise 3.A
print('Exercise 3.A')

sents = brown.sents()
my_model = gensim.models.Word2Vec(sentences=sents)
vocab_2 = [word for word in my_model.wv.vocab]
print(len(vocab_2))

# Exercise 3.B
print('Exercise 3.B')

r1 = wv.most_similar(positive=['car'], topn=10)
r2 = my_model.wv.most_similar(positive=['car'], topn=10)
table = [[a[0], b[0]] for a, b in zip(r1, r2)]

for i in table:
    print(f'Google News: {i[0]}, Brown: {i[1]}')

r1_1 = wv.most_similar(positive=['queen'], topn=10)
r2_1 = my_model.wv.most_similar(positive=['queen'], topn=10)
table_1 = [[a[0], b[0]] for a, b in zip(r1_1, r2_1)]

for i in table_1:
    print(f'Google News: {i[0]}, Brown: {i[1]}')

# Exercise 3.C
print(my_model.wv.most_similar(positive=['man', 'queen'], negative = ['king'], topn=5))
print(my_model.wv.most_similar(positive=['queen', 'man'], negative=['king'], topn=5))
print(my_model.wv.most_similar(positive=['kitten', 'dog'], negative=['cat'], topn=5))

print(my_model.wv.most_similar(positive=['infant', 'animal'], negative=['people'], topn=5))
print(my_model.wv.most_similar(positive=['apple', 'vegetable'], negative=['fruit'], topn=5))
print(my_model.wv.most_similar(positive=['potato', 'fruit'], negative=['vegetable'], topn=5))

# Exercise 4
print('Exercise 4')
path=datapath('questions-words.txt')

eval_model = wv.evaluate_word_analogies(path)
print(eval_model[0])

# Exercise 5.A-B
print('Exercise 5.A-B')

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
train_texts_tokens = [word_tokenize(text) for text in train_texts]
train_target = [label for text, label in train_data]

dev_test_texts = [text for text, label in dev_test_data]
dev_test_texts_tokens = [word_tokenize(text) for text in dev_test_texts]
dev_test_target = [label for text, label in dev_test_data]

# Without normalization
train_texts_average_vectors = []
for text in train_texts_tokens:
    embeddings = [wv[token] for token in text if token in wv.vocab]
    text_average = np.mean(embeddings, axis=0)
    train_texts_average_vectors.append(text_average)

dev_test_texts_average_vectors = []
for text in dev_test_texts_tokens:
    embeddings = [wv[token] for token in text if token in wv.vocab]
    text_average = np.mean(embeddings, axis=0)
    dev_test_texts_average_vectors.append(text_average)

alphas = [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
results = []
for alpha in alphas:
    classifier = LogisticRegression(max_iter=1000, C=alpha)
    classifier.fit(train_texts_average_vectors, train_target)
    result = classifier.score(dev_test_texts_average_vectors, dev_test_target)
    results.append(result)

print('Using document embeddings without normalization...')
for x, y in zip(alphas, results):
    print(f'C: {x}, Accuracy: {y}')

# With normalization
train_texts_average_vectors_2 = []
for text in train_texts_tokens:
    embeddings = [wv[token] for token in text if token in wv.vocab]
    text_average = np.mean(embeddings, axis=0)
    norm = np.linalg.norm(text_average)
    train_texts_average_vectors_2.append(text_average / norm)

dev_test_texts_average_vectors_2 = []
for text in dev_test_texts_tokens:
    embeddings = [wv[token] for token in text if token in wv.vocab]
    text_average = np.mean(embeddings, axis=0)
    norm = np.linalg.norm(text_average)
    dev_test_texts_average_vectors_2.append(text_average / norm)

alphas = [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
results_2 = []
for alpha in alphas:
    classifier = LogisticRegression(max_iter=1000, C=alpha)
    classifier.fit(train_texts_average_vectors_2, train_target)
    result = classifier.score(dev_test_texts_average_vectors_2, dev_test_target)
    results_2.append(result)

print('Using document embeddings with normalization...')
for x, y in zip(alphas, results_2):
    print(f'C: {x}, Accuracy: {y}')

# Exercise 5.C
print('Exercise 5.C')

activations = ['identity', 'logistic', 'tanh', 'relu']
results_3 = []
for activation in activations:
    clf = MLPClassifier(random_state=1, max_iter=1000, activation=activation)
    clf.fit(train_texts_average_vectors_2, train_target)
    score = clf.score(dev_test_texts_average_vectors_2, dev_test_target)
    results_3.append(score)

for x, y in zip(activations, results_3):
    print(f'Activations: {x}, Accuracy: {y}')
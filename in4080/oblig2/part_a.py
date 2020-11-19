from itertools import chain
from collections import Counter
import nltk
from nltk.corpus import brown
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from consecutivepostagger import ConsecutivePosTagger
from scikitconsecutivepostagger import ScikitConsecutivePosTagger
from featureextractors import pos_features, pos_features_2, pos_features_3, pos_features_4, pos_features_5,\
    pos_features_6, pos_features_7, pos_features_8
from sampler import my_sampler


tagged_sents = brown.tagged_sents(categories='news')
size = int(len(tagged_sents) * 0.1)
train_sents, test_sents = tagged_sents[size:], tagged_sents[:size]

# Task 1.0.4
print('Task 1.0.4')
tagger = ConsecutivePosTagger(train_sents)
print(round(tagger.evaluate(test_sents), 4))

# Task 1.1.1
print('Task 1.1.1')
tagged_sents_universal = brown.tagged_sents(categories='news', tagset='universal')
news_test, news_dev_test, news_train = my_sampler(tagged_sents_universal, [0.1, 0.1, 0.8])
tagger_2 = ConsecutivePosTagger(news_train)
print(round(tagger_2.evaluate(news_dev_test), 4))

# Task 1.1.2
print('Task 1.1.2')

def baseline_tagger(training, testing):
    cfd = nltk.ConditionalFreqDist((word, tag) for word, tag in chain(*training))
    tag_frequency = Counter(tag for word, tag in chain(*training))
    most_commmon_tag = tag_frequency.most_common(1)[0]

    # Break ties
    for word, tag_freq in cfd.items():
        if len(tag_freq) > 1 and len(set(tag_freq.values())) == 1:
            sorted_by_total_freq = sorted(tag_freq.keys(), key=lambda x: tag_frequency[x], reverse=True)
            for tag in sorted_by_total_freq[1:]:
                cfd[word][tag] = 0

    result = []
    for sent in testing:
        updated_sent = []
        for word, tag in sent:
            if cfd.get(word) is not None:
                updated_sent.append((word, cfd[word].max()))
            else:
                updated_sent.append((word, most_commmon_tag))
        result.append(updated_sent)

    return result


def accuracy(y_true, y_predict):
    number_elements = len(list(chain(*y_true)))
    matches = 0
    for y_t, y_p in zip(chain(*y_true), chain(*y_predict)):
        if y_t == y_p:
            matches += 1
    return matches / number_elements


baseline_prediction = baseline_tagger(train_sents, test_sents)
acc = accuracy(test_sents, baseline_prediction)
print(f'Baseline accuracy for train_sents, test_sents:{round(acc, 4)}\n')

baseline_prediction_2 = baseline_tagger(news_train, news_dev_test)
acc_2 = accuracy(news_dev_test, baseline_prediction_2)
print(f'Baseline accuracy for news_train, news_dev_test:{round(acc_2, 4)}\n')

# Task 1.2.1
print('Task 1.2.1')
tagger_3 = ScikitConsecutivePosTagger(news_train)
print(round(tagger_3.evaluate(news_dev_test), 4))

# Task 1.2.2
print('Task 1.2.2')


def find_best_alpha(features=pos_features):
    print('Looking for the best alpha...')
    alphas = [1, 0.5, 0.1, 0.01, 0.001, 0.0001]
    for alpha in alphas:
        clf = BernoulliNB(alpha=alpha)
        tgr = ScikitConsecutivePosTagger(news_train, features=features, clf=clf)
        evaluation = tgr.evaluate(news_dev_test)
        print(f'Alpha {alpha}: {round(evaluation, 4)}')

find_best_alpha()

# Task 1.2.3
print('Task 1.2.3')
find_best_alpha(pos_features_2)

# Task 1.3.1
print('Task 1.3.1')

tagger_4 = ScikitConsecutivePosTagger(news_train, features=pos_features_2, clf=LogisticRegression(max_iter=500))
print(round(tagger_4.evaluate(news_dev_test), 4))

# Task 1.3.2
print('Task 1.3.2')


def find_best_alpha_2(features=pos_features):
    print('Looking for the best alpha...')
    alphas = [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    for alpha in alphas:
        clf = LogisticRegression(C=alpha, max_iter=1000)
        tgr = ScikitConsecutivePosTagger(news_train, features=features, clf=clf)
        evaluation = tgr.evaluate(news_dev_test)
        print(f'Alpha {alpha}: {round(evaluation, 4)}')


find_best_alpha_2(pos_features_2)

# Task 1.4.1
print('Task 1.4.1')

tagger_5 = ScikitConsecutivePosTagger(news_train, features=pos_features_3, clf=LogisticRegression(C=10.0, max_iter=1000))
print(round(tagger_5.evaluate(news_dev_test), 4))

# Task 1.4.2
print('Task 1.4.2')


def test_features():
    print('Testing additional features...')
    my_features = [pos_features_4, pos_features_5, pos_features_6, pos_features_7, pos_features_8]
    feature_names = ["word-first-upper", "word-all-upper", "word-hyphen", "2 tokens before", "all together"]
    for feature, name in zip(my_features, feature_names):
        tgr = ScikitConsecutivePosTagger(news_train, features=feature, clf=LogisticRegression(C=10.0, max_iter=1000))
        accuracy = tgr.evaluate(news_dev_test)
        print(f'Feature: {name}, Accuracy: {round(accuracy, 4)}')

test_features()

# Task 1.5.1
print('Task 1.5.1')
tagger_6 = ScikitConsecutivePosTagger(news_train, features=pos_features_6, clf=LogisticRegression(C=10.0, max_iter=1000))
print(round(tagger_6.evaluate(news_test), 4))

# Task 1.5.2
print('Task 1.5.2')
tagged_sents_rest_universal = brown.tagged_sents(categories=['belles_lettres', 'editorial', 'fiction', 'government',
                                                             'humor', 'learned', 'lore', 'mystery', 'religion',
                                                             'reviews', 'romance', 'science_fiction'],
                                                 tagset='universal')

rest_train, rest_dev_test, rest_test = my_sampler(tagged_sents_rest_universal, [0.8, 0.1, 0.1])
train = rest_train + news_train
test = rest_test + news_test

baseline_prediction_3 = baseline_tagger(train, test)
acc_3 = accuracy(test, baseline_prediction_3)
print(f'Baseline accuracy: {round(acc_3, 4)}')

# Task 1.5.3
print('Task 1.5.3')
tagger_7 = ScikitConsecutivePosTagger(train, features=pos_features_6, clf=LogisticRegression(C=10.0, max_iter=1000))
print(round(tagger_7.evaluate(test), 4))

# Task 1.5.4
print('Task 1.5.4')

adventure = brown.tagged_sents(categories='adventure', tagset='universal')
hobbies = brown.tagged_sents(categories='hobbies', tagset='universal')

print(round(tagger_7.evaluate(adventure), 4))
print(round(tagger_7.evaluate(hobbies), 4))

# Task 1.6.1
print('Task 1.6.1')

news_hmm_tagger = nltk.HiddenMarkovModelTagger.train(news_train)
print(round(news_hmm_tagger.evaluate(news_dev_test), 4))

news_hmm_tagger_2 = nltk.HiddenMarkovModelTagger.train(train)
print(round(news_hmm_tagger_2.evaluate(test), 4))

# Task 1.6.2
print('Task 1.6.2')

per_tagger = nltk.PerceptronTagger(load=False)
per_tagger.train(news_train)
print(round(per_tagger.evaluate(news_dev_test), 4))

per_tagger_2 = nltk.PerceptronTagger(load=False)
per_tagger_2.train(train)
print(round(per_tagger_2.evaluate(test), 4))

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier


class IntentionsParser:
    def __init__(self, input_data='data/intentions.txt'):
        self.sentences = []
        self.labels = []
        with open(input_data, 'r') as input_file:
            for line in input_file:
                sentence, label = line.split(',')
                self.sentences.append(sentence.strip().lower())
                self.labels.append(int(label.strip()))

        self.count_vect = CountVectorizer()
        self.X_train = self.count_vect.fit_transform(self.sentences)

        self.tfidf_transformer = TfidfTransformer()
        self.X_train_tfidf = self.tfidf_transformer.fit_transform(self.X_train)

        self.cls = SGDClassifier(max_iter=1000, tol=1e-3)
        self.cls.fit(self.X_train_tfidf, self.labels)

    def predict(self, input_string):
        s = self.count_vect.transform([input_string.lower()])
        s = self.tfidf_transformer.transform(s)
        prediction = self.cls.predict(s)[0]
        return prediction

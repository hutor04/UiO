from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from classifier.data import prepare_data
from sklearn.metrics import accuracy_score
from itertools import combinations
import warnings


class Predictor:
    """
    Handles Model training, prediction, and evaluation of accuracy
    """
    def __init__(self, training_data, testing_data):
        """
        Initialize class with Pandas DFs for training and testing data
        :param training_data: Pandas DF
        :param testing_data: Pandas DF
        """
        self.feature_names = ['pregnant', 'glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree', 'age']
        self.rclass = 'diabetes'
        self.classifiers = [KNeighborsClassifier(), SVC(), GaussianNB()]

        self.training_data = training_data
        self.testing_data = testing_data
        self.model = None
        self.y_pred = None
        self.y_train = None
        self.y_test = None


        warnings.filterwarnings("ignore", category=FutureWarning)

    def fit(self, features_list=None, mode=0):
        """
        Fits the data to the given model. Provide a list of features (if nothing is provided in uses all the features).
        Provide mode: 0 - kNN, 1 - SVC, 2 - NB. NB is default.
        :param features_list: list
                            List of features from 'pregnant', 'glucose', 'pressure', 'triceps', 'insulin',
                            'mass', 'pedigree', 'age'
        :param mode: int
                    Mode 0-2
        :return: Trained model
        """
        classifier = self.classifiers[mode]
        if features_list is not None:
            self.feature_names = features_list

        X_train = self.training_data[self.feature_names]
        self.y_train = self.training_data[self.rclass]

        self.model = classifier.fit(X_train, self.y_train)

        return self.model

    def predict(self):
        """
        Make prediction based on the trained model. Returns Series of predicted results.
        :return: Series
        """
        X_test = self.testing_data[self.feature_names]
        self.y_test = self.testing_data[self.rclass]
        self.y_pred = self.model.predict(X_test)

        return self.y_pred

    def get_accuracy(self, test=None, pred=None):
        """
        Evaluates accuracy of the classifier.
        :return: float
                Accuracy of the classifier
        """
        t = self.y_test if test is None else test
        p = self.y_pred if pred is None else pred
        return accuracy_score(t, p)


def test_precision():
    """
    Picks out 9 combinations of 3 features from the feature list. Checks the precision for the three available
    classifiers. And does the same for the full set of features.
    :return: None
    """
    training, test = prepare_data('./static/diabetes.csv')
    features = ['pregnant', 'glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree', 'age']
    classifiers = ['KNN', 'SVC', 'NB']

    agenda = list(combinations(features, 3))[0:9]
    agenda.append(features)

    for feature_list in agenda:
        print(f'Features: {" ".join(feature_list)}')
        for mode in range(3):
            p = Predictor(training, test)
            p.fit(list(feature_list), mode)
            p.predict()
            print(f'Classifier: {classifiers[mode]}, Precision: {p.get_accuracy()}')


if __name__ == '__main__':
    test_precision()

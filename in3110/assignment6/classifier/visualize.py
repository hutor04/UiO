import io
from classifier.data import prepare_data
from classifier.fitting import Predictor
import numpy as np
import matplotlib.pyplot as plt


def visualize(features, mode=0, standalone=True):
    """
    Visualizes the decision boundaries for a chosen classifier. Supported modes: 0 - kNN, 1 - SVC,
    2 - NB. NB is default. Takes as an argument the list of features (maximum 2) from the following set
    of features: 'pregnant', 'glucose', 'pressure', 'triceps', 'insulin', 'mass', 'pedigree', 'age'.
    The function can either display the plot or return it as the byt object.
    :param features: list
                    List of features. Maximum 2 features are allowed.
    :param mode: int
                0 - kNN, 1 - SVC, 2 - NB.
    :param standalone: boolean
                    Determines weather the plot is displayed or returned as byte_image.
    :return: None
            Displays a scatter plot with decision boundaries.
    """
    X_train, X_test = prepare_data('./static/diabetes.csv')
    y_train = X_train['diabetes']
    p = Predictor(X_train, X_test)
    classifier = p.fit(features, mode)

    x_min, x_max = X_train[features[0]].min() - 1, X_train[features[0]].max() + 1
    y_min, y_max = X_train[features[1]].min() - 1, X_train[features[1]].max() + 1

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))

    plt.plot(sharex='col', sharey='row', figsize=(10, 8))

    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X_train[features[0]], X_train[features[1]], c=y_train, s=20, edgecolor='k')

    if standalone:
        plt.show()
    else:
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        plt.close()
        return bytes_image


if __name__ == '__main__':
    visualize(['pregnant', 'glucose'], mode=2)

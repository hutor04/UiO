#!/usr/bin/env python3
from flask import Flask, render_template, send_file, request
import matplotlib
from classifier.visualize import visualize
from classifier.fitting import Predictor
from classifier.data import prepare_data

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 #  Forces flask to not cache images

train, test = prepare_data('./static/diabetes.csv')
matplotlib.use('agg')
classifiers = ['kNN', 'SVC', 'NB']


@app.route('/')
def select_features():
    """
    Home page, allows to choose type of classifier and features.
    :return: HTML
    """
    return render_template('slct.html')


@app.route('/show', methods=['POST'])
def classifier_visualization():
    """
    Handles the page where the scatter plot and classifier accuracy is displayed.
    :return:
    """
    mode = int(request.form['classifier'])
    features = request.form.getlist('features')
    no_features = len(features)

    p = Predictor(train, test)
    p2 = Predictor(train, train)
    p.fit(features, mode)
    p2.fit(features, mode)
    p.predict()
    p2.predict()
    test_acc = p.get_accuracy()
    train_acc = p2.get_accuracy()

    cur_features = ', '.join(features)
    cls = classifiers[mode]

    return render_template('cls.html', features=cur_features, train_acc=train_acc, test_acc=test_acc, classifier=cls,
                           mode=mode, no_features=no_features)


@app.route("/plot.png", methods=['GET'])
def plot_png():
    """
    Plots the scatter plot, mode and features are passed as get parameters.
    """
    mode = int(request.args.get('m'))
    features = request.args.get('f').split(', ')
    graph = visualize(features, mode=mode, standalone=False)
    return send_file(graph,
                     attachment_filename='plot.png',
                     mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)

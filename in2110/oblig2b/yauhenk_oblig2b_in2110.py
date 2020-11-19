import spacy
from spacy import displacy

from in2110.oblig2b import plot_learning_curve
#from oblig2b import plot_learning_curve
from in2110.conllu import ConlluDoc

#from conllu import ConlluDoc

from typing import Iterable, Any, List, Tuple
from itertools import chain
from operator import attrgetter
from pathlib import Path
from multiprocessing import Pool, cpu_count

# Settings
DIR_WITH_MODELS = '.'
MODELS_DIR = 'models-*'
CONNLU_DEV = 'no_bokmaal-ud-dev.conllu'
TRAIN_SIZE = [1.5625, 3.125, 6.25, 12.5, 25, 50, 100]
METRICS = ['Accuracy', 'UAS', 'LAS']
# 1.5625 % (246), 3.125 % (491), 6.25 % (981), 12.5 % (1962), 25 % (3924), 50 % (7848)

TEXT = 'Jeg har nå lagt ut siste kvalifiseringsoppgave i Canvas.'

# Attribute names
POS = 'tag_'
DEP = 'dep_'
HEAD = 'head.orth'


def tag_parse_spacy(model, unlabeled_docs) -> None:
    for i in unlabeled_docs:
        model.tagger(i)
        model.parser(i)


def _get_attributes(prediction, attributes: List[str]):  # Collects the required attributes
    getter = attrgetter(*attributes)
    return ((getter(token) for token in doc) for doc in prediction)


def _accuracy(true: Iterable[Iterable[Any]],
             pred: Iterable[Iterable[Any]]) -> float:
    true = chain(*true)
    pred = chain(*pred)

    size = 0
    fails = 0

    for tag, prediction in zip(true, pred):
        if tag != prediction:
            fails += 1
        size += 1

    return 1-fails/size


def accuracy(true, pred):
    spacy_tags_prediction = _get_attributes(pred, [POS])
    gold_standard_tags = _get_attributes(true, [POS])

    return _accuracy(gold_standard_tags, spacy_tags_prediction)


def attachment_score(true: List, pred: List) -> Tuple[float, float]:
    spacy_head_prediction = _get_attributes(pred, [HEAD])
    spacy_head_dep_prediction = _get_attributes(pred, [HEAD, DEP])

    gold_head_prediction = _get_attributes(true, [HEAD])
    gold_head_dep_prediction = _get_attributes(true, [HEAD, DEP])

    las = _accuracy(gold_head_dep_prediction, spacy_head_dep_prediction)
    uas = _accuracy(gold_head_prediction, spacy_head_prediction)

    return uas, las


def _worker(model: str) -> Tuple[float, float, float]:
    print('Processing model {}...'.format(model))
    nb = spacy.load(model)
    conllu_dev = ConlluDoc.from_file(CONNLU_DEV)
    dev_docs = conllu_dev.to_spacy(nb)
    dev_docs_unlabeled = conllu_dev.to_spacy(nb, keep_labels=False)
    tag_parse_spacy(nb, dev_docs_unlabeled)
    acc = accuracy(dev_docs_unlabeled, dev_docs)
    att = attachment_score(dev_docs_unlabeled, dev_docs)

    return acc, att[0], att[1]


def worker() -> List[Tuple[float, float, float]]:
    root = Path(DIR_WITH_MODELS)
    models = [str(folder) for folder in root.glob(MODELS_DIR)]
    models.sort()

    data = []  # List of tuples (accuracy, uas, las)

    cores = cpu_count()

    with Pool(cores) as pool:
        for i in pool.map(_worker, models):
            data.append(i)

    return data


def printer(data: List[Tuple[float, float, float]]) -> None:
    template = '{:>12} | {:>20} | {:>20} | {:>20}'
    header = template.format('Size (%):', METRICS[0], METRICS[1], METRICS[2])

    print('Results:')
    print(header)
    for size, d in zip(TRAIN_SIZE, data):
        print(template.format(size, d[0], d[1], d[2]))


def get_images(data: List[Tuple[float, float, float]]) -> None:
    print('Creating Charts...')
    x_labels = [round(i, 2) for i in TRAIN_SIZE]

    for i, metric in enumerate(METRICS):
        plot_learning_curve(x_labels, [d[i] for d in data], metric)


if __name__ == '__main__':
    data = worker()
    printer(data)
    get_images(data)

    # Task 3b
    nb = spacy.load('models-06')
    doc = nb(TEXT)

    # Saving image
    svg = displacy.render(doc, style='dep', options={'fine_grained': True})
    output_path = Path('sentence.svg')
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(svg)

    # Serving image
    displacy.serve(doc, style="dep", options={"fine_grained": True})

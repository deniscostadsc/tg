# coding: utf-8
import unicodedata

from nltk import NaiveBayesClassifier


def clean(document):
    # remove non ascii characters
    document = unicodedata.normalize('NFD', document)
    return document.encode('ASCII', 'ignore')


def ngrams(document, n=3):
    if not isinstance(document, list):
        document = document.split()
    document = [clean(word) for word in document]
    return [tuple(document[i:i + n])
        for i in range(len(document) - n + 1)]


def all_trigrams(documents):
    all_trigrams = set()
    for document in documents:
        all_trigrams.update(ngrams(document[0]))
    return all_trigrams


documents = (
    (u'a menina está com dengue', 'reliable'),
    (u'pessoa com dengue é dengosa?', 'unreliable'),
    (u'Essa semana acordei mal. Será que estou com dengue?', 'reliable'),
    (u'Fui no médico. Deu dengue!', 'reliable')
)


def document_feature(document):
    document_trigrams = ngrams(document)
    feature = {}
    for trigram in all_trigrams(documents):
        feature['-'.join(trigram)] = trigram in document_trigrams
    return feature


def generate_training_set(documents):
    return [(document_feature(d), c) for d, c in documents]

classifier = NaiveBayesClassifier.train(generate_training_set(documents))

print(classifier.classify(document_feature(u'Á menina pegou dengue')))



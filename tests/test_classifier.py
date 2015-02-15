# coding: utf-8
import pytest 

import classifier


def test_clean_remove_accents():
    text = u'Antes se escrevia idéia. Agora é ideia.'
    expected = 'antes se escrevia ideia agora e ideia '
    assert expected == classifier.clean(text) 


def test_trigrams():
    text = u'Antes se escrevia idéia. Agora é ideia.'
    expected = [('antes', 'se', 'escrevia'),
        ('se', 'escrevia', 'ideia'),
        ('escrevia', 'ideia', 'agora'),
        ('ideia', 'agora', 'e'),
        ('agora', 'e', 'ideia')]
    assert expected == classifier.ngrams(text)


def test_all_trigrams():
    documents = ((u'a menina está com dengue', 'reliable'),
        (u'pessoa com dengue é dengosa?', 'unreliable'),
        (u'Essa semana acordei mal. Será que estou com dengue?', 'reliable'),
        (u'Fui "no médico. Deu dengue!', 'reliable'))
    expected = set([('a', 'menina', 'esta'),
        ('acordei', 'mal', 'sera'),
        ('com', 'dengue', 'e'),
        ('dengue', 'e', 'dengosa'),
        ('essa', 'semana', 'acordei'),
        ('esta', 'com', 'dengue'),
        ('estou', 'com', 'dengue'),
        ('fui', 'no', 'medico'),
        ('mal', 'sera', 'que'),
        ('medico', 'deu', 'dengue'),
        ('menina', 'esta', 'com'),
        ('no', 'medico', 'deu'),
        ('pessoa', 'com', 'dengue'),
        ('que', 'estou', 'com'),
        ('semana', 'acordei', 'mal'),
        ('sera', 'que', 'estou')])
    assert expected == classifier.all_trigrams(documents)


def test_document_feature():
    text = u'A minha irmã está com dengue.'
    documents = ((u'a menina está com dengue', 'reliable'),
        (u'pessoa com dengue é dengosa?', 'unreliable'),
        (u'Essa semana acordei mal. Será que estou com dengue?', 'reliable'),
        (u'Fui "no médico. Deu dengue!', 'reliable'))
    expected = {'a-menina-esta': False,
        'acordei-mal-sera': False,
        'com-dengue-e': False,
        'dengue-e-dengosa': False,
        'essa-semana-acordei': False,
        'esta-com-dengue': True,
        'estou-com-dengue': False,
        'fui-no-medico': False,
        'mal-sera-que': False,
        'medico-deu-dengue': False,
        'menina-esta-com': False,
        'no-medico-deu': False,
        'pessoa-com-dengue': False,
        'que-estou-com': False,
        'semana-acordei-mal': False,
        'sera-que-estou': False}
    assert expected == classifier.document_feature(text, documents)

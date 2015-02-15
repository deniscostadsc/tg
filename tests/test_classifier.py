# coding: utf-8
import pytest 

import classifier


def test_clean_remove_accents():
    text = u'Antes se escrevia idéia. Agora é ideia.'
    expected = 'antes se escrevia ideia agora e ideia '
    assert expected == classifier.clean(text) 

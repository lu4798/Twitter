from twitter_api import word_counter
import pytest

def test_argument_not_string():
    with pytest.raises(TypeError):
        word_counter(5)

def test_two_same_words():
    assert word_counter("hola hola")==[["hola", 2]]

def test_with_numbers():
    assert word_counter("ho1a ho1a 5 5 7")==[["ho1a", 2],["5",2],["7",1]]

def test_many_spaces():
    assert word_counter("hola           hola") == [["hola", 2]]

def test_stop_words():
    assert word_counter("de")==[]

def test_two_equal_words_and_stopwords():
    assert word_counter("hola de hola")==[["hola", 2]]

def test_two_equal_words_and_two_stopwords():
    assert word_counter("hola de a hola") == [["hola", 2]]

def test_two_pairs_of_equal_words():
    assert word_counter("hola adios adios hola")==[["hola", 2],["adios", 2]]

def test_two_words_capitalize_difference():
    assert word_counter("HoLa hola")==[["hola", 2]]

def test_not_letter_simbols():
    assert word_counter(". ,-´")==[]

def test_all_different_words_with_stopwords():
    assert word_counter("hola adios que tal como va")==[["hola",1],["adios",1],["tal",1]]

def test_english_stopwords():
    assert word_counter("The rain is in the su'n Sun thE Rain RAIN the In")==[["rain",3],["sun",2]]


def test_czech_stopwords():
    assert word_counter("pokuD déšt Déšt naproti kocka")==[["déšt",2],["pokud",1],["kocka", 1]]

def test_all_different_words_with_stopwords_from_different_languages():
    assert word_counter("hola adios que tal como va naproti ???? ????")==[["hola",1],["adios",1],["tal",1]]

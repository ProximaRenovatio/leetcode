from solutions.tries.medium._0211_design_add_and_search_words_data_structure import WordDictionary

def test_design_add_and_search_words_data_structure():
    dictionary = WordDictionary()

    dictionary.addWord("bad")
    dictionary.addWord("dad")
    dictionary.addWord("mad")

    assert dictionary.search("pad") is False
    assert dictionary.search("bad") is True
    assert dictionary.search(".ad") is True
    assert dictionary.search("b..") is True

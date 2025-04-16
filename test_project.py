from project import get_objective, get_char_dict, generate

def test_get_objective_learn():
    assert get_objective("Learn") == "LEARN"
    assert get_objective("  learn  ") == "LEARN"

def test_get_objective_test():
    assert get_objective("test") == "TEST"
    assert get_objective("TEST") == "TEST"

def test_get_char_dict_hiragana_level1():
    d = get_char_dict("HIRAGANA", 1)
    assert "あ" in d
    assert "が" not in d
    assert "きゃ" not in d

def test_get_char_dict_hiragana_level3():
    d = get_char_dict("HIRAGANA", 3)
    assert "が" in d
    assert "きゃ" in d

def test_get_char_dict_katakana_level3():
    d = get_char_dict("KATAKANA", 3)
    assert "ガ" in d
    assert "キャ" in d

def test_generate():
    test_dict = {"あ": "a", "い": "i"}
    kana, romaji = generate(test_dict)
    assert kana in test_dict
    assert romaji == test_dict[kana]

import random
import time

hiragana_basic = {
        "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
        "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
        "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
        "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
        "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
        "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
        "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
        "や": "ya", "ゆ": "yu", "よ": "yo",
        "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
        "わ": "wa", "を": "wo", "ん": "n"
}

hiragana_dakuon = {
        "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
        "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
        "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do",
        "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
        "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"
}

hiragana_yoon = {
        "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo",
        "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo",
        "しゃ": "sha", "しゅ": "shu", "しょ": "sho",
        "じゃ": "ja", "じゅ": "ju", "じょ": "jo",
        "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho",
        "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo",
        "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo",
        "びゃ": "bya", "びゅ": "byu", "びょ": "byo",
        "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo",
        "みゃ": "mya", "みゅ": "myu", "みょ": "myo",
        "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo"
}

katakana_basic = {
        "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
        "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
        "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
        "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
        "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
        "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
        "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
        "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
        "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
        "ワ": "wa", "ヲ": "wo", "ン": "n"
}

katakana_dakuon ={
    "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go",
        "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo",
        "ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de", "ド": "do",
        "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",
        "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po"
}

katakana_yoon = {
        "キャ": "kya", "キュ": "kyu", "キョ": "kyo",
        "ギャ": "gya", "ギュ": "gyu", "ギョ": "gyo",
        "シャ": "sha", "シュ": "shu", "ショ": "sho",
        "ジャ": "ja", "ジュ": "ju", "ジョ": "jo",
        "チャ": "cha", "チュ": "chu", "チョ": "cho",
        "ニャ": "nya", "ニュ": "nyu", "ニョ": "nyo",
        "ヒャ": "hya", "ヒュ": "hyu", "ヒョ": "hyo",
        "ビャ": "bya", "ビュ": "byu", "ビョ": "byo",
        "ピャ": "pya", "ピュ": "pyu", "ピョ": "pyo",
        "ミャ": "mya", "ミュ": "myu", "ミョ": "myo",
        "リャ": "rya", "リュ": "ryu", "リョ": "ryo"
}

def main():
    objective = get_objective(input("What do you want to do? (Learn/Test)"))
    char = "Character? (Hiragana/Katakana)"
    if objective == "LEARN":
        study(input(char).strip().upper())
    elif objective == "TEST":
        chars = input(char).strip().upper()
        level = get_level()
        char_dict = get_char_dict(chars, level)
        start = time.perf_counter()
        score = marks(char_dict)
        end = time.perf_counter()
        total_time = end-start
        print(f"Score: {score}%")
        print(f"Time used: {total_time:.2f} seconds")

def get_objective(prompt):
    while True:
        objective = prompt.strip().upper()
        if objective == "LEARN":
            return "LEARN"
        elif objective == "TEST":
            return "TEST"
        else:
            print("Invalid input. Please type Learn or Test.")
            pass

def study(char):
    if char == "HIRAGANA":
        print("Hiragana")
        print("\nBasic")
        for key, value in hiragana_basic.items():
            print(key,":", value)
        print("\nDakuon")
        for key, value in hiragana_dakuon.items():
            print(key,":", value)
        print("\nYoon")
        for key, value in hiragana_yoon.items():
            print(key,":", value)
    elif char == "KATAKANA":
        print("Katakana")
        print("\nBasic")
        for key, value in katakana_basic.items():
            print(key,":", value)
        print("\nDakuon")
        for key, value in katakana_dakuon.items():
            print(key,":", value)
        print("\nYoon")
        for key, value in katakana_yoon.items():
            print(key,":", value)
    else:
        print("Invalid input. Please type Hiragana or Katakana.")
        pass

def get_level():
    while True:
        try:
            n = int(input("Level (1/2/3): "))
            if 1 <= n <= 3:
                return n
            else:
                print("Invalid level. Please choose a level from 1 to 3")
        except ValueError:
            print("Please type a number")

def get_char_dict(char, level):
    if char == "HIRAGANA":
        hiragana = {}
        if level >= 1:
            hiragana.update(hiragana_basic)
        if level >= 2:
            hiragana.update(hiragana_dakuon)
        if level == 3:
            hiragana.update(hiragana_yoon)
        return hiragana
    elif char == "KATAKANA":
        katakana = {}
        if level >= 1:
            katakana.update(katakana_basic)
        if level >= 2:
            katakana.update(katakana_dakuon)
        if level == 3:
            katakana.update(katakana_yoon)
        return katakana
    else:
        print("Invalid input. Please type Hiragana or Katakana.")
        pass

def generate(char_dict):
    return random.choice(list(char_dict.items()))

def play(kana, romaji):
    answer = input(f"{kana}: ")
    if answer == romaji:
        print("Correct ✅")
        return True
    else:
        print(f"Wrong ❌ Correct answer = {kana} : {romaji}")
        return False
        
def marks(char_dict):
    i = 0
    score = 0
    while i <= 19:
        kana, romaji = generate(char_dict)
        if play(kana, romaji) == True:
            score += 5
        i += 1
    return score

if __name__ == "__main__":
    main()
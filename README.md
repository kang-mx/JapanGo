# **JapanGo**

#### Video Demo: <https://youtu.be/vmor-YoqcIA>
####
#### Slides Link: <https://www.canva.com/design/DAGkqeJ8zSA/z8-QHYi-d8L-qGZHeBr8cQ/edit?utm_content=DAGkqeJ8zSA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton>
####
#### Description: This is a project to learn and test your Japanese.

In Japanese, Nihon means Japan and Nihongo means Japanese.
Other languages such as English is Eigo and Chinese is Chuugoku go where Chuugoku stands for China.

This project is JapanGo which is to learn the Japanese language efficiently.
Two Japanese character systems (Hiragana & Katakana) are included.

#### Choose to study or to test your Japanese proficiency!
Level 1: Basic only
Level 2: Basic + Dakuon
Level 3: Basic + Dakuon + Yoon
**Challenge yourself for the highest score within the fastest time**

### Code description
Main function will be below to better arrange the logic of the full code.

#### The dictionary for hiragana basic, hiragana dakuon, hiragana yoon, katakana basic, katakana dakuon and katakana yoon are generated
Dakuon is the extension of basic characters.
Yoon is the combination of basic characters and/or with dakuon characters.

#### get_objective()
It gets the objective for the user of the project.
The user can prompt whether they want to learn or test their Japanese language.
If the user types in learn (ignoring the casing and spaces), this function will return "LEARN" which will be used in the main function.
If the user types in test (ignoring the casing and spaces), this function will return "TEST" which will be used in the main function.
If the user types in anything else, this function will show the user that the input is invalid and will get the prompt from the user again until the user provides either learn or test for the prompt.

#### study(char)
It requires an object 'char'.
If char is equals to "HIRAGANA", it will show the full dictionary of Hiragana characters in both kana and romaji which contains all three types (basic, dakuon, yoon).
If char is equals to "KATAKANA", it will show the full dictionary of Katakana characters in both kana and romaji which contains all three types (basic, dakuon, yoon).
If char is anything else, this function will show the user that the input is invalid and will get the prompt from the user again until the char is either HIRAGANA or KATAKANA.

#### get_level()
It gets the level from the user
Only levels 1 to 3 are available. If the user inputs the prompt as either value, the function will return the same value.
If the number input is out of the range given, the function will tell the user that the level is invalid.
If the input is not a number, the function will tell the user to input a number instead.
The function will keep on looping until the user inputs a value between 1 to 3

#### get_char_dict(char, level)
It gets the character dictionary for the test later on.
The character has to be either "HIRAGANA" or "KATAKANA".
The level has to be between 1 to 3.

For both hiragana and katakana:
    If their level is at least 1, the basic kana and romaji dictionaries will be added into a new empty dictionary.
    If their level is at least 2, the dakuon kana and romaji dictionaries will be added into the dictionary.
    If their level is 3, the yoon kana and romaji dictionaries will be added into the dictionary.

In simpler terms:
    The character dictionary in level 1 will only have basic kana and romaji.
    The character dictionary in level 2 will have both basic and dakuon kana and romaji.
    The character dictionary in level 3 will contain all kana and romaji from basic, dakuon to yoon.

The character dictionary will be returned and will be referred as the term char_dict in the next few functions.

#### generate(char_dict)
It generates a random word from char_dict.

#### play(kana, romaji)
First it will get the answer from the user after showing the input of kana.
If the answer obtained is equal to the romaji of the kana shown, it will show "Correct ✅" and it will return the function as True.
If the answer is wrong, it will show "Wrong ❌" followed by the correct romaji of the kana. It will return the function as False.

#### marks(char_dict)
The game will play for 20 rounds.
The initial score is 0.
In each round, it will generate a character from the given character dictionary (char_dict). The kana and the romaji is then generated.
Next, the play function will use the kana and romaji generated.
If the play function returns True (which means the users' answer is correct), then a score of +5 will be given.
If the play function returns False (which means the users' answer is wrong), then no score will be given.
The score will accumulate outside of the rounds as the total score.
This function will return the final score of the player.

#### main()
This will be the main function where the user will only run this line of code.
First, it will prompt the user to get their objective of using this project via the get_objective() function.
Next, it will ask whether the user chooses Hiragana or Katakana and this input will be defined as char.

It will then check the objective the user gave.
If the objective is "LEARN", it will run the study(char) function where the char will go through both upper() (to capitalize every word) and strip() (to remove all spaces). The dictionary of the given character will then be shown to the user.

If the objective is "TEST", it will get the char and the level via get_level() function first.
Next, it will get the character dictionary via get_char_dict() function.
The timer will start then where the test starts.
The score is obtained via the marks() function.
The timer will then end and the total time used will be obtained from the start and end time counters.
At last, both the score and the time used will be printed out as the output for the user.

#### Note
if __name__ == "__main__":
    main()

This function is used instead of main() to make sure the project will only be called with the exact name.
It also helps in testing the project.

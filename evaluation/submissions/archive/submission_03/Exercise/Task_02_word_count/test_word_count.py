
from word_count import count_words

def test_count_words():
    assert count_words("That's the password: 'PASSWORD 123'!, cried the Special Agent.\nSo I fled.") == {
        "that's": 1,
        "the": 2,
        "password": 2,
        "123": 1,
        "cried": 1,
        "special": 1,
        "agent": 1,
        "so": 1,
        "i": 1,
        "fled": 1
    }
    assert count_words("You come back, you hear me? DO YOU HEAR ME?") == {
        "you": 3,
        "come": 1,
        "back": 1,
        "hear": 2,
        "me": 2,
        "do": 1
    }

test_count_words()
print("All tests passed!")

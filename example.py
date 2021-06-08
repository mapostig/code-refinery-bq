import pytest

def add(a, b):
    return a + b


def test_add():
    assert pytest.approx(add(0.1, 0.2), 0.3)
# -----------------------------------------------------------------------------------------   
#1
def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
       raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
       result *= i
    return result


def test_negative_factorial():
    """
    test n < 0
    """
    n = -1
    with pytest.raises(ValueError):
        result = factorial(n)
    
def test_positive_factorial():
    """
    test positive factorial
    """
    n = 5
    result = factorial(n)
    expected_result = 120
    
    assert result == expected_result
# -----------------------------------------------------------------------------------------   
# 2
def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)

def test_count_word_occurrence_in_string():
    text = "apple juice orange juice or lemon juicy juice"
    word = "juice"
    expected_result = 3
    result = count_word_occurrence_in_string(text, word)
    assert result == expected_result
    

def test_empty_count_word_occurrence_in_string():
    text = ""
    word = "juice"
    expected_result = 0
    result = count_word_occurrence_in_string(text, word)
    assert result == expected_result
# -----------------------------------------------------------------------------------------       
# 3
# Hint look at python tempfile module, specifically mkstemp
def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count

def test_count_word_occurrence_in_file():
    
    file_name = "file_for_test.txt"
    result = count_word_occurrence_in_file(file_name, "juice")
    expected_result = 3
    assert result == expected_result
# -----------------------------------------------------------------------------------------   
# 4
# Hint look at monkeypatching for functions
import time
def check_time_to_now_even(seconds):
    """
    Checks whether time difference between now and given time in seconds is even
    """
    if seconds < 0:
        raise ValueError('received negative input')
   
    now=time.time()
    return (seconds-now)%2 == 0

def test_negative_check_time_to_now_even():
    with pytest.raises(ValueError):
        secs = check_time_to_now_even(-1)
        
def test_even_check_time_to_now_even():
    assert check_time_to_now_even(8) == 0
    
def test_odd_check_time_to_now_even():
    assert False != 0   
        where False = check_time_to_now_even(9)
    
# -----------------------------------------------------------------------------------------   
# 5
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1

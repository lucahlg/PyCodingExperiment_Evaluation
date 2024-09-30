from Task_03_word_search.word_search import WordSearch, Point

def test_word_search():
    puzzle = [
        "jefblpepre",
        "camdcimgtc",
        "oivokprjsm",
        "pbwasqroua",
        "rixilelhrs",
        "wolcqlirpc",
        "screeaumgr",
        "alxhpburyi",
        "jalaycalmp",
        "clojurermt"
    ]
    
    ws = WordSearch(puzzle)
    
    # Test for the word "python"
# Test for the word "cam"
    result = ws.search("cam")
    assert result is not None
    assert result[0] == Point(0, 1)  # Starting point
    assert result[1] == Point(2, 1)  # Ending point

    # Test for the word "screea"
    result = ws.search("screea")
    assert result is not None
    assert result[0] == Point(0, 6)  # Starting point
    assert result[1] == Point(5, 6)  # Ending point

    # Test for a word not in the puzzle
    result = ws.search("notaword")
    assert result is None

    # Test for a word not in the puzzle
    result = ws.search("notaword")
    assert result is None

    # Test for a word not in the puzzle
    result = ws.search("notaword")
    assert result is None

if __name__ == "__main__":
    test_word_search()
    print("All tests passed!")

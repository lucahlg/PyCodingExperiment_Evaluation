from Task_01_collatz_conjecture.collatz_conjecture import steps

def test_collatz():
    assert steps(12) == 9
    assert steps(1) == 0
    assert steps(19) == 20

if __name__ == "__main__":
    test_collatz()
    print("All tests passed!")

from Task_02_prime_factors.prime_factors import factors

def test_prime_factors():
    assert factors(60) == [2, 2, 3, 5]
    assert factors(1) == []
    assert factors(28) == [2, 2, 7]

if __name__ == "__main__":
    test_prime_factors()
    print("All tests passed!")

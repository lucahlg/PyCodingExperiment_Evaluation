
from raindrops import convert

def test_convert():
    assert convert(28) == "Plong"
    assert convert(30) == "PlingPlang"
    assert convert(34) == "34"
    assert convert(15) == "PlingPlang"
    assert convert(21) == "PlingPlong"
    assert convert(35) == "PlangPlong"
    assert convert(105) == "PlingPlangPlong"
    assert convert(1) == "1"

test_convert()
print("All tests passed!")

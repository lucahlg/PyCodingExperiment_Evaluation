
from resistor_color_expert import resistor_label

def test_resistor_label():
    assert resistor_label(["orange", "orange", "black", "green"]) == "33 ohms ±0.5%"
    assert resistor_label(["orange", "orange", "orange", "grey"]) == "33 kiloohms ±0.05%"
    assert resistor_label(["orange", "orange", "blue", "red"]) == "33 megaohms ±2%"
    assert resistor_label(["orange", "orange", "brown", "green"]) == "330 ohms ±0.5%"
    assert resistor_label(["orange", "orange", "red", "grey"]) == "3.3 kiloohms ±0.05%"
    assert resistor_label(["orange", "orange", "orange", "black", "green"]) == "333 ohms ±0.5%"
    assert resistor_label(["orange", "red", "orange", "blue", "violet"]) == "323 megaohms ±0.1%"
    assert resistor_label(["black"]) == "0 ohms"

test_resistor_label()
print("All tests passed!")

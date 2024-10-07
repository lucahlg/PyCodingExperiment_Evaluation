def resistor_label(colors):
    color_values = {
        'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
        'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9,
        'gold': 5, 'silver': 10
    }
    
    tolerance_values = {
        'grey': '±0.05%', 'violet': '±0.1%', 'blue': '±0.25%', 'green': '±0.5%',
        'brown': '±1%', 'red': '±2%', 'gold': '±5%', 'silver': '±10%'
    }
    
    if len(colors) == 1:
        return f"{color_values[colors[0]]} ohms"
    
    elif len(colors) == 4:
        value_1 = color_values[colors[0]]
        value_2 = color_values[colors[1]]
        multiplier = 10 ** color_values[colors[2]]
        tolerance = tolerance_values[colors[3]]
        resistance = (value_1 * 10 + value_2) * multiplier
        return f"{resistance} ohms {tolerance}"
    
    elif len(colors) == 5:
        value_1 = color_values[colors[0]]
        value_2 = color_values[colors[1]]
        value_3 = color_values[colors[2]]
        multiplier = 10 ** color_values[colors[3]]
        tolerance = tolerance_values[colors[4]]
        resistance = ((value_1 * 100) + (value_2 * 10) + value_3) * multiplier
        return f"{resistance} ohms {tolerance}"
    
    else:
        return "Invalid number of colors"

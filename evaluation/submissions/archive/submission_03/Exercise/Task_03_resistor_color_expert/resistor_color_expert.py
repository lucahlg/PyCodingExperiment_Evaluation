def resistor_label(colors):
    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    tolerance_values = {
        "grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%",
        "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"
    }
    
    if len(colors) == 1:
        return "0 ohms"
    
    if len(colors) == 4:
        value = (color_values[colors[0]] * 10 + color_values[colors[1]]) * (10 ** color_values[colors[2]])
        tolerance = tolerance_values[colors[3]]
    elif len(colors) == 5:
        value = (color_values[colors[0]] * 100 + color_values[colors[1]] * 10 + color_values[colors[2]]) * (10 ** color_values[colors[3]])
        tolerance = tolerance_values[colors[4]]
    
    if value >= 1_000_000:
        value_str = f"{value // 1_000_000} megaohms"
    elif value >= 1_000:
        value_str = f"{value // 1_000} kiloohms"
    else:
        value_str = f"{value} ohms"
    
    return f"{value_str} {tolerance}"

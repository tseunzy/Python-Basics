# Covers: Functions, Conditionals, String formatting
def convert_temperature(temp, unit):
    if unit.upper() == "C":
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        return f"Temperature in Fahrenheit: {fahrenheit:.2f}°F, Kelvin: {kelvin:.2f}K"
    elif unit.upper() == "F":
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        return f"Temperature in Celsius: {celsius:.2f}°C, Kelvin: {kelvin:.2f}K"
    else:
        return "Invalid unit"


print(convert_temperature(8, 'g'))
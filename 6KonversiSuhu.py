print("======= Program Konversi Suhu ========")
celcius = float(input("Masukkan suhu dalam celcius : "))

# celcius to reamur
reamur = (4/5) * celcius
# celcius to fahrenheit
fahrenheit = ((9/5)*celcius)+32
# celcius to kelvin
kelvin = celcius + 273.15

print(f"{celcius}°C = {reamur}°R")
print(f"{celcius}°C = {fahrenheit}°F")
print(f"{celcius}°C = {kelvin}K")

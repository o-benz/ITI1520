#Commentaires
#Student number: 300262795
#Student name: Omar Benzekri

def celsius_en_fahrenheit(temp_Celsius):
    "Transforme la temperature du Celsius en Fahrenheit"
    temp_Fahrenheit = temp_Celsius*9/5+32
    return temp_Fahrenheit
temp_Celsius=100
t_Fahrenheit = celsius_en_fahrenheit(temp_Celsius)
print(temp_Celsius, "Celsius est", t_Fahrenheit, "Fahrenheit.")

temp_Celsius=10
t_Fahrenheit = celsius_en_fahrenheit(temp_Celsius)
print(temp_Celsius, "Celsius est", t_Fahrenheit, "Fahrenheit.")

temp_Celsius=0
t_Fahrenheit = celsius_en_fahrenheit(temp_Celsius)
print(temp_Celsius, "Celsius est", t_Fahrenheit, "Fahrenheit.")


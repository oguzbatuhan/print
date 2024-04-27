name = "Oguz"
print('My name is {}'.format(name))

dizi = ("Antalya", "Ankara", "Adana")
print(dizi[2])

dizi1 = ("Antalya" "Ankara" "Adana")
print(dizi1[2:5])
print(len(dizi1))

number : int = 11
name : str = "Batuhan"

print("I'm "+name+" and nambur "+str(number))

print(">>>>>>>>>>>")

name = "Oğuz"
surName = "Batuhan"
age = "20"
işlem = 200 / 700

print(f"I'm {name} {surName} years old {age}.")
print("I'm {} {} years old {}".format(name, surName, age))
print("{x:3.2}".format(x=işlem))

print(">>>>>>>>>")

message = "   Hi python. hi Oğuz. hi Sude."
print(message)
print(message.upper())
print(message.title())
print(message.lower())
print(message.capitalize())
print(message.strip())
dizi = (message.split("."))
print(dizi[0])
print(dizi[2] + dizi[1])
print(" ".join(dizi))
print(message.find("Sude"))
print(message.startswith(" "))
print(message.endswith("."))
message2 = message.replace("ğ","g").replace(" ","/").replace(",",".")
print(message2)

 
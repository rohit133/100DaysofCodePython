# file not find 
try:
    file = open("Day-30\\a_file.txt")
    a_directionary = {"Key": "value"}
    print(a_directionary["Key"])
except FileNotFoundError:
    file = open("Day-30\\a_file.txt","w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
   raise TypeError("Type not compatiable")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
 
bmi = weight / height ** 2 
print(bmi)
 
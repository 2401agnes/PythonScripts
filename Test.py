is_hot = False
is_cold =False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    pass
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


name ="wertt"
if len(name) <3:
    print ("name must be at least 3 characters")
elif len(name) >50:
    print("name must be a maximum of 50 characters")
else:
    print("name looks good")


secret_number =9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count += 1
    if guess== secret_number:
        print("Congragulations. You won!!!")
        break
    elif guess != secret_number:
        print("Sorry you failed")

 
prices =[10, 20, 30]
total=0
for price in prices:
    total +=price
print(f"Total:{total}")


phone = input("Phone: ")
digits_mapping ={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "5": "Five"
}
output=""
for ch in phone:
    output +=digits_mapping.get(ch, "!") + ""
print(output)


import random
class Dice:
    def roll(self):
        first= random.randint(1, 6)
        second= random.randint(1, 6)
        return first, second
dice = Dice()
print(dice.roll())


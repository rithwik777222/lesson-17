class elements:
    def __init__(self,value):
         self.value = value
        
stone = elements('x')
paper = elements('y')
scissors = elements('z')

player = int(input('stone,paper or scissors(1,2 or 3):'))

import random
a = random.choice([1,2,3])
print("the computer has chosen",a)

if player == a:
 print("draw")
elif player==1:
    if a == 2:
        print("the computer won over stone using paper")
    elif a == 3:
        print("you won over scissors using stone")
elif player == 2:
    if a == 1:
        print("you won over stone using paper")
    elif a ==3:
        print("the coputer won over paper using scissors")
elif player ==3:
    if a ==1:
        print("the computer won over scissors using stone")
    elif a==2:
        print('you won over paper using scissors ')
else:
    print('choose valid number')


        
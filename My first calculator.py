import re

print('Simple Calculator program using Python')
print("Type 'exit' to quit the program\n")

previous = 0
run = True

def MyAdvanceCalc():
   global previous
   global run

   equation = " "
   if previous == 0:
       equation = input("Enter your values:\n")
   else:
       equation = input(str(previous))

   if equation == 'exit':
       print("See you later")
       run = False
   else:
       equation = re.sub('[a-zA-z,.:()" "]', ' ', equation)

       if previous == 0:
         previous = eval(equation)
       else:
          previous = eval(str(previous) + equation)

while run:
   MyAdvanceCalc()

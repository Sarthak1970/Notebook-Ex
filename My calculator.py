import re

print("My Calculator")
print("Type 'Quit' to exit \n")

previous=0
run=False
def performMath():
    global run
    global previous
    equation=""
    if equation == 0:
            equation=input("Enter Equation:")
    else:
        equation=input(str(previous))


    if equation =="quit":
        print("Goodbye")
        run=False
    else:
        equation=re.sub('[a-zA-Z,.:()" "]','',equation)
    if previous==0:
        previous=eval(equation)
    else:
        previous=eval(str(previous)+ equation)  
       

while run:
    performMath()

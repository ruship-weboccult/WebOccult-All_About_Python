import math
# Recursive Method
def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)

#program starts from here
while True:
    try:
        input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the Number for which you want to find Factorial.\n\nEnter Your Input:""")
        temp=input_string.lower()

        # Check to run program or not
        if temp=='exit':
            break
        else:
            num=float(input_string)
            if num<0:
                raise Exception("Factorial of Negative Number doesn't exist.\n")
                
            if float(input_string).is_integer():
                # calling function recursively from here
                print(f"\n\n💡Factorial of {int(num)} Number is:",factorial(int(num)),"\n")
            else:
                print(f"\n\n💡Factorial of {num} Number is:",math.gamma(num + 1),"\n")

    except Exception as e:
        print("\n\n❌Error: ",e,"\n")
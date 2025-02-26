# Iterative Method
import math
#Program starts from here
while True:
    try:
        input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the Number for which you want to find Factorial.\n\nEnter Your Input:""")
        temp=input_string.lower()
        ans=1
        # Check to run program or not
        if temp=='exit':
            break
        else:
            if float(input_string)<0.0:
                raise Exception("Factorial of Negative Number doesn't exist.\n")
            if float(input_string).is_integer():
                num=int(input_string)
                n=num
                # executing formula
                while num>0:
                    ans=ans*num
                    num=num-1
            else:
                n=float(input_string)
                ans=math.gamma(n + 1)
            print(f"\n\n💡Factorial of {n} Number is:",ans,"\n")
    except Exception as e:
        print("\n\n❌Error: ",e,"\n")
num=int(input("Enter the Number for which you want to make Pattern: "))

for i in range (0,(2*num)+3):
    for j in range(0,(2*num)+2):
        if (i==0 or i==((2*num)+2)) and j!=0:
            print("0 ",end="")
        elif j==0:
            print("O ",end="")
        elif i==(num+1) and j==(num+1):
            print("O ",end="")
        elif i==(num+1) or j==(num+1):
            print("  ",end="")
        else:
            if i<=num:
                if i<=j and j<=num:
                    print(num-j+1,end=" " if (num-j+1)<10 else "")
                elif i>j and j<=num:
                    print("  ",end="")
                elif i+j>((2*num)+1) and j>(num+1):
                    print((2*num)+2-j,end=" " if (2*num)+2-j<10 else "")
                elif i+j<=((2*num)+1) and j>(num+1):
                    print("  ",end="")
                else:
                    print("  ",end="")
            elif i>(num+1):
                if i+j<=2*(num+1) and j<=num:
                    print(j,end=" " if j<10 else "")
                elif i+j>2*(num+1) and j<=num:
                    print("  ",end="")
                elif i>=j and j>(num+1):
                    print(j-num-1,end=" " if (j-num-1)<10 else "")
                elif i<j and j>(num+1):
                    print("  ",end="")
            else:
                print(" ",end="")
    print("O\n",end="")
def func(str):
    try:
        ls=str.split()
        output=[]
        for i in ls:
            if not i.isnumeric():
                raise Exception("\n*** Only Enter the Sequence of Number Separated by Space ***")
            else:
                if int(i) not in output:
                    output.append(int(i))
                else:
                    print("\n\n*** Not all Number are different from each other ***")
                    return
        print("\n***\nAll Number are different from each other.\nNumbers are:",output,"\n***\n")

    except Exception as e:
        print("\n\n❌Error: ",e,"\n")

while True:
    input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the Enter the Sequence of Number(Space Separated).\n\nEnter Your Input:""")
    temp=input_string.lower()

    # Check to run program or not
    if temp=='exit':
        break
    else:
        func(input_string)
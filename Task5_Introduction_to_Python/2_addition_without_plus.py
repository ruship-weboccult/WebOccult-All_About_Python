# prompt: Write a Python program to add two positive integers without using the '+' operator

def add_without_plus(sequence_of_number):
    try:
        ls=sequence_of_number.split()

        if not (ls[0].strip().isnumeric() or ls[1].strip().isnumeric()) or len(ls)>2:
            raise Exception("\n*** Only Enter two Numbers Separated by Space ***")

        first=int(ls[0])
        second=int(ls[1])
        
        while second != 0:
            carry = first & second  # Calculate the carry bits
            first = first ^ second      # Calculate the sum without carry
            second = carry << 1  # Shift the carry bits to the left

        print("\n***\nAddition of ",int(ls[0])," & ",int(ls[1])," is : ",first,"***\n")

    except Exception as e:
        print("\n\n❌Error: ",e,"\n")

while True:
    input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the Numbers(Space Separated).\n\nEnter Your Input:""")
    temp=input_string.lower()

    # Check to run program or not
    if temp=='exit':
        break
    add_without_plus(input_string)
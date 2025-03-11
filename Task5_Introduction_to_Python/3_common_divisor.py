def common_divisors(sequence_of_number):
    try:
        ls=sequence_of_number.split()

        if not (ls[0].isnumeric() or ls[1].isnumeric()) or len(ls)>2:
            raise Exception("\n*** Only Enter the Numbers Separated by Space ***")

        first=int(ls[0])
        second=int(ls[1])
        
        print("\n***\nAll Common Divisors: ")
        for i in range(1, min(first, second) + 1):
            if first % i == 0 and second % i == 0:
                print(i)
        print("***\n")

    except Exception as e:
        print("\n\n❌Error: ",e,"\n")

while True:
    input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the Numbers(Space Separated).\n\nEnter Your Input:""")
    temp=input_string.lower()

    # Check to run program or not
    if temp=='exit':
        break
    common_divisors(input_string)
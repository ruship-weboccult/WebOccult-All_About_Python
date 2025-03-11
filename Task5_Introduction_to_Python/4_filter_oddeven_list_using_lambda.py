def filter_list(sequence_of_number):
    try:
        ls=sequence_of_number.split()
            
        even_numbers = list(filter(lambda x: int(x) % 2 == 0, ls))

        odd_numbers = list(filter(lambda x: int(x) % 2 != 0, ls))
        print("\n***\nOdd Numbers: ",odd_numbers,"\nEven Numbers: ",even_numbers,"\n***\n")
    except ValueError as ve:
        print("\n\n❌Value Error: Enter Only Numeric Value separated by Spaces.\n",ve,"\n")
    except Exception as e:
        print("\n\n❌Error: ",e,"\n")

while True:
    input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the Sequence of Number(Space Separated).\n\nEnter Your Input:""")
    temp=input_string.lower()

    # Check to run program or not
    if temp=='exit':
        break
    filter_list(input_string)
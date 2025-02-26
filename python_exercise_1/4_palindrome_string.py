while True:
    input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the String that want to check is Palindrom or not.\n\nEnter Your Input:""")
    temp=input_string.lower()

    # Check to run program or not
    if temp=='exit':
        break
    else:
        temp=''.join([i for i in input_string if i.isalpha() or i.isnumeric()]).lower()
        if temp==temp[::-1]:
            print("\n\n✅String is Palindrome.\n")
        else:
            print("\n\n❌String is not Palindrome.\n")
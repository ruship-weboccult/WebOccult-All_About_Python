# import string
while True:
    input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the String for you want Frequency of each word.\n\nEnter Your Input:""")
    temp=input_string.lower()

    # Check to run program or not
    if temp=='exit':
        break
    else:
        input_string = ''.join(ch if ch not in '!”#$%&()*+,-./:;<=>?@[\]^_`{|}~' else " " for ch in input_string)

        list_of_word=input_string.lower().strip().split()
        dict_of_word={}

        for i in list_of_word:
            if i in dict_of_word:
                dict_of_word[i]+=1
            else:
                dict_of_word[i]=1
        print("\n***\nFrequency of each word in Text:\n",dict_of_word,"\n***\n")
import re

def list_of_vowel_words(input_string):
    result=[]

    #main logic
    words = re.findall(r'\b\w+\'?\w*\b', input_string)
    for word in words:
        if word[0] in 'aeiouAEIOU':
            result.append(word)

    print("\n\n***\n📄List with all Words that Starts with vowel:\n",result,"\n***\n")

#Program starts from here
print("You have to give words separated by spaces as input, In Output it will give all words that starts with vowel character.")

while True:
    input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the Words separated by Spaces.\n\nEnter Your Input:""")
  
    temp=input_string.lower()
    # Check to call function or not
    if temp=='exit':
        break
    else:
        list_of_vowel_words(input_string)
    

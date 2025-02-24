import random
class InvalidInputError(Exception):
    def __init__(self, message):
        # super().__init__(message)
        self.message=message

    def __str__(self):
        return f"\nError: {self.message}"

# for next number guess  
def ask_again():
    ask=input("\nDo You Want to Guess Again(Yes/No): ")
    ask=ask.lower()
    if ask=="yes":
        print("\nYou Have 5 Guesses.")
        guess_numbers()
    elif ask=="no":
        return
    else:
        print("\n❌ Enter Correct Input(Yes/No).")
        ask_again()

def guess_numbers():
    tries=5
    Value=random.randint(1,10)
    flag=False
    # can run for 5 time maximum
    while tries>0:
        try:
            if tries<5:
                print(f"\nRemaining Guess:{tries}")
            tries-=1
            inputs=int(input("🤔Guess the Number(between 1 to 10):"))

            if inputs<1 or inputs>10:
                raise InvalidInputError("\n❌ Number must be in the range of 1 to 10.")
            
            # correct guess
            if inputs == Value:
                print(f"\n*** ✅ Correct Guess ***\n*** Number is {Value} ***")
                flag=True
                # print(f"...Your Score is(Out of 5): {tries} ...\n")
                break
            elif inputs<Value:
                print(f"\n📉 Input is Lower than Number to Guess.")
            else:
                print(f"\n📈 Input is Higher than Number to Guess.")

        except ValueError:
            print(InvalidInputError("\n❌ Input Must be in Number Format."))
        except InvalidInputError as iie:
            print(iie)
    
    # score
    if flag:
        print(f"\n*** Your Score is(Out of 5): {tries+1} {'⭐'*(tries+1)} ***\n")
    else:
        print(f"\n*** Your Score is(Out of 5): {tries} {'⭐'*(tries)} ***\n")
    ask_again()

# program starts executing from here
print("\n👋 Welcome to the Game where you have to guess a number between 1-10.")
print("... You Have 5 Guesses ...")
guess_numbers()

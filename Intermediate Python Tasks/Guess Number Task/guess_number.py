import random
class InvalidInputError(Exception):
    def __init__(self, message):
        # super().__init__(message)
        self.message=message

    def __str__(self):
        return f"Error: {self.message}"

# for next number guess  
def ask_again():
    ask=input("Do You Want to Guess Again(Yes/No): ")
    ask=ask.lower()
    if ask=="yes":
        guess_numbers()
    elif ask=="no":
        return
    else:
        ask_again()

def guess_numbers():
    tries=5
    Value=random.randint(1,11)
    # can run for 5 time maximum
    while tries>0:
        try:
            inputs=int(input("Guess the Number(between 1 to 10):"))

            if inputs<1 or inputs>10:
                raise InvalidInputError("Number must be in the range of 1 to 10.")
            
            # correct guess
            if inputs == Value:
                print(f"\n...Correct Guess...\n...Number is {Value}...")
                # print(f"...Your Score is(Out of 5): {tries} ...\n")
                break
            tries-=1

        except ValueError:
            print(InvalidInputError("Input Must be in Number Format."))
        except InvalidInputError as iie:
            print(iie)
    
    # score
    print(f"\n...Your Score is(Out of 5): {tries} ...\n")
    ask_again()

# program starts executing from here
guess_numbers()
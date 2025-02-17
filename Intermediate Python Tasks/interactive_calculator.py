class FormulaError(Exception):
    def __init__(self, message):
        # super().__init__(message)
        self.message=message

    def __str__(self):
        return f"Error: {self.message}"

def take_input():
    # to run program until input as "quit"
    while True:
        # take input
        inputs=input("Enter the Formula: ")

        input_to_check=inputs.lower()
        if input_to_check=="quit":
            break

        ls=inputs.split()

        try:
            # checking if length of input is 3
            if len(ls) > 3 or len(ls) < 3:
                raise FormulaError("Enter only 3 element separated by spaces.")
            
            # Converting string into float for 1st and 3rd element
            operator1=float(ls[0])
            operator2=float(ls[2])

            # checking operator
            if ls[1]=='+':
                ans=operator1+operator2
            elif ls[1]=='-':
                ans=operator1-operator2
            else:
                raise FormulaError("Operator must be + or -.")

            print(f"Answer of {ls[0]} {ls[1]} {ls[2]} is : {ans}")

        except ValueError as ve:
            print(FormulaError(f"Enter Correct Input.{ve}"))
        except FormulaError as fe:
            print(fe)

# Program starts from here
take_input()
class FormulaError(Exception):
    def __init__(self, message):
        # super().__init__(message)
        self.message=message

    def __str__(self):
        return f"\n❌ Error: {self.message}"

def take_input():
    # to run program until input as "quit"
    while True:
        # take input
        inputs=input("\n*** Formula must have two operand and one operator separated by spaces. *** \n*** Operator Must be + or - or * or / ***\n*** (For Example:1 + 1) *** \n\nEnter the Formula : ")

        input_to_check=inputs.lower()
        if input_to_check=="quit":
            break
        
        ls=[]
        symbols=['+','-','*','/']
        temp=''
        for i in inputs:
            if i in symbols:
                if temp:
                    ls.append(temp)
                    temp=''
                if not(i == ' '):
                    ls.append(i)
            else:
                temp+=i
        if temp:
            ls.append(temp)
        # ls=inputs.split()

        try:
            # checking if length of input is 3
            if len(ls) > 3 or len(ls) < 3:
                raise FormulaError("\nFormula Error: Enter only 3 element separated by spaces.")
            
            # Converting string into float for 1st and 3rd element
            operand1=float(ls[0])
            operand2=float(ls[2])

            # checking operator
            if ls[1]=='+':
                ans=operand1+operand2
            elif ls[1]=='-':
                ans=operand1-operand2
            elif ls[1]=='*':
                ans=operand1*operand2
            elif ls[1]=='/':
                ans=operand1/operand2
            else:
                raise FormulaError("\nFormula Error: Operator must be + or - or * or / .")

            print(f"\nAnswer of {operand1} {ls[1]} {operand2} is : {ans}")

        except ValueError as ve:
            print(FormulaError(f"\nFormula Error: Enter Correct Input.{ve}"))
        except FormulaError as fe:
            print(fe)

# Program starts from here
print("\n👋 Welcome. Here You can give formula and you will get output of it.")
take_input()

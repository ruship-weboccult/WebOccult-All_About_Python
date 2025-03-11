print("This program will get student data from you and give you detail about student who got more than 90 Grade.")
while True:
    try:
        input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the Number of Students.\n\nEnter Your Input:""")
        temp=input_string.lower()

        # Check to run program or not
        if temp=='exit':
            break
        else:
            n=int(input_string)

            if n<=0:
                raise Exception("\n*** Student must be more than 0 ***")

            student_dict={}
            student_above_90={}
            total=0

            for i in range(0,n):
                name=input(f"\n\nEnter the Name of Student-{i+1}:")
                grade=float(input(f"\nEnter the Grade of  {name}  (0-100):"))
                student_dict[name]=grade

                if grade>100 or grade<0:
                    raise Exception("\n*** Grade must be in range of 0-100 ***")
                elif grade>90.0:
                    total+=1
                    student_above_90[name]=grade

            print("\n***\nNumber of Students with Grade above 90:",total)
            print("\nStudents List whose grade is above 90:\n",student_above_90,"\n***")

    except Exception as e:
        print("\n\n❌ Error: ",e,"\n")

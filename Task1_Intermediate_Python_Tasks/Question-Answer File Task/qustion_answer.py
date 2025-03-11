def question_answer():
    try:
        questions = {}
        answers = {}

        # For Question File
        with open("Task1_Intermediate_Python_Tasks/Question-Answer File Task/question.txt", 'r') as question_file:
            for line in question_file:
                num, question = line.split('.', 1)
                questions[int(num.strip())] = question.strip()

        # For Answer file
        with open("Task1_Intermediate_Python_Tasks/Question-Answer File Task/answer.txt", 'r') as answer_file:
            for line in answer_file:
                num, answer = line.split('.', 1)
                answers[int(num.strip())] = answer.strip()

        # For output file
        with open("Task1_Intermediate_Python_Tasks/Question-Answer File Task/Output.txt", 'w') as output_file:
            for num in sorted(questions.keys()):
                output_file.write(f"{num}. {questions[num]}\n")
                
                # If answer is avilable for perticulat question
                if num in answers:
                    output_file.write(f"{answers[num]}\n")
                else:
                    output_file.write("Answer not found\n")

            print(f"\n✅ Process Done.")
    except FileNotFoundError as fe:
        print(f"\n❌Error: File Not Found. {fe}")
    except Exception as e:
        print(f"\n❌Error: {e}")

# Program Starts from here
print("\n*** There must present Question.txt and Answer.txt file in your present working directory. *** \n*** It will print final output that have Question with it's Answer in sorted numeric value in Output.txt file. ***")
question_answer()

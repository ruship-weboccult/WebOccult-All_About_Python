def question_answer():
    try:
        questions = {}
        answers = {}

        # For Question File
        with open("question.txt", 'r') as question_file:
            for line in question_file:
                num, question = line.split('.', 1)
                questions[int(num.strip())] = question.strip()

        # For Answer file
        with open("answer.txt", 'r') as answer_file:
            for line in answer_file:
                num, answer = line.split('.', 1)
                answers[int(num.strip())] = answer.strip()

        # For output file
        with open("Output.txt", 'w') as output_file:
            for num in sorted(questions.keys()):
                output_file.write(f"{num}. {questions[num]}\n")
                
                # If answer is avilable for perticulat question
                if num in answers:
                    output_file.write(f"{answers[num]}\n")
                else:
                    output_file.write("Answer not found\n")
        
    except FileNotFoundError as fe:
        print(f"Error: File Not Found. {fe}")
    except Exception as e:
        print(f"Error: {e}")

# Program Starts from here
question_answer()

import re
from datetime import datetime

while True:
    input_string=input("""\nFor Exit from Program enter 'exit'.\nOR \nFor Input Enter the string for which you want to extract Date and Time.\n(Input Example:2020-01-15 09:03:32.744178)\n\nEnter Your Input:""")
    temp=input_string.lower()

    # Check to run program or not
    if temp=='exit':
        break
    else:
        try:
            datetime_object = datetime.strptime(input_string, "%Y-%m-%d %H:%M:%S.%f")

            #lambda function to extract information
            extract = lambda date_time: {
                'year': date_time.year,
                'month': date_time.month,
                'day': date_time.day,
                'time': date_time.strftime("%H:%M:%S.%f")
            }

            result = extract(datetime_object)

            if result:
                print(f"\n***\nExtracted Information:\nYear: {result['year']}\nMonth: {result['month']}\nDay: {result['day']}\nTime: {result['time']}\n***")
        except Exception as e:
            print("\n\n❌Error:",e,"\n")
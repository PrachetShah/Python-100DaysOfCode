import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "testpythondays@gmail.com"
password = "Python123"

day = dt.datetime.now()
today_month = day.month
today_day = day.day
today = (today_month, today_day)


data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        # This line makes the connection secure by encrypting the message
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject:Happy Birthday!!\n\n{contents}")






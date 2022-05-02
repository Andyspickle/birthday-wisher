##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas as pd
import datetime as dt
from data.secret import USERNAME, PASSWORD

now = dt.datetime.now()
data = pd.read_csv("data/birthdays.csv")


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs=USERNAME,
            msg=f"Subject: Today's Quote! \n\n {message}.",
        )


for index, row in data.iterrows():
    if now.month == row["month"] and now.day == row["day"]:
        print(f"{row['name']} has a birthday today!")
        print(row["email"])
        with open("letter.txt", "r") as file:
            letter = file.read()
        letter = letter.replace("[NAME]", row["name"])
    else:
        print("No birthdays today.")

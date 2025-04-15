import smtplib
import datetime
import random
import pandas

EMAIL = "" #insert email here
PASSWORD = "" #insert app password here

now = datetime.datetime.now()
date = (now.month, now.day)

birthdays = pandas.read_csv("./Intermediate/Birthday_Wisher/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

if date in birthdays_dict:
  birthday_details = birthdays_dict[date]
  letter_choice = random.randint(1, 3)
  
  with open(f"./Intermediate/Birthday_Wisher/letter_templates/letter_{letter_choice}.txt") as letter:
    letter_form = letter.read()
  
  birthday_letter = letter_form.replace("[NAME]", birthday_details["name"])

  with smtplib.SMTP("smtp.server.com") as connection: #correct the SMTP server.
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
      from_addr=EMAIL, 
      to_addrs=birthday_details["email"], 
      msg=f"Subject:Happy Birthday\n\n{birthday_letter}"
      )


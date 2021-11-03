# WAP to add 2 months to the current date.

from datetime import datetime, timedelta

now = datetime.now()
date_after_2months = now + timedelta(days=60)
print("current date : ", now)
print("date after 2months(60days) : ", date_after_2months)


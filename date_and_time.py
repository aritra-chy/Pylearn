from datetime import datetime

ekhon = datetime.now()

print(ekhon.strftime("Date: %d-%B-%Y Time: %H:%M:%S"))


# timedelta (difference between two dates)

from datetime import timedelta

ekhon = datetime.now()
# dob = datetime(1998, 10, 5)

# diff = ekhon - dob

# print(type(ekhon))
# print(diff)
# print(type(diff))

print(ekhon+timedelta(days=5, minutes=5))

import json


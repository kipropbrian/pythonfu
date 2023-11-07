import re

email = 'test@harvard.edu'

if(re.search(r'^[^@]+@[^@]+\.edu$', email, re.IGNORECASE)):
    print('Email is valid')
else:
    print('Email is invalid')
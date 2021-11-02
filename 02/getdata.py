# Blog date checker
from htmldate import find_date
import arrow
from datetime import datetime

when = find_date('https://aws.amazon.com/blogs/aws/')
updated = datetime.strptime(when,'%Y-%m-%d')
hu = arrow.get(updated)

# Calculates time difference between right now and the page updated value
print("AWS Official Blog, last updated:")
print(hu.humanize())

# Check when was the page updated
print("Microsoft Azure Official Blog, last updated:")
when = find_date('https://azure.microsoft.com/en-us/blog/')
updated = datetime.strptime(when,'%Y-%m-%d')
hu = arrow.get(updated)
print(hu.humanize())
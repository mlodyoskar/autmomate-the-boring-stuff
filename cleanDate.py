import pyperclip, re


dateRegex = re.compile(r'''
    (\d{1,4})        #year or day
    (-|/|\.)            #separator
    (\d{1,2})        #day or month
    (-|/|\.)            #seperator
    (\d{1,4})        #day or year
''', re.VERBOSE)

datesImport = pyperclip.paste()
dates = dateRegex.findall(datesImport)

for date in dates:
    month = date[2]
    if len(date[0]) > 2:
        year = date[0]
        day = date[4]
    else:
        day = date[0]
        year = date[4]
    print("Day: {}, Month: {}, Year: {}".format(day,month,year))

#21 05 2020
#2020 05 29








# 2020/5/31
#31.5.2020
#31-5-2020
import datetime
import calendar

def zodiac(year):
    year_zodiac = ["ปีมะเส็ง,ปีงูเล็ก", "ปีมะเมีย,ปีม้า", "ปีมะแม,ปีแพะ", "ปีวอก,ปีลิง", "ปีระกา,ปีไก่", "ปีจอ,ปีหมา",
                "ปีกุน,ปีหมู", "ปีชวด,ปีหนู", "ปีฉลู,ปีวัว", "ปีขาล,ปีเสือ", "ปีเถาะ,ปีกระต่าย", "ปีมะโรง,ปีงูใหญ่"]
    return year_zodiac[year % 12]

date_now = datetime.datetime.now()

date_input_str = input('enter date (2544-08-16): ')
date_input_obj = datetime.datetime.strptime(date_input_str, '%Y-%m-%d')

DaysInBdayMonth = calendar.monthrange(date_input_obj.year, date_input_obj.month)[1] # 31
DaysRemain = date_now.day + (DaysInBdayMonth - date_input_obj.day) # 49

year, month, day = 0,0,0

if (date_now.month > date_input_obj.month):
    year = (date_now.year + 543) - date_input_obj.year
    month = date_now.month - (date_input_obj.month + 1) + abs(DaysRemain / DaysInBdayMonth)
    day = (DaysRemain % DaysInBdayMonth + DaysInBdayMonth) % DaysInBdayMonth
elif (date_now.month == date_input_obj.month):
    if (date_now.day >= date_input_obj.day):
        year = (date_now.year + 543) - date_input_obj.year
        month = 0
        day = date_now.day - date_input_obj.day
    else:
        year = ((date_now.year + 543) - 1) - date_input_obj.year
        month = 11
        day = calendar.monthrange(date_input_obj.year, date_input_obj.month) - (date_input_obj.day - date_now.day)
else:
    year = ((date_now.year + 543) - 1) - date_input_obj.year
    month = date_now.month + (11 - date_input_obj.month) + abs(DaysRemain / DaysInBdayMonth)
    day = (DaysRemain % DaysInBdayMonth + DaysInBdayMonth) % DaysInBdayMonth

print("อายุของคุณ {} ปี {} เดือน {} วัน".format(year, int(month), day))
print("ปีนักษัตร : " + zodiac(date_input_obj.year))
from datetime import datetime, date, time, timedelta


d1 = date(2000, 10, 12)
d2 = date(day=4, month=7, year=2002)

print(d1, d2, d2 - d1, sep='\n')


# >>> d1
# datetime.date(2000, 10, 12)
# >>> d1.year
# 2000
# >>> d1.month
# 10
# >>> d1.day
# 12
# >>>
# >>> d1.year = 2020
# ...
# AttributeError: attribute 'year' of 'datetime.date' objects is not writable
# >>>
# >>> d1.replace(year=2020)
# datetime.date(2020, 10, 12)


# >>> date_format = '%Y/%m/%d'
# >>>
# >>> d1.strftime(date_format)
# '2000/10/12'
# >>>
# >>> f'{d1:{date_format}}'
# '2000/10/12'
# >>>
# >>> f'{d1:%d.%m.%Y}'
# '12.10.2000'
# >>>
# >>> f'{d1:%d.%m.%y}'
# '12.10.00'
# >>>
# >>> f'{d1:%d %B %Y}'
# '12 October 2000'


# >>> from locale import setlocale, LC_ALL
# >>> setlocale(LC_ALL, 'ru_RU')
# 'ru_RU'


# >>> f'{d1:%d %B %Y}'
# '12 Октябрь 2000'
# >>>
# >>> f'{d2:%d %b %Y}'
# '04 июл 2002'
# >>>
# >>> f'{d2:%j}'
# '185'
# >>>
# >>> f'{d2:%W}'
# '26'


# >>> datetime.now()
# datetime.datetime(2023, 7, 15, 17, 16, 13, 540135)
# >>>
# >>> datetime.utcnow()
# datetime.datetime(2023, 7, 15, 12, 17, 0, 755937)
# >>>
# >>> datetime.now().hour - datetime.utcnow().hour
# 5

# >>> dt1 = datetime(2023, 7, 12, 20, 31)
# >>> 
# >>> dt1
# datetime.datetime(2023, 7, 12, 20, 31)
# >>>
# >>> f'{dt1:%H:%M %d.%m.%Y}'
# '20:31 12.07.2023'

# >>> datetime.strptime('12.10.2005', '%d.%m.%Y')
# datetime.datetime(2005, 10, 12, 0, 0)
# >>>
# >>> datetime.strptime('6:05 12.10.2005', '%H:%M %d.%m.%Y')
# datetime.datetime(2005, 10, 12, 6, 5)

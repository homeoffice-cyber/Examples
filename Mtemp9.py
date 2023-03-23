import datetime

x = []
y = []

date = 9
month = 9

x = [datetime.datetime(2022, month , date, 0), 38.5]

x.append(datetime.datetime(2022, month , date, 2)), x.append(37.7)
x.append(datetime.datetime(2022, month , date, 4)), x.append(37.4)
x.append(datetime.datetime(2022, month , date, 6)), x.append(37.1)
x.append(datetime.datetime(2022, month , date, 9)), x.append(38.1)
x.append(datetime.datetime(2022, month , date, 10, 35)), x.append(39.5)
x.append(datetime.datetime(2022, month , date, 11, 20)), x.append(37.8)
x.append(datetime.datetime(2022, month , date, 12)), x.append(37.3)
x.append(datetime.datetime(2022, month , date, 13)), x.append(37)
x.append(datetime.datetime(2022, month , date, 14)), x.append(36.9)
x.append(datetime.datetime(2022, month , date, 16)), x.append(37.6)
x.append(datetime.datetime(2022, month , date, 17)), x.append(37.8)
x.append(datetime.datetime(2022, month , date, 4)), x.append(37.4)


print(x[::2])
print(x[1::2])
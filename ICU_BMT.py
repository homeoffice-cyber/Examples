import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

Bun_Cre = ['2/16-04:20', 23, 1.08, '2/17-04:20', 21, 1.02, '2/18-06:00', 22, 1.03, '2/19-04:40', 15, 1.07, '2/20-04:55',
           16, 1.12, '2/21-04:40', 20, 1.16,
           '2/22-05:45', 32, 1.13, '2/23-05:15', 35, 1.28, '2/23-15:55', 38, 1.35, '2/24-06:00', 36, 1.28, '2/25-06:25',
           39, 1.33, '2/26-04:52', 43, 1.45,
           '2/27-04:59', 56, 1.7, '02/28-05:40', 82, 1.74, '2/28-14:32', 87, 1.73, '2/28-22:00', 90, 1.62, '3/1-05:45',
           90, 1.65,'3/1-13:40',91,1.54,'3/1-22:49',90,1.45,'3/2-05:50',86,1.39,'3/2-16:10',85,1.33,'3/2-23:56',80,1.38,'3/3-6:02',76,1.29,
           '3/3-14:20',76,1.43,'3/3-22:22',72,1.23,'3/4-5:30',74,1.33,'3/4-15:22',80,1.39,'3/5-5:40',72,1.34,
           '3/5-14:15',63,1.03,'3/5-22:50',72,1.35,'3/6-06:00',75,1.28,
           '3/6-14:31',85,1.45,'3/6-23:30',82,1.45,'3/7-5:50',75,1.55,'3/7-15:00',83,1.59,'3/7-22:36',79,1.68,'3/8-6:15',87,1.78,
           '3/8-13:57',96,2.1,'3/8-22:42',93,2.22,'3/9-1:36',97,2.36,'3/9-6:10',94,2.43,'3/9-14:12',96,2.41,
           '3/9-16:31',87,2.11,'3/10-0:35',85,2.14,'3/10-6:30',94,2.29,'3/10-17:39',108,2.51,'3/11-0:50',120,2.88,'3/11-5:00',102,2.57,
'3/11-14:16',79,1.61,'3/12-0:0',62,1.5,'3/12-13:15',50,1.22,'3/12-18:05',49,1.3,'3/13-0:0',50,1.47,'3/13-6:57',47,1.63,
           '3/13-12:31',48,1.66,'3/13-18:00',49,1.77,'3/14-0:0',52,1.96,'3/14-5:45',47,1.88,'3/15-5:20',49,1.88,'3/16-8:25',90,2.87,
           '3/16-13:28',104,3.23,'3/16-22:55',107,3.15,'3/17-3:10',96,2.75,'3/17-10:09',80,2.37,
           '3/17-23:05',63,1.87,'3/18-6:00',59,1.83,'3/18-14:20',53,1.66,'3/18-22:10',49,1.65,'3/19-6:10',55,1.52,
'3/19-14:10',52,1.64,'3/19-22:20',49,1.61,'3/20-6:08',54,1.44,'3/20-13:01',51,1.65,'3/20-22:12',69,2.13,'3/21-9:10',89,2.66,
'3/21-21:45',113,3.34,'3/22-5:38',118,3.31,'3/22-15:13',126,3.56,'3/22-18:20',93,2.46,'3/23-5:41',84,2.73,'3/23-18:00',97,3.19,'3/24-6:00',95,3.33,
           '3/24-18:05',45,2.28,'3/25-5:58',57,3.04,'3/25-18:15',63,3.6,'3/26-6:00',69,3.68,'3/26-18:10',36,2.45,
           '3/27-6:10',48,2.95]

cbc = ['2/16-04:20', 1.3, 82, '2/17-04:20',1.6, 64 , '2/18-06:00', 1.4, 52, '2/19-04:40', 0.7, 36, '2/20-04:55',0.2, 28
           , '2/21-04:40', 0.1,10,
           '2/22-05:45', 0, 4, '2/23-05:15', 0, 5, '2/23-17:55', 0, 7, '2/24-06:00',0, 4 , '2/25-06:25',0, 4
           , '2/26-04:52',0.1,  12,
           '2/27-04:59', 0,3, '02/28-10:23', 0,3, '2/28-22:00', 0,3, '3/1-10:30',0,3,
           '3/1-22:49',0,6,'3/2-05:50',0.1,6,'3/2-16:10',0.1, 8,'3/3-6:02',0, 6,
           '3/3-17:55',0,8,'3/4-5:30',0.1,9,'3/4-18:07',0.1, 8,'3/5-5:40',0, 13,'3/5-17:20',0,19,'3/6-6:00',0,16,
       '3/6-18:25',0,23,'3/7-5:50',0.2,11,'3/7-18:00',0,7,'3/8-6:15',0,5,'3/8-19:00',0.2,17,'3/9-6:10',0.1,7,'3/9-18:49',0.1,10,
       '3/10-6:30',0.1,11,'3/10-17:39',0.2,32,'3/11-5:00',0.3,21,'3/11-14:16',0.5,27,'3/12-0:0',0.2,14,'3/12-5:33',.2,19,'3/12-9:33',.2,21,
       '3/12-21:03',0.1,14,'3/13-6:57',0.2,22,'3/13-18:00',0.2,18,'3/14-5:45',.2,21,'3/14-17:40',.2,16,
       '3/15-5:20',.2,15,'3/15-18:23',.2,8,'3/16-4:45',.3,8,'3/16-12:20',.3,7,'3/16-22:01',.3,6,'3/17-10:09',.3,14,
       '3/17-20:45',0.3,17,'3/18-6:00',0.4,15,'3/18-18:10',0.2,8,'3/19-6:10',0.2,11,'3/19-18:05',0.3,7,'3/20-6:08',0.2,12,'3/20-22:12',0.4,17,'3/21-9:10',0.4,24,'3/21-21:45',0.4,33,'3/22-5:38',0.5,27,
       '3/22-18:20',.5,9,'3/23-5:41',.4,18,'3/23-18:00',.6,12,'3/24-6:00',.6,9,'3/24-18:05',.7,8,
       '3/25-5:58',1,13,'3/25-18:15',1.3,7,'3/26-6:00',1.4,12,'3/26-12:45',1.4,7,'3/26-18:10',1.4,5,'3/27-2:30',1.3,8,
       '3/27-6:10',1.3,6]

neu = ['2/16-4:20',83,1.1,'2/17-4:20',89,1.4,'2/18-6:00',90,1.2,'2/19-4:40',94,.7,'3/11-5:00',60,.2,'3/11-2:16',88,.4,'3/16-4:45',7,0,'3/16-12:20',7,0,'3/17-10:09',7,0,'3/18-6:00',11,0,'3/19-6:05',22,.1,
       '3/20-10:12',31,.1,'3/21-9:10',60,.2,'3/21-21:45',58,.2,'3/22-5:38',42,.2,'3/22-18:20',44,.2,'3/23-5:41',52,.2,'3/23-18:00',65,.4,'3/24-6:00',64,.4,'3/24-18:05',64,.4,
       '3/25-5:58',66,.7,'3/25-18:15',53,.7,'3/26-6:00',53,.7,'3/26-18:10',64,.9,'3/27-2:30',50,.7,'3/27-6:10',57,.7]

dialysis = ['03/16 21:45','03/19 16:00','03/22 17:15','03/22 19:30','03/24 09:07','03/24 12:17','03/26 09:42','03/26 12:15']

platelets = ['3/20 01:00','3/20 13:00','3/20 21:00','3/21 02:00','3/21 07:00','3/21 17:00','3/22 23:00',
             '3/23 02:00','3/23 11:00','3/24 11:00','3/24 12:30','3/24 23:30','3/25 01:00','3/25 22:45',
             '3/26 00:45','3/26 15:10','3/26 22:30','3/27 00:00','3/27 06:55','3/27 11:43']

dt = []
bun = []
cre = []

for i in range(0, len(Bun_Cre), 3):
    date = datetime.datetime.strptime(Bun_Cre[i], "%m/%d-%H:%M")
    date = date.replace(2023)
    dt.append(date)
    bun.append(Bun_Cre[i + 1])
    cre.append(Bun_Cre[i + 2])

dt_n = []
neu_n = []
neu_a = []

for i in range(0, len(neu), 3):
    date = datetime.datetime.strptime(neu[i], "%m/%d-%H:%M")
    date = date.replace(2023)
    dt_n.append(date)
    neu_n.append(neu[i + 1])
    neu_a.append(neu[i + 2]*1000)


fig, ax = plt.subplots()
# make a plot
ax.plot(dt, bun, color="red", marker="o")
plt.axhline(25, color='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.xticks(rotation=45)

date_max = datetime.datetime.now()
date_max += datetime.timedelta(days=1)
lims = (np.datetime64('2023-03-15'), np.datetime64(date_max))
ax.set_xlim(lims)

for idx, i in enumerate(dialysis):
    date = datetime.datetime.strptime(i, "%m/%d %H:%M")
    date = date.replace(2023)
    if idx % 2 == 0:
        color = 'red'
    else:
        color = 'green'
    plt.axvline(np.datetime64(date), color=color)


plt.grid(True)
# set y-axis label
ax.set_ylabel('BUN [mg/dL]', color="red", fontsize=14)
# twin object for two different y-axis on the sample plot
ax2 = ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(dt, cre, color="blue", marker="o")
plt.axhline(1.1, color='blue')
ax2.set_ylabel('Creatinine [mg/dL]', color="blue", fontsize=14)
plt.tight_layout()
plt.show()




dt = []
pl = []
wb = []

for i in range(0, len(cbc), 3):
    date = datetime.datetime.strptime(cbc[i], "%m/%d-%H:%M")
    date = date.replace(2023)
    dt.append(date)
    wb.append(cbc[i + 1])
    pl.append(cbc[i + 2])


fig, ax = plt.subplots()
plt.plot(dt,pl,color="red", marker="o" )
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.ylabel('Platelets [k/cumm]', color="red", fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.axhline(130, color='red')

ax2 = ax.twinx()
ax2.plot(dt, wb, color="blue", marker="o")
plt.axhline(4.1, color='blue')
ax2.set_ylabel('WBC [k/cumm]', color="blue", fontsize=14)
plt.tight_layout()
plt.show()



fig, ax = plt.subplots()
plt.plot(dt_n,neu_a,color="red", marker="o" )
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.ylabel('Neutrophil Count [/cumm]', color="red", fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.axhline(1.58*1000, color='red')

ax2 = ax.twinx()
ax2.plot(dt, wb, color="blue", marker="o")
plt.axhline(4.1, color='blue')
ax2.set_ylabel('WBC [k/cumm]', color="blue", fontsize=14)

plt.tight_layout()
plt.show()


timedeltas = [dt[i] - dt[i-1] for i in range(1, len(dt))]
dateTimeDifferenceInHours = [timedeltas[i].total_seconds() / 3600 for i in range(len(timedeltas))]
dpl = [pl[i] - pl[i-1] for i in range(1, len(pl))]
grad = [dpl[i]/dateTimeDifferenceInHours[i] for i in range(len(dateTimeDifferenceInHours))]


fig, ax = plt.subplots()
plt.plot(dt,pl,color="red", marker="o" )
for idx, val in enumerate(grad):
    if idx >= 57:
        plt.text(dt[idx+1],1.1*pl[idx+1],"{:.2f}".format(val))

ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.ylabel('Platelets [k/cumm]', color="red", fontsize=14)
plt.xticks(rotation=45)
lims = (np.datetime64('2023-03-21'), np.datetime64(date_max))
ax.set_xlim(lims)
ax.set_ylim((0,40))
plt.grid(True)

for idx, i in enumerate(dialysis):
    date = datetime.datetime.strptime(i, "%m/%d %H:%M")
    date = date.replace(2023)
    if idx % 2 == 0:
        color = 'red'
    else:
        color = 'green'
    plt.axvline(np.datetime64(date), color=color)

for i in platelets:
    date = datetime.datetime.strptime(i, "%m/%d %H:%M")
    date = date.replace(2023)
    plt.axvline(date, color='blue')

plt.tight_layout()
plt.show()


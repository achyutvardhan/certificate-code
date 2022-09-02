import pandas as pd
from cert import certi
# df = pd.read_excel(r'C:\Users\KIIT\Desktop\certificates\final.xlsx', sheet_name=3)
# names = df['name']

df = pd.read_excel(r'C:\Users\KIIT\Desktop\certificates\final.xlsx', sheet_name=5)
names = []


# print(names)

for i in df['nameleader']:
    names.append(i)
for i in df['member2name']:
    names.append(i)
for i in df['member3name']:
    names.append(i)
for i in df['member4name']:
    names.append(i)
for i in df['member5name']:
    names.append(i)

while ' ' in names:
    names.remove(' ')

for i in range(len(names)):
    names[i] = names[i].title()


# print(len(names))
print(*names,sep='\n')
for i in names:
    certi(i)


'''
from collections import OrderedDict

s = OrderedDict()
num = ['0','1','2','3','4','5','6','7','8','9','.']

with open('EQ_guide.txt') as f:
    for i in range (4):
        line = f.readline()
    

    line = f.readline()
    
    while line != '':

        ind1 = line.index('g')-2
        cad = ''
        while line[ind1] in num:
            cad += line[ind1]
            ind1 -= 1
        m1 = cad[::-1]
        m1 = float(m1)
        ind2 = -4
        cad = ''    
        while line[ind2] in num:
            cad += line[ind2]
            ind2 -= 1
        m2 = float(cad[::-1])
        maxi = round(max(m1,m2),1)

        if maxi not in s.keys():
            s[maxi] = [line[0:4]]
        else:
            s[maxi].append(line[0:4])
        
        line = f.readline()

lista  = []
for i in s.keys():
    lista.append(i)

lista.sort()

D = OrderedDict()

for i in lista:
    D[i] = s[i]

print(D)

with open('EQ_Bins.txt', 'w') as w:
    w.write('Bins (peak acceleration in g, samples): \n')
    for i in D:
        w.write('   '+str(i) + ' = ' + str(D[i])+ '\n')
    w.write('m = '+str(len(D))+'\n')
    w.write('r = ' + str(D.keys())[11:-1:]+'\n')
    lista = []
    for i in D.values():
        lista.append(len(i))
    w.write('n = ' + str(lista)+'\n')
'''    

import csv
count = {0.1: 0, 
         0.2: 0,
         0.3: 0,
         0.4: 0,
         0.5: 0,
         0.6: 0,
         0.7: 0,
         0.8: 0,
         0.9: 0,
         1.0: 0,
         1.1: 0,
         1.2: 0,
         1.3:0}

with open('query.csv', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if float(row['mag']) < 3:
            count[0.1] = count[0.1]+1
        elif float(row['mag']) < 3.3:
            count[0.2] = count[0.2]+1
        elif float(row['mag']) < 3.6:
            count[0.3] = count[0.3]+1
        elif float(row['mag']) < 3.9:
            count[0.4] = count[0.4]+1
        elif float(row['mag']) < 4.2:
            count[0.5] = count[0.5]+1
        elif float(row['mag']) < 4.5:
            count[0.6] = count[0.6]+1
        elif float(row['mag']) < 4.8:
            count[0.7] = count[0.7]+1
        elif float(row['mag']) < 5.1:
            count[0.8] = count[0.8]+1
        elif float(row['mag']) < 5.4:
            count[0.9] = count[0.9]+1
        elif float(row['mag']) < 5.7:
            count[1.0] = count[1.0]+1
        elif float(row['mag']) < 6.0:
            count[1.1] = count[1.1]+1
        elif float(row['mag']) < 6.3:
            count[1.2] = count[1.2]+1
        else:
            count[1.3] = count[1.3]+1

for key in count.keys():
    count[key] = count[key]/(102)

count[1] = 0.03
count[1.2] = 0.01

print (count)

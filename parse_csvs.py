import csv, json
from collections import OrderedDict


def go_through_data(c,info,counties):
    for row in c:
        if row['STNAME'] not in info:
            info[row['STNAME']] = {}
            counties[row['STNAME']] = {}
        n = row['CTYNAME'].decode('latin-1')
        if n not in info[row['STNAME']]:
            #print info
            #print row['CTYNAME']
            #print n
            counties[row['STNAME']][n] = ''
            info[row['STNAME']][n] = []
        new_person = {}
        new_person['sex'] = row['SEX']
        new_person['his'] = row['ORIGIN']
        new_person['age'] = row['AGEGRP']
        new_person['race'] = row['IMPRACE']
        #new_person['res_pop'] = row['RESPOP']
        info[row['STNAME']][n].append(new_person)

f1 = open('stco-mr2010_al_mo.csv','r')
f2 = open('stco-mr2010_mt_wy.csv','r')

info = OrderedDict()
counties = OrderedDict()
c1 = csv.DictReader(f1)
c2 = csv.DictReader(f2)

go_through_data(c1,info,counties)
go_through_data(c2,info,counties)


with open('demographics.json','w') as dt:
    json.dump(info,dt)

with open('counties.json','w') as dt:
    json.dump(counties,dt)





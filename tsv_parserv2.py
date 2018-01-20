import csv


def parse():

    f = open('candidates.csv','r')
    r = csv.DictReader(f, delimiter='\t')

    data = {}
    viewed_ids = {}
    
    for row in r:
        if row['v05'] == '2010':
            state = row['v01']
            if state not in data:
                data[state] = {}
            d_no = int(row['v09'])
            if d_no not in data[state]:
                data[state][d_no] = {'D':0,'R':0,'I':0}
            candidate_id = int(row['v18'])
            if candidate_id not in viewed_ids:
                viewed_ids[candidate_id] = ''
            else:
                print 'already found'


    f.close()



parse()

    
'''
caseid

multiply by population for each rep

v01 - state num alphabet
v02 - state abbr
v05 - year of election
v06 - month of election
v07 - senate or house
v08 - district name
v09 - district number
v18 - candidate code
v20 - detailed party code
v21 - simplified party code - 100 dem 200 rep     anything else is independent

look through list
if year = 2010
if id not in checked ids

data[state][district no][party] += 1


Final Product should be:

State: {District: {D:, R:, I}


'''

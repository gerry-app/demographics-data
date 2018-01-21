import csv, json


def parse():

    f = open('candidates.csv','r')
    r = csv.DictReader(f, delimiter='\t')

    data = {}
    viewed_ids = {}
    
    for row in r:
        if row['v05'] == '2010' and row['v01'] != ' ' and row['v09'] != ' ' and row['v36'] != ' ' and row['v29'] != ' ':
            state = row['v02']
            d_no = int(row['v09'])
            if state not in data:
                data[state] = {}
            if d_no not in data[state]:
                data[state][d_no] = {'D':0,'R':0,'I':0}
            candidate_id = int(row['v18'])
            if candidate_id not in viewed_ids:
                party = int(row['v21'])
                if party == 100:
                    data[state][d_no]['D'] += int(int(row['v29'])*float(row['v36'])/100.0)
                elif party == 200:
                    data[state][d_no]['R'] += int(int(row['v29'])*float(row['v36'])/100.0)
                else:
                    data[state][d_no]['I'] += int(int(row['v29'])*float(row['v36'])/100.0)
                viewed_ids[candidate_id] = ''
                
            if '0' not in data[state]:
                data[state]['0'] = {'D':0,'R':0,'I':0}

    f.close()

    with open('output.json','w') as dt:
        json.dump(data,dt)

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
v29 - total votes
v30 - votes for demo
v31 - votes for repub
v32 - votes for other
v36 - votes percent received

look for percentage of voters


look through list
if year = 2010
if id not in checked ids

data[state][district no][party] += 1


Final Product should be:

State: {District: {D:, R:, I}


'''

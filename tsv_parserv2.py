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

    with open('party_counts.json','w') as dt:
        json.dump(data,dt)

parse()

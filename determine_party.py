import json


def determine_party(person):
    black_african = {2:'',10:'',11:'',12:'',16:'',17:'',18:'',22:'',23:'',24:'',26:'',27:'',28:'',30:'',31:''}
    indian_alaska_native = {13:'',14:'',16:'',19:'',20:'',22:'',23:'',25:'',26:'',27:'',29:'',30:'',31:''}
    pacific_non_black = {5:'',9:'',14:'',18:'',20:'',21:'',25:''}
    asian = {4:'',8:'',11:'',13:'',15:'',17:'',19:'',21:'',22:'',24:'',25:'',26:'',28:'',29:'',30:''}
    
    age = int(person['age'])
    race = int(person['race'])
    sex = int(person['sex'])
    if age <= 4:
        return None
    elif race in indian_alaska_native and age >= 14:
        return 'R'
    elif race in indian_alaska_native or race in black_african:
        return 'D'
    elif race == 1 and sex == 1:
        return 'R'
    elif race == 8 and age >= 14:
        return 'R'
    elif race in pacific_non_black:
        return 'R'
    elif race in asian and age <= 16:
        return 'D'
    
    else:
        return 'R'
    

def do():
    with open('demographics.json') as dt:
        demographics = json.load(dt)
        
    with open('districts_counties.json') as dt:
        districts = json.load(dt)

    party_counts = {}
    count = 0
    d_count = 0
    
    for state in districts:
        party_counts[state] = {}
        for d in districts[state]:
            count += 1
            party_counts[state][int(d)] = {'D':0,'R':0}
            for c in districts[state][d]:
                for person in demographics[state][c]:
                    party = determine_party(person)
                    if party != None:
                        party_counts[state][int(d)][party] += 1
            if party_counts[state][int(d)]['D'] > party_counts[state][int(d)]['R']:
                #print state, d
                d_count += 1
    print d_count, count

    with open('party_counts.json','w') as dt:
        json.dump(party_counts,dt)
    
do()

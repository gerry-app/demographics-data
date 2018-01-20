import json

with open('counties.json') as dt:
    counties_dict = json.load(dt)


cities = ['Baltimore city', 'Fredericksburg city', 'Newport News city', 'Poquoson city', 'Carson City']
    
for state in counties_dict:

    if state != 'Wyoming' and state != 'Montana' and state != 'Vermont' and state != 'Alaska' and state != 'North Dakota' and state != 'South Dakota' and state != 'District of Columbia' and state != 'Rhode Island':

    
        f = open('Districts/%s.txt' % (state.replace(' ','_')),'rU')

        sections = f.read().split('Congressional District')[1:]
        print state
    
        for section in sections:
            counties = section.split('\n')
            district = int(counties[0])
            counties = counties[2:]
            for c in counties:
            
                print c, state
                c_name = (c.split(' (')[0]).decode('latin-1')
                if state == 'Louisiana':
                    c_name += ' Parish'
                elif c_name not in cities and 'city' not in c_name:
                    c_name += ' County'


                
                if state == 'Louisiana' and c_name == 'Jefferson County':
                    c_name = 'Jefferson Davis Parish'
            
                if c != '':
                    if type(counties_dict[state][c_name]) != list:
                        counties_dict[state][c_name] = []
                    counties_dict[state][c_name].append(int(district))
    else:
        for c in counties_dict[state]:
            counties_dict[state][c] = 1
                    
with open('counties.json','w') as dt:
    json.dump(counties_dict,dt)
    

# Alaska and Delware and Wyoming and Montana are at-large
# Vermont has 1

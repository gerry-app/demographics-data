import json

with open('counties.json') as dt:
    all_counties = json.load(dt)

new_counties = {}

for state in all_counties:
    new_counties[state] = {}
    for c in all_counties[state]:
        if type(all_counties[state][c]) == list:
            for d in all_counties[state][c]:
                if d not in new_counties[state]:
                    new_counties[state][d] = []
                new_counties[state][d].append(c)
        else:
            if 1 not in new_counties[state]:
                new_counties[state][1] = []
            new_counties[state][1].append(c)
        
with open('districts_counties.json','w') as dt:
    json.dump(new_counties,dt)
        

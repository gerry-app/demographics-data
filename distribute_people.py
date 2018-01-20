import json, random

abbreviations = {'Mississippi': 'MS', 'Oklahoma': 'OK', 'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR', 'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV', 'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI', 'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD', 'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA', 'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX', 'Nevada': 'NV', 'Maine': 'ME'}

full = {'WA': 'Washington', 'DE': 'Delaware', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'HI': 'Hawaii', 'FL': 'Florida', 'WY': 'Wyoming', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'TX': 'Texas', 'LA': 'Louisiana', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'TN': 'Tennessee', 'NY': 'New York', 'PA': 'Pennsylvania', 'AK': 'Alaska', 'NV': 'Nevada', 'VA': 'Virginia', 'CO': 'Colorado', 'CA': 'California', 'AL': 'Alabama', 'AR': 'Arkansas', 'VT': 'Vermont', 'IL': 'Illinois', 'GA': 'Georgia', 'IN': 'Indiana', 'IA': 'Iowa', 'MA': 'Massachusetts', 'AZ': 'Arizona', 'ID': 'Idaho', 'CT': 'Connecticut', 'ME': 'Maine', 'MD': 'Maryland', 'OK': 'Oklahoma', 'OH': 'Ohio', 'UT': 'Utah', 'MO': 'Missouri', 'MN': 'Minnesota', 'MI': 'Michigan', 'RI': 'Rhode Island', 'KS': 'Kansas', 'MT': 'Montana', 'MS': 'Mississippi', 'SC': 'South Carolina', 'KY': 'Kentucky', 'OR': 'Oregon', 'SD': 'South Dakota'}



def fill_in_cell(districts,counts,val,spaces,state_info,y,x):
    d = val.split('-')[1]
    people = districts[d]

    if counts[val] < spaces[val]:
        total = people['R'] + people['D']
        num_to_choose = total/spaces[val]
        d_choose = random.randrange(total%spaces[val],num_to_choose+1)
        r_choose = num_to_choose-d_choose
    else:
        d_choose = people['D']
        r_choose = people['R']
        
    #print val,people['D'],people['R']
    #print num_to_choose,d_choose, r_choose

        
    num_subtracted = 0
    data = {'D':0,'R':0,'dis':val}
    
    num_subtracted += min(d_choose,people['D'])
    data['D'] += min(d_choose,people['D'])
    people['D'] -= min(d_choose,people['D'])
    num_subtracted += min(r_choose,people['R'])
    data['R'] += min(r_choose,people['R'])
    people['R'] -= min(r_choose,people['R'])

    #print num_subtracted, num_to_choose
    #print people['D'],people['R']
    
    if counts[val] < spaces[val] and num_subtracted != num_to_choose:
        if people['D'] == 0:
            num_subtracted += min(num_to_choose-num_subtracted,people['R'])
            data['R'] += min(num_to_choose-num_subtracted,people['R'])
            people['R'] -= min(num_to_choose-num_subtracted,people['R'])
        else:
            num_subtracted += min(num_to_choose-num_subtracted,people['D'])
            data['D'] += min(num_to_choose-num_subtracted,people['D'])
            people['D'] -= min(num_to_choose-num_subtracted,people['D'])

    state_info[y][x] = data
    counts[val] += 1
    



#state is abbrev
# convert between stateabrev-num and num
def get_state_people(state,state_array):

    dem = 0
    rep = 0
    
    with open('party_counts.json') as dt:
        districts = json.load(dt)[state]
    
    spaces = {state+'-'+str(d):0 for d in districts}
    counts = {state+'-'+str(d):1 for d in districts}
    state_info = [[None for x in xrange(len(state_array[y]))] for y in xrange(len(state_array))]
    for row in state_array:
        for d in spaces:
            spaces[d] += row.count(d)
    
    for y in xrange(len(state_array)):
        for x in xrange(len(state_array[x])):
            val = state_array[y][x]
            if val != '0':
                fill_in_cell(districts,counts,val,spaces,state_info,y,x)
                #if state_info[y][x]['dis'] == 'NY-1':
                #    dem += state_info[y][x]['D']
                #    rep += state_info[y][x]['R']

    #print dem, rep
    return state_info

            



a = [
    ['NY-1', 'NY-1', 'NY-1', 'NY-3', 'NY-3'],
    ['NY-1', 'NY-1', 'NY-1', 'NY-2', 'NY-3'],
    ['NY-1', 'NY-2', 'NY-2', 'NY-2', 'NY-3'],
    ['NY-1', 'NY-1', 'NY-2', 'NY-3', 'NY-3'],
    ['0', 'NY-1', '0', '0', '0']
]

#ny1 r: 403 d: 542
#38 28 68 458


print get_state_people('NY',a)

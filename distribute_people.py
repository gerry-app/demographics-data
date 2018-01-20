import json, random

def fill_in_cell(districts,counts,val,spaces,state_info,y,x):
    d = val.split('-')[1]
    people = districts[d]

    if counts[val] < spaces[val]:
        total = people['R'] + people['D']
        num_to_choose = total/spaces[val]
        d_choose = random.randrange(0,num_to_choose+1)
        r_choose = num_to_choose-d_choose
    else:
        d_choose = people['D']
        r_choose = people['R']
        
    num_subtracted = 0
    data = {'D':0,'R':0,'dis':val}
    
    num_subtracted += min(d_choose,people['D'])
    data['D'] += min(d_choose,people['D'])
    people['D'] -= min(d_choose,people['D'])
    num_subtracted += min(r_choose,people['R'])
    data['R'] += min(r_choose,people['R'])
    people['R'] -= min(r_choose,people['R'])

    
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

    with open('party_counts.json') as dt:
        districts = json.load(dt)[state]
    
    spaces = {state+'-'+str(d):0 for d in districts}
    counts = {state+'-'+str(d):1 for d in districts}
    state_info = [[None for x in xrange(len(state_array[y]))] for y in xrange(len(state_array))]
    for row in state_array:
        for d in spaces:
            spaces[d] += row.count(d)
    
    for y in xrange(len(state_array)):
        for x in xrange(len(state_array[y])):
            val = state_array[y][x]
            if val != 0:
                fill_in_cell(districts,counts,val,spaces,state_info,y,x)

    return state_info

            



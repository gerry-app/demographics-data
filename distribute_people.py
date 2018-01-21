import json, random

# state is abbrev
# convert between stateabrev-num and num
# states with only one rep (XX-0): WY, VT, SD, AK, DE, ND, MT

def get_state_people(state,state_array):

    with open('districts.json') as cds:
        districts = json.load(cds)
        districts = {a: districts[a] for a in districts.keys() if a[:2] == state}

    spaces = {d:0 for d in districts}
#    counts = {state+'-'+str(d):1 for d in districts}
    state_info = [[None for x in xrange(len(state_array[y]))] for y in xrange(len(state_array))]
    for row in state_array:
        for d in spaces:
            spaces[d] += row.count(d)

    for y in xrange(len(state_array)):
        for x in xrange(len(state_array[y])):
            val = state_array[y][x]
            if val != 0:
                inform_cell(districts,val,spaces,state_info,y,x)

    return state_info

def inform_cell(districts, val, spaces, state_info, y, x):
    state_info[y][x] = {
        'D': districts[val]['D'] / spaces[val],
        'R': districts[val]['R'] / spaces[val],
        'I': districts[val]['I'] / spaces[val],
        'row': y,
        'col': x,
        'dis': val
    }

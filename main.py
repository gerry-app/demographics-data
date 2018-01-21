import ast
import distribute_people as d

with open('states.json') as f:
    states = ast.literal_eval(f.read())
    print len(states)
    states_with_info = {}
    for key, value in states.items():
        print key
        states_with_info[key] = d.get_state_people(key, states[key])
    with open('informed_states.json', 'w') as g:
        json.dump(states_with_info, g)

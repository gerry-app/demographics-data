import ast, json
import distribute_people as d

with open('states.json') as f:
    states = ast.literal_eval(f.read())
    states_with_info = {}
    for key, value in states.items():
        print key
        states_with_info[key] = d.get_state_people(key, states[key])
    with open('huge_ass.json', 'w') as g:
        json.dump(states_with_info, g)


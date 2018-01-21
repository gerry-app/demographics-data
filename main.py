import ast, json
import distribute_people as d

with open('states.json') as f:
    states = ast.literal_eval(f.read())
    states_with_info = {}
    for key, value in states.items():
        states_with_info[key] = d.get_state_people(key, states[key])
    with open('hi.json', 'w') as g:
        g.write(str(states_with_info["NY"]).replace("None", "null"))
#        json.dump(states_with_info, g)

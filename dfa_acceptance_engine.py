from sys import argv
f = open(argv[1], "r")
cuv=argv[2]
letters = []
states = []
transitions = []
# se face inainte validarea cu dfa_parser_engine.py
for s in f:
    # print(s)
    if s[0] == "#":
        pass
    elif s == "Sigma:\n":
        for letter in f:
            if letter[0]=="#":
                pass
            else:
                if letter == "End\n":
                    break
                letter.strip()
                letters.append(letter[0])
    elif s == "States:\n":
        for line in f:
            if line[0]=="#":
                pass
            else:
                if line == "End\n":
                    break
                state = [x for x in line.strip().split(",")]
                if len(state[len(state)-1])>1:
                    state[len(state) - 1]=state[len(state)-1][0]
                if len(state) == 2:
                    if state[1] == 'S':
                        s_curent = state[0]
                if len(state) == 3:
                    if state[1] == 'S' or state[2] == 'S':
                        s_curent = state[0]
                states.append(state)
    elif s == "Transitions:\n":
        for line in f:
            if line[0] == "#":
                pass
            else:
                if line == "End":
                    break
                transition = [x for x in line.strip().split(",")]
                if len(transition[len(transition) - 1]) > 1:
                    transition[len(transition) - 1] = transition[len(transition) - 1][0:2]
                transitions.append(transition)
f.close()
"""
print(letters)
print(states)
print(transitions)
"""
def cheie(v):
    return v[0], v[1]
transitions.sort(key=cheie)
#print(s_curent)

ok = 0
for letter in cuv:
    #print(letter)
    c = 0
    for i in range(len(transitions)):
        if transitions[i][0] == s_curent and transitions[i][1] == letter:
            s_curent = transitions[i][2]
            # print(s_curent)
            c = 1
            break
    if c == 0:
        ok = 2
        break
if ok == 2:
    print("neacceptat")
    exit()
for state in states:
    if state[0] == s_curent:
        if len(state) == 2:
            if state[1] == 'F':
                print("acceptat")
                ok = 1
        if len(state) == 3:
            if state[1] == 'F' or state[2] == 'F':
                print("acceptat")
                ok = 1
if ok == 0:
    print("neacceptat")
import copy

def ProgrammAlarm(code_list_ori, noun, verb):
    code_list = copy.deepcopy(code_list_ori)
    code_list[1] = noun
    code_list[2] = verb
    idx = 0
    while code_list[idx] != 99:
        op = code_list[idx]
        val1 = code_list[code_list[idx+1]]
        val2 = code_list[code_list[idx+2]]
        out_pos = code_list[idx+3]
        if op == 1:
            code_list[out_pos] = val1 + val2
        elif op == 2:
            code_list[out_pos] = val1 * val2
        idx += 4
    return code_list[0]

def solve(code_list, target):
    for noun in range(100):
        for verb in range(100):
            val = ProgrammAlarm(code_list, noun, verb)
            if val == target:
                answer = noun * 100 + verb
                return answer

if __name__ == "__main__":
    with open("input",'r') as f:
        codes = f.read()
    codes = codes.split(',')
    code_list = list(map(int, codes))
    answer = ProgrammAlarm(code_list, 12, 2)
    print(f"Part1 anser: {answer}")
    answer = solve(code_list, 19690720)
    print(f"Part2 anser: {answer}")

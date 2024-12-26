parent = []
value = []
N = 51
M = 51


def solution(commands):
    global parent
    global value
    answer = []
    parent = [[[j, i] for i in range(M)] for j in range(N)]
    value = [['EMPTY' for _ in range(M)] for _ in range(N)]
    for command in commands:
        com = command.split()
        if com[0] == "UPDATE":
            if len(com) == 4:
                r, c = map(int, com[1:3])
                v = com[3]
                pr, pc = get_parent(r, c)
                value[pr][pc] = v
            else:
                v1, v2 = com[1:]
                for ri in range(1, 51):
                    for ci in range(1, 51):
                        if value[ri][ci] == v1:
                            value[ri][ci] = v2
        elif com[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, com[1:])
            union_parent(r1, c1, r2, c2)
        elif com[0] == 'UNMERGE':
            r, c = map(int, com[1:])
            disunion_parent(r, c)
        elif com[0] == 'PRINT':
            r, c = map(int, com[1:])
            pr, pc = get_parent(r, c)
            answer.append(value[pr][pc])
    return answer


def get_parent(r, c):
    global parent
    if parent[r][c] != [r, c]:
        parent[r][c] = get_parent(*parent[r][c])
    return parent[r][c]


def union_parent(r1, c1, r2, c2):
    global parent, value
    p1 = get_parent(r1, c1)
    p2 = get_parent(r2, c2)
    if value[p1[0]][p1[1]] == 'EMPTY':
        parent[p1[0]][p1[1]] = p2
    else:
        parent[p2[0]][p2[1]] = p1


def disunion_parent(r, c):
    global parent, value
    p = get_parent(r, c)
    temp = value[p[0]][p[1]]

    for ri in range(1, 51):
        for ci in range(1, 51):
            get_parent(ri, ci)

    for ri in range(1, 51):
        for ci in range(1, 51):
            pi = get_parent(ri, ci)
            if p == pi:
                parent[ri][ci] = [ri, ci]
                value[ri][ci] = 'EMPTY'
    value[r][c] = temp


command1 = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice",
            "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta",
            "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik",
            "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
command2 = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1",
            "MERGE 2 1 1 1",
            "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
print(solution(command1))
print(solution(command2))

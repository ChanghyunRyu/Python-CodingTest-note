code_dict = {
    "ADD": "00000",
    "ADDC": "00001",
    "SUB": "00010",
    "SUBC": "00011",
    "MOV": "00100",
    "MOVC": "00101",
    "AND": "00110",
    "ANDC": "00111",
    "OR": "01000",
    "ORC": "01001",
    "NOT": "01010",
    "MULT": "01100",
    "MULTC": "01101",
    "LSFTL": "01110",
    "LSFTLC": "01111",
    "LSFTR": "10000",
    "LSFTRC": "10001",
    "ASFTR": "10010",
    "ASFTRC": "10011",
    "RL": "10100",
    "RLC": "10101",
    "RR": "10110",
    "RRC": "10111"
}


def num_to_binary(num, length):
    result = []
    while num >= 2:
        num, remain = divmod(num, 2)
        result.append(str(remain))
    else:
        result.append(str(num))
    for _ in range(length-len(result)):
        result.append("0")
    return ''.join(result[::-1])


t = int(input())
for _ in range(t):
    answer = []
    command = input().split()
    answer.append(code_dict[command[0]])
    answer.append('0')
    answer.append(num_to_binary(int(command[1]), 3))
    answer.append(num_to_binary(int(command[2]), 3))
    if command[0][-1] == 'C':
        imm = num_to_binary(int(command[3]), 4)
        answer.append(imm)
    else:
        imm = num_to_binary(int(command[3]), 3)
        answer.append(imm)
        answer.append('0')

    print(''.join(answer))

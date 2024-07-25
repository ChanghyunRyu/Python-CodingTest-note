import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = delete_not_characters(new_id)
    new_id = delete_double_dot(new_id)
    new_id = delete_start_end_dot(new_id)
    if new_id == '':
        new_id = 'a'
    new_id = slice_id(new_id)
    new_id = add_letters(new_id)
    return new_id


def delete_not_characters(string):
    string = re.sub('[^0-9a-z\-\.\_]', '', string)
    return string


def delete_double_dot(string):
    string = re.sub('\.\.+', '.', string)
    return string


def delete_start_end_dot(string):
    if string[0] == '.':
        string = string[1:]
    if string != '' and string[len(string)-1] == '.':
        string = string[:-1]
    return string


def slice_id(string):
    if len(string) >= 16:
        string = string[:15]
    if string[len(string)-1] == '.':
        string = string[:-1]
    return string


def add_letters(string):
    last_letter = string [-1]
    while len(string) < 3:
        string = string + last_letter
    return string


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution('=.='))
print(solution("123_.def"))
print(solution(	"abcdefghijklmn.p"))

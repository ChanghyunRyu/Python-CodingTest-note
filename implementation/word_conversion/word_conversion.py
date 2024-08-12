def solution(begin, target, words):
    answer = 0
    dp = {}
    count = 0
    dp[0] = {begin}
    all_word = {begin}
    before_word_len = len(begin)

    while True:
        word_list = dp[count]
        new_set = set()
        for word in word_list:
            conversion_word(word, words, new_set)
        count += 1
        dp[count] = new_set
        if target in dp[count]:
            answer = count
            break
        all_word = all_word.union(new_set)
        if len(all_word) == before_word_len:
            break
        before_word_len = len(all_word)
    return answer


def check_word(word, target):
    count = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            count += 1
            if count > 1:
                return False
    if count == 1:
        return True
    return


def conversion_word(begin, word_list, word_set):
    for word in word_list:
        if check_word(word, begin):
            word_set.add(word)


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))

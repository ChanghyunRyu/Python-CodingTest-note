import heapq


def solution(genres, plays):
    play_times = {}
    songs = {}
    answer = []
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in play_times:
            play_times[genre] += play
        else:
            play_times[genre] = play

        if genre in songs:
            songs[genre].append((play, i))
        else:
            songs[genre] = [(play, i)]
    q = []
    for genre in play_times:
        heapq.heappush(q, (-play_times[genre], genre))
    while q:
        genre = heapq.heappop(q)[1]
        song_list = songs[genre]
        song_list.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        while count < 2 and song_list:
            index = song_list.pop()[1]
            answer.append(index)
            count += 1
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

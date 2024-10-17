import heapq


def solution(genres, plays):
    genre_record = {}
    song_record = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in genre_record:
            genre_record[genre] += play
        else:
            genre_record[genre] = play

        if genre in song_record:
            song_record[genre].append((play, -i))
        else:
            song_record[genre] = [(play, -i)]

    q = []
    for key in genre_record.keys():
        heapq.heappush(q, (-genre_record[key], key))

    answer = []
    while q:
        _, g = heapq.heappop(q)
        songs = song_record[g]
        songs.sort()
        answer.append(-songs[-1][1])
        if len(songs) >= 2:
            answer.append(-songs[-2][1])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

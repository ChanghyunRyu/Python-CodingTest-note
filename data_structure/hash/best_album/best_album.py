from collections import defaultdict
import heapq


def solution(genres, plays):
    answer = []
    genres_plays = dict()
    genres_songs = defaultdict(list)
    for i in range(len(genres)):
        if genres[i] in genres_plays:
            genres_plays[genres[i]] += plays[i]
        else:
            genres_plays[genres[i]] = plays[i]
        genres_songs[genres[i]].append((plays[i], i))
    q = []
    for genre in genres_plays:
        heapq.heappush(q, (-genres_plays[genre], genre))
    while q:
        pop_genre = heapq.heappop(q)
        songs = genres_songs[pop_genre[1]]
        songs.sort(key=lambda x: (x[0], -x[1]))
        if len(songs) > 1:
            answer.append(songs[-1][1])
            answer.append(songs[-2][1])
        else:
            answer.append(songs[-1][1])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

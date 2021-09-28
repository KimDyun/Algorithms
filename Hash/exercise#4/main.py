"""
Problem: Best album

Description:
     We are planning to release the best album by collecting two of the most played songs_info
    by genre on the streaming site.
     songs_info are classified by unique numbers and the criteria for containing songs_info are as follows.

    1. You have to contain the genre in which the song is the most played first.
    2. You have to contain the most played song in the genre first.
    3. If there are the songs_info with the same number of plays, you have to contain the lower one first.

     When the 'genres', a string type array(list) which represents genres and
    the 'plays', a integer type array(list) which represents play count by song
    are given, implement 'solution' method to return unique number of song
    that's going to be contained to best album in order.

Restrictions:
    1. The genres[i] is the genre of a song with a unique number i.
    2. The plays[i] is the play count of a song with a unique number i.
    3. Genres and plays have same length, and these are 1 to 10,000 in length.
    4. The type of genres is less than 100
    5. If there is only one song in the genre, choose it.
    6. all genres have different play count.
"""
from collections import defaultdict
from functools import cmp_to_key
def playcount(songs):
    sum = 0
    for song in songs:
        sum += song[0]
    return sum

def sortcondition(x,y):
    if x[0] < y[0]: return 1 # 이전 인덱스 노래의 재생수가 낮으면 1을 반환하여 sort 수행
    elif x[0] > y[0]: return -1
    else: # 노래 재생수가 같으면
        if x[1] <= y[1]: return -1 # 이전 인덱스 노래의 고유번호가 낮거나 같으면 sort 수행하지 않음
        else: return 1

def solution(genres, plays):
    album=[]
    songs_info = defaultdict(list)
    for i in range(len(genres)):
        songs_info[genres[i]].append((plays[i], i))
    songs_info = dict(sorted(songs_info.items(), key = lambda x : playcount(x[1]), reverse = True))# 장르마다 속한 곡들의 재생수 합이 큰 순서대로 장르 정렬

    for genre in songs_info:
        songs = songs_info[genre] # 해당 장르의 노래들
        best_songs = list(sorted(songs, key = cmp_to_key(sortcondition)))[:2]#상위 2개 노래
        for best_song in best_songs:
            unique_number_of_song = best_song[1]
            album.append(unique_number_of_song)
    return album

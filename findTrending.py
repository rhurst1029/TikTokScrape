from TikTokApi import TikTokApi
import string
import random
from datetime import date
import json
import pandas as pd 



# THIS LINE
verifyFp = 'verify_kngd0n5c_MNpHdxYL_m64K_4y4O_Aejf_xQKslqaYxk13'

did = ''.join(random.choice(string.digits) for num in range(19))

api = TikTokApi.get_instance(custom_verifyFp = verifyFp)

# When fp stops working:

# THIS LINE
# api = TikTokApi.get_instance(custom_verifyFp = verifyFp, use_test_endpoints = True, custom_did = did)


def get_trending(numSongs):
    '''
    Gets trending data for the top 'numSongs' trending on TikTok
    
    '''
    ids = {}
    num_songs = numSongs
    trending = api.by_trending(count = num_songs)

    for i in trending:
        if i.get('music')['title'] == 'original sound':
            continue
        else:
            ids[ i.get('music')['id']] = i.get('music')['title']
    artistInfo = {}
    ### Initializing primary key for json to be current date
    today = date.today()
    today = today.strftime("%m/%d/%y")

    ## ITERATING THROUGH TRENDING SOUND IDS AT CURRENT RUN
    for n in ids:
        music = api.get_music_object_full(n)
        artistInfo[n] = {}
        info_obj = artistInfo[n]
        
        if i.get('music') is None:
            print(f'music object for soundID {n} has no music tag')
            break
        else:
            info_obj['date_run'] = today
            info_obj['songTitle'] = music.get('music')['title']
            info_obj['authorName'] = music.get('music')['authorName']
            info_obj['private'] = music.get('music')['private']
            info_obj['duration'] = music.get('music')['duration']
            info_obj['album'] = music.get('music')['album']
            info_obj['scheduleSearchTime'] = music.get('music')['scheduleSearchTime']
            info_obj['numTimesUsed'] = music.get('stats')['videoCount']
            
        if music.get('author'):
            info_obj['artist_id'] = music.get('author')['id']
            info_obj['uniqueId'] = music.get('author')['uniqueId']
            info_obj['nickname'] = music.get('author')['nickname']
            info_obj['createTime'] = music.get('author')['createTime']
            info_obj['verified'] = music.get('author')['verified']
            info_obj['secUid'] = music.get('author')['secUid']
            info_obj['relation'] = music.get('author')['relation']
            info_obj['openFavorite'] = music.get('author')['openFavorite']
            info_obj['commentSetting'] = music.get('author')['commentSetting']
            info_obj['duetSetting'] = music.get('author')['duetSetting']
            info_obj['stitchSetting'] = music.get('author')['stitchSetting']
            info_obj['privateAccount'] = music.get('author')['privateAccount']
            
        elif music.get('artist'):
            info_obj['artist_id'] = music.get('artist')['id']
            info_obj['uniqueId'] = music.get('artist')['uniqueId']
            info_obj['nickname'] = music.get('artist')['nickname']
            info_obj['createTime'] = music.get('artist')['createTime']
            info_obj['verified'] = music.get('artist')['verified']
            info_obj['secUid'] = music.get('artist')['secUid']
            info_obj['relation'] = music.get('artist')['relation']
            info_obj['openFavorite'] = music.get('artist')['openFavorite']
            info_obj['commentSetting'] = music.get('artist')['commentSetting']
            info_obj['duetSetting'] = music.get('artist')['duetSetting']
            info_obj['stitchSetting'] = music.get('artist')['stitchSetting']
            info_obj['privateAccount'] = music.get('artist')['privateAccount']
        else:
            info_obj['artist_id'] = 'NA'
            info_obj['uniqueId'] = 'NA'
            info_obj['nickname'] = 'NA'
            info_obj['createTime'] = 'NA'
            info_obj['verified'] = 'NA'
            info_obj['secUid'] = 'NA'
            info_obj['relation'] = 'NA'
            info_obj['openFavorite'] = 'NA'
            info_obj['commentSetting'] = 'NA'
            info_obj['duetSetting'] = 'NA'
            info_obj['stitchSetting'] = 'NA'
            info_obj['privateAccount'] = 'NA'
    
    df = pd.DataFrame.from_dict(artistInfo, orient="index")

    df.to_csv('trendingStats.csv')


numSongs = 40
get_trending(numSongs)
 
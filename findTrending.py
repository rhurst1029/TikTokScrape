from TikTokApi import TikTokApi
import string
import random
from datetime import date
import json



# THIS LINE
verifyFp = 'verify_kngd0n5c_MNpHdxYL_m64K_4y4O_Aejf_xQKslqaYxk13'

did = ''.join(random.choice(string.digits) for num in range(19))

api = TikTokApi.get_instance(custom_verifyFp = verifyFp)

# When fp stops working:

# THIS LINE
# api = TikTokApi.get_instance(custom_verifyFp = verifyFp, use_test_endpoints = True, custom_did = did)



ids = {}
count = 200
trending = api.by_trending(count = count)

for i in trending:
    if i.get('music')['title'] == 'original sound':
        continue
    else:
        ids[ i.get('music')['id']] = i.get('music')['title']



artistInfo = {}
### Initializing primary key for json to be current date
today = date.today()
today = today.strftime("%m/%d/%y")
artistInfo[today] = {}

## ITERATING THROUGH TRENDING SOUND IDS AT CURRENT RUN
for n in ids:
    music = api.get_music_object_full(n)
    artistInfo[today][n] = {}
    info_obj = artistInfo[today][n]
    
    if i.get('music'):
        info_obj['songTitle'] = music.get('music')['title']
        info_obj['authorName'] = music.get('music')['authorName']
        info_obj['private'] = music.get('music')['private']
        info_obj['duration'] = music.get('music')['duration']
        info_obj['album'] = music.get('music')['album']
        info_obj['scheduleSearchTime'] = music.get('music')['scheduleSearchTime']
        info_obj['numTimesUsed'] = music.get('stats')['videoCount']
        info_obj['artistInfo'] = {}
        
    else:
        print('music object has no music tag')
        print(music)     
    
    info_dict = info_obj['artistInfo']
    if music.get('author'):
        info_dict['id'] = music.get('author')['id']
        info_dict['uniqueId'] = music.get('author')['uniqueId']
        info_dict['nickname'] = music.get('author')['nickname']
        info_dict['createTime'] = music.get('author')['createTime']
        info_dict['verified'] = music.get('author')['verified']
        info_dict['secUid'] = music.get('author')['secUid']
        info_dict['relation'] = music.get('author')['relation']
        info_dict['openFavorite'] = music.get('author')['openFavorite']
        info_dict['commentSetting'] = music.get('author')['commentSetting']
        info_dict['duetSetting'] = music.get('author')['duetSetting']
        info_dict['stitchSetting'] = music.get('author')['stitchSetting']
        info_dict['privateAccount'] = music.get('author')['privateAccount']
        
    elif music.get('artist'):
        info_dict['id'] = music.get('artist')['id']
        info_dict['uniqueId'] = music.get('artist')['uniqueId']
        info_dict['nickname'] = music.get('artist')['nickname']
        info_dict['createTime'] = music.get('artist')['createTime']
        info_dict['verified'] = music.get('artist')['verified']
        info_dict['secUid'] = music.get('artist')['secUid']
        info_dict['relation'] = music.get('artist')['relation']
        info_dict['openFavorite'] = music.get('artist')['openFavorite']
        info_dict['commentSetting'] = music.get('artist')['commentSetting']
        info_dict['duetSetting'] = music.get('artist')['duetSetting']
        info_dict['stitchSetting'] = music.get('artist')['stitchSetting']
        info_dict['privateAccount'] = music.get('artist')['privateAccount']
    else:
        info_dict['id'] = 'NA'
        info_dict['uniqueId'] = 'NA'
        info_dict['nickname'] = 'NA'
        info_dict['createTime'] = 'NA'
        info_dict['verified'] = 'NA'
        info_dict['secUid'] = 'NA'
        info_dict['relation'] = 'NA'
        info_dict['openFavorite'] = 'NA'
        info_dict['commentSetting'] = 'NA'
        info_dict['duetSetting'] = 'NA'
        info_dict['stitchSetting'] = 'NA'
        info_dict['privateAccount'] = 'NA'

with open('trendingStats.json', 'w') as fp:
    json.dump(artistInfo, fp)



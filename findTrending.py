from TikTokApi import TikTokApi
import string
import random


# THIS LINE
verifyFp = 'verify_kngd0n5c_MNpHdxYL_m64K_4y4O_Aejf_xQKslqaYxk13'

did = ''.join(random.choice(string.digits) for num in range(19))

api = TikTokApi.get_instance(custom_verifyFp = verifyFp)

# When fp stops working:

# THIS LINE
# api = TikTokApi.get_instance(custom_verifyFp = verifyFp, use_test_endpoints = True, custom_did = did)


# Trending
ids = {}
count = 300
trending = api.by_trending(count = count)

for i in trending:
    if i.get('music')['title'] == 'original sound':
        continue
    else:
        ids[ i.get('music')['id']] = i.get('music')['title']



ids2 = {}
## Filtered is the number of sounds_ids from 'count' (300 rn) that weren't original sounds
filtered = 0
## Artist_author is the number of filtered sound ids that have artis/author data
artist_author = 0
missing_artist = 0
for n in ids:
    music = api.get_music_object_full(n)
    # ids2[music['music']['id']] = []
    # ids2[music['music']['id']].append(music['music']['title'

    if music.get('author'):
        artist_author += 1
        # print(music)
    elif music.get('artist'):
        artist_author += 1
        # print('artist', '\n','\n','\n', music)
    else:
        missing_artist += 1
        # print('NEITHER', '\n','\n','\n', music)
filtered += 1
    
print('Total_original/300', count - filtered)
print('total_w_artist_data', artist_author)
print('total_without_artist_data', missing_artist)

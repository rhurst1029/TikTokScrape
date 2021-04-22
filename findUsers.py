from TikTokApi import TikTokApi
import pandas as pd
from operator import itemgetter
import json

# Key last updated 4/20 blaze
verifyFp = 'verify_kngd0n5c_MNpHdxYL_m64K_4y4O_Aejf_xQKslqaYxk13'

api = TikTokApi.get_instance(custom_verifyFp = verifyFp, use_test_endpoints = True)

# Useful functions
'''
    user_posts: returns an array of dictionaries representing TikToks for a user
    by_username: Returns a dictionary listing TikToks given a user&#39;s username.
    by_sound: dictionary with given sound
    user_page: dictionary listing of one page of TikToks given user ID
    get_user_pager: returns a generator to page through a user's feed
    discover_music: discover page for music
    get_user_object: gets a user object || get_user
    TikTokUser class:
        get_insights
'''

# From Ryan: 
sounds = {'6885449331428558861': ['Jump in the Line (Shake, Senora)', 'Harry Belafonte'], 
'6826096341966456833': ['Buss It', 'Erica Banks'], 
'6927076140512135170': ['Bongo cha-cha-cha - Remastered', 'Caterina Valente'], 
'6921891821358435077': ['strawhatdan', 'STRAWHAT DAN'], 
'6669854674113317638': ['BREAKFAST CHALLENGE', 'spence'], 
'6808641827374222085': ['GET WATER OUT OF PHONE SPEAKERS', 'Victoria Bachlet'], '6832618984580335617': ['Stuck in the Middle', 'Tai'], '6816496693551450885': ['Astronaut In The Ocean', 'MaskedWolf'], '6769046027488987137': ['FEEL THE GROOVE', 'Queens Road, Fabian Graetz'], '6778968637492430849': ['Blue Blood', 'Heinz Kiessling & Various Artists'], '6746993352891189249': ['Monkeys Spinning Monkeys', 'Kevin MacLeod'], '6948521578766371590': ['Levitating', 'Dua Lipa'], '118053679': ['Pink Panther Intro', 'Henry Mancini']}

# Getting the user keys
# keys = sounds.keys()
# real_keys = []
# for key in keys:
#     real_keys.append(key)

def get_ids(sounds):
    ''' 
    Given a dictionary of trending sounds, formatted like such:
        {'6885449331428558861': ['Jump in the Line (Shake, Senora)', 'Harry Belafonte']}
        where
        {'sound ID': ['sound_title', 'authorName']}
    Outputs a list of the sound ids, to make id extraction easier.
    '''
    temp_keys = sounds.keys()
    keys = []
    for key in temp_keys:
        keys.append(key)
    return keys

top_id = get_ids(sounds)[0]

# Change count to 2000 max
info = api.by_sound(top_id)
# print(info[0])

# df = pd.read_json('trendingStats.json', orient = 'index')
# print(df.iloc[0][0])
# print(df)

''' TURN JSON INTO DATAFRAME '''
# trending_sounds = pd.read_json('trendingStats.json')
# trending_sounds = trending_sounds.reset_index()
# trending_sounds = trending_sounds.rename(columns={'index': 'id'})
# trending_sounds.columns = ['id', '2021-04-20']

def only_id(string):
    '''
    Currently, the index (or now renamed 'id' column) outputs id like such: 
        before: 1970-01-01 00:00:00.118053679
        after: 118053679
    We want only the last 9 digits, which correspond to the id of the song.
    '''
    string = str(string)
    string = string[-9:]
    return string

# Apply only_id to each row of the id column, so we have a column of ids.
# trending_sounds['id'] = trending_sounds['id'].apply(only_id)
ids = [6885449331428558861, 6785326848835488518, 6826096341966456833,
6927076140512135170, 6921891821358435077, 6808641827374222085]

test_sound = ids
# print(api.by_sound(test_sound)[0].get('authorStats').keys())
final = {}
keys = ['followingCount', 'followerCount', 'heartCount', 'videoCount', 'diggCount', 'heart']
for i in ids:
    ### Initializing dict to carry all user data for a given sondID
    final[i] = {}
    userData = api.by_sound(i, count = 3)
    for h in userData:
        post_id = h.get('id')
        final[i][post_id] = {}
        # stats = {}
        for n in keys:
            # stats[n] = h.get('authorStats')[n]
            final[i][post_id][n] = h.get('authorStats')[n]
print(final)
with open('trendingStats.json', 'w') as fp:
    json.dump(final, fp)

# print(api.by_sound(test_sound, count = 20))
    





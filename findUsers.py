from TikTokApi import TikTokApi
import pandas as pd
from operator import itemgetter
import json
from datetime import date

# Key last updated 4/20 blaze
verifyFp = 'verify_kngd0n5c_MNpHdxYL_m64K_4y4O_Aejf_xQKslqaYxk13'

api = TikTokApi.get_instance(custom_verifyFp = verifyFp, use_test_endpoints = True)

### Useful functions ### 
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



def write_ids():
    '''
    Takes in literally nothing, Finds and formats the current date, reads in soundIDs.json, and returns list of soundIDs
    '''
    today = date.today()
    today = today.strftime("%m/%d/%y")
    # Opening csv
    df = pd.read_csv('trendingStats.csv')
    ## Subsetting CSV to contain today's runs
    df = df[df['date_run']== today]
    soundIDs = df.iloc[:,0].to_list()
    return soundIDs


def get_post_data(ids, keys, numPosts):
    '''
    Main method used for receiving post data for a given soundID. 
    Takes in:
        1) ids: List of soundIDs
        2) keys: Data from postData we want to collect
        3) numPosts: number of posts to query for a given soundID
    '''
    ## Getting date_run attribute
    today = date.today()
    today = today.strftime("%m/%d/%y")
    ### Initializing datastructure for final json dump
    final = {}
    for i in ids:
        ### Converting soundID to string because JSON prefers this for writing and opening
        i = str(i)
        ### Initializing an array at the soundID to contain all the data on posts 
        
    
        userData = api.by_sound(i, count = numPosts)
        j = 0
        for h in userData:
            post_id = h.get('id')
            final[post_id] = {}
            final[post_id]['soundID'] = i
            final[post_id]['date_run'] = today
            for n in keys:
                final[post_id][n] = h.get('authorStats')[n]
                
            j +=1

    ## Append to csv file for today's run:
    data = pd.DataFrame.from_dict(final, orient="index")
    compression_opts = dict(method='zip',
                        archive_name='userStats.csv')  
    data.to_csv('userStats.csv', compression=compression_opts)
    


### Getting list of IDs for today's date
ids = write_ids()

### List of keys from the post datastructure needed 
keys = ['followingCount', 'followerCount', 'heartCount', 'videoCount', 'diggCount', 'heart']
num_posts = 50
get_post_data(ids, keys, num_posts)





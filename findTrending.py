### This script finds the top trending songs on tiktok and stores them in the topSongs.json file w/ the following structure

from TikTokApi import TikTokApi
import string
import random


# THIS LINE
verifyFp = 'verify_kngd0n5c_MNpHdxYL_m64K_4y4O_Aejf_xQKslqaYxk13'

did = ''.join(random.choice(string.digits) for num in range(19))

# api = TikTokAPI.get_instance(custom_verifyFp = verifyFp)

# When fp stops working:

# THIS LINE
api = TikTokApi.get_instance(custom_verifyFp = verifyFp, use_test_endpoints = True, custom_did = did)

#THIS LINE
# Ryan's code
h = api.discoverMusic(language='en', proxy=None)

ids = []
for i in h:
    ids.append(i['cardItem']['id'])
id_dict = {}
for i in ids:
    #### Gets top tiktoks made with the trending sound IDs ###
    n = api.by_sound( i, count=30, offset=0)
    # print(n)

    id_dict[i] = []
    for j in n:
        id_dict[i].append(j['authorStats'])
print(id_dict)

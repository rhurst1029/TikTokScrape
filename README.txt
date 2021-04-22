This project serves to predict the top tiktok songs at the end of a given week from data collected throughout the week. 

RUN COMMANDS:
*** Before running: Make sure that both post and sound CSVs are deleted or the query will act up ***
*** Current default number of trending sounds to query is 250. TO CHANGE: go to the bottom of findTrending.py and change 'numSongs' variable ***
*** Current default number of posts per sound to query is 100. TO CHANGE: go to the bottom of findUsers.py and change 'num_posts' variable ***
RUNNING QUERY:
$ python3 findTrending.py
$ python3 findUsers.py

ACTIVATING VIRTUAL ENVIRONMENT:
      
    - python3 -m venv venv
    - virtualenv venv
    - source venv/bin/activate


Git Commands (for Ivy):

**INITIALIZING GIT REPO ON LOCAL MACHINE:**
1. pen terminal to clone git repo from command line:
2. cd into some directory (I prefer Documents) and run the below to clone git repo to local machine:

$ git clone https://github.com/rhurst1029/TikTokScrape.git

3. Now, if you cd into the directory you cloned from, the file should exist. 
    Go ahead and open up the repo in VS code and cd into into it
4. To PUSH changes: Make any changes you want the run:

$ git add -A 
$ git commit -m "Ivys first commit"
$ git push origin master

** PULLING CHANGES BEFORE WORK **
To check what cchanges have been made:
$ git status

To Pull most recent changes from git:

$ git pull 


METHOD DESCRIPTIONS:
findTrending.py:
1. Finds top trending sounds on tiktok at current date
2. Takes soundID, returns stats on top users using those songs
3. (Right now just copied and pasted): Stores Json in the form of:
{soundID:[{
     userData1
},
{
    userData2
}]}
### Note: We will need to format the query s,t it returns more info on the given SOundID 
(can be found in the Json returned by trending()) along with user data on each user who has used the song

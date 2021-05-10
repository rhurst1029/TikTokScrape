
This project serves to predict the top tiktok songs at the end of a given week from data collected throughout the week.


ACTIVATING VIRTUAL ENVIRONMENT:
$ python3 -m venv venv
$ virtualenv venv
$ source venv/bin/activate

METHOD DESCRIPTIONS:

findTrending.py:
1. Finds top trending sounds on tiktok at current date
2. Takes soundID, returns stats on top users using those songs

findUsers.py:
1. Takes in CSV from findTrending and collects soundIDs for most recent trending sounds
2. Queries 'num_posts' # of posts using a given soundID, collects, and formats data 


*** Before running: Make sure that both post and sound CSVs are deleted or the query will act up ***
*** Current default number of trending sounds to query is 250. TO CHANGE: go to the bottom of findTrending.py and change 'numSongs' variable ***
*** Current default number of posts per sound to query is 100. TO CHANGE: go to the bottom of findUsers.py and change 'num_posts' variable ***

RUN COMMANDS:
$ python3 findTrending.py
$ python3 findUsers.py


Git Commands:

** INITIALIZING GIT REPO ON LOCAL MACHINE: **
1. pen terminal to clone git repo from command line:
2. cd into some directory (I prefer Documents) and run the below to clone git repo to local machine:

$ git clone https://github.com/rhurst1029/TikTokScrape.git

3. Now, if you cd into the directory you cloned from, the file should exist. 
    Go ahead and open up the repo in VS code and cd into into it
4. To PUSH changes: Make any changes you want the run:

$ git add -A 
$ git commit -m "My First Commit"
$ git push origin master

** PULLING CHANGES BEFORE WORK **

To check what changes have been made:
$ git status

To Pull most recent changes from git:
$ git pull 







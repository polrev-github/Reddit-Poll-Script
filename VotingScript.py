import praw
import time
import pdb
from datetime import datetime


def Main():
    username = 'USERNAME' # reddit username, must be moderator account
    password = 'PASSWORD' # reddit password
    user_agent = ("Polling Script by /u/scriggities, modified by /u/Tyree07, v0.2")

    clientID = 'CLIENTID'
    clientSecret = 'CLIENTSECRET'
    clientCallback = 'REDIRECT_URI'
    subredditName = 'Political_Revolution' # Subreddit name

    print ("Logging into Reddit") #DO NOT MODIFY VARIABLES HEREIN; Fill in details above
    r = praw.Reddit(client_id=clientID,
                    client_secret=clientSecret,
                    password=password,
                    user_agent=user_agent,
                    username=username)
    print ("Connected to /r/" + subredditName)

    threadID = input('Enter Thread ID (from comments URL): ')
    #numchoices = input('Enter number of choices: ')

    # Define dictionary of result tally and voters #
    tally = {'long comment' : 0, 'new accounts' : 0, 'bad poster' : 0}
    voted = {}
    bad = {}

    submission = r.submission(id = threadID)
    #flat_comments = praw.helpers.flatten_tree(submission.comments)

    #for comment in flat_comments:
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        if comment.author.name in voted:
            continue
        excludeSub = False
        now = time.mktime(time.gmtime())-21600
        created = comment.author.created_utc
        age = int(now-created)/60/24 #account age in days
        for authorcomment in comment.author.comments.new(limit=100):
            sub = authorcomment.subreddit.display_name
            if sub == "The_Donald" or sub == 'Enough_Sanders_Spam' or sub == 'WayOfTheBern': #Subreddits you want to exclude from vote if in user's history
                excludeSub = True
                break
        if excludeSub:
            tally['bad poster'] = tally['bad poster'] + 1
            bad[comment.author.name] = comment.body
        elif len(comment.body) == 1 and age >= 30 :
            if comment.body in tally:
                tally[comment.body] = tally[comment.body] + 1
                voted[comment.author.name] = comment.body
            else:
                tally[comment.body] = 1
                voted[comment.author.name] = comment.body
        elif len(comment.body) == 1 and age < 30:
            tally['new accounts'] = tally['new accounts'] + 1
            voted[comment.author.name] = comment.body
        else:
            tally['long comment'] = tally['long comment'] + 1
    print("Vote Totals")
    print(tally)
    print("Good votes")
    print(voted)
    print("T_D/ESS/WotB votes") #Print vote tally by excluded subreddits
    print(bad)

Main()

import praw
import pickle
import time
pickleFile = "myPickleFile.pk"


def storeUTC():
    with open(pickleFile, 'wb+') as pick:
        pickle.dump(0, pick)
        #pickle.dump(int(time.time()), pick)
    return

def loadUTC():
    with open(pickleFile, 'rb') as pick:
        try:
            return pickle.load(pick)
        except EOFError:
            return 0

def checkSubmission(submission):
    
    return

def getFromReddit():
    lastCheckTime = loadUTC()
    print(lastCheckTime)
    reddit = praw.Reddit(client_id="KrKvK25tPXyhsuYKURx4aA", client_secret="WFLyQT2FYaVau7pDTUwlKCupDF2wqQ",
                         user_agent="python:praw:gameDealsParser (by /u/dewarden)")
    reddit.read_only = True
    for submissions in reddit.subreddit("GameDeals").new(limit=10):
        if submissions.created_utc > lastCheckTime:
            #file hasn't been checked before
            checkSubmission(submissions)
        else:
            #checked all new ones
            print("Checked all the new ones")
            return
    #stopped checking because passed limit
    print("There were new submissions that haven't been checked yet")
    return

def main():
    getFromReddit()
    storeUTC()
    return


main()

exit(0)


#docs: https://praw.readthedocs.io/en/stable/code_overview/models/submission.html?highlight=submission#praw.models.Submission
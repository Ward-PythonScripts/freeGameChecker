import praw
import pickle
import time

pickleFile = "myPickleFile.pk"


class freeGame:
    def __init__(self, category, title, redditLink):
        self.cat = category
        self.title = title
        self.reddit = redditLink


def storeUTC():
    with open(pickleFile, 'wb+') as pick:
        pickle.dump(0, pick)
        # pickle.dump(int(time.time()), pick)
    return


def loadUTC():
    with open(pickleFile, 'rb') as pick:
        try:
            return pickle.load(pick)
        except EOFError:
            return 0


def checkSubmission(submission):
    # get category
    s = str(submission.title)
    if s.__contains__("Free") or s.__contains__("FREE") or s.__contains__("free"):
        category = s[s.find("[")+len("["):s.rfind("]")]
        print(s)
        target = "[" + str(category) + "]"
        title = str.replace(submission.title, target, "")
        return freeGame(category,title,submission.permalink)
    else:
        return None


def getFromReddit():
    freeGames = []
    lastCheckTime = loadUTC()
    print(lastCheckTime)
    reddit = praw.Reddit(client_id="KrKvK25tPXyhsuYKURx4aA", client_secret="WFLyQT2FYaVau7pDTUwlKCupDF2wqQ",
                         user_agent="python:praw:gameDealsParser (by /u/dewarden)")
    reddit.read_only = True
    for submissions in reddit.subreddit("GameDeals").new(limit=100):
        if submissions.created_utc > lastCheckTime:
            # file hasn't been checked before
            game = checkSubmission(submissions)
            if not game is None:
                freeGames.append(game)
        else:
            # checked all new ones
            print("Checked all the new ones")
            return freeGames
    # stopped checking because passed limit
    print("There were new submissions that haven't been checked yet")
    return freeGames

def sendGames(freeGames):
    for game in freeGames:
        print(game.cat)

def main():
    freeGames = getFromReddit()
    storeUTC()
    sendGames(freeGames)
    return


main()

exit(0)

# docs: https://praw.readthedocs.io/en/stable/code_overview/models/submission.html?highlight=submission#praw.models.Submission

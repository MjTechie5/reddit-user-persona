import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_data(username):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    redditor = reddit.redditor(username)
    posts = []
    comments = []

    try:
        for submission in redditor.submissions.new(limit=50):
            posts.append({
                "title": submission.title,
                "body": submission.selftext,
                "permalink": f"https://www.reddit.com{submission.permalink}"
            })

        for comment in redditor.comments.new(limit=50):
            comments.append({
                "body": comment.body,
                "permalink": f"https://www.reddit.com{comment.permalink}"
            })

    except Exception as e:
        print("Error fetching data:", e)

    return posts, comments

import sys
import re
from reddit_scraper import get_reddit_data
from llm_persona_builder import generate_persona
from persona_report import save_persona_as_pdf

def extract_username(url):
    return re.findall(r"reddit\.com/user/([^/]+)", url)[0]

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py https://www.reddit.com/user/<username>/")
        return

    profile_url = sys.argv[1]
    username = extract_username(profile_url)

    print(f" Fetching Reddit data for u/{username}...")
    posts, comments = get_reddit_data(username)

    print(f" Generating user persona for u/{username} using model...")
    persona = generate_persona(posts, comments, username)

    print(f" Saving persona as PDF...")
    save_persona_as_pdf(username, persona)

if __name__ == "__main__":
    main()

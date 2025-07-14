import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_prompt(posts, comments, username="unknown"):
    content = ""
    for p in posts:
        content += f"\nPOST:\nTitle: {p['title']}\nText: {p['body']}\n[Source: {p['permalink']}]\n"
    for c in comments:
        content += f"\nCOMMENT:\nText: {c['body']}\n[Source: {c['permalink']}]\n"

    prompt = f"""
You are an expert in behavioral analysis and user research.

Analyze the following Reddit posts and comments from u/{username} and generate a **structured and readable user persona**.

Be cautious but smart: If you find hints or context that help infer a person's **age**, **occupation**, or **location**, include them with justification.

If something is clearly not mentioned or inferable, say: **"Not enough data"**

Your output MUST follow this format:

───────────────────────────────────────────────
           REDDIT USER PERSONA
───────────────────────────────────────────────

# Username: u/{username}
# Name: ...
# Age: ...
# Occupation: ...
# Location: ...

#Quote:
"..."

───────────────────────────────────────────────
# PERSONALITY TRAITS
- ...

# MOTIVATIONS
- ...

# GOALS & NEEDS
- ...

# BEHAVIORS & HABITS
- ...

# FRUSTRATIONS
- ...

# OVERALL PERSONALITY SUMMARY
"3–5 word phrase"

# CITED SOURCES
- [reddit.com/...]
- [reddit.com/...]
───────────────────────────────────────────────

Only include real, quoted content. Never invent. Be clean, structured, and markdown-compatible.

Here is the user's Reddit activity:

{content}
"""
    return prompt

def generate_persona(posts, comments, username="anonymous"):
    posts = posts[:20]
    comments = comments[:20]

    prompt = build_prompt(posts, comments, username)

    print(" Prompt token length (words):", len(prompt.split()))

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
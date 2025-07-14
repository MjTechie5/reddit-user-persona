# Reddit User Persona Generator

This project generates a detailed user persona from any public Reddit user profile. It scrapes the user’s posts and comments, analyzes them using a powerful LLM (Groq's LLaMA-3), and outputs a structured persona saved as a PDF file.

---------------------------------------------------------------------

## Step0 : Requirement Specifications

- Python 3.8+
- API keys for Reddit and Groq (free)


## Step 1 :  API Key Setup

1. **Reddit API Credentials:**

      Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) and:
       - Click "Create App"
       - Choose type: `script`
       - Set Redirect URI: `http://localhost`

      Copy your:
       - `client_id`
       - `client_secret`
       - `user_agent` (any string)

2. **Groq API Key (Free):**

      Go to [https://console.groq.com/keys](https://console.groq.com/keys)  
      Click “Create Key” → Copy the key (`gsk_...`)


##  Creating Environment file in the root folder 

   Create a .env file in the root directory and add the following to it : 

           REDDIT_CLIENT_ID=your_reddit_client_id
           REDDIT_CLIENT_SECRET=your_reddit_client_secret
           REDDIT_USER_AGENT=persona-script by u/yourusername
           GROQ_API_KEY=gsk_your_groq_api_key 


##  Installing Python dependencies

           pip install -r requirements.txt


##  Generating persona from scrapped data 

   Run the following script in  terminal of the root folder:

         Script :  python main.py https://www.reddit.com/user/<reddit_username>/

         Eg: python main.py https://www.reddit.com/user/Hungry-Move-6603/


   This will scrape the user's posts and comments.

   Analyze them with the LLaMA-3 model from Groq.

   Save a structured persona PDF in the output folder.


**Sample outputs have been saved in the output folder of this repository** 


##   The PDF Format of the Persona : 


     Name (if inferable)

     Age range

     Occupation

     Location

     Quote

     Motivations

     Personality traits

     Habits

     Frustrations

     Goals

     Cited Reddit sources


-------------------------------------------------------------------------------------------------------------------------------------------------------------

**This project has been done as a task by Manit Jain**

import openai
import tweepy
import parse_riddle
import os
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY=os.getenv('CONSUMER_KEY')
CONSUMER_SECRET=os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.getenv('ACCESS_TOKEN_SECRET')

openai.api_key = os.getenv('OPENAI_KEY')

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a grumpy but silly little troll who lives under a bridge. Every day you give travelers a riddle to answer if they would like to pass. Please give a different riddle every time, no duplicates!. Please give both the riddle and the answer in this format: Riddle-Here is a riddle.\n\nAnswer-Here is the answer."},
        {"role": "user", "content": "Hello Troll, I would like to cross your bridge. What is your riddle?"},
        {"role": "assistant", "content": "Hmmmmmmm, let me think..."}
    ]
)
print(response)

question, answer = parse_riddle.parse(response['choices'][0]['message']['content'])
print(question)

solutionFile = open('solution.txt', 'w')
solutionFile.write(answer)
solutionFile.close()

client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text=question)

print(response)

# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%

# coding: utf-8

# %%
import requests_oauthlib
import json
import pya3rt
import os



url = "https://stream.twitter.com/1.1/statuses/filter.json"
CK=os.environ["CONSUMER_KEY"]
CS=os.environ["CONSUMER_SECRET"]
AT=os.environ["ACCESS_TOKEN"]
AS=os.environ["ACCESS_TOKEN_SECRET"]


# %%
TALKAPI = os.environ["TALK_API"]


# %%
twitter = requests_oauthlib.OAuth1Session(CK,CS,AT,AS)
client = pya3rt.TalkClient(TALKAPI)

r = twitter.post(url, data=dict(track="@A_incompetence"), stream=True)
for line in r.iter_lines():
    try:
        tmp = line.decode()
        tmp = json.loads(tmp)
        follow = tmp['user']['id']
        followurl = "https://api.twitter.com/1.1/friendships/create.json"
        req = twitter.post(followurl+"?user_id="+str(follow))
        content = tmp["text"]
        content = content[content.find(" ")+1:]
        reply = client.talk(content)["results"][0]["reply"]
        reply = "@" + tmp["user"]["screen_name"] + " " + reply
        params = {"status": reply,"in_reply_to_status_id":tmp["id_str"]}
        twipost = "https://api.twitter.com/1.1/statuses/update.json"
        req = twitter.post(twipost, params = params)
    except:
        #print("exception")
        pass
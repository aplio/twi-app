# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import random
import sys
if  random.choice([1,4]) == 4:
    ##
    sys.exit()

from requests_oauthlib import OAuth1Session
import json
import os
from datetime import datetime, timedelta, timezone
from bs4 import BeautifulSoup
from bottlenose import api
from janome.tokenizer import Tokenizer

CK=os.environ["CONSUMER_KEY"]
CS=os.environ["CONSUMER_SECRET"]
AT=os.environ["ACCESS_TOKEN"]
AS=os.environ["ACCESS_TOKEN_SECRET"]
Amazon_access_key_Id=os.environ["AMAZON_ACCESS_KEY_ID"]
Amazon_secret_key=os.environ["AMAZON_SECRET_KEY"]
Amazon_assocc_tag=os.environ["AMAZON_ASSOC_TAG"]
twitter = OAuth1Session(CK, CS, AT, AS)
JST = timezone(timedelta(hours=+9), 'JST')

def twisearcher(query):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    req = twitter.get(url,params={"q" : query+" exclude:retweets -filter:links" ,"result_type" : "recent","count":100 }).json()
    req = [each['text'] for each in req['statuses'] if each['text'][0] != '@' if each['source'].find("Twitter") != -1 if each['text'].find('https://') == -1]
    return req

def prep_title(title):
    while title.rfind('(') != -1:
        title = title[:title.rfind('(')]
    while title.rfind('（') != -1:
        title = title[:title.rfind('（')]
    while title.rfind('【') != -1:
        title = title[:title.rfind('【')]
    if title.rfind(' ') != -1:
        if title[title.rfind(' ')-2] == ' ':
            title = title[:title.rfind(' ')-2]
    if title.endswith(' '):
        title = title[:-1]
    while title[-1] in ["0","1","2","3","4","5","6","7","8","9","１","２","３","４","５","６","７","８","９","０"]:
        title = title[:-1]
    while title.endswith(' '):
        title = title[:-1]
    return title

def item_search(item_page, amazon, search_index="Books", response_group="Small,Reviews", browse_node="2275256051"):    
    response = amazon.ItemSearch(
        SearchIndex=search_index, 
        BrowseNode=browse_node, 
        ItemPage=item_page, 
        ResponseGroup=response_group
        )

    time.sleep(1.5)

    return response.findAll('item')

def do_it(EoM):
    amazon = api.Amazon(Amazon_access_key_Id, Amazon_secret_key, Amazon_assocc_tag, Region="JP",
        Parser=lambda text: BeautifulSoup(text,'lxml'), ErrorHandler=error_handler
    )
    if EoM == 1:
        item = ([manga_search(random.randint(1,8), amazon)])
    if EoM == 0:
        item = ([movie_search(random.randint(1,8), amazon)])
    item = item[0][random.randint(1,8)]
    title = item.find('title').text
    url = item.find('detailpageurl').text
    if EoM == 1:
        title = prep_title(title)
    return title,url

def manga_search(item_page, amazon, search_index="Books", response_group="Small", browse_node="2275256051"):    
    response = amazon.ItemSearch(
        SearchIndex=search_index, 
        BrowseNode=browse_node, 
        ItemPage=item_page, 
        ResponseGroup=response_group
        )

    return response.findAll('item')

def movie_search(item_page, amazon, search_index="VideoDownload", response_group="Small", browse_node="2351650051"):    
    response = amazon.ItemSearch(
        SearchIndex=search_index, 
        BrowseNode=browse_node, 
        ItemPage=item_page, 
        ResponseGroup=response_group
        )

    return response.findAll('item')

###

def selecter(tweets,word):
    t = Tokenizer()
    gen = []
    tweet = tweets
    for each in tweet:
        NVcount = 0
        Scount = 0
        for token in t.tokenize(each):
            Scount +=1
            if token.part_of_speech.split(",")[0] in ['名詞','動詞']:
                if token.surface != word:
                    NVcount += 1
        if Scount > 70:
            gen.append(1)
            continue
        if Scount <10 and NVcount < 4:
            gen.append(0.3)
            continue
        gen.append(NVcount/Scount)
    gen = [each for each in (enumerate(gen)) if each[1] < 0.5]
    selected = []
    num = 0.2
    while selected == []:
        selected = [each for each in gen if each[1] < num]
        num += 0.1
        if num > 0.6:
            break
    gen = random.choice(selected)[0]
    return tweet[gen]

def spammer():
    url = "https://api.twitter.com/1.1/followers/ids.json"
    a = twitter.get(url+"?screen_name=A_incompetence&count=10").json()
    tmp = a["ids"][random.randint(0,9)]
    a = twitter.get(url+"?user_id="+str(tmp)+"&count=5").json()
    url = "https://api.twitter.com/1.1/friendships/create.json"
    for each in a["ids"]:
        req = twitter.post(url+"?user_id="+str(each))
    return

def trendgetter():
    url = "https://api.twitter.com/1.1/trends/place.json"
    tokyo = 1118370
    params = {"id" : tokyo}
    req = twitter.get(url, params = params).json()

    i = random.randint(1,10)
    onetrend = req[0]["trends"][i]["name"]
    return onetrend

#

if __name__ == '__main__':
    nowtime = datetime.now(JST).hour
    ##
    if nowtime >=6 and nowtime <= 9:
        if random.choice([1,2]) == 1:
            ###
        else:
            ####
    elif nowtime == 10 or nowtime == 11:
        ###
    elif nowtime == 12:
        ###
    elif nowtime >= 13 and nowtime <= 17:
        if random.choice([1,2,2]) == 1:
            ###
        else:
            ###
    elif (nowtime >= 18 and nowtime <= 24) or nowtime == 0 or  nowtime == 1 or nowtime == 2:
        if random.choice([1,2,2]) == 1:
            ##
        else:
            ###
    else:
        print(##)
        sys.exit()
        
    
    tmp = twisearcher(word)
    tmp = selecter(tmp,word)
    flag = 0
    
    if word in contents:
        if random.choice([0,0,1]) == 0:
            if # or #:
                title,url = do_it(0)
            else:
                title,url = do_it(1)
           ###

    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = {"status":tmp})
    if req.status_code == 200:
        print(tmp)
    if random.choice([1,2]) == 1:
        spammer()

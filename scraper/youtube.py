# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:07:15 2021

@author: joseph
"""


from apiclient.discovery import build

YOUTUBE_API_KEY = "Youtube-API"

youtube = build('youtube','v3',developerKey = YOUTUBE_API_KEY)


request = youtube.search().list(q='elon musk',part='snippet',type="video",
                                publishedAfter='2021-11-07T00:00:00Z', maxResults = 100)
res = request.execute()
for item in res['items']:
    print(item['snippet']['title'], "\n")

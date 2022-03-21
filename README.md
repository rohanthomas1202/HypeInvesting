# HYPEINVEST

## Inspiration

As the world of investing becomes more competitive, so too must stock market prediction algorithms that guide investors. Traditional stock market prediction algorithms generally don't use information from social media or the news in their predictions. This is a significant weakness for these predictions, as they ignore a major component of why many people choose to invest in a company. If a company is both talked about and is viewed positively, more people are inclined to support the company by investing in it. This is the major inspiration for HypeInvest.

## What it does

HypeInvest allows users to enter various stocks and obtain both hype information and stock information about the stock in question.

To determine hype, HypeInvest scours Twitter, Reddit, Youtube, and many news outlets to find recent mentions of the company. The sentiment of each mention is determined by Flair, a state-of-the-art sentiment analysis algorithm framework. With the social media mentions, each sentiment is then weighted according to platform specific measures, like upvotes for Reddit. The popularity of a mention in social media is found by determining how much it has been viewed, which is measured differently on each platform. In the case of news mentions, we treat all reliable news sites equally. From there, each overall platform perception is calculated as a weighted average scaled between -1 and 1, where -1 refers to extremely negative perception and 1 refers to extremely positive perception. Each overall platform popularity is calculated as a sum of the popularities of each mention on that platform scaled between 0 and 1, where 0 refers to no mentions and 1 refers to many mentions. Lastly, the overall perception and popularity of the company is found as a weighted average of the platform perceptions and platform popularities respectively.

The hype index is a function of overall perception and overall popularity that scales between -100 and 100, where -100 refers to extremely negative hype, 100 refers to extremely positive hype, and 0 refers to little interest. This is the main result of HypeInvest.

HypeInvest also gathers information about the stock itself. Although hype is useful to guide investing, it should never be used in isolation. Having both stock information and hype information together gives users a bigger picture into how to interpret stock within the context of hype and vice versa.

## How we built it

To access social media and news information, we used Reddit API, Twitter API, Youtube Data API, and News API. To determine sentiment of mentions of a given company, we used Flair. To get stock information, we used the Yahoo Finance API. To deliver back-end data to the front-end, we used an API we built using Flask. To design the front-end, we used React. To do calculations in the back-end, we used Python.

## Challenges we ran into

One of the challenges we ran into was finding social media platforms that could provide valid information. Originally, we hoped to include Facebook in our analysis of social media. However, we soon noticed that we wouldn't be able to interpret the information from Facebook in a way that would be useful. Because of this we pivoted to Youtube in its place.

There was also a major challenge in figuring out how to determine and interpret popularity and perception in a fair way. We swapped between a number of methodologies before settling on what we ended up going forward with. Many of the formulas that we originally thought up of had implementation issues. The popularity of news especially was trickier to interpret, as there's no straightforward way of determining traffic for news articles in the general case.

Working with Flask proved to be difficult as well. More specifically, it was difficult for us to integrate information gathered by our custom API elsewhere. This was the biggest challenge in the later portion of the development of the project.

## Accomplishments that we're proud of

None of us had any real experience with any of the APIs we worked with in this competition, and some of us have have little to no experience with APIs at all. Because of this, we're proud of the fact that were able to successfully use these APIs so prominently in our final product.

Flask was also difficult to work with, so it was all the better that we were able to figure it out to create a custom API that connected our project together.

## What we learned

As a whole, we learned a lot about how to access and utilize APIs overall. We also learned a lot about web development, especially for the purposes of connecting the back-end and front-end of a web application. Besides code, we all got better at determining how we should interpret messages about stocks, as some of us have had no experience in the investing world prior to the hackathon.

## What's next for HypeInvest

There are many ways to build up HypeInvest to be even more accurate. If we had time to create a custom dataset of stock-specific statements and their respective sentiments, we could train a custom Flair model with the dataset and more accurately determine where a statement is positive or negative toward a company.

HypeInvest could also have its own dedicated back-end datatable to retain and update hype information about many of the most popular stocks. This would both make calculations faster and give us access to historical hype data, which could be used to make better predictions. With enough of this data, we could even utilize machine learning to best determine how patterns in hype correlate with a stock rising or falling.<img width="1792" alt="Screen_Shot_2021-11-14_at_1 31 47_PM" src="https://user-images.githubusercontent.com/47799137/141816514-ce1de958-5f1a-486d-b132-5c7b9a7d63d7.png">


https://user-images.githubusercontent.com/47799137/141816650-89520d7c-60b5-4ff1-aa86-1d4948a68b8a.mp4

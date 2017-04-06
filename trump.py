def trump_tweet():
    from urllib.request import urlopen
    html = urlopen("https://twitter.com/realDonaldTrump").read().decode('utf-8')
    a = html.find('TweetTextSize TweetTextSize--large js-tweet-text tweet-text" lang="en" data-aria-label-part="0">')
    b = html.find('<', a + 96)
    return '@realDonaldTrump says : ' + html[a+96:b-1]

print(trump_tweet())
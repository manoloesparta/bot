def trump_tweet():
    from string_cleaner import string_cleaner
    from urllib.request import urlopen
    html = urlopen("https://twitter.com/realDonaldTrump").read().decode('utf-8')
    a = html.find('<div class="content">')
    b = html.find('</p>', a)

    if html[a+2424:b].find('@') == -1 and html[a+2424:b].find('#') == -1:
        return '@realDonaldTrump says : ' + html[a + 2424:b]
    else:
        html = '>' + html[a + 2424:b] + '<'
        return '@realDonaldTrump says : ' + string_cleaner(html)[:-1]
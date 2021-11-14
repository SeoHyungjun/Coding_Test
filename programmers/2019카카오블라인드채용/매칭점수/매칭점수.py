# 2021-03-17 20:48 ->

import re

index_url = {}
basic_rank = {}
outlink = {}
num_link = {}

def solution(word, pages):
    index_check = 0

    p = re.compile(r'<meta(.{0,})content="https://(.{0,})\"/>')

    for page in pages:
        page = page.lower()
        url = p.search(page).group(2)

        #print(url)
        index_url[url] = index_check
        index_check+=1

        count = 0
        
        for text in re.findall(r'[a-zA-Z]{0,}', page):
            if text == word.lower():
                count += 1
        basic_rank[url] = count
        #print(basic_rank)
        num_link[url] = count

        outlink[url] = []
        for text in re.findall('<a href="https://(.\S*)"', page):#re.findall('<a href="https://.\S">', page):
            #print(text)
            #text = text.split('\"')
            #text = text[1].replace('https://', '')
            outlink[url].append(text)
        #print(outlink)

    for link in outlink:
        #print(link, outlink[link])
        for l in outlink[link]:
            if l in num_link:
                num_link[l] += basic_rank[link]/len(outlink[link])
    #print(num_link)
    #print(index_url)
    #print('num_link = ', num_link)

    return index_url[max(num_link.items(), key=lambda x : (x[1], -1*int(index_url[x[0]])))[0]]


word = 'blind'
#word = 'Muzi'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
#pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution(word,pages))
from db import init_db
from network import create_web
import recursive_branch

currentURL = 'https://en.wikipedia.org/wiki/Linux'
visited = []
init_db()
network_counter = 0
network_limit = 100
depth = 0

while True:
    recursive_branch.recursive_branch(currentURL, depth)
    create_web()
    break
#     pageData = webCrawl(currentURL)
        
#     print(f'Currently at {pageData['title']}')
#     insert_page(currentURL, pageData['title'], pageData['summary'])
    
#     print("checking for links...")
#     wikiLinks = [
#     l for l in pageData['links']
#     if l.startswith('/wiki/')
#     and 'Main_Page' not in l
#     and 'Help:' not in l
#     and 'Template:' not in l
#     and 'Wikipedia:' not in l
#     and 'Special:' not in l
#     and 'File:' not in l
#     and 'Category' not in l
#     and 'Talk:' not in l
#     and ('https://en.wikipedia.org' + l) not in visited
# ]
#     if not wikiLinks:
#         print("Reached a dead end..?")
#         break

#     print("checking links for connections...")
#     for link in wikiLinks:
#         for visited_link in visited:
#             if visited_link == 'https://en.wikipedia.org' + link:
#                 insert_link(currentURL, 'https://en.wikipedia.org' + link)
#                 print ("found connection!")

    network_counter += 1
    if network_counter == network_limit:
        print(f"Reached {network_limit} nodes in the network, creating visualization...")
        create_web()
        break
    
    # newURL = 'https://en.wikipedia.org' + random.choice(wikiLinks)
    # insert_link(currentURL, newURL)
    # currentURL = newURL


    

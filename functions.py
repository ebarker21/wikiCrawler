from pyvis.network import Network
from db import insert_page, insert_link, get_pages, get_links
from lxml import html
import requests

web = Network()
visited = {}


def webCrawl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15)'}
    response = requests.get(url, headers=headers)
    tree = html.fromstring(response.content)

    title = tree.xpath('//span[@class="mw-page-title-main"]/text()')
    links = tree.xpath('//div[@id="mw-content-text"]//a/@href')
    paragraphs = tree.xpath('//div[@id="mw-content-text"]//p[not(@class)][1]')
    summary = paragraphs[0].text_content().strip() if paragraphs else ""

    print(title)

    return {
        "title": title[0] if title else "Unknown",
        "links": links,
        "summary": summary
        }


def create_web():
    for page in get_pages():
        web.add_node(n_id=page[1],value=page[0], label=page[2], title=page[3])
        print(f"Added node: {page[2]}")
    for link in get_links():
        web.add_edge(link[0], link[1])
        print(f"Added edge: {link[0]} -> {link[1]}")


def recursive_branch(currentURL, depth):
    if depth > 2:  # Limit the depth of the recursion
        return
    
    if currentURL in visited:
        return

    pageData = webCrawl(currentURL)
    title = pageData['title']
    print(f'Currently at {title} (depth: {depth})')

    visited[currentURL] = title
    insert_page(currentURL, pageData['title'], pageData['summary'])

    if depth >= 2:
        return
    
    print(pageData['links'])

    wikiLinks = []
    for l in pageData['links']:
        if 'en.wikipedia.org/wiki' in l and 'disambiguation' not in l and 'File:' not in l and 'Help:' not in l and 'Special:' not in l and 'Template' not in l and 'Category:' not in l:
            if l.startswith('//'):
                url = 'https:' + l
            elif l.startswith('https://'):
                url = l
            else:
                continue
            if url not in visited:
                wikiLinks.append(url)

    print(wikiLinks)

    for link in wikiLinks:
        newURL = link
        insert_link(currentURL, newURL)
        recursive_branch(newURL, depth + 1)
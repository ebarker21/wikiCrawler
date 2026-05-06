from pyvis.network import Network
from db import insert_page, insert_link, get_pages, get_links
from lxml import html
import requests

web = Network()


def webCrawl(url):
    headers = {'User-Agent': 'MyUserAgent/1.0'}
    response = requests.get(url, headers=headers)

    tree = html.fromstring(response.content)

    title = tree.xpath('//h1[@id="firstHeading"]//text()')
    links = tree.xpath('//a/@href')
    paragraphs = tree.xpath('//div[@id="mw-content-text"]//p[not(@class)][1]')
    summary = paragraphs[0].text_content().strip() if paragraphs else ""

    return {
        "title": title[0],
        "links": links,
        "summary": summary
        }


def create_web():
    for page in get_pages():
        web.add_node(value=page[0], n_id=page[1], label=page[2], title=page[3])
        print(f"Added node: {page[2]}")
    for link in get_links():
        web.add_edge(link[0], link[1])
        print(f"Added edge: {link[0]} -> {link[1]}")


def recursive_branch(currentURL, depth):
    if depth > 2:  # Limit the depth of the recursion
        return

    pageData = webCrawl(currentURL)
    print(f'Currently at {pageData["title"]} (depth: {depth})')
    visited[currentURL] = pageData['title']
    insert_page(currentURL, pageData['title'], pageData['summary'])

    wikiLinks = [
        l for l in pageData['links']
        if l.startswith('/wiki/')
        and 'Main_Page' not in l
        and 'Help:' not in l
        and 'Template:' not in l
        and 'Wikipedia:' not in l
        and 'Special:' not in l
        and 'File:' not in l
        and 'Category' not in l
        and 'Talk' not in l
        and 'User:' not in l
#        and 'Portal:' not in l
        and ('https://en.wikipedia.org' + l) not in visited
    ]

    for link in wikiLinks:
        newURL = 'https://en.wikipedia.org' + link
        insert_link(currentURL, newURL)
        recursive_branch(newURL, depth + 1)
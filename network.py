from pyvis.network import Network
from db import get_pages, get_links
web = Network()

def create_web():
    for page in get_pages():
        web.add_node(value=page[0], n_id=page[1], label=page[2], title=page[3])
        print(f"Added node: {page[2]}")
    for link in get_links():
        web.add_edge(link[0], link[1])
        print(f"Added edge: {link[0]} -> {link[1]}")
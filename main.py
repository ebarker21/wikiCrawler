from db import init_db
import functions

currentURL = 'https://en.wikipedia.org/wiki/Linux'
visited = []
init_db()
network_counter = 0
network_limit = 100
depth = 0


functions.recursive_branch(currentURL, depth)
functions.create_web()
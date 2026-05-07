from db import init_db
import functions

currentURL = 'https://en.wikipedia.org/wiki/Linux'
init_db()
depth = 0


functions.recursive_branch(currentURL, depth)
functions.create_web()
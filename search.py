from utils import getAll

import re

def searchC(alias, term):

    list = []

    posts = getAll(alias)

    for post in posts:
        body = post['body']

        result = re.findall(term, body, re.IGNORECASE)

        if result != []:
            list.append(post)

        else:
            continue

    return list

import writeas

def getAll(alias):
    c = writeas.NewClient()

# List where all the posts from a collection will go
    list = []

# I assume 100 posts is more than generous!
    for i in range(1,10):
# Iterate through the pages...
        cposts = c.retrieveCPosts(alias, i)
        posts = cposts['posts']
# If the posts are not an empty list, take each post and put it in a list!
# That way it catches pages that don't have 10 posts
        if posts != []:
            for post in posts:
# Append to the list of posts
                list.append(post)

        else:
            break

    return list

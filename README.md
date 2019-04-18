# Writeas-Search

Make sure you have the latest version of the [Write.as API Library](https://github.com/cjeller1592/Writeas-API). 

This will not work on anything before version 0.1.7. 

---

All that is required is the **alias** of the collection you are searching and the **query**. 

The search is case insensitive (which might change). 

```
>>> posts = search('matt', 'golang')

>>> for post in posts:
      print(post['title'])
  
>>> How I built a multi-platform app
```

To see this integrated into a Flask app, go [here](https://wa-search.glitch.me).

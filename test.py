import requests

url = 'http://localhost:8080/post/deal'

for i in range(20):
    i = str(i)
    d = {
        'title' : 'hello test' + i,
        'author': 'robots',
        'content': 'it is a script-generated text' + i,
        'slug': 'robots' + i
    }
    r = requests.post(url, data=d)  # requests.post() 中利用 data 属性
    print(r.text)
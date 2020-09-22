from bottle import route, run, template, view, request, redirect, abort
import redis
import time
import json

import convert

r = redis.StrictRedis(decode_responses=True)

@route('/')
@view('index')
def index():
    order_by = request.query.order or '0'
    page = request.query.page or '1'
    page = int(page)
    posts_per_page = 10

    start = (page - 1) * posts_per_page
    end = page * posts_per_page - 1
    if order_by == '0':
        posts_id = r.lrange('posts:list', start, end)
    else:
        posts_id = r.zrevrange('posts:visited', start, end)

    post_list = {}
    for id in posts_id:
        post_data = r.hgetall('post:{}'.format(id))
        post_list[id] = post_data

    return dict(posts=post_list, page=page)

@route('/post/new')
@view('newpost')
def post_new():
    return dict()

@route('/post/deal', method='POST')
@view('newpost')
def post_deal():
    postid = r.incr("posts:count")

    title = request.forms.getunicode('title')
    content = request.forms.getunicode('content')
    author = request.forms.getunicode('author')
    slug = request.forms.getunicode('slug')
    ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    is_slug_available = r.hsetnx('slug.to.id', slug, postid)
    if not is_slug_available:
        return dict(tips='slug已经存在,请更换')

    post_data = {
        'title' : title,
        'content' : content,
        'author' : author,
        'ctime' : ctime,
        'slug' : slug
    }
    r.hmset('post:{}'.format(postid), post_data)
    r.lpush('posts:list', postid)
    redirect('/post/show/{}'.format(slug))

@route('/post/show/<slug>')
@view('showpost')
def post_show(slug):
    id = r.hget('slug.to.id', slug)
    if not id:
        abort(404, '文章不存在')    

    r.zincrby('posts:visited', 1, id)
    visit_times = int(r.zscore('posts:visited', id))
    post_data = r.hgetall('post:{}'.format(id))

    tags = r.smembers('post:{}:tags'.format(id))

    return dict(post_data = post_data, visit_times = visit_times, post_id=id, tags=tags)

@route('/tags/add', method='POST')
def tag_add():
    post_id = request.forms.getunicode('post_id').strip()
    tag = request.forms.getunicode('tag').strip()

    r.sadd('post:{}:tags'.format(post_id), tag)
    r.sadd('tag:{}:post'.format(tag), post_id)

    tags = r.smembers('post:{}:tags'.format(post_id))
    return dict(tags=[t for t in tags])

@route('/tag/show/<tag>')
@view('showtags')
def tag_show(tag):
    posts_id = r.smembers('tag:{}:post'.format(tag))

    post_list = {}
    for id in posts_id:
        post_data = r.hgetall('post:{}'.format(id))
        post_list[id] = post_data
    
    return dict(posts = post_list, tag = tag)

run(host='localhost',reloader=True, port=8080)
#!/usr/bin/env python
from itty import get, post, Redirect, run_itty

LOG = []
TEMPLATE = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>Party Time</title>
</head>
<body>
    <form action="/post_a/" method="post">
        <p><input type="submit" value="Post A"></p>
    </form>
    <form action="/post_b/" method="post">
        <p><input type="submit" value="Post B"></p>
    </form>
    <hr>
    %s
</body>
</html>
"""

def render_logs(logs):
    """returns html displaying log strings in ``logs``"""
    return TEMPLATE % (''.join('<p>' + x + '</p>' for x in logs))

@get('/')
def index(request):
    LOG.append('GET /')
    return render_logs(LOG)

@post('/post_a/')
def post_a(request):
    LOG.append('POST /post_a/')
    raise Redirect('/')

@post('/post_b/')
def post_b(request):
    LOG.append('POST /post_b/')
    raise Redirect('/')

run_itty()
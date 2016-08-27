
def route_index(request):
    """
    主页面
    """
    r = b'HTTP/1.x 200 FOUND\r\n\r\n<h1>Hello FOUND</h1>'

    return  r

routes = {
    '/':  route_index,
}

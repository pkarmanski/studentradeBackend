import threading


def background(f):
    def background_func(*a, **kw):
        threading.Thread(target=f, args=a, kwargs=kw).start()
    return background_func


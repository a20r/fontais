
import urllib
import urllib2
import json
import time
import threading


class HttpHeart(object):

    def __init__(self, ns_host, ns_port, route="/alive", data=None, delay=1):
        self.beat_url = self.get_beat_url(ns_host, ns_port)
        self.delay = delay  # second
        self.route = route
        self.beating = False
        if self.data is None:
            self.data = dict()

    def get_beat_url(self, ns_host, ns_port):
        ns_route = "http://{}:{}".format(ns_host, ns_port)
        return ns_route + self.route

    def beat(self):
        try:
            post_str = urllib.urlencode(self.data)
            req = urllib2.Request(self.beat_url, post_str)
            resp = urllib2.urlopen(req)
            return json.loads(resp.read())
        except urllib2.URLError:
            pass

    def live(self):
        while self.beating:
            self.beat()
            time.sleep(self.delay)

    def start(self):
        self.beating = True
        heart = threading.Thread(target=self.live)
        heart.daemon = True
        heart.start()

    def kill(self):
        self.beating = False


def make(*args, **kwargs):
    return HttpHeart(*args, **kwargs)

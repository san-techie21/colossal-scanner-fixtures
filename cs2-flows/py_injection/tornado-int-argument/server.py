import os

import tornado.web


class PingHandler(tornado.web.RequestHandler):
    def post(self):
        count = int(self.get_argument("count"))
        process = os.popen("ping -c " + str(count) + " 127.0.0.1")
        self.write(process.read())

import os

import tornado.web


class PingHandler(tornado.web.RequestHandler):
    def post(self):
        server = self.get_argument("server")
        process = os.popen("ping -c 3 " + server)
        self.write(process.read())

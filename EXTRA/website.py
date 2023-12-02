from twisted.web.server import Site
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.web.util import redirectTo


class WebSite(Resource):
    isLeaf = True

    def render_GET(self, request):
        content = b'''<html><body><p>Please enter your name before entering the site!</p>

                    <p>&nbsp;</p>

                    <form method="POST">
                    <p>Your username:</p>
                    <input name="username" type="text" />
                    <p>&nbsp;</p>
                    <input type="submit" value="ENTER">
                    <p>&nbsp;</p>
                    </form>
                    <p>ENTER TO LOGIN!</p> </body></html>'''


        return content

    def render_POST(self, request):
        return b'<html><body>Hello ' + request.args[b'username'][0] + b'''!

                <p>Welcome</p>
                <p>The Website is available at: http://mysite.com</p>
                <p>&nbsp;</p>

                </body></html>'''

listen_site = Site(WebSite())
reactor.listenTCP(8080, listen_site)
reactor.run()


from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
import subprocess
from twisted.python import log
log.startLogging(open('/var/log/name.log', 'a'))

class WebSite(Resource):
    isLeaf = True
    
    def render_GET(self, request):
        content = b'''cat greetings.txt | grep "''' + request.args[b'name'][0] + b'''" | awk -F"|" '{printf $2}' '''
        greeting = subprocess.check_output(content, shell=True)
        return b'<html><body>' + bytearray(greeting) + b' ' + request.args[b'name'][0] + b'!</body></html>'

listen_site = Site(WebSite())
reactor.listenTCP(8080, listen_site)
reactor.run()

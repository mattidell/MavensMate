import logging
import os.path
import sys
#handler = logging.FileHandler('/Users/josephferraro/Desktop/foo.log')
#handler = logging.FileHandler('')
logging.raiseExceptions = False
handler = logging.NullHandler()
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.INFO)
logging.getLogger('suds.client').propagate = False
logging.getLogger('suds.client').addHandler(handler) 
logger = logging.getLogger('mm')
logging.getLogger('mm').propagate = False 
logging.getLogger('mm').addHandler(handler)
logger.setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.ERROR)
# logging.getLogger('suds.transport.http').propagate = False
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)
# logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
# logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
def __get_base_path():
    if hasattr(sys, 'frozen'):
        # print sys._MEIPASS
        # print sys.executable
        # print os.path.dirname(sys.executable)
        # config.base_path = os.path.dirname(sys.executable)
        return sys._MEIPASS
    else:
        return os.path.dirname(os.path.dirname(__file__))

def __get_is_frozen():
    if hasattr(sys, 'frozen'):
        return True
    else:
        return False


frozen = __get_is_frozen()
base_path = __get_base_path()
connection = None
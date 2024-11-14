from logging import Formatter, StreamHandler, DEBUG, getLogger
import sys

formater = Formatter(fmt= '[%(asctime)s][%(levelname)s] %(message)s')
handler = StreamHandler(sys.stdout)
handler.setFormatter(formater)
handler.setLevel(DEBUG)
logger = getLogger('logger')
logger.setLevel(DEBUG)
logger.addHandler(handler)


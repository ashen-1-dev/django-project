import logging
import colorlog

logger = colorlog.getLogger()
logger.setLevel(colorlog.DEBUG)
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)
logging.basicConfig(format='%(levelname)s: %(message)s')

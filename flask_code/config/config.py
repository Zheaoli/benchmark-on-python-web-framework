import greenify
from gevent import monkey

greenify.greenify()


monkey.patch_all()
import multiprocessing


loglevel = "debug"

bind = "0.0.0.0:12345"

workers = 11

worker_class = "gevent"

timeout = 180

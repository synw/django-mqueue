import redis
import time
from mqueue.conf import DOMAIN
from mqueue.hooks.redis import serializer
from mqueue.conf import HOOKS

conf = HOOKS["redis"]
R = redis.StrictRedis(host=conf["host"], port=conf["port"], db=conf["db"])
event_num = int(time.time()) 

def save(event, conf):
    name = DOMAIN+"_event"+str(event_num)
    event.request = event.request.replace("\n", "//")
    data = serializer.Pack(event)  
    R.set(name, data)
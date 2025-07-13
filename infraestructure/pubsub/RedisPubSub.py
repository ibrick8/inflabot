import redis
import json
from settings import REDIS_HOST, REDIS_PORT, REDIS_CHANNEL
from domain.interfaces.IPubSub import IPubSub

class RedisPubSub(IPubSub):
    def __init__(self, ):
        self.conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        self.pubsub = self.conn.pubsub()
        self.pubsub.subscribe(REDIS_CHANNEL)

    def publish(self, evento: dict):
        self.conn.publish(REDIS_CHANNEL, json.dumps(evento))

    def listen(self):
        return self.pubsub.listen()
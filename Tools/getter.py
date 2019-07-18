from proxypool.db import RedisClient


class Getter():
    def __init__(self):
        self.redis = RedisClient()
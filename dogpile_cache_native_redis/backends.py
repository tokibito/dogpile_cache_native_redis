import time

from dogpile.cache.backends.redis import RedisBackend
from dogpile.cache.api import NO_VALUE, CachedValue
from dogpile.cache.region import value_version

__all__ = 'NativeRedisBackend',


class NativeRedisBackend(RedisBackend):
    def strip_value(self, value):
        return value.payload

    def wrap_value(self, value):
        return CachedValue(
            value,
            {
                'ct': time.time(),
                'v': value_version
            })

    def get(self, key):
        value = self.client.get(key)
        if value is None:
            return NO_VALUE
        return self.wrap_value(value)

    def get_multi(self, keys):
        if not keys:
            return []
        values = self.client.mget(keys)
        return [self.wrap_value(v) if v is not None else NO_VALUE for v in values]

    def set(self, key, value):
        if self.redis_expiration_time:
            self.client.setex(key, self.redis_expiration_time,
                              self.strip_value(value))
        else:
            self.client.set(key, self.strip_value(value))

    def set_multi(self, mapping):
        mapping = dict(
            (k, self.strip_value(v))
            for k, v in mapping.items()
        )

        if not self.redis_expiration_time:
            self.client.mset(mapping)
        else:
            pipe = self.client.pipeline()
            for key, value in mapping.items():
                pipe.setex(key, self.redis_expiration_time, value)
            pipe.execute()

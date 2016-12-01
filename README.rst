==========================
dogpile_cache_native_redis
==========================

Install
=======

Use pip::

   pip install dogpile_cache_native_redis

Usage
=====

See the example.

Code::

   from dogpile.cache import make_region

   region = make_region().configure(
       'native_redis',
       # arguments are same as redis backend.
       arguments = {
           'host': "127.0.0.1",
       }
   )

   region.set("test", b"value")
   region.set_multi({"key1": b"value1", "key2": 100})
   print(region.get("test"))
   print(region.get_multi(["key1", "key2"]))

Result::

   $ python main.py
   b'value'
   [b'value1', b'100']

See with redis-cli::

   $ redis-cli
   127.0.0.1:6379> get test
   "value"
   127.0.0.1:6379> mget key1 key2
   1) "value1"
   2) "100"

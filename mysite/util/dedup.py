import redis
import hashlib

r = redis.Redis()
key = "title_dedup"


def is_new_md5(m):
    return r.sismember(key, m)


def add_title_to_md5(m):
    md5 = hashlib.md5(m).hexdigest()
    return r.sadd(key, md5)

if __name__ == '__main__':
    print is_new_md5("abc")
def ensure_unicode(s):
    if isinstance(s, unicode):
        return s
    elif isinstance(s, str):
        return s.decode('utf-8')
    else:
        return s


def ensure_utf8(s):
    if isinstance(s, str):
        return s
    elif isinstance(s, unicode):
        return s.encode('utf-8')
    else:
        return s
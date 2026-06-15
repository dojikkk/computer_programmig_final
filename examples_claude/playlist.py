# playlist.py
# The DJ's Queue — a FIFO playlist module

def getPlaylist():
    """Create and return an empty playlist."""
    return []


def isEmpty(pl):
    """Return True if pl is empty, else False."""
    if pl == []:
        return True
    else:
        return False


def addSong(pl, song):
    pl.append(song)
    # TODO


def peek(pl):
    if isEmpty(pl):       # 비었으면 먼저 차단
        return None
    return pl[0]

def playNext(pl):
    if isEmpty(pl):       # 여기도 동일하게
        return None
    res = pl[0]
    del pl[0]
    return res


def copyPlaylist(pl):
    res = pl[:]
    return res
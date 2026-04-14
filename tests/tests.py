# -*- coding: utf-8 -*-
import itunes
import pytest

U2 = 'U2'
U2_ONE = 'One'
U2_ACHTUNGBABY = 'Achtung Baby (Deluxe Edition) [Remastered]' # 'Achtung Baby'

MUSIC_VIDEO_KIND = 'music-video'
SONG_KIND = "song"
COLLECTION_KIND = "collection"

U2_ONE_ID = 475391315 # Before it was 368617
U2_ACHTUNGBABY_ID = 475390461 # Before it was 368713
U2_ID = 78500

U2_URL = 'https://itunes.apple.com/us/artist/u2/id%s?uo=4' % U2_ID
U2_ACHTUNGBABY_URL = 'https://itunes.apple.com/us/album/achtung-baby-deluxe-edition/id%s?uo=4' % U2_ACHTUNGBABY_ID
U2_ONE_URL = 'https://itunes.apple.com/us/album/one/id%s?i=%s&uo=4' % (U2_ACHTUNGBABY_ID, U2_ONE_ID)

#SEARCHES
def test_search_track_kind():
    assert itunes.search_track('u2 achtung baby one')[0].get_type() == SONG_KIND

def test_search_album():
    assert itunes.search_album('u2 achtung baby')[0].get_type() == COLLECTION_KIND

def test_search_artist():
    assert itunes.search_artist('u2')[0].get_id() == U2_ID

def test_search_artist_store():
    U2_URL_ES = 'https://itunes.apple.com/es/artist/u2/id78500?l=en&uo=4'
    assert itunes.search_artist('u2', store='ES')[0].get_id() == U2_ID
    assert itunes.search_artist('u2', store='ES')[0].get_url() == U2_URL_ES

#LOOKUPS
def test_lookup_track():
    item = itunes.lookup(U2_ONE_ID)
    assert isinstance(item, itunes.Track)
    assert item.get_id() == U2_ONE_ID
    assert item.get_name() == U2_ONE

    assert item.get_album().get_id() == U2_ACHTUNGBABY_ID
    assert item.get_artist().get_id() == U2_ID

def test_lookup_album():
    item = itunes.lookup(U2_ACHTUNGBABY_ID)
    assert isinstance(item, itunes.Album)
    assert item.get_id() == U2_ACHTUNGBABY_ID
    assert item.get_name() == U2_ACHTUNGBABY

    assert item.get_artist().get_id() == U2_ID

def test_lookup_artist():
    item = itunes.lookup(U2_ID)
    assert isinstance(item, itunes.Artist)
    assert item.get_id() == U2_ID
    assert item.get_name() == U2

def test_lookup_notfound():
    UNKNOWN_ID = 0
    with pytest.raises(itunes.ServiceException):
        itunes.lookup(UNKNOWN_ID)

#METHODS
def test_artist_url():
    item = itunes.lookup(U2_ID)
    assert item.get_url() == U2_URL

def test_album_url():
    item = itunes.lookup(U2_ACHTUNGBABY_ID)
    assert item.get_url() == U2_ACHTUNGBABY_URL

def test_track_url():
    item = itunes.lookup(U2_ONE_ID)
    assert item.get_url() == U2_ONE_URL

def test_album_length():
    item = itunes.lookup(U2_ACHTUNGBABY_ID)
    assert len(item.get_tracks()) == 26 # 12)

def test_music_video_kind():
    item = itunes.lookup(U2_ID)
    assert item.get_music_videos()[0].get_type() == MUSIC_VIDEO_KIND

#TEXT: Unicode
def test_unicode():
    assert itunes.search_artist('Björk')[0].get_id() == itunes.search_artist(u'Bj\xf6rk')[0].get_id()

def test_unicode2():
    assert itunes.search_artist('Björk')[:5] == itunes.search_artist(u'Bj\xf6rk')[:5]

def test_movie_as_track():
    item = itunes.search(query='the godfather', media='movie')[0]
    assert item.get_artist() == None

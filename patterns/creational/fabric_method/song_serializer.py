import json
import xml.etree.ElementTree as et

# product
class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:

    # client
    def serialize(self, song, format):
        serialized = get_serializer(format)
        return serialized(song)


# creator
def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)


# concrete action on product object
def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)


# concrete action on product object
def _serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')



# app
song = Song('1', 'Water of Love', 'Dire Straits') # concrete PRODUCT

serialized_json = SongSerializer().serialize(song, 'JSON') # use CLIENT to make CREATOR do concrete serialization(JSON) on PRODUCT
print(serialized_json)

serialized_xml = SongSerializer().serialize(song, 'XML') # use CLIENT to make CREATOR do concrete serialization(XML) on PRODUCT
print(serialized_xml)


# app -> client -> creator -> concrete action on product object
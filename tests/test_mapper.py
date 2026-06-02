from domain.mapper import( map_track_payload,
    map_recent_tracks
)
from domain.models import Track

def test_map_track_playload_returns_normalized_track():
    playload = {
        'name': 'Long Long Road',
        'artist': {
            '#text': 'Ringo Starr'
        },
        'album': {
            '#text': 'Long Long Road'
        },
        'image': [
            {'#text': 'https://lastfm.freetls.fastly.net/i/u/34s/ebb60fab27897bad30c666a9627e2c2b.jpg'},
            {'#text': 'https://lastfm.freetls.fastly.net/i/u/64s/ebb60fab27897bad30c666a9627e2c2b.jpg'},
            {'#text': 'https://lastfm.freetls.fastly.net/i/u/174s/ebb60fab27897bad30c666a9627e2c2b.jpg'},
            {'#text':'https://lastfm.freetls.fastly.net/i/u/300x300/ebb60fab27897bad30c666a9627e2c2b.jpg'},
        ],
        'date': {
            "#text": "27 May 2026, 11:29"
        }

    }
    result = map_track_payload(playload)

    assert all([
        result.track == "Long Long Road",
        result.artist == "Ringo Starr",
        result.album == "Long Long Road",
        result.track_key == "long long road-ringo starr",
        result.played_at == "27 May 2026, 11:29",
        result.cover_image == "https://lastfm.freetls.fastly.net/i/u/300x300/ebb60fab27897bad30c666a9627e2c2b.jpg"
    ])

# Тест для функции map_recent_tracks, который проверяет,
#  что она возвращает список треков из recenttracks.track в полезной нагрузке
def test_map_recent_tracks_returns_track_list():

    payload = {

        "recenttracks": {

            "track": [

                {
                    "name": "All That Goes Around"
                },

                {
                    "name": "Still Waiting"
                }
            ]
        }
    }

    result = (
        map_recent_tracks(
            payload
        )
    )

    assert len(result) == 2

    assert result[0]["name"] == (
        "All That Goes Around"
    )

def test_should_map_Played_at():
    payload = {
        'name': 'Long Long Road',

        'artist': {
            '#text': 'Ringo Starr'
        },

        'album': {
            '#text': 'Long Long Road'
        },

        "date": {
             "#text": "26 May 2026, 21:00"
        }
    }


    result = (
        map_track_payload(
            payload
        )
    )
    assert result.played_at == "26 May 2026, 21:00"

def test_should_map_Cover_image():
    payload = {
        'name': 'Long Long Road',
        
        'artist': {
            '#text': 'Ringo Starr'
        },

        'album': {
            '#text': 'Long Long Road'
        },

        "date": {
             "#text": "26 May 2026, 21:00"
        },

        'image': [
            {},
            {},
            {},
            {   
                "#text": 
                    "https://lastfm.freetls.fastly.net/i/u/300x300/d52df9b1ecc01cd5da0530322198f8d1.jpg"
            }
        ]
    }


    result = (
        map_track_payload(
            payload
        )
    )
    assert result.cover_image == "https://lastfm.freetls.fastly.net/i/u/300x300/d52df9b1ecc01cd5da0530322198f8d1.jpg"

def test_should_map_without_album():
    payload = {
        'name': 'Long Long Road',
        
        'artist': {
            '#text': 'Ringo Starr'
        },

        "date": {
             "#text": "26 May 2026, 21:00"
        },

        'image': [
            {},
            {},
            {},
            {   
                "#text": 
                    "https://lastfm.freetls.fastly.net/i/u/300x300/d52df9b1ecc01cd5da0530322198f8d1.jpg"
            }
        ]
    }


    result = (
        map_track_payload(
            payload
        )
    )
    assert result.album is None

def test_should_map_without_image():
    payload = {
        'name': 'Long Long Road',
        
        'artist': {
            '#text': 'Ringo Starr'
        },

        'album': {
            '#text': 'Long Long Road'
        },

        "date": {
             "#text": "26 May 2026, 21:00"
        }
    }


    result = (
        map_track_payload(
            payload
        )
    )
    assert result.cover_image is None

def test_should_normalize_track_key():

    payload = {

        "name": " NUMB ",

        "artist": {
            "#text": " Linkin Park "
        }
    }

    result = (
        map_track_payload(
            payload
        )
    )

    assert result.track_key == (
        "numb-linkin park"
    )

def test_should_fail_with_empty_artist():
    payload = {

        "name": " NUMB ",

        "artist": {
            "#text": ""
        }
    }

    result = ( map_track_payload(payload) ) 

    assert result.artist == ""
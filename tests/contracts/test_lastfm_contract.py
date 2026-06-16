import pytest

from domain.errors import InvalidTrackNameError

from domain.mapper import map_track_payload

# Проверка: Last.fm не всегда возвращает поле artist. Маппер должен отклонить обработку трека
def test_should_require_artist_name():
    payload = {
                "name": "Numb"
            }

    with pytest.raises(KeyError):
        map_track_payload(payload)

# Проверка: Last.fm не всегда возвращает поле name. Маппер должен отклонить обработку трека
def test_should_require_track_name():
    
    payload = {
                "artist": {
                    "#text": "Linkin Park"
                }
            }

    with pytest.raises(KeyError):
        map_track_payload(payload)

# Album — необязательное поле в контракте Last.fm. Track должен создаться успешно
def test_should_accept_missing_album():
    
    payload = {
                "name": "Numb",
                "artist": {
                    "#text": "Linkin Park"
                }
            }

    track = (
        map_track_payload(
            payload
            )
    )

    #Track должен создаться успешно

    assert track.album is None

    assert track.track == "Numb"

    assert track.artist == "Linkin Park"

# Cover image — необязательное поле в контракте Last.fm. Track должен создаться успешно
def test_should_accept_missing_cover_image():
    
    payload = {
                "name": "Numb",
                "artist": {
                    "#text": "Linkin Park"
                }
            }

    track = (
        map_track_payload(
            payload
            )
    )

    #Track должен создаться успешно

    assert track.cover_image is None

    assert track.track == "Numb"

    assert track.artist == "Linkin Park"

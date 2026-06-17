import os
import pytest

from infrastructure.lastfm_client import LastFMClient

from domain.mapper import map_track_payload

# .env для локальной проверки берём os.getenv
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.integration
def test_should_fetch_recent_tracks_from_lastfm():

    client = LastFMClient (
        api_key = os.getenv(
            "LASTFM_API_KEY"
        ),

        user = os.getenv(
            "LASTFM_USER"
        )
    )


    result = (
        client.get_recent_tracks()
    )

    # Структура ответа может измениться, 
    # поэтому мы проверяем наличие ключа 'recenttracks' в ответе
    assert (
        'recenttracks' in result
    )
    
    # и что список треков не пустой, а не конкретные значения
    assert (
        len(
            result[
                'recenttracks'
            ][
                'track'
            ]
        ) > 0
    )

@pytest.mark.integration
# Integration + Contract test - проверяем, что ответ содержит все необходимые поля для маппера, 
# а не конкретные значения
def test_should_map_real_lastfm_payload():

    # Arrange

    client = LastFMClient (
        api_key = os.getenv(
            "LASTFM_API_KEY"
        ),

        user = os.getenv(
            "LASTFM_USER"
        )
    )

    # Act

    response = (
        client.get_recent_tracks()
    )

    payload = (
        response[
            "recenttracks"
        ][
            "track"
        ][0]
    )

    track = (
        map_track_payload(
            payload
        )
    )

    # Assert

    assert track.track != ""
    assert track.artist != ""
    assert track.track_key != ""
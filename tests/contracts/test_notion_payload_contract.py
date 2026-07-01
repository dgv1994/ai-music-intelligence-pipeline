from domain.models import Track

from application.notion_payload_builder import build_notion_payload

# проверка серелизации данных в Notion
def test_should_create_valid_notion_payload():

    track = Track(
        track="Numb",
        artist="Linkin Park",
        album="Meteora",
        track_key="numb-linkin park"
    )

    payload = (
        build_notion_payload(
            track
        )
    )

    assert payload == {
        "Track": "Numb",
        "Artist": "Linkin Park",
        "Track Key": "numb-linkin park"
    }

# проверка обязательного поля
def test_should_include_track_key_in_payload():

    track = Track(
        track="Numb",
        artist="Linkin Park",
        album="Meteora",
        track_key="numb-linkin park"
    )

    payload = (
        build_notion_payload(
            track
        )
    )

    assert (
        "Track Key"
        in payload
    )

def test_should_include_track_name_in_payload():
    
    track = Track(
        track="Numb",
        artist="Linkin Park",
        album="Meteora",
        track_key="numb-linkin park"
    )

    payload = (
        build_notion_payload(
            track
        )
    )

    assert "Track" in payload

def test_should_include_artist_in_payload():
    
    track = Track(
        track="Numb",
        artist="Linkin Park",
        album="Meteora",
        track_key="numb-linkin park"
    )

    payload = (
        build_notion_payload(
            track
        )
    )

    assert "Artist" in payload
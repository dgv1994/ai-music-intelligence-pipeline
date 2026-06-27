from event_contracts.events import TrackCreatedEvent

# проверка сериализации
def test_should_serialize_track_created_event():
    event = TrackCreatedEvent(
        track_key="numb-linkin park",
        track="Numb",
        artist="Linkin Park"
    )

    payload = event.model_dump()

    assert payload == {
        "track_key": (
            "numb-linkin park"
        ),
        "track": (
            "Numb"
        ),
        "artist": (
            "Linkin Park"
        )
    }

# проверка создания события

def test_should_require_track_created_event_fields():

    event = TrackCreatedEvent(
        track_key="numb-linkin park",
        track="Numb",
        artist="Linkin Park"
    )

    payload = (
        event.model_dump()
    )

    assert "track_key" in payload
    assert "track" in payload
    assert "artist" in payload


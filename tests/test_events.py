from event_contracts.events import TrackCreatedEvent


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
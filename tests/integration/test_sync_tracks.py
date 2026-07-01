
import os

from application.track_service import TrackService
from infrastructure.lastfm_client import LastFMClient
from infrastructure.sqlite_repository import SQLiteTrackRepository

def test_should_import_recent_tracks():

    repository = SQLiteTrackRepository(":memory:")

    client = LastFMClient(
        api_key=os.getenv("LASTFM_API_KEY"),
        user=os.getenv("LASTFM_USER")
    )

    service = TrackService(
        repository,
        client
    )

    service.sync_recent_tracks()

    tracks = repository.get_all()

    assert len(tracks) > 0
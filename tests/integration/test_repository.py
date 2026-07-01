
from domain.models import Track
from infrastructure.sqlite_repository import SQLiteTrackRepository


def test_should_save_track():

    repository = SQLiteTrackRepository(":memory:")

    track = Track(...)

    repository.save(track)

    saved = repository.get_all()

    assert saved[0].track == "Numb"
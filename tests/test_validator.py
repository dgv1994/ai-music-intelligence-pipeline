import pytest

from unittest.mock import (
    Mock
)

from domain.errors import (
    DuplicateTrackError,
    InvalidTrackNameError,
    InvalidArtistError
)

from domain.validator import (
    validate_track_uniqueness,
    validate_track_name,
    validate_artist_name
)

from domain.models import (
    Track
)

def test_should_raise_duplicate_error_when_track_exists():

    repository = Mock()

    repository.exists.return_value = (
        True
    )

    track = Track(
        track="Numb",
        artist="Linkin Park",
        album="Meteora",
        track_key="numb-linkin park"
    )

    with pytest.raises(
        DuplicateTrackError
    ):

        validate_track_uniqueness(
            repository,
            track
        )

# параметризация для проверки различных невалидных названий трека
@pytest.mark.parametrize(
    'track_name',
    [
        "",
        "   ",
        None
    ]
)

def test_should_reject_invalid_track_name(
    track_name
):

    track = Track(
        track=track_name,
        artist="Linkin Park",
        album="Meteora",
        track_key="numb-linkin park"
    )

    with pytest.raises(
        InvalidTrackNameError
    ):

        validate_track_name(
            track
        )
        
def test_should_reject_empty_track_name():

    track = Track(
        track="",
        artist="Linkin Park",
        album="Meteora",
        track_key="numb-linkin park"
    )

    with pytest.raises(
        InvalidTrackNameError
    ):

        validate_track_name(
            track
        )

def test_should_reject_empty_artist():
    
    track = Track(
        track="Numb",
        artist="",
        album="Meteora",
        track_key="numb-linkin park"
    )

    with pytest.raises(
        InvalidArtistError
    ):

        validate_artist_name(
            track
        )    
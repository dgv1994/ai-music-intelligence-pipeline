import pytest

from unittest.mock import (
    Mock
)

from domain.errors import (
    DuplicateTrackError
)

from domain.validator import (
    validate_track_uniqueness
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
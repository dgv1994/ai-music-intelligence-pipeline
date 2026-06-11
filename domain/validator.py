from domain.errors import (
    DuplicateTrackError,
    InvalidTrackNameError,
    InvalidArtistError
)


def validate_track_uniqueness(
    repository,
    track
):

    if repository.exists(
       track.track_key
    ):

        raise (
            DuplicateTrackError()
        )

    return True

def validate_track_name(
    track
):

    # Treat None, empty string and whitespace-only strings as invalid
    value = track.track
    if value is None or not str(value).strip():
        raise (
            InvalidTrackNameError()
        )

    return True

def validate_artist_name(
    track
):

    # Treat None, empty string and whitespace-only strings as invalid
    value = track.artist
    if value is None or not str(value).strip():
        raise (
            InvalidArtistError()
        )

    return True
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

    if not track.track:

        raise (
            InvalidTrackNameError()
        )

    return True

def validate_artist_name(
    track
):

    if not track.artist:

        raise (
            InvalidArtistError()
        )

    return True
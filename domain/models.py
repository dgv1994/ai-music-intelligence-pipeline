class Track:

    def __init__(
        self,
        track,
        artist,
        album,
        track_key,
        played_at=None,
        cover_image=None
    ):

        self.track = track

        self.artist = artist

        self.album = album

        self.track_key = (
            track_key
        )

        self.played_at = (
            played_at
        )

        self.cover_image = (
            cover_image
        )
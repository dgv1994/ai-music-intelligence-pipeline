from domain.models import (
    Track
)

def map_recent_tracks(
    payload
):

    return payload[
        "recenttracks"
    ][
        "track"
    ]

def map_track_payload(
    track
):

    return Track(

        track=(
            track["name"]
        ),

        artist=(
            track["artist"]["#text"]
        ),

        album=(
            track.get(
                "album",
                {}
            ).get(
                "#text"
            )
        ),

        track_key=(

            track["name"]
            .lower()
            .strip()

            + "-"

            + track["artist"]["#text"]
            .lower()
            .strip()
        ),

        played_at=(
            track.get(
                "date",
                {}
            ).get(
                "#text"
            )
        ),

        cover_image=(
            track.get(
                "image",
                [{}]
            )[-1].get(
                "#text"
            )
        )
    )


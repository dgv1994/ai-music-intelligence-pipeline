from domain.models import (
    Track
)
# загрузка всех треков
def map_recent_tracks(
    payload
):

    return payload[
        "recenttracks"
    ][
        "track"
    ]

# загрузка одного трека как доменную модель Track
# и нормализация его track_key
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


from domain.mapper import (
    map_recent_tracks,
    map_track_payload
        
)

from domain.validator import (
    validate_track_uniqueness,
    validate_track_name,
    validate_artist_name
)   


# Сервис, который использует репозиторий для проверки существования трека
class TrackService:
    # Иницилизация сервиса с репозиторием
    # по контракту (exists, save должны соблюдаться)
    # Иницилизация сервиса с клиентом Last.fm
    # по контракту (get_recent_tracks должен соблюдаться)
    def __init__(
        self,
        repository,
        lastfm_client
    ):

        self.repository = (
            repository
        )

        self.lastfm_client = (
            lastfm_client
        )

    # Метод, который получает недавние треки пользователя с 
    # помощью клиента Last.fm,
    # и сохраняет их в репозитории, если они не существуют
    def sync_new_track(
            self
    ):
        
        payload = (
            self.lastfm_client
            .get_recent_tracks()
        )

        tracks= (
            map_recent_tracks(
                payload
            )
        )
    
        created_tracks = []

        for track in tracks:

            mapped_track = (
                map_track_payload(
                    track
                )
            )
            
            validate_track_name(
                mapped_track
            )

            validate_artist_name(
                mapped_track
            )

            validate_track_uniqueness(
                self.repository,
                mapped_track
            )

            self.repository.save(
                mapped_track
            )

            created_tracks.append(
                mapped_track
            )

        return created_tracks

    # Метод, который проверяет, существует ли трек в репозитории по ключу,
    def sync_duplicate(
        self,
        track
    ):

        validate_track_uniqueness(
            self.repository,
            track
        )

        return True
    
    # Метод, который возвращает обложку трека, если она есть, иначе None
    def sync_cover(
        self,
        track
    ):

        return track.cover_image
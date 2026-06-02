from abc import (
    ABC,
    abstractmethod
) # создает абстрактные классы и методы, которые должны быть реализованы в подклассах

# Универсальный интерфейс для репозитория треков,
#  который может быть реализован
#  для различных хранилищ данных (например, Notion, SQL, etc.)
class ITrackRepository(
    ABC
):

    @abstractmethod # флаг, показывающий, что нельзя Repository без exists
    # метод, обращающийся к репозиторию для проверки существования трека по ключу
    def exists(
        self,
        track_key
    ):
        pass
    # метод, обращающийся к репозиторию для сохранения трека
    @abstractmethod # и save
    def save(
        self,
        track
    ):
        pass

# Универсальный интерфейс для клиента Last.fm,
#  который может быть реализован для различных
#  способов получения данных (например, API, web scraping)
class ILastFmClient(
    ABC
):
    # метод, обращающийся к Last.fm для получения недавних треков пользователя
    @abstractmethod
    def get_recent_tracks(
        self
    ):
        pass
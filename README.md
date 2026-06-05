
# AI Music Intelligence Pipeline

Автоматизированный пайплайн синхронизации музыкальных данных между Last.fm и Notion с использованием принципов Domain-Driven Design, Test Automation и CI/CD.

## Project Overview

Проект получает данные о прослушанных треках из Last.fm API, преобразует их в доменную модель, валидирует бизнес-правила и сохраняет результаты в Notion Database.

Основная цель проекта — продемонстрировать навыки:

- Python
- Pytest
- Test Automation
- Domain Modeling
- CI/CD
- GitHub Actions
- Requirements Traceability
- API Testing

## Architecture
The project follows Vladimir Khorikov's principles of testable architecture.

- Domain logic is isolated from infrastructure.
- External dependencies are accessed through contracts.
- Application Service coordinates use cases.
- Unit tests validate domain rules.
- Module tests validate application behavior.

<p align="center">
  <img src="docs/architecture.png" width="900">
</p>

## Testing Strategy

Проект построен с использованием рекомендаций Владимира Хорикова по тестируемой архитектуре.

### Unit Tests

Проверяют отдельные доменные правила.

Примеры:

- test_should_reject_empty_track_name
- test_should_reject_empty_artist
- test_should_raise_duplicate_error_when_track_exists
- test_map_track_payload_returns_normalized_track
- test_should_normalize_track_key

Покрываемые компоненты:

- Mapper
- Validator
- Domain Rules

### Module Tests

Проверяют поведение Application Service.

Примеры:

- test_should_sync_new_track
- test_should_sync_multiple_tracks
- test_should_not_save_duplicate_track
- test_should_sync_track_without_album

Покрываемые компоненты:

- TrackService
- Repository Contract
- LastFm Contract

## CI/CD

GitHub Actions автоматически выполняет:

- Checkout Repository
- Install Dependencies
- Run Pytest
- Generate JUnit Report

Workflow запускается при каждом push в master.

## Requirements Traceability Matrix

Трассировка требований ведётся в Notion.

Связи:

User Story → Test Case → Pytest Test → CI Result

Пример:

UStory JSON Processing
↓
TS-T22
↓
test_map_track_payload_returns_normalized_track
↓
GitHub Actions
↓
PASS

##  Documentation

- User Stories
- - RTM
- Test Strategy
- Architecture
- Glossary
- Meeting Notes

Документация проекта ведётся в Notion.
[https://www.notion.so/AI-Music-Intelligence-Pipeline-3739f31d991b80379464ee6d12c3f1a2?source=copy_link]

## Repository Structure

application/
├── track_service.py

domain/
├── models.py
├── mapper.py
├── validator.py
├── contracts.py
├── errors.py

tests/
├── test_mapper.py
├── test_validator.py
├── test_track_service.py

.github/
└── workflows/
    └── tests.yml

## Технологии

- Python
- Pytest
- Git
- GitHub
- GitHub Actions
- Notion
- Last.fm API
- n8n

## Author

Dmitriy G.
QA Automation Portfolio Project

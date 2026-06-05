
## AI Music Intelligence Pipeline

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

## Тестирование

### Unit Tests

- Mapper
- Validator

### Module Tests

- TrackService

## Технологии

- Python
- Pytest
- Notion
- n8n
- Zephyr Scale

## Запуск тестов

```bash
pytest
```

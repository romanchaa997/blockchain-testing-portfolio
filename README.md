# Портфолио тест-кейсов для тестирования смарт-контрактов

## Описание проекта

Этот проект содержит набор автоматизированных тестов для проверки функциональности, безопасности и производительности смарт-контрактов на Ethereum. Тесты разработаны с использованием Python, Web3.py, Pytest, solcx, Ganache и Slither. Проект демонстрирует:
- Функциональное тестирование (развертывание контракта, проверка методов `set()` и `get()`, граничные условия)
- Негативное тестирование (откат транзакции при недопустимых входных данных)
- Нагрузочное тестирование (анализ производительности и расхода газа)
- Статический анализ безопасности с помощью Slither

## Используемые технологии

- **Python 3.x**
- **Web3.py** – для взаимодействия с Ethereum
- **Pytest** – для написания автотестов
- **solcx** – для компиляции Solidity-контрактов
- **Ganache** – локальная тестовая сеть для быстрого тестирования
- **Slither** – инструмент статического анализа смарт-контрактов
- **Infura** – (опционально) для интеграционного тестирования с публичными тестовыми сетями (например, Sepolia)

## Структура проекта

# Портфолио тест-кейсов для тестирования смарт-контрактов

## Описание проекта

Этот проект содержит набор автоматизированных тестов для проверки функциональности, безопасности и производительности смарт-контрактов на Ethereum. Тесты разработаны с использованием Python, Web3.py, Pytest, solcx, Ganache и Slither. Проект демонстрирует:
- Функциональное тестирование (развертывание контракта, проверка методов `set()` и `get()`, граничные условия)
- Негативное тестирование (откат транзакции при недопустимых входных данных)
- Нагрузочное тестирование (анализ производительности и расхода газа)
- Статический анализ безопасности с помощью Slither

## Используемые технологии

- **Python 3.x**
- **Web3.py** – для взаимодействия с Ethereum
- **Pytest** – для написания автотестов
- **solcx** – для компиляции Solidity-контрактов
- **Ganache** – локальная тестовая сеть для быстрого тестирования
- **Slither** – инструмент статического анализа смарт-контрактов
- **Infura** – (опционально) для интеграционного тестирования с публичными тестовыми сетями (например, Sepolia)

## Структура проекта

blockchain-testing-portfolio/ ├── README.md ├── requirements.txt ├── contracts/ │ ├── SimpleStorage.sol │ └── SimpleStorageV2.sol ├── tests/ │ ├── test_contract.py │ ├── test_integration.py │ └── test_negative.py └── docs/ ├── STATIC_ANALYSIS.md └── NEGATIVE_TESTS.md

## Установка

1. **Клонируйте репозиторий:**

   ```sh
   git clone git@github.com:romanchaa997/blockchain-testing-portfolio.git
Перейдите в директорию проекта:

sh
Копировать
cd blockchain-testing-portfolio
Установите зависимости:

sh
Копировать
pip install -r requirements.txt
(Опционально) Для статического анализа:
Установите Slither (если не установлен):

sh
Копировать
pip install slither-analyzer
Если вы используете WSL или виртуальное окружение, убедитесь, что все зависимости установлены в нужном окружении.

## Запуск тестов
# Локальные тесты
Для запуска всех автотестов выполните:

sh
Копировать
pytest -v
# Интеграционные тесты
Чтобы проверить подключение к сети Sepolia через Infura, отредактируйте файл tests/test_integration.py, заменив YOUR_INFURA_API_KEY на ваш ключ, и выполните:

sh
Копировать
pytest -v
# Статический анализ
Для проверки смарт-контракта с помощью Slither выполните:

sh
Копировать
slither contracts/SimpleStorage.sol

## Тест-кейсы
## Функциональное тестирование
test_deployment: Проверяет, что контракт успешно разворачивается и получает корректный адрес.
test_set_and_get: Проверяет корректность работы методов set() и get().
test_default_value: Проверяет, что значение по умолчанию равно 0.
test_set_max_value: Устанавливает максимально возможное значение (2**256 - 1) и проверяет корректность его возврата.
Негативное тестирование
В контракте SimpleStorageV2.sol реализована функция set() с проверкой, что значение не должно превышать 1000.

test_set_too_high (в файле test_negative.py): Проверяет, что при попытке установить значение больше 1000 транзакция откатывается и возвращается ошибка "Value too high".
Подробнее см. docs/NEGATIVE_TESTS.md.

## Нагрузочное тестирование
test_load_set_extended: Выполняет большое число транзакций для функции set() и измеряет время выполнения, а также средний расход газа.
Интеграционное тестирование
test_infura_connection (в файле test_integration.py): Проверяет подключение к публичной тестовой сети (например, Sepolia через Infura) и получает текущий номер блока.
Статический анализ
Для проверки безопасности смарт-контрактов использовался Slither.
Подробные результаты анализа находятся в docs/STATIC_ANALYSIS.md.

Контактная информация
Если у вас есть вопросы, пишите: your.email@example.com

Лицензия
Этот проект распространяется под лицензией MIT.

# Makefile
install: # Установка зависимостей и виртуального окружения
	poetry install

gendiff: # Запуск скрипта пакета gendiff
	poetry run gendiff

build: # Сборка пакета
	poetry build

publish: # Отладка публикации
	poetry publish --dry-run

package-install: # Установка пакета из файла whl
	python3 -m pip install --user dist/*.whl

lint: # Запуск линтера на проверку директории gendiff
	poetry run flake8 gendiff

test: # Проверка тестов с помощью pytest
	poetry run pytest

coverage: # Проверка покрытия тестами
	poetry run pytest --cov=gendiff


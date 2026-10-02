from dynaconf import Dynaconf

from definitions import BASE_FOLDER

# pip isntall dynaconf
d_settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[BASE_FOLDER / ".settings.toml", BASE_FOLDER / ".secrets.toml"],
    environments=True,
    load_dotenv=True,
)

# https://www.dynaconf.com/
# 1) pip isntall dynaconf - сама бібліотека
# 2) порписуємо шлях до файлів в settings_files
# 3) все інше лишаємо як є
# 4) Створюємо settings_files, дивись формат .settings.toml в корені репозиторія
# 5) створити файл .env( з точкою перед іменем) в якомму буде змінна ENV_FOR_DYNACONF=dev

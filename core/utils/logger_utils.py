import logging
import sys

# Створення логера
internal_function_logger = logging.getLogger('internal_function')


# Налаштування рівня логування
internal_function_logger.setLevel(logging.DEBUG)

# Створення обробника для запису в файл
file_handler = logging.FileHandler('internal_function_logger.txt')
file_handler.setLevel(logging.INFO)

file_handler_critical = logging.FileHandler('internal_function_logger_critical.txt')
file_handler_critical.setLevel(logging.CRITICAL)

cli_handler = logging.StreamHandler()
cli_handler.setLevel(logging.DEBUG)

# Створення форматера для обробників
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)

formatter_cli = logging.Formatter('%(funcName)s - %(levelname)s: %(message)s')
cli_handler.setFormatter(formatter_cli)

# Додавання обробників до логера
internal_function_logger.addHandler(file_handler)
internal_function_logger.addHandler(file_handler_critical)
internal_function_logger.addHandler(cli_handler)
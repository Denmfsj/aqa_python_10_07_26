

import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


name = 'Ihor'
st = 'qweqweeqw'
log_event(username=name, status=st)
# піти і перевірити останній рядок,
# він повинен закінчуватись на  f"Login event - Username: {username}, Status: {status}"

expected_row = f"Login event - Username: {name}, Status: {st}"
with open('login_system.log') as f:
    last_row = f.readlines()[-1]

print(last_row)
is_correct = expected_row  in last_row
print(is_correct)


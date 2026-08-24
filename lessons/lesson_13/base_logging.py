

import logging


# Налаштування конфігурації логування
logging.basicConfig(filename='example.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.debug('Це повідомлення рівня DEBUG')
logging.info('Це повідомлення рівня INFO')

logging.warning('Це повідомлення рівня WARNING')

logging.error('Це повідомлення рівня ERROR')
logging.critical('Це повідомлення рівня CRITICAL')


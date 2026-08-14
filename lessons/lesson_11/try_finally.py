


def open_connection(raise_error=False):
    if raise_error:
        raise ConnectionError
    print('Opening connection ....')

def close_connection():
    print('Closing connection ....')

def execute_query(raise_error=False):

    if raise_error:
        raise TypeError('Error during execution ')

    print('Executing ....')


connection_is_open = False

try:
    open_connection()  # precondition

    # test body
    connection_is_open = True
    execute_query(raise_error=True)

finally:   # post condition
    if connection_is_open:
        close_connection()
#
# try:
#     open_connection()
# finally:
#     print('cant connect')
#
# try:
#     # test body
#     execute_query(raise_error=True)
# finally:   # post condition
#     close_connection()
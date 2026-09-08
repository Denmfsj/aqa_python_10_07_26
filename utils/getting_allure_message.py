import os


def get_failed_result_from_allure_report(path_to_allure):
    pass


def generate_error_message(data):
    pass


def write_error_message_to(message, path_ot_write):
    pass



if __name__ == '__main__':

    allure_data = get_failed_result_from_allure_report('allure-results')
    error_message = generate_error_message(allure_data)
    write_error_message_to(error_message, os.environ('path_to_allure_msg_error'))
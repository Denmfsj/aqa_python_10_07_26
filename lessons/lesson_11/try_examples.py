


def _checking_percent_cacl(list_of_items):


    for company in list_of_items:

        cid = company.id

        analys_data = send_request(...)

        percent_expected = analys_data['total_market_cap_percent']
        actual_percent = analys_data['raw_market_cap'] / company['count_of_smth']

        if percent_expected != actual_percent:
            raise AssertionError('actual != expected')  # Викликає AssertionError



try:
    _checking_percent_cacl([])

except AssertionError as e:
    raise e

except ZeroDivisionError as e:
    print(f'Division by zero\n{e}')

except TypeError as e:
    print(f'Some value are not numbers\n{e}')

except KeyError as e:
    print(f'Some value are not exists\n{e}')

except Exception as e:
    print(f'Smth went wrong\n{e}')


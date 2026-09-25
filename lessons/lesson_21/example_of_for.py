def get_score_of_smth(n):

    if n == 'apple':
        return 1

    elif n == 'samsung':
        return 2

    elif n == 'xiaomi':
        return 3

    else:
        return 4


def get_brand_by_model_name(model_name):

    def is_it_apple(name):
        if name.starstwith('apple'):
            return True, 'apple'
        return False

    def is_it_samsung(name):
        if name.starstwith('samsung'):
            return True, 'samsung'
        return False

    for k in [is_it_apple, is_it_samsung]:
        is_true, name = k(model_name)
        if is_true:
            return name

def get_score_of_n_v2(phone_name):


    scores ={
        'apple' : 1,
        'samsung' : 2,
        'xiaomi' : 3
    }

    return scores.get(get_brand_by_model_name(phone_name))







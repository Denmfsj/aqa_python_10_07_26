


for n in [1,2,0,6]:
    try:
        print(10/ n)  # основне тіло де ми очікуємо помилку

    except ZeroDivisionError:  #Перехоплення конкретної помилки
        print('0.0')

    else:  # буде виконано ЯКЩО НЕМА помилок
        print('NO errors appears')

    finally: #  буде виконано завжди
        print('-'*80)

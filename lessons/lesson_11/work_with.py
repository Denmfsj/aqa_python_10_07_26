import os

file = None
try:
    # Відкриття файлу для читання
    file = open("example.txt", "r")

    print(file)
    # Операції змістом файлу

    file_data = file.read()
    print(file_data)

except Exception as e:  # Вловлювання помилки та збереження її у змінну e
    print(f"Виникла помилка: {e}")
finally:
    # Закриття файлу у блоку finally, щоб гарантувати його виклик навіть якщо виникає помилка
    if file is not None:
        file.close()


with open("example.log", "w") as file:      # менеджер контексту
    file.write('My data')



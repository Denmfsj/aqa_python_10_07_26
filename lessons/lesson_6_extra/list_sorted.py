

words = ["яблуко", "апельсин", "банан", "груша", "слива"]

# Сортування за довжиною рядків
sorted_words = sorted(words, key=lambda x: len(x))
# len(яблуко) = 6, len(апельсин) = 8, len(банан) =5,...


sorted_words_by_a_letter = sorted(words, key=lambda x: x.count('а'))
print(sorted_words_by_a_letter)



numbers = [1,5,4,3,7,8]
numbers.sort()  # сміє порівнювати числа і переставляти елемети відповідно до цього порівнняння

print(numbers)
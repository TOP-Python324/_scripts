text = input("Введите текст: ")
text_words = text.replace(' ', '')
words = len(text_words)
price = words * 30

print(f'{(price) // 100} руб. {(price) % 100} коп.')

#Введите текст: Как сказала бы кровь здорового человека: "Пора сворачиваться"
#16 руб. 20 коп.



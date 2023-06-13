symb = '.,:;!?–—\'\"()*/'
text_ls = [c for c in input("Введите текст: ") if c not in symb]
text_str = "".join(text_ls)
print(text_str)

#Введите текст: "Блин!" - сказал слон, наступив на Колобка.
#Блин - сказал слон наступив на Колобка
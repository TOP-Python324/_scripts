def test_data(data: list) -> 'callable':
    results = []
    def decorator(func_obj: 'callable') -> 'callable':
        def wrapper():
            for elem in data:
                results.append(func_obj(elem))
            return results
        return wrapper
    return decorator


text = '!float also accepts the strings "nan" and "inf" with, an optional prefix "+" or "-" for Not a Number (NaN) and positive or negative infinity.'

@test_data(text.split())
def word_stripper(word: str) -> str:
    return word.strip('.,:;!?()\'\"-–—')


results = word_stripper()


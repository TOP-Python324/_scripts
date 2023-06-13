codes = {n: chr(n+35) for n in range(10, 31, 10)}
print(codes, end='\n\n')

# >>> codes[10]
# '-'
# >>> codes[50]
# 'U'
# >>> codes[55]
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# KeyError: 55
# >>>

for k in range(18, 23):
    print(f'{k=} {codes.get(k, "")!r}')
print(codes, end='\n\n')

for k in range(18, 23):
    print(f'{k=} {codes.setdefault(k, "")!r}')
print('codes =', codes, end='\n\n')


new_codes = {k: chr(k+12) for k in [20, 21, 22, 40, 50]}
print('new_codes =', new_codes, end='\n\n')

codes.update(new_codes)
print('codes =', codes, end='\n\n')

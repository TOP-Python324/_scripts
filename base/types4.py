print(f"bool('') = {bool('')}")
print(f"bool(' ') = {bool('a1')}")
print(f"bool('a1') = {bool('a1')}\n")

print(f"int('23') = {int('23')}")
print(f"int('-8') = {int('-8')}\n")
# приведёт к возникновению исключения ValueError
# print(f"int('7.1') = {int('7.1')}")
# print(f"int('z1') = {int('z1')}")
# print(f"int('9+1') = {int('9+1')}")

print(f"float('86') = {float('86')}")
print(f"float('-4.5') = {float('-4.5')}")
# приведёт к возникновению исключения ValueError
# print(f"float('6,1') = {float('6,1')}")
# print(f"float('0dot23') = {float('0dot23')}")

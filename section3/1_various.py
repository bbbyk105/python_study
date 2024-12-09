# num = 1
name = 'Mike'
is_ok = True
num = name
name= "1"

# 型を推測できる
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# strになる
print(num, type(num))

# 型変換も可能である
new_num = int(name)
print(new_num, type(new_num))
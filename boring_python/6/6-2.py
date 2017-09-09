
spam = "52"
ret = spam.isalnum()
print(ret)

spam = "hello123"
ret = spam.isalpha()
print(ret)

spam = " "
ret = spam.isspace()
print(ret)

spam = "Hello world"
ret = spam.startswith('Hello')
print(ret)
ret = spam.startswith('hello')
print(ret)


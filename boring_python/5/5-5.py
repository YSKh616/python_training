
num = 20
picnic_items = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnic_items.get('eggs', num)) + ' eggs.')

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)

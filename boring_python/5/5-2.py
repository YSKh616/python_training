
birthday = {'アリス': '4/1', 'ボブ': '12/12', 'キャロル': '4/4'}

while True:
    print('名前を入力してください: (終了はEnterのみを押してください)')
    name = input()
    if name == '':
        break

    if name in birthday:
        print(name + 'の誕生日は' + birthday[name])
    else:
        print(name + 'の誕生日は未登録です。')
        print('誕生日を入力してください。')
        bday = input()
        birthday[name] = bday
        print('誕生日データベースを更新しました。')



#! python3
# クリップボードのテキストの各行に
# 点を打って、Wikiの箇条書きにする

import pyperclip

text = pyperclip.paste()

# TODO: 行を分割して、'*'を追加する

pyperclip.copy(text)


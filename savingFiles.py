import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

clipboardContent = pyperclip.paste()
print(clipboardContent)

mcbShelf.close()

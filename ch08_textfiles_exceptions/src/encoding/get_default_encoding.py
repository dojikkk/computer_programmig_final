import locale

print('default locale on this system:', locale.getdefaultlocale())
# Win10: ('en_US', 'cp1252')

print('encoding used for text data:', locale.getpreferredencoding(False))
# Win10: cp1252
# macOS, Linux: UTF-8

print('\N{HANGUL SYLLABLE TAEG}')  # ok

# Fails on Win10, works on macOS, Linux:
f = open('myfile.txt', 'w')
f.write('\N{HANGUL SYLLABLE TAEG}')
f.close()

# Works on all three:
f = open('myfile.txt', 'w', encoding='UTF-8')
f.write('\N{HANGUL SYLLABLE TAEG}')
f.close()

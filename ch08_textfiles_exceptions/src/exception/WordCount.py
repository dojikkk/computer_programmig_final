"""
File WordCount.py

Program to count the number of occurrences of a word
in a textfile.
"""


def getFile():
    """
    Return the file name and associated file object for reading the
    file  as tuple of the form (file_name, input_file).
    """
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file name (with extension): ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except OSError:
            print('Unable to open input file, please reenter')
    return (file_name, input_file)


def countWords(input_file, search_word):
    """
    Return the number of occurrences
    of search_word in the provided input_file object.
    """
    num_occurrences = 0
    word_delimiters = (' ', ',', ';', ':', '.', '\n',
                       '"', "'", '(', ')')
    search_word_len = len(search_word)
    for line in input_file:
      line = line.lower()  # convert to lower case characters.
      end_of_line = False
      begin_of_line = True  # the begin of line counts as a word_delimiter
      while not end_of_line:
        # print('>' + line.strip() + '<')
        try:
          found_search_word = False
          index = line.index(search_word)  # throws ValueError if not found
          if index == 0:
            # Only valid case for 'index == 0' is at begin of line. In the
            # middle of a line, line[index-1] must be a delimiter. If not, the
            # word lacks a LEFT delimiter and we're in the middle of a word,
            # for example at the second 'foo' in 'foofoo' when counting 'foo'.
            # Thus, index==0 is not possible in the middle of a line.
            if begin_of_line and line[search_word_len] in word_delimiters:
              found_search_word = True
          elif index > 0:
            # All matching cases in middle of line must have 'index > 0',
            # because line[index - 1] must be a delimiter! (So index=0 is
            # invalid, because the LEFT delimiter is missing.)
            if line[index - 1] in word_delimiters and \
                line[index + search_word_len] in word_delimiters:
              found_search_word = True
          if found_search_word:
            # print('Pos:', index)
            num_occurrences = num_occurrences + 1
          begin_of_line = False  # we moved past the begin of line
          line = line[index + search_word_len:]
        except ValueError:
          end_of_line = True
    return num_occurrences


def upgrade_countWords(input_file, search_word):
    """
    구분자들로 모두 나누고 거기를 모두 공백으로 채우고 split 써서 판단하기 여기서 count 까지 적절하게 섞어서 써주기
    """
    search_word = search_word.lower()
    delimiters = ' ,;:.\n"\'()'
    count = 0
    for line in input_file:
        line = line.lower()
        for d in delimiters:          # 모든 구분자를 공백으로 통일
            line = line.replace(d, ' ')
        count += line.split().count(search_word)  # 쪼갠 뒤 정확히 일치하는 것만 셈
    return count



file_name, input_file = getFile()

search_word = input('Enter word to search: ')
search_word = search_word.lower()

num_occurrences = countWords(input_file, search_word)

if num_occurrences == 0:
    print('No occurrences of word', "'" + search_word + "'",
          'found in file', file_name)
else:
    print('The word', "'" + search_word + "'", 'occurs', num_occurrences,
          'times in file', file_name)

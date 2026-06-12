def getFile():
    '''
        Returns the file name and associated file object for reading the
        file  as tuple of the form (file_name, input_file).
    '''
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file name (with extension): ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except OSError:
            print ('Input file could not be opened, please try again')
    return (file_name, input_file)

def countWords(input_file, search_word):
    ''' Returns the number of occurrences
        of search_word in the provided input_file object.'''
    num_occurrences = 0
    word_delimiters = (' ', ',', ';', ':', '.','\n',
                       '"',"'", '(', ')')
    search_word_len = len(search_word)
    for line in input_file:
        end_of_line = False
        line = line.lower() #convert to all lower case characters.
        while not end_of_line:
            try:   
                found_search_word = False
                index = line.index(search_word)
                if index == 0 and line[search_word_len] in word_delimiters:
                    found_search_word = True
                elif line[index - 1] in word_delimiters and \
                    line[index + search_word_len] in word_delimiters:
                    found_search_word = True
                if found_search_word:
                   num_occurrences = num_occurrences + 1
                   line = line[index + search_word_len: len(line)]
            except ValueError:
                end_of_line = True               
    return num_occurrences


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

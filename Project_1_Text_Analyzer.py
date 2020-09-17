# '''
# author = Vitek Kral
# '''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

ID_DB = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
LINE = (40 * '-')

# LOGIN

print(LINE + '\nWelcome to the app. Please log in: ')
attempt = 3
while attempt > 0:
    user_id = input('USERNAME: ')
    user_pass = input('PASSWORD: ')
    if ID_DB.get(user_id) != user_pass:
        attempt -= 1
        if attempt >= 1:
            print('WRONG USER ID OR PASSWORD - {0} attempts remain'.format(str(attempt)))
        if attempt == 0:
            print('END OF PROGRAM.')
            exit()
    else:
        break

# TEXT SELECTION

selection = input(LINE + '\nWe have 3 texts to be analyzed.\nEnter a number btw. 1 and 3 to select: ')
while (selection.isnumeric() is not True) or (int(selection) > 3) or (int(selection) < 1):
    selection = input('YOUR SELECTION IS INVALID! Repeat your answer in range 1-3: ')
print(LINE)

# TEXT ANALYSIS

words = TEXTS[int(selection) - 1].split()
word_count = len(words)
i = title = upper = lower = numeric = key_count = num_out_sum = 0
WORD_LENGTH = {}

while i < word_count:
    j = 1
    filter_out = filter_num_out = ""
    filter_in = words[i]
    while j <= len(filter_in):
        if filter_in[j-1].isalnum() is True:
            filter_out += filter_in[j-1]
        elif (filter_in[j-1] is '-') and (filter_in[j-2].isalnum() is True) and (filter_in[j].isalnum() is True):
            filter_out += filter_in[j-1]
        if filter_in[j - 1].isnumeric() is True:
            filter_num_out += filter_in[j-1]
        j += 1
    if filter_num_out.isnumeric() is True:
        num_out_sum += float(filter_num_out)
    if filter_out.istitle() is True:
        title += 1
    if filter_out.isupper() is True:
        upper += 1
    if filter_out.islower() is True:
        lower += 1
    if filter_out.isnumeric() is True:
        numeric += 1
    if WORD_LENGTH.get(len(filter_out)) is None:
        WORD_LENGTH[len(filter_out)] = 1
        key_count += 1
    elif WORD_LENGTH.get(len(filter_out)) >= 1:
        WORD_LENGTH[len(filter_out)] += 1
    i += 1

print('''There are {0} words in the selected text.\nThere are {1} titlecase words
There are {2} uppercase words\nThere are {3} lowercase words
There are {4} numeric strings'''.format(str(word_count), str(title), str(upper), str(lower), str(numeric)))
print(LINE)

# BAR GRAPH

sorted_keys = sorted(WORD_LENGTH)
i = 0
bar_graph_print_str = ""
while i < key_count:
    bar_graph_print_str += (str(sorted_keys[i])+' ')
    j = 0
    while j < (WORD_LENGTH.get(sorted_keys[i])):
        bar_graph_print_str += '*'
        j += 1
    bar_graph_print_str += (' '+str(WORD_LENGTH.get(sorted_keys[i])))
    if i < key_count-1:
        bar_graph_print_str += chr(10)
    i += 1

print(bar_graph_print_str + chr(10) + LINE)
print('If we summed all the numbers in this text we would get: {0}'.format(str(num_out_sum)) + chr(10) + LINE)

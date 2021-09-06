import json

class WORD:
    word = ''
    reading = ''
    translation = ''

    def __init__(self):  
        self.word = ''
        self.reading = '' 
        self.translation = ''

    def change(self, word, reading, translation):
        self.word = word  
        self.reading = reading  
        self.translation = translation

def add_kanji(filename):
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    print('Put a kanji')
    kanji_input = input()
    for kanji in data.keys():
        if kanji_input == kanji:
            print("It's already here\n")
            return
    key_general = kanji_input
    param_mass = ["ON", "KUN", "WORDS", "TRANSLATION"]
    values = [[], [], [], []]
    
    print('Put 音読み:')
    input_word = input()
    for part in input_word.split():
        values[0].append(part)
    
    print('Put 訓読み:')
    input_word = input()
    for part in input_word.split():
        values[1].append(part)

    print('Put translation:')
    input_word = input()
    values[3].append(input_word)
    
    param_mass_kotoba = ["WORD", "READING", "TRANSLATION"]
    values_kotoba = [[], [], []]

    print('Put 言葉, to exit put 4')
    input_word = input()
    while input_word != '4':
        values_kotoba[0] = input_word.split('.')[0]
        values_kotoba[1] = input_word.split('.')[1]
        values_kotoba[2] = input_word.split('.')[2]
        input_word = input()

    if len(values_kotoba[0]) != 0:
        kotoba = dict(zip(param_mass_kotoba, values_kotoba))
        values[2].append(kotoba)
        kotoba = {}
        values_kotoba = [[], [], []]
    
    for kanji in data.keys():
        for row in data[kanji]['WORDS']:
            word = row['WORD']
            res = word.find(key_general)
            if res != -1:
                if word not in values[2].keys():
                    values_kotoba[0] = word
                    values_kotoba[1] = data[kanji]['WORDS'][word]['READING']
                    values_kotoba[2] = data[kanji]['WORDS'][word]['TRANSLATION']
                    kotoba = dict(zip(param_mass_kotoba, values_kotoba))
                    values[2].append(kotoba)
                    kotoba = {}
                    values_kotoba = [[], [], []]

    param_dict = dict(zip(param_mass, values))
    data[key_general] = param_dict
    
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file)

def add_word(filename):
    with open(filename,"r",encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    print('Put a word')
    word_input = input()
    for kanji in data.keys():
        count = 0
        res = word_input.split('.')[0].find(kanji)
        if res != -1:
            for row in data[kanji]['WORDS']:
                if word_input.split('.')[0] == row['WORD'][0]:
                    count = count + 1
            if count == 0:
                param_mass_kotoba = ["WORD", "READING", "TRANSLATION"]
                values_kotoba = [[], [], []]
                values_kotoba[0] = word_input.split('.')[0]
                values_kotoba[1] = word_input.split('.')[1]
                values_kotoba[2] = word_input.split('.')[2]
                kotoba = dict(zip(param_mass_kotoba, values_kotoba))
                data[kanji]['WORDS'].append(kotoba)
                print(data[kanji]['WORDS'])
    
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file)


def repeat_kanji(filename):
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    print("All kanji:")
    for kanji in data.keys():
        print(kanji + ' ', end = '')
    print('Put a kanji to repeat')
    kanji = input()
    print("音読み:  ", end = ' ')
    for i in data[kanji]['ON']:
        print(i + ' ', end = ' ')
    print("\n訓読み:  ", end = ' ')
    for i in data[kanji]['KUN']:
        print(i + ' ', end = ' ')
    print("\nTranslation:  ", end = ' ')
    print(data[kanji]['TRANSLATION'][0])
    print("言葉:")
    if len(data[kanji]['WORDS']) != 0:
        print(len(data[kanji]['WORDS']))
        i = 1
        for row in data[kanji]['WORDS']:
            print('    ' + str(i) + '.Word: ' + row['WORD'] + ', ' + 'reading: ' + row['READING'] + ', ' + 'translation: ' + row['TRANSLATION'] + '.')
            i = i + 1

def add_text_word(filename):
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    print('Put a word')
    word_input = input()
    count = 0
    if len(data) != 0:
        for row in data:
            if word_input.split('.')[0] == row['WORD'][0]:
                count = count + 1
    if count == 0:
        param_mass_kotoba = ["WORD", "READING", "TRANSLATION"]
        values_kotoba = [[], [], []]
        values_kotoba[0] = word_input.split('.')[0]
        values_kotoba[1] = word_input.split('.')[1]
        values_kotoba[2] = word_input.split('.')[2]
        kotoba = dict(zip(param_mass_kotoba, values_kotoba))
        data.append(kotoba)
    
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file)

def show_text_word(filename):
    # wrd = WORD
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    if len(data) != 0:
        for row in data:
            # setattr(wrd, 'word', row['WORD'])
            # setattr(wrd, 'reading', row['READING'])
            # setattr(wrd, 'translation', row['TRANSLATION'])
            # wrd.change(row['WORD'], row['READING'], row['TRANSLATION'])
            print(row['WORD'], end = '')
            for i in range(10 - len(row['WORD'])):
                print('  ', end = '')
            print(row['READING'], end = '')
            for i in range(10 - len(row['READING'])):
                print('  ', end = '')
            print(row['TRANSLATION'] + ';')
            # print("{0.word}  {0.reading}  {0.translation}".format(wrd))
    


if __name__ == '__main__':
    # with open("data_file_old.json","r", encoding = 'utf8') as read_file: 
    #     data = json.load(read_file)
    # print(data)
    print("What do yiu want, nigga:", "1.Add kanji", "2.Add word for kanji", "3.Repeat kanji", "4.Add word from text", "5.Show words from texts", "6.Exit", sep = '\n')
    command = int(input('Enter a command:'))
    while command != 6:
        if(command == 1):
            add_kanji("data_file.json")
        if(command == 2):
            add_word("data_file.json")
        if(command == 3):
            repeat_kanji("data_file.json")
        if(command == 4):
            add_text_word("words.json")
        if(command == 5):
            show_text_word("words.json")
        command = int(input('Enter a command:'))
    print('Bie, bitch\n')


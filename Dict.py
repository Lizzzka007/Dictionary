import json
import random
import keyboard

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
    values[3].append(input_word.lower())
    
    param_mass_kotoba = ["WORD", "READING", "TRANSLATION"]
    values_kotoba = [[], [], []]

    print('Put 言葉, to exit put 4')
    input_word = input()
    while input_word != '4':
        values_kotoba[0] = input_word.split('.')[0]
        values_kotoba[1] = input_word.split('.')[1]
        values_kotoba[2] = input_word.split('.')[2].lower()
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
            # print(word + ' ' + str(res))
            if res != -1:
                if len(values[2]) != 0:
                    # print('For ' + key_general + 'added')
                    print(values[2])
                    if word not in values[2][0]['WORD']:
                        values_kotoba[0] = word
                        values_kotoba[1] = row['READING']
                        values_kotoba[2] = row['TRANSLATION']
                        kotoba = dict(zip(param_mass_kotoba, values_kotoba))
                        values[2].append(kotoba)
                        kotoba = {}
                        values_kotoba = [[], [], []]
                else:
                    values_kotoba[0] = word
                    values_kotoba[1] = row['READING']
                    values_kotoba[2] = row['TRANSLATION']
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
                # print(word_input.split('.')[0] + ' vs ' + row['WORD'])
                if word_input.split('.')[0] == row['WORD']:
                    # print('Yes')
                    count = count + 1
            if count == 0:
                param_mass_kotoba = ["WORD", "READING", "TRANSLATION"]
                values_kotoba = [[], [], []]
                values_kotoba[0] = word_input.split('.')[0]
                values_kotoba[1] = word_input.split('.')[1]
                values_kotoba[2] = word_input.split('.')[2].lower()
                kotoba = dict(zip(param_mass_kotoba, values_kotoba))
                data[kanji]['WORDS'].append(kotoba)
                print('For ' + kanji + ' added')
                # print(data[kanji]['WORDS'])
    
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file)


def repeat_kanji(filename):
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    print("All kanji:")
    k = 0
    for kanji in data.keys():
        # print(str(k) + '.' + kanji + ' ', end = ' ')
        print(str(k) + '.' + kanji)
        k = k + 1
    print('\nPut a kanji to repeat')
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
            if word_input.split('.')[0] == row['WORD']:
                count = count + 1
    if count == 0:
        param_mass_kotoba = ["WORD", "READING", "TRANSLATION"]
        values_kotoba = [[], [], []]
        values_kotoba[0] = word_input.split('.')[0]
        values_kotoba[1] = word_input.split('.')[1]
        values_kotoba[2] = word_input.split('.')[2].lower()
        kotoba = dict(zip(param_mass_kotoba, values_kotoba))
        data.append(kotoba)
    
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file)

def show_text_word(filename):
    k = 0
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    if len(data) != 0:
        for row in data:
            print(str(k) + '. ' + row['WORD'], end = '')
            for i in range(10 - len(row['WORD'])):
                print('  ', end = '')
            print(row['READING'], end = '')
            for i in range(10 - len(row['READING'])):
                print('  ', end = '')
            print(row['TRANSLATION'] + ';\n')
            k = k + 1
            # print("{0.word}  {0.reading}  {0.translation}".format(wrd))

def add_adverb(filename):
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    print('Put a word')
    word_input = input()
    count = 0
    if len(data) != 0:
        for row in data:
            if word_input.split('.')[0] == row['WORD']:
                count = count + 1
    if count == 0:
        param_mass_kotoba = ["WORD", "READING", "TRANSLATION"]
        values_kotoba = [[], [], []]
        values_kotoba[0] = word_input.split('.')[0]
        values_kotoba[1] = word_input.split('.')[1]
        values_kotoba[2] = word_input.split('.')[2].lower()
        kotoba = dict(zip(param_mass_kotoba, values_kotoba))
        data.append(kotoba)
    
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file)

def show_adverb(filename):
    # wrd = WORD
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    if len(data) != 0:
        for row in data:
            print(row['WORD'], end = '')
            for i in range(10 - len(row['WORD'])):
                print('  ', end = '')
            print(row['READING'], end = '')
            for i in range(10 - len(row['READING'])):
                print('  ', end = '')
            print(row['TRANSLATION'] + ';')
            # print("{0.word}  {0.reading}  {0.translation}".format(wrd))

def remem_kanji(filename):
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    
    kanjis = list(data.keys())
    # print(kanjis)
    random.shuffle(kanjis)
    repeat = []
    for kanji in kanjis:
        while len(repeat) == 5:
            random.shuffle(repeat)
            for forgotten_kanji in repeat:
                print(forgotten_kanji)
                command = int(input('Put 1 if Ok, else 0: '))
                if command == 1:
                    repeat.remove(forgotten_kanji)
                print("音読み:  ", end = ' ')
                for i in data[kanji]['ON']:
                    print(i + ' ', end = ' ')
                print("\n訓読み:  ", end = ' ')
                for i in data[kanji]['KUN']:
                    print(i + ' ', end = ' ')
                print("\nTranslation:  ", end = ' ')
                print(data[kanji]['TRANSLATION'][0])
                if len(data[kanji]['WORDS']) != 0:
                    print("言葉:")
                    i = 1
                    for row in data[kanji]['WORDS']:
                        print('    ' + str(i) + '.Word: ' + row['WORD'] + ', ' + 'reading: ' + row['READING'] + ', ' + 'translation: ' + row['TRANSLATION'] + '.')
                        i = i + 1
                print('-----------------------------------------------------------------------------------')
        print(kanji)
        command = int(input('Put 1 if Ok, else 0: '))
        if command == 0:
            repeat.append(kanji)
        print("音読み:  ", end = ' ')
        for i in data[kanji]['ON']:
            print(i + ' ', end = ' ')
        print("\n訓読み:  ", end = ' ')
        for i in data[kanji]['KUN']:
            print(i + ' ', end = ' ')
        print("\nTranslation:  ", end = ' ')
        print(data[kanji]['TRANSLATION'][0])
        if len(data[kanji]['WORDS']) != 0:
            print("言葉:")
            i = 1
            for row in data[kanji]['WORDS']:
                print('    ' + str(i) + '.Word: ' + row['WORD'] + ', ' + 'reading: ' + row['READING'] + ', ' + 'translation: ' + row['TRANSLATION'] + '.')
                i = i + 1
        print('-----------------------------------------------------------------------------------')
    


if __name__ == '__main__':
    print("What do you want:", "1.Add kanji", "2.Add word for kanji", 
    "3.Repeat kanji", "4.Add word from text", "5.Show words from texts", "6.Add adverb", 
    "7.Show adverbs","8.Add expression", "9.Show expressions", "10.Remember kanji", "11.Exit", sep = '\n')
    command = int(input('Enter a command:'))
    while command != 11:
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
        if(command == 6):
            add_text_word("adverbs.json")
        if(command == 7):
            show_text_word("adverbs.json")
        if(command == 8):
            add_text_word("expressions.json")
        if(command == 9):
            show_text_word("expressions.json")
        if(command == 10):
            remem_kanji("data_file.json")
        command = int(input('Enter a command:'))
    print('Bie\n')


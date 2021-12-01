import json
import random
import pandas as pd

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

    read_file.close()

    print('Put a kanji')
    kanji_input = input()
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
                    # print(values[2])
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

    for kanji in data.keys():
        if kanji_input == kanji:
            print("\n----------------------------------------------------------")
            print(kanji)
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
                    print('    ' + str(i) + row['WORD'] + '\t' + row['READING'] + '\t' + row['TRANSLATION'] + '.')
                    i = i + 1 
            else:
                print("There's no words for", kanji)
            print("----------------------------------------------------------\n")
            Signal = input("It's already here, should I change it? y/n: ")
            if Signal == "n":
                return

    data[key_general] = param_dict
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file)
    file.close()

def delete_kanji_word(filename):
    with open(filename,"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)

    read_file.close()

    kanji = input("Choose kanji: ")
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
            print('    ' + str(i) + row['WORD'] + '\t' + row['READING'] + '\t' + row['TRANSLATION'] + '.')
            i = i + 1

    Signal = input("Which word should I delete? Put the word:\n")
    print("Signal = ", Signal)
    for i in range(len(data[kanji]['WORDS'])):
        if data[kanji]['WORDS'][i]['WORD'] == Signal:
            data[kanji]['WORDS'].pop(i)
            break

    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file)

    file.close()

def add_word(filename):
    with open(filename,"r",encoding = 'utf8') as read_file: 
        data = json.load(read_file)
    print('Put a word')
    word_input = input()
    AlreadyExist = []
    count = 0
    flag = 0
    stop = 0
    for kanji in data.keys():
        res = word_input.split('.')[0].find(kanji)
        if res != -1:
            for row in data[kanji]['WORDS']:
                # print(word_input.split('.')[0] + ' vs ' + row['WORD'])
                if word_input.split('.')[0] == row['WORD']:
                    # print('Yes')
                    count = count + 1
                    AlreadyExist = row['WORD'] + "\t" + row['READING'] + "\t" + row['TRANSLATION']

            if count != 0:
                print("Already here: ", AlreadyExist)
                Signal = input('Should I change it? y/n: ')
                if Signal == "y":
                    flag = 1
                else:
                    break

            if count == 0:
                flag = 1

            if flag == 1:
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
            print('    ' + str(i) + row['WORD'] + '\t' + row['READING'] + '\t' + row['TRANSLATION'] + '.')
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
            print(str(k) + '. ' + row['WORD'] + '\t\t' + row['READING'] + '\t\t' + row['TRANSLATION'])
            k = k + 1

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
    k = 0
    if len(data) != 0:
        for row in data:
            print(str(k) + '. ' + row['WORD'] + '\t' + row['READING'] + '\t' + row['TRANSLATION'])
            k += 1

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
                for i in data[forgotten_kanji]['ON']:
                    print(i + ' ', end = ' ')
                print("\n訓読み:  ", end = ' ')
                for i in data[forgotten_kanji]['KUN']:
                    print(i + ' ', end = ' ')
                print("\nTranslation:  ", end = ' ')
                print(data[forgotten_kanji]['TRANSLATION'][0])
                if len(data[forgotten_kanji]['WORDS']) != 0:
                    print("言葉:")
                    i = 1
                    for row in data[forgotten_kanji]['WORDS']:
                        print('    ' + str(i) + '. ' + row['WORD'] + '\t' + row['READING'] + '\t' + row['TRANSLATION'] + '.')
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
                print('    ' + str(i) + '. ' + row['WORD'] + '\t' + row['READING'] + '\t' + row['TRANSLATION'] + '.')
                i = i + 1
        print('-----------------------------------------------------------------------------------')

def AddKanjiLesson():
    with open('KanjiLessons.json',"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)

    read_file.close()

    Lesson_number = float(input('Put the number of the lesson: '))
    kanji = input('Put a kanji to add, to exit print any number : ')

    Kanjis = []

    while kanji.isnumeric() != True:
        Kanjis.append(kanji)
        kanji = input('Put a kanji to add, to exit print any number : ')
        # print(kanji, ": ", kanji.isnumeric())
        # print(kanji.encode('utf8'))

    # Final_dict = {Lesson_number: Kanjis}
    data[Lesson_number] = Kanjis

    with open('KanjiLessons.json',"w", encoding = 'utf8') as file: 
        json.dump(data, file)

    file.close()

def RepeatKanjiLesson():
    with open('KanjiLessons.json',"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)

    Lesson_number = str(input('Put the number of the lesson to repeat: '))
    Kanjis = data[Lesson_number]

    with open('data_file.json',"r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)

    print('-----------------------------------------------------------------------------------')
    for kanji in Kanjis:
        print(kanji)
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
                print('    ' + str(i) + '.' + row['WORD'] + '\t' + row['READING'] + '\t' + row['TRANSLATION'] + '.')
                i = i + 1
        print('-----------------------------------------------------------------------------------')    

    # rows = []
    # column_ON = []
    # column_KUN = []
    # column_TRANSL = []
    # column_words = []

    # for i in Final_dict[Lesson_number]:
    #     print(i)
    #     kanji = i
    #     rows.append(kanji)
    #     column_ON.append(Final_dict[Lesson_number][i]['ON'])
    #     column_KUN.append(Final_dict[Lesson_number][i]['KUN'])
    #     column_TRANSL.append(Final_dict[Lesson_number][i]['TRANSLATION'])
    #     lst = []
        
    #     for word in Final_dict[Lesson_number][i]['WORDS']:
    #         lst.append(word['WORD'])
    #         lst.append(word['READING'])
    #         lst.append(word['TRANSLATION'])

    #     KanjiWord = ''

    #     print('Len lst = ' + str(len(lst)))
    #     for i in range(int(len(lst) / 3)):
    #         KanjiWord += lst[i * 3] + ' '
    #         KanjiWord += lst[i * 3 + 1] + ' '
    #         KanjiWord += lst[i * 3 + 2]
    #         KanjiWord += ',\n'


    #     column_words.append([KanjiWord])

    # Columns = ['ON', 'KUN', "Translation", "Words"]
    # data = [column_ON[0], column_KUN[0], column_TRANSL[0], column_words[0]]

    # print('Check ' + KanjiWord[0])
    # # print(data)
    # print(data)

    # table = pd.DataFrame(data=data, index=rows, columns=Columns)
    # print(table)

def AddTextWordsByOrder():
    with open("中級から学ぶ日本語.txt","r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)

    Lesson_number = str(input('Put the number of the text: '))
    Words = []

    print("Print words which should be added to the lesson %s, at the end print any number" %Lesson_number)

    while 1:
        word = input()

        if word.isnumeric() == True:
            break

        lst = []
        res = word.split('.')
        for i in res:
            lst.append(i)

        Words.append(lst.copy())

    data[Lesson_number] = Words

    with open("中級から学ぶ日本語.txt","w", encoding = 'utf8') as file: 
        json.dump(data, file)

def AddOnTextWordsByOrder():
    with open("中級から学ぶ日本語.txt","r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)

    Lesson_number = str(input('Put the number of the text: '))

    Words = []

    while 1:
        word = input()

        if word.isnumeric() == True:
            break

        lst = []
        res = word.split('.')
        for i in res:
            lst.append(i)

        data[Lesson_number].append(lst.copy())

    with open("中級から学ぶ日本語.txt","w", encoding = 'utf8') as file: 
        json.dump(data, file)

def RepeatTextWords():
    with open("中級から学ぶ日本語.txt","r", encoding = 'utf8') as read_file: 
        data = json.load(read_file)

    Lesson_number = str(input('Put the number of the text to repeat: '))
    Words = data[Lesson_number]

    print('\n-----------------------------------------------------------------------------------')
    k = 1
    for wrd in Words:
        print("{0}.{1:<20} {2:<20} {3:<20}".format(k, wrd[0], wrd[1], wrd[2]))
        # print("%d.%6s %6s %6s" %(k, wrd[0], wrd[1], wrd[2]))
        # print(str(k) + "." + wrd[0] + "\t" + wrd[1] + "\t" + wrd[2])
        k += 1
    print("\n")
        
    


if __name__ == '__main__':
    print("What do you want:", "1.Add kanji", "2.Add word for kanji", "3.Delete word for kanji",
    "4.Repeat kanji", "5.Add word from text", "6.Show words from texts", "7.Add adverb", 
    "8.Show adverbs","9.Add expression", "10.Show expressions", "11.Remember kanji", "12.Add kanji lesson", "13.Repeat kanji lesson", "14.Add text words by order", "15.Add on text words by order", "16.Repeat text words by order", "17.Exit", sep = '\n')
    command = int(input('Enter a command:'))
    while command != 17:
        if(command == 1):
            add_kanji("data_file.json")
        if(command == 2):
            add_word("data_file.json")
        if(command == 3):
            delete_kanji_word("data_file.json")
        if(command == 4):
            repeat_kanji("data_file.json")
        if(command == 5):
            add_text_word("words.json")
        if(command == 6):
            show_text_word("words.json")
        if(command == 7):
            add_text_word("adverbs.json")
        if(command == 8):
            show_text_word("adverbs.json")
        if(command == 9):
            add_text_word("expressions.json")
        if(command == 10):
            show_text_word("expressions.json")
        if(command == 11):
            remem_kanji("data_file.json")
        if(command == 12):
            AddKanjiLesson()
        if(command == 13):
            RepeatKanjiLesson()
        if(command == 14):
            AddTextWordsByOrder()
        if(command == 15):
            AddOnTextWordsByOrder()
        if(command == 16):
            RepeatTextWords()
        command = int(input('Enter a command:'))
    print('Bie\n')


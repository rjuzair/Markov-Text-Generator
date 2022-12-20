import text_stats
import sys
import random
import os


#Check for chek_errors
def check_errors():

    if len(sys.argv) != 4:
        print("Insufficient input parameters")
        exit(1)

    elif os.path.isfile(sys.argv[1]):
        print("\nFound the input file! \nPlease wait, generating text... \n\n\n")

    else:
        print("\nThe file does not exists!")
        exit(1)

def successors(words, word):

    successor_words = dict()
    for i in range(len(words)):
        if word == words[i]:
            if words[i+1] in successor_words:
                successor_words[words[i+1]] += 1
            else:
                successor_words[words[i+1]] = 1

    t_words = sum(list(successor_words.values()))
    for key,value in successor_words.items():
        successor_words[key] = round((value/t_words), 2)

    return successor_words

def text_gen(given_word, words, words_limit):

    cur_word = given_word
    msg = cur_word
    successors_dict = {}
    successor_words = successors(words, given_word)
    successors_dict[given_word] = successor_words

    for i in range(words_limit):

        if cur_word in successors_dict:
            successor_words = successors_dict[cur_word]
        else:
            successor_words = successors(words, cur_word)
            successors_dict[cur_word] = successor_words

        #generate new word
        cur_word = random.choices(population = list(successor_words.keys()),
         weights=list(successor_words.values()), k = 1)[0]
        msg = msg + " " + cur_word

    print(msg)

def main():

        with open(sys.argv[1], encoding="utf-8", mode="r") as input_file:

            file_data = input_file.readlines()
            words = text_stats.all_words(file_data)
            given_word = sys.argv[2]
            words_limit = int(sys.argv[3])
            text_gen(given_word, words, words_limit)

            return None

if __name__ == '__main__':

    check_errors()
    main()

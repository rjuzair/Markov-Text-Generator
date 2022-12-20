import os
import sys
import collections
from string import punctuation

#Checking for error
def check_errors():

    if len(sys.argv) <= 1:
        print("\nNo input file provided \n")
        exit(1)

    elif os.path.isfile(sys.argv[1]):
        print("\nFound the input file! \nPlease wait, processing the file...")

    else:
        print("\nThe file does not exists!")
        exit(1)

#Finding all the words in file
def all_words(file_data):

    words = []

    lines = [line.split() for line in file_data]
    temp = [[one_word.strip(punctuation).lower() for one_word in line] for line in lines]

    for i in temp:
        words += i
    return words


#Five most common words and their occurances
def m_common_words(file_data):

    words = all_words(file_data)
    num_common_words = 5
    common_words = collections.Counter(words).most_common(num_common_words)
    return common_words


#Calculating total number of words
def num_words(file_data):
    words = all_words(file_data)
    n_words = len(words)
    return n_words

#Calculating occurances of letters
def num_letters(file_data):
    temp  = []
    words = all_words(file_data)

    for i in words:
        temp += i

    letters = list(filter(lambda x:x.isalpha(), temp))
    n_letters = collections.Counter(letters).most_common()
    return n_letters


#Calculating total number of unique words
def num_unique_word(file_data):

    unique_words = []
    words = all_words(file_data)
    unique_words = set(words)

    #for word in words:
        #if word not in unique_words:
            #unique_words.append(word)

    return len(unique_words)



#Most commonly used words and 3 words following them
def common_successor_words(file_data):

    num_successors = 3
    words = all_words(file_data)
    temp = dict(m_common_words(file_data))
    common_words = [i[:] for i in temp]
    common_words = {i: {} for i in common_words}
    for word in temp.keys():
        for i in range(len(words)):
            if word == words[i]:
                if words[i+1] in common_words[word].keys():
                    common_words[word][words[i+1]] += 1
                else:
                    common_words[word][words[i+1]] = 1

    for word in common_words.keys():
        common_words[word] = dict(collections.Counter(common_words[word]).most_common(num_successors))

    return dict(common_words)

def output(results):

    if len(sys.argv) == 3:

        with open(sys.argv[2] , "w") as f:

            print("\n", "\n********File Stats*********", file= f)

            print("Total number of words are: " + str(results[0]) + "\n", file = f)

            print("Total number of unique words are: " +str(results[3]) + "\n", file = f)

            print("Frequency table for alphabetic letters are given below: " + "\n", file = f)
            for i in range(len(results[2])):
                print(" " + str(results[2][i][0]) +" "+ str(results[2][i][1]) + "\n", file = f)

            print("\nTop 5 commonly used words and their 3 successors is given below:", file = f)
            for i in results[4].items():
                print("\n " +str(i[0]) +" "+ "(" +str(dict(results[1])[i[0]])+ " Occurances)", file = f)
                for j in i[1].items():
                    print(" --"+str(j[0]) +"  "+ str(j[1]), file = f)

        print("\nText stats are written to " + str(sys.argv[2]))
        #with open(sys.argv[2], mode = "r") as f:
            #lines = f.readlines()
            #for line in lines:
                #print(lines)


    else:
            print("\n\t********File Stats*********\n\n")

            print("Total number of words are: " + str(results[0]) + "\n")

            print("Total number of unique words are: " +str(results[3]) + "\n")

            print("Frequency table for alphabetic letters are given below: " + "\n")
            for i in range(len(results[2])):
                print(" " + str(results[2][i][0]) +" "+ str(results[2][i][1]) + "\n")

            print("\nTop 5 commonly used words and their 3 successors is given below:")
            for i in results[4].items():
                print("\n " +str(i[0]) +" "+ "(" +str(dict(results[1])[i[0]])+ " Occurances)")
                for j in i[1].items():
                    print(" --"+str(j[0]) +"  "+ str(j[1]))


def main():


    with open(sys.argv[1], encoding="utf-8", mode = "r") as input_file:

        file_data = input_file.readlines()
        t_num_words = num_words(file_data)
        t_num_letters = num_letters(file_data)
        common_words = m_common_words(file_data)
        t_num_unique = num_unique_word(file_data)
        common_successor = common_successor_words(file_data)

        output([t_num_words,
        common_words,
        t_num_letters,
        t_num_unique,
        common_successor])

        return None

if __name__ == '__main__':

    check_errors()
    main()

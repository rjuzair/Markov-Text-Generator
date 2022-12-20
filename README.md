# Markov Text Generator

This a small program that doubles as a somewhat reusable module and a command-line
script. It will read a text file and produce some simple statistics about the contents, along with data that can be
used to create a crude Markov text generator. The main focus is on Python as a scripting language, program
structure and naming, and the usage of proper data structures.

## 1. text_stats.py 

text_stats.py a command-line script which reads the file in home directory (in this case shakespeare.txt) and prints some basic information about its contents.
It should be invoked from the shell/terminal by ./text_stats.py <filename> (so, for example ./text_stats.py shakespeare.txt ). On Windows, this might look like python text_stats.py <filename> 

![Screenshot 2022-12-20 171633](https://user-images.githubusercontent.com/73039575/208714391-0d60310d-1001-4df0-9566-faab5f166a78.png)

![image](https://user-images.githubusercontent.com/73039575/208714640-05c97300-9fc3-40ae-b37e-09b5ec662d42.png)


## 2. text_generator.py

Script generate_text.py which takes three arguments: a file name of a text file, a starting word and a maximum number of words. It then generates very least interesting-looking new text.
It can be invoked from the sell/terminal by ./generate_text.py shakespeare.txt king 500 , ./generate_text.py nilsholgersson.txt akka 1500.


# Rodrigue Andela
# 05/19/2021
# in this task I write a function that take as a parameter as string and return dictionary

# count_letters takes in a string and produces a letter frequency dictionary
def count_letters(list):
     letters = {}
     #for every letter in list
     for P in list:
        if P.upper() >= 'A' and P.upper() <= 'Z':
            if P.upper() in letters:
                # for every letter recognized adding one count
                letters[P.upper()]+= 1
            else:
                letters[P.upper()] = 1
                # returning letters dictionary
     return letters


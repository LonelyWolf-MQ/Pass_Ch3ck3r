#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from platform import system


def score(isCap, isSml, Num, Sym, ptr, length, isdict):
    score = 0
    if length >= 6:
        if (isCap and isSml and Num and Sym) > 0:
            score = 10
            if isdict is True:
                score -= 2
                if 'Symbol pattern found' in ptr:
                    score -= -1
                elif 'Letter pattern found' in ptr:
                    score -= 2
                elif 'Number pattern found' in ptr:
                    score -= 1.5
                if score < 0:
                    score = 0
                    return score
                else:
                    return score
            elif isdict is False:
                if 'Symbol pattern found' in ptr:
                    score -= -1
                elif 'Letter pattern found' in ptr:
                    score -= 2
                elif 'Number pattern found' in ptr:
                    score -= 1.5
                if score < 0:
                    score = 0
                    return score
                else:
                    return score
        elif (isCap and isSml and Num) > 0:
            score = 7
            if isdict is True:
                score -= 2
                if 'Symbol pattern found' in ptr:
                    score -= -1
                elif 'Letter pattern found' in ptr:
                    score -= 2
                elif 'Number pattern found' in ptr:
                    score -= 1.5
                return score
            elif isdict is False:
                if 'Symbol pattern found' in ptr:
                    score -= -1
                elif 'Letter pattern found' in ptr:
                    score -= 2
                elif 'Number pattern found' in ptr:
                    score -= 1.5
                if score < 0:
                    score = 0
                    return score
                else:
                    return score
        elif (isCap or isSml) > 0:
            score = 4
            if isdict is True:
                score -= 2
                if 'Symbol pattern found' in ptr:
                    score -= -1
                elif 'Letter pattern found' in ptr:
                    score -= 2
                elif 'Number pattern found' in ptr:
                    score -= 1.5
                if score < 0:
                    score = 0
                    return score
                else:
                    return score
            elif isdict is False:
                if 'Symbol pattern found' in ptr:
                    score -= -1
                elif 'Letter pattern found' in ptr:
                    score -= 2
                elif 'Number pattern found' in ptr:
                    score -= 1.5
                if score < 0:
                    score = 0
                    return score
                else:
                    return score
    elif length < 6:
        return score



def isDict(filename, passwd):
    line_number = 0
    with open(filename, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if passwd in line:
                return True
        return False


def hasPatterns(password):
    passwd = password.lower()
    list_of_results = {}
    letter_pat1 = "qwertyuiop"
    letter_pat2 = "asdfghjkl"
    letter_pat3 = "zxcvbnm"
    number_pat = "123456789"
    symbol_pat = "!@#$%^&*()-=+`/'"
    letter_rows = [
        letter_pat1, letter_pat1[::-1],
        letter_pat2, letter_pat2[::-1],
        letter_pat3, letter_pat3[::-1]
    ]
    num_row = [
        number_pat, number_pat[::-1],
    ]
    sym_row = [
        symbol_pat, symbol_pat[::-1]
    ]
    for index in range(0, len(passwd)-2):
        sequence = passwd[index:index+3]
        for i in range(0, len(letter_rows)-1):
            if sequence in letter_rows[i]:
                list_of_results['L'] = 'Letter pattern found'
        for i in range(0, len(num_row)-1):
            if sequence in num_row[i]:
                list_of_results['N'] = 'Number pattern found'
        for i in range(0, len(sym_row)-1):
            if sequence in sym_row[i]:
                list_of_results['S'] = 'Symbol pattern found'
    if len(list_of_results) > 0:
        return list_of_results
    else:
        return 'No Pattern Found'


def clearConsole():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass


def main():
    clearConsole()

    B = '\033[34m'
    G = '\033[32m'
    R = '\033[31m'
    print(R+'''
=============================================================================================
=██████   █████  ███████ ███████      ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████ =
=██   ██ ██   ██ ██      ██          ██      ██   ██ ██      ██      ██  ██  ██      ██   ██= 
=██████  ███████ ███████ ███████     ██      ███████ █████   ██      █████   █████   ██████ = 
=██      ██   ██      ██      ██     ██      ██   ██ ██      ██      ██  ██  ██      ██   ██= 
=██      ██   ██ ███████ ███████      ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██= 
=                                                                                           =
=                                                                                           =        
=                               By: Mohammed Qintar                                         =
=============================================================================================                               
                                                                     	    ''')

    Password = input(B+'''Enter your password:: ''')
    small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                     'm',   'n', 'o',  'p', 'q', 'r', 's', 't', 'u', 'v',   'w', 'x', 'y',  'z']
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                       'L', 'M', 'N',  'O',  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',  'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_char = ['`', '!', '@', '#', '$', '%', '&',
                    '*', '(', ')', '-', '_', '-', '/', ';', '+']
    Count_Sml = Count_Cpl = Count_Num = Count_Spchar = 0
    for c in Password:
        if (c in small_letters):
            Count_Sml += 1
        if (c in capital_letters):
            Count_Cpl += 1
        if (c in numbers):
            Count_Num += 1
        if (c in special_char):
            Count_Spchar += 1

    if (((Count_Sml or Count_Cpl) and Count_Num and Count_Spchar) > 0):
        print('Password Conatains Letter, Number, Symbol')
    elif (((Count_Sml or Count_Cpl) and Count_Num) > 0 and Count_Spchar == 0):
        print('Password Conatains Letter, Number')
    elif (((Count_Sml or Count_Cpl) and Count_Spchar) > 0 and Count_Num == 0):
        print('Password Conatains Letter, Symbol')
    elif ((Count_Num and Count_Spchar) > 0 and (Count_Sml or Count_Cpl) == 0):
        print('Password Conatains Number, Symbol')
    elif ((Count_Sml or Count_Cpl) > 0 and (Count_Num and Count_Spchar) == 0):
        print('Password Conatains just Letter')
    elif (Count_Num > 0 and ((Count_Sml or Count_Cpl) and Count_Spchar) == 0):
        print('Password Conatains just Number,')
    elif (Count_Spchar > 0 and (Count_Num and (Count_Sml or Count_Cpl)) == 0):
        print('Password Conatains just Symbol')

    Pass_len = len(Password)
    print('The Password Length is: ' + str(Pass_len))
    Pr = hasPatterns(Password)
    if Pr == 'No Pattern Found':
        print('No Pattern Found')
    else:
        for x in Pr.values():
            print(x)
    mat = isDict('Common-100k-pass.txt', Password)
    scr = score(Count_Cpl, Count_Sml, Count_Num,
                Count_Spchar, Pr, Pass_len, mat)
    if mat is True:
        print('Found a password in the common password list')
    elif mat is False:
        print('No Match Found in Dictionary')
    

    if (scr == 0):
        print('Password is too weak')
    elif (1 < scr <= 5):
        print('Password score is ' + str(scr) + ' Weak Password')
    elif (5 < scr < 7):
        print('Password score is ' + str(scr) + ' Meduim Password')
    elif (scr >= 7):
        print('Password score is ' + str(scr) + ' Strong Password')

if __name__ == "__main__":
    main()

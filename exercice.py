#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	return [max(elem) for elem in numbers]

def join_integers(numbers):
	return int("".join([str(elem) for elem in numbers]))

def generate_prime_numbers(limit):
	premiers = []
	nombres = [i for i in range(2, limit+1)] #premier nombre premier
	while len(nombres) != 0:
		#Ajouter à premiers le premier entier de nombres
		premiers.append(nombres[0])
		#nombres = liste des entiers de nombres non multiples du premier
		nombres = [elem for elem in nombres if elem % nombres[0] != 0]
		#nombres_2 = []
		#for elem in nombres:
		# 	if elem % nonmbres[0] !=0:
		# 		nombres_2.append(elem)
		# 	nombres = nombres_2
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):

    # string_1 = strings[0] + str(1)
    # print(string_1)

    result=[]
    #Generer une liste de nombre allant de 1 a num_comb (inclus)
    #pour chaque entier dans la liste de nombre
    for i in range(1, num_combinations+1):
        if excluded_multiples is None or i % excluded_multiples !=0:
            #Pour chaque string dans strings
            for string in strings:
                    #concatener la string et le nombre
                    #ajouter ca a la liste de resultat
                    result.append(string+ str(i))

    # result = [
    #     string +str(i)
    #             for i in range(1, num_combinations+1)
    #             if excluded_multiples is None or i% excluded_multiples !=0
    #                 for string in strings
    # ]

    return result
    # return [
    #     string +str(i)
    #     for i in range(1, num_combinations+1)
    #     if excluded_multiples is None or i% excluded_multiples !=0
    #         for string in strings]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))

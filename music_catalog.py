import sys
from linked_list import *
from array_list import *

def looper(lst, sorting_choice):
	print("Song Catalog\n" + "   1) Print Catalog\n" + "   2) Song Information\n" + "   3) Sort\n" + "   4) Add Songs\n" + "   0) Quit\n")
	choice = int(input("Enter Selection: "))

	if choice == 1:
		catalog(lst, sorting_choice)

	elif choice == 2:
		choice_2(lst, sorting_choice)

	elif choice == 3:
		choice_3(lst, sorting_choice)

	elif choice == 4:
		choice_4(lst, sorting_choice)

	elif choice == 0:
		sys.exit()

def choice_1(file, song_list, sorting_choice):
    txt_file = open(file, "r")
    lines_music = txt_file.readlines()
    song_list = empty_list()
    accumu = 0
    error = 0
    print("\nCatalog input errors:")
    for line in lines_music:
        line = line.strip()
        error += 1
        if line != "" and len(line.split("--")) == 3:
            song_list = add(song_list, length(song_list), str(accumu) + "--" + line)
            accumu += 1
        elif line != "" and len(line.split("--")) != 3:
            print("line " + str(error) + ": malformed song information")
    print("")
    looper(song_list, sorting_choice)

def catalog(song_list, sorting_choice):
    for i in range(length(song_list)):
        print(song_list.lst[i])
    print("")
    looper(song_list, sorting_choice)

def choice_2(song_list, sorting_choice):
    song_choice = int(input("Enter song number: "))
    x = get(song_list, song_choice)
    y = x.split("--")
    print("\nSong information ...\n" + "   Number: " + y[0] + "\n   Title: " + y[1] + "\n   Artist: " + y[2] + "\n   Album: " + y[3] + "\n")
    looper(song_list, sorting_choice)

def choice_3(song_list, sorting_choice):
	print("Sorting Choice:\n" + "   1) Artist\n" + "   2) Album\n" + "   3) Title\n" + "   4) Number\n")
	sort_choice = int(input("Enter Selection: "))
	if sort_choice == 1:
		looper(sort(song_list, artist_comp), 1)
	elif sort_choice == 2:
		looper(sort(song_list, album_comp), 2)
	elif sort_choice == 3:
		looper(sort(song_list, title_comp), 3)
	elif sort_choice == 4:
		looper(sort(song_list, number_comp), 4)

def choice_4(song_list, sorting_choice):
	txt_choice = input("Enter File Name: ")
	new_txt_file = open(txt_choice, "r")
	new_lines_music = new_txt_file.readlines()
	accumulator = length(song_list)
	error = 0
	print("\nCatalog input errors:")
	for line in new_lines_music:
		line = line.strip()
		error += 1
		if line != "" and len(line.split("--")) == 3:
			song_list = add(song_list, length(song_list), str(accumulator) + "--" + line)
			accumulator += 1
		elif line != "" and len(line.split("--")) != 3:
			print("line " + str(error) + ": malformed song information")
	print("")
	if sorting_choice == 1:
		looper(sort(song_list, artist_comp), 1)
	elif sorting_choice == 2:
		looper(sort(song_list, album_comp), 2)
	elif sorting_choice == 3:
		looper(sort(song_list, title_comp), 3)
	elif sorting_choice == 4:
		looper(sort(song_list, number_comp), 4)

#artist -> album -> title -> number
def artist_comp(value1, value2):
	x = value1.split("--")
	y = value2.split("--")
	if x[2] < y[2]:
		return True
	elif x[2] > y[2]:
		return False
	elif x[2] == y[2]:
		album_comp(value1, value2)

def album_comp(value1, value2):
	x = value1.split("--")
	y = value2.split("--")
	if x[3] < y[3]:
		return True
	elif x[3] > y[3]:
		return False
	elif x[3] == y[3]:
		title_comp(value1, value2)

def title_comp(value1, value2):
	x = value1.split("--")
	y = value2.split("--")
	if x[1] < y[1]:
		return True
	elif x[1] > y[1]:
		return False
	elif x[1] == y[1]:
		number_comp(value1, value2)

def number_comp(value1, value2):
	x = value1.split("--")
	y = value2.split("--")
	if int(x[0]) < int(y[0]):
		return True
	elif int(x[0]) > int(y[0]):
		return False

song_list = empty_list()
song_list = choice_1(sys.argv[1], song_list, 4)

















































from characters import characters

# # with open('characters.py', 'r') as got:
# #     for i in got:
# #         print(i)

# print(characters[0].keys()

# dict_keys(['url', 'allegiances', 'died', 'aliases', 'spouse', 'father', 'name', 'gender',
#            'books', 'born', 'culture', 'tvSeries', 'playedBy', 'titles', 'mother', 'povBooks'])

# example of creating function for finding the first letter of a value in a key

# def how_many_starts_with(letter):
#   count = 0
#   for i in characters:
#     if i['name'].startswith(letter):
#       count += 1
#   # print(A)
#   return count

# starts = how_many_starts_with("Q")

# print(starts)

# How many characters names start with "A"? 168

# A = 0

# for i in characters:
#   if i['name'].startswith('A'):
#     A+= 1
# print(A)

#     # How many characters names start with "Z"? 8

# # Z = 0

# # for i in characters:
# #   if i['name'].startswith('Z'):
# #     Z += 1
# # print(Z)

# # How many characters are dead? 553

# # dead = 0

# # for i in characters:
# #     if i['died'] == '':
# #         print ("they are alive")
# #     else:
# #         dead+= 1

# # print(dead)

# # Who has the most titles?

# title_lengths = []
# for person in characters:
#   # get the length of the 'titles' key /
#   num_titles = len(person['titles'])
#   title_lengths.append(num_titles)

# record_for_most_titles = max(title_lengths)
# print(record_for_most_titles)

# index_of_record = title_lengths.index(record_for_most_titles)

# # print(index_of_record) /

# person_with_title_record = characters[index_of_record]
# print(person_with_title_record['name'])

# How many are Valyrian? 57

# V = 0

# for i in characters:
#   if i["culture"] == 'Valyrian':
#     V += 1

# print(V)

# What actor plays "Hot Pie" (and don't use IMDB)?

for person in characters:
  if person['name'] == 'Hot Pie':
    print("We found Hot Pie.")
    print(person['playedBy'][0])

# How many characters are * not* in the tv show?

# Produce a list characters with the last name "Targaryen"? 49

# T = 0

# for i in characters:
#   split_name = i['name'].split()
#   if len(split_name) == 2 and split_name[1] == 'Targaryen':
#     T += 1
# print(T)

# Create a histogram of the houses(it's the "allegiances" key)

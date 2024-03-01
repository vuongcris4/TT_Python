f = open("dictionary.txt", "r")
dic = str(f.read().lower())

dictionary_database = []
for line in dic.split("\n")[:-1]:
    item = line.split(": ")
    each_word = dict(word=item[0], meaning=item[1])
    dictionary_database.append(each_word)

for each_word in dictionary_database:
    print(each_word)

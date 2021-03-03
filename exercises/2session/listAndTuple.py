# Exercise 0.1: Slicing

listA = ['Hello', 'World', 'Huston', 'we', 'are', 'here']

# 1
print (listA[1:-1])
# 2
print(listA[0:2])
# 3
print(listA[-2:])
# 4
print(listA[-2:-1])
# 5
print(listA[0::2])
# 6 
print(listA[::-1])
# 7
tupleA = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
listB = list(tupleA)[1:-1]
print(listB)
# 8
strA = 'Hello World Huston we are here'
print(strA[6:21])

# Exercise 1: Build-in-functions on lists

# testet in intepretor
# https://docs.python.org/3/library/functions.html

# Exercise 2: Sort a text

def rmVowels(s) :
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')

    for x in s.lower():
        if x in vowels:
            s = s.replace(x, '') 
    s = sorted(s)
    return ''.join([str(elem) for elem in s])

print(rmVowels('abcdefghijklmnopqrstuvwxyz'))

# Exercise 3: Sort a list

# 1.
l = ['Ib','Erik','Anders','Mowgli','Tom','Anakin','Lucifer','Hannibal','Jerry','Pedro','Darth Vader']

# 2.
print(sorted(l))

# 3.
print(sorted(l, reverse=True))

# 4.
print(sorted(l, key=len))

# 5.
print(sorted(l, key=lambda s: str(s[-1:])))

# 6.
def a_is(s):
    if 'a' in s.lower():
        return False
    return True

print(sorted(l, key=a_is))

# Exercise 4: Files

# 1. Create a file and call it lyrics.txt (it does not need to have any content)
lyrics = open('lyrics.txt', 'w')

# 2. Create a new file and call it songs.docx and in this file write 3 lines of text to it.
songs = open('songs.docx', 'w')
songs.write('This is a line\nThis is also a line\nThis is the third line\n')

# 3. open and read the content and write it to your terminal window.
# * you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

#read()
songs = open('songs.docx', 'r')
print(songs.read())
songs.close()

#readline()
songs = open('songs.docx', 'r')
print(songs.readline())
print(songs.readline())
print(songs.readline())
songs.close()

#readline() with loop
songs = open('songs.docx', 'r')
for x in songs:
    print(x)

#readlines()
songs = open('songs.docx', 'r')
print(songs.readlines())
songs.close()

# Exercise 5: Sort a list of tuples

# Based on list of tuple underneath
listOfTuples = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
# sort the list so the result looks like this: [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]

def lastElm(t):
    return (t[-1], t[0])
print(sorted(listOfTuples, key=lastElm))

#oneliner solution 
print(sorted(listOfTuples, key= lambda x: (x[-1], x[0])))
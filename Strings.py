# while loop through strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

# for loop through strings
fruit = 'banana'
for letter in fruit:
    print(letter)

# slicing strings
fruit = 'apple'
slice = fruit[0:2]
print(slice)

slice2 = fruit[:2]
slice3 = fruit[1:]

# string concatenation
a = 'Hello'
b = 'World'
print(a + ' ' + b)

# using 'in' as a logical operator
fruit = 'berry'
if 'e' in fruit:
    print('Found it')

# string comparison
word = 'soccer'
if word == 'soccer':
    print('Yup')

if word < 'banana':
    print(word + ' comes before banana')

if word > 'banana':
    print(word + ' comes after banana')

# String library exists since it's object
# make a lower case copy without changing the original
greet = 'Hello Jason'
informal = greet.lower()
print(informal)
print(greet)

# show string methods
dir('Hello World')

# search for first occurence in a string
fruit = 'cherry'
pos = fruit.find('er')
print(pos)

pos2 = fruit.find('z')
print(pos2)

# extract url from your email in a time stamp
# you know @ precedes and and ' ' succeeds url
timestamp = 'jason.paulose@capgemini.com 10:35 2021'
startPos = timestamp.find('@')
endPos = timestamp.find(' ', startPos)
url = timestamp[startPos + 1: endPos]
print(url)

# Write code using find() and string slicing (see section 6.10) to extract 
# the number at the end of the line below. Convert the extracted value to a 
# floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
startPos = text.find(':')
rawSlice = text[startPos + 1:]
cleanSlice = rawSlice.strip()
fpValue = float(cleanSlice)
print(fpValue)
 # String Based Problems
'''Q1 Write a program to reverse a string.'''

s = input("Enter a string :")
reverse_string=s[::-1]
print("Reversed string is ",reverse_string)
Reversed string is  .anexaS tahskA si eman yM
'''Q2 Check if a string is a palindrome.'''

k = input("Enter a string :")
removed_whitespaces = k.replace(" ", "").lower()
reversed = removed_whitespaces[::-1]
if reversed == removed_whitespaces:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
The input string is not a palindrome.
'''Q3 Convert a string to uppercase.'''

a = input("Enter a string :")
uppercase_string = a.upper()
print("Uppercase string is ",uppercase_string)
Uppercase string is  MY NAME IS AKSHAT SAXENA.
'''Q4 Convert a string to lowercase.'''

a = input("Enter a string :")
lowercase_string = a.lower()
print("Lowercase string is ",lowercase_string)
Lowercase string is  my name is akshat saxena.
'''Q5 Count the number of vowels in a string.'''

b = input("Enter a string :")
vowels = b.count("A") + b.count("E") + b.count("I") + b.count("O") + b.count("U") + b.count("a") + b.count("e") + b.count("i") + b.count("o") + b.count("u")
print("Number of vowels in string provided is ",vowels)
Number of vowels in string provided is  8
'''Q6 Count the number of consonants in a string.'''

consonant = 0
s = input("Enter a string :")
length = len(s)
v = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
for i in range(length):
    if s[i] in v:
        consonant += 1
print("Number of consonants in string provided is ",consonant)
Number of consonants in string provided is  12
'''Q7 Remove all whitespaces from a string.'''

string = input("Enter a string :")
modified_string = ""
for i in string:
    if i != " ":
        modified_string += i
print("Modified string without spaces is ",modified_string)
Modified string without spaces is  MynameisAkshatSaxena.
'''Q8 Find the length of a string without using the `len()` function.'''

count = 0
string = input("Enter a string :")
for i in string:
    count += 1
print("Length of string provided is ",count)
Length of string provided is  25
'''Q9 Check if a string contains a specific word.'''

string = input("Enter a string :")
word = input("Enter the specific word to be checked :")
if word in string:
    print(word ,"is present in string")
else:
    print(word ,"is not present in string")
IS is not present in string
'''Q10 Replace a word in a string with another word.'''

string = input("Enter a string :")
word = input("Enter the specific word to be replaced :")
new_word = input("Enter the new word :")
replace_string = string.replace(word , new_word)
print("New string with replaced word is ",replace_string)
New string with replaced word is  Today is Monday.
'''Q11 Count the occurrences of a word in a string.'''

word_count = 0
string = input("Enter a string :")
word = input("Enter the word to be counted :")
f = string.split()
for i in range(len(f)):
    if word == f[i]:
        word_count += 1    
print("The occurances of", word ,"in string provided is",word_count)
The occurances of school in string provided is 1
'''Q12 Find the first occurrence of a word in a string.'''

string = input("Enter a string :")
word = input("Enter the word to be searched :")
o = string.find(word)
if o == -1:
    print("Entered word is not in string")
else:
    print("The first occurance of" ,word ,"is" ,o)
The first occurance of Akshat is 11
'''Q13 Find the last occurrence of a word in a string.'''

string = input("Enter a string :")
length = len(string)
word = input("Enter the word to be searched :")
reverse_string = string[::-1]
l = reverse_string.find(word[::-1])
if l == -1:
    print("Entered word is not in string")
else:
    print("The last occurance of" ,word ,"is" ,length - l -len(word))
The last occurance of Hello is 6
'''Q14 Split a string into a list of words.'''

string = input("Enter a string :")
word_split = input("Enter the word to split the string on :")
l = string.split(word_split)
print("Splitted string is ",l)
Splitted string is  ['My', 'name', 'is', 'Akshat', 'Saxena', '.']
'''Q15 Join a list of words into a string.'''

list_of_words = eval(input("Enter list of words :"))
joined = ' '.join(list_of_words)
print("Joined list of words into a string is ",joined)
Joined list of words into a string is  I study in PW SKILLS
'''Q16 Convert a string where words are separated by spaces to one where words
are separated by underscores.'''

string = input("Enter a string separated by spaces :")
print("String separated by spaces is ",string)
underscore = string.replace(" ","_")
print("String separated by underscores is ",underscore)
String separated by spaces is  My name is Akshat Saxena .
String separated by underscores is  My_name_is_Akshat_Saxena_.
'''Q17 Check if a string starts with a specific word or phrase.'''

string = input("Enter a string :")
word = input("Enter a word or phrase :")
check = string.startswith(word)
if check == True:
    print("The string starts with ", word)
else:
    print("The string does not starts with ", word)
The string does not starts with  study
'''Q18 Check if a string ends with a specific word or phrase.'''

string = input("Enter a string :")
word = input("Enter a word or phrase :")
check = string.endswith(word)
if check == True:
    print("The string ends with ", word)
else:
    print("The string does not ends with ", word)
The string ends with  PW SKILLS
'''Q19 Convert a string to title case (e.g., "hello world" to "Hello World").'''

string = input("Enter a string :")
t = string.title()
print("Title cased string is",t)
Title cased string is I Study In Pw Skills
'''Q20 Find the longest word in a string.'''

string = input("Enter a string :")
L =[]
k = string.split()
for i in range(len(k)):
    L.append(len(k[i]))
    max_num = max(L)
    index_word = L.index(max_num)
print("The longest word in the string provided is", k[index_word])
The longest word in the string provided is Akshat
'''Q21 Find the shortest word in a string.'''

string = input("Enter a string :")
L =[]
k = string.split()
for i in range(len(k)):
    L.append(len(k[i]))
    min_num = min(L)
    index_word = L.index(min_num)
print("The shortest word in the string provided is", k[index_word])
The shortest word in the string provided is I
'''Q22 Reverse the order of words in a string.'''

string = input("Enter a string :")
reverse_string = ""
k = string.split()
for i in k :
    reverse_string += i[::-1]
    reverse_string += " "
print("String after reversing the order of words is", reverse_string)
String after reversing the order of words is yM eman si tahskA anexaS . 
'''Q23 Check if a string is alphanumeric.'''

string = input("Enter a string :")
check = string.isalnum()
if check:
    print("String is alphanumeric")
else:
    print("String is not alphanumeric")
String is not alphanumeric
'''Q24 Extract all digits from a string.'''

string = input("Enter a string :")
digit = " "
for i in string :
    if i.isdigit() :
        digit += i
print("Extracted digits from string are", digit) 
Extracted digits from string are  1812
'''Q25 Extract all alphabets from a string.'''

string = input("Enter a string :")
alphabets = " "
for i in string :
    if i.isalpha() :
        alphabets += i
print("Extracted alphabets from string are", alphabets)
Extracted alphabets from string are  IamyearsoldIstudyinclassth
'''Q26 Count the number of uppercase letters in a string.'''

string = input("Enter a string :")
count = 0
for i in string :
    if i.isupper() :
        count += 1
print("The number of uppercase letters in the string are", count)
The number of uppercase letters in the string are 3
'''Q27 Count the number of lowercase letters in a string.'''

string = input("Enter a string :")
count = 0
for i in string :
    if i.islower() :
        count += 1
print("The number of lowercase letters in the string are", count)
The number of lowercase letters in the string are 17
'''Q28 Swap the case of each character in a string.'''

string = input("Enter a string :")
new_string = ""
for i in string :
    new_string += i.swapcase()
print("Swapped case string is", new_string)
Swapped case string is mY NAME IS aKSHAT sAXENA .
'''Q29 Remove a specific word from a string.'''

string = input("Enter a string :")
new_string = ""
a = True
while a :
    word = input("Enter a word to be removed :")
    if word in string.split() :
        a = False
    else :
        print("Enter valid word to be removed")
s = string.split()
for i in s :
    if i != word :
        new_string += i
        new_string += " "
print("String after removing specific word is", new_string)
Enter valid word to be removed
Enter valid word to be removed
String after removing specific word is My name is Saxena . 
'''Q30 Check if a string is a valid email address.'''

import re

def check_valid_email(email) :
    regular_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(regular_pattern , email) :
        return "valid email"
    else :
        return "invalid email"

email_1 = "hello@email.com"
email_2 = "invalid*email"
output_1 = check_valid_email(email_1)
output_2 = check_valid_email(email_2)
print("email_1 is ", output_1)
print("email_2 is ", output_2)
email_1 is  valid email
email_2 is  invalid email
'''Q31 Extract the username from an email address string.'''


def extract_username(e):
    u = e.split("@")[0]
    return u

email = input("Enter a email address :")
username = extract_username(email)
print("Username is ", username)
Username is  akshat
'''Q32 Extract the domain name from an email address string.'''

def extract_domain_name(e):
    d = e.split("@")[1]
    return d

email = input("Enter a email address :")
domain_name = extract_domain_name(email)
print("Domain name is ", domain_name)
Domain name is  email.com
'''Q33 Replace multiple spaces in a string with a single space.'''

def replace_multiple_spaces(s) :
    new_string = " ".join(s.split())
    return new_string
    
string = input("Enter a string :") # "  akshat hello    how  are you    "
output = replace_multiple_spaces(string)
print("String after replacing multiple spaces is ",output)          
String after replacing multiple spaces is  akshat hello how are you
'''Q34 Check if a string is a valid URL.'''

from urllib.parse import urlparse
def check_valid_url(url):
    try :
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError :
        return False

url_1 = "https://www.youtube.com/"
url_2 = "invalid*url"
output_1 = check_valid_url(url_1)
output_2 = check_valid_url(url_2)
print("url_1 is ", output_1)
print("url_2 is ", output_2)
url_1 is  True
url_2 is  False
'''Q35 Extract the protocol (http or https) from a URL string.'''

def extract_protocol(url) :
    index = url.find("://")
    if index != -1 :
        return url[:index]
    else :
        return "No protocol"
            
url_1 = input("Enter 1st url :")
url_2 = input("Enter 2nd url :")
url_3 = input("Enter 3rd url :")

protocol_1 = extract_protocol(url_1)
protocol_2 = extract_protocol(url_2)
protocol_3 = extract_protocol(url_3)

print("Protocol 1 is ",protocol_1)
print("Protocol 2 is ",protocol_2)
print("Protocol 3 is ",protocol_3)
Protocol 1 is  http
Protocol 2 is  ftp
Protocol 3 is  https
'''Q36 Find the frequency of each character in a string.'''

string = input("Enter a string :")
new_string = ""
dictionary = {}
for i in string :
    if i not in new_string :
        dictionary[i] = 1
        new_string += i
    else :
        dictionary.update({i : dictionary[i] + 1})
for i , k in dictionary.items() :
    print("Frequency of ", i ,":" , k)
Frequency of  h : 1
Frequency of  e : 1
Frequency of  l : 3
Frequency of  o : 2
Frequency of  w : 1
Frequency of  r : 1
Frequency of  d : 1
'''Q37 Remove all punctuation from a string.'''

import string
def remove_puntuations(input_string) :
    translator = str.maketrans("","",string.punctuation)
    clean_string = input_string.translate(translator)
    return clean_string
    
input_string = input("Enter a string :")
cleaned_string = remove_puntuations(input_string)
print("Original string :",input_string)
print("Cleaned string :",cleaned_string)
Original string : Hello, Rahul! What's up?
Cleaned string : Hello Rahul Whats up
'''Q38 Check if a string contains only digits.'''

string = input("Enter a string :")
if string.isdigit() :
    print("String contains only digits")
else :
    print("String does not contains only digits")
String contains only digits
'''Q39 Check if a string contains only alphabets.'''

string = input("Enter a string :")
if string.isalpha() :
    print("String contains only alphabets")
else :
    print("String does not contains only alphabets")
String does not contains only alphabets
'''Q40 Convert a string to a list of characters.'''

string = input("Enter a string :")
convert = list(string)
print("Converted string to a list of characters :",convert)
Converted string to a list of characters : ['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'A', 'k', 's', 'h', 'a', 't', ' ', 'S', 'a', 'x', 'e', 'n', 'a', ' ', '.']
''' Q41 Check if two strings are anagrams.'''

string_1 = input("Enter 1st string :") #worth
string_2 = input("Enter 2nd string :") #throw
new_string1 = ""
new_string2 = ""
dictionary_1 = {}
dictionary_2 = {}

#Checking 1st string
for i in string_1 :
    if i not in new_string1 :
        dictionary_1[i] = 1
        new_string1 += i
    else :
        dictionary_1.update({i : dictionary_1[i] + 1})
        
#Checking 2nd string
for i in string_2 :
    if i not in new_string2 :
        dictionary_2[i] = 1
        new_string2 += i
    else :
        dictionary_2.update({i : dictionary_2[i] + 1})
        
#Comparing both dictionaries
if dictionary_1 == dictionary_2 :
    print("Both strings are amagrams")
else :
    print("Bothe strings are not amagrams")
Both strings are amagrams
'''Q42 Encode a string using a Caesar cipher.'''

#defining function Caesar_cipher
def Caesar_cipher(text , shift) :
    encoded_text = ""
    for char in text :
        if char.isalpha() :
            encoded_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else :
            encode_char = char
        
        encoded_text += encoded_char
    
    return encoded_text
    
#Defining the input text and shift value for encoding
string = input("Enter a string to encode :")
shift = int(input("Enter shift value for encoding :"))

#Calling function Caesar_cipher
encoded_text = Caesar_cipher(string , shift)
            
#Printing the encoded text
print("Encoded text :", encoded_text)
Encoded text : wmujcvvoczgpc
'''Q43 Decode a Caesar cipher encoded string.'''

#Defining function Caesar_cipher_decode
def Caesar_cipher_decode(text , shift) :
    decoded_text = ""
    for char in text :
        if char.isalpha() :
            decoded_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else :
            decoded_char = char
        
        decoded_text += decoded_char
        
    return decoded_text


#defining input text and shift value for decoding
string = input("Enter a string to decode :")
shift = int(input("Enter shift value for decoding :"))

#Calling function Caesar_cipher_decode
decoded_text = Caesar_cipher_decode(string , shift)

#Printing the decoded text
print("Decoded text :", decoded_text)
Decoded text : fcjjm fmu ypc wms
'''Q44 Find the most frequent word in a string.'''

string = input("Enter a string :")
arrange_words = string.split()
frequency = {}
for i in arrange_words :
    if i in frequency :
        frequency[i] += 1
    else :
        frequency[i] = 1

frequent = max(frequency.values())
for i in frequency :
    if frequency[i] == frequent :
        print("Most frequent word is ", i ," with ", frequent ,"times repetition")  
Most frequent word is  world  with  3 times repetition
'''Q45 Find all unique words in a string.'''

string = input("Enter a string :")
arrange_words = string.split()
unique_words = set()
for i in arrange_words :
    unique_words.add(i)
    
print("All unique words in string are :")
for i in unique_words :
    print(i)
All unique words in string are :
felt
the
feel
others
were
really
saw
because
happy,
wasn't
and
but
happy.
I
knew
happy
should
'''Q46 Count the number of syllables in a string.'''

def syllables(string) :
    arrange_words = string.split()
    count = 0
    for word in arrange_words :
        for char in word :
            if char in ["a","e","i","o","u","A","E","I","O","U"] :
                count += 1
    return count
string1 = input("Enter 1st string :")
string2 = input("Enter 2nd string :")

syllable_1 = syllables(string1)
syllable_2 = syllables(string2)


print("The number of syllables in the", string1, " are ", syllable_1)
print("The number of syllables in the ", string2, "are  ", syllable_2) 
The number of syllables in the Mat  are  1
The number of syllables in the  Game are   2
'''Q47 Check if a string contains any special characters.'''

import re

def check_special_characters(string) :
    pattern = re.compile(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/]')
    match = pattern.search(string)
    return bool(match)

string_1 = input("Enter 1st string :")
string_2 = input("Enter 2nd string :")

result_1 = check_special_characters(string_1)
result_2 = check_special_characters(string_2)

print(f"'{string_1}' contains special characters:", result_1)
print(f"'{string_2}' contains special characters:", result_2)
'Hello! How are you?' contains special characters: True
'Let's go! It's showtime .' contains special characters: True
'''Q48 Remove the nth word from a string.'''

string = input("Enter a string :")
nth_value = int(input("Enter nth word to be removed :"))
arrange_words = string.split()
if nth_value >=1 and nth_value <= len(arrange_words) :
    removed_word = arrange_words.pop(nth_value-1)
    cleaned_string = " ".join(arrange_words)
print("Original string :", string)
print("Cleaned string :", cleaned_string)
print("Removed word :", removed_word)
Original string : Please bring your books with you to every class.
Cleaned string : Please bring books with you to every class.
Removed word : your
'''Q49 Insert a word at the nth position in a string.'''

string = input("Enter a string :")
nth_value = int(input("Enter nth value to insert word :"))
word = input("Enter word to be inserted :")
arrange_words = string.split()
if nth_value >=1 and nth_value <= len(arrange_words) :
    arrange_words.insert(nth_value - 1 , word)
    cleaned_string = " ".join(arrange_words)
print("Original string :", string)
print("Cleaned string :", cleaned_string)
Original string : Please bring books with you to every class.
Cleaned string : Please bring your books with you to every class.
'''Q50 Convert a CSV string to a list of lists.'''

def csv_string_list(string) :
    new_list = []
    lines = string.split("\n")
    for line in lines:
        fields = line.split(",")
        new_list.append(fields)

    return new_list

string = "Roll No., Name, Marks\n01, Rahul, 79\n02, Sonu, 89"
list_of_lists = csv_string_list(string)

for row in list_of_lists :
    print(row)
['Roll No.', ' Name', ' Marks']
['01', ' Rahul', ' 79']
['02', ' Sonu', ' 89']
 

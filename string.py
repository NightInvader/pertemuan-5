# String
# String di python dapat dideklarasi dengan single ('') atau double ("") quote,
# sebab python sangat sensitif dengan spasi, 
# maka gunakan tiga single atau double quote untuk mendeklarasikan multiline string

theString = "Hello World"

thesMultiLineString = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# NOTE
# String adalah list (array), 
# maka kita bisa gunakna segala macam operasi list pada string

print(len(theString))

for x in theString:
    print(x)

if "Hello" in theString:
    print("Hi")

# Slicing
# Kalian dapat bereksperimen dengan kode di bawah dengan cara menghapus salah satu angka atau menambahkan negatif
print(theString[2:5])

# Escape Character
# Escape Character digunakan saat kalian ingin menggunakan sebuah character atau symbol yang dapat mengganggu string
print("I am \"ironman\"")

# Formatter
# Formatter membantu kalian untuk membuat string yang lebih dinamis
profession = "programmer"
verb = "slacking"
text = "i am a {}, and i will {}"
print(text.format(profession, verb))

# String method
# String method adalah fungsi-fungci yang dapat dioperasikan pada string
print(theString.upper())
print(theString.lower())
# NOTE
# python memiliki banyak string method, kalian dapat melihatnya di https://www.w3schools.com/python/python_strings_methods.asp


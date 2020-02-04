#Please write a program that reads a text file containing some text and for each word in the file counts how many times it
#appears. Please note you can use a dictionary structure. Before starting to count words it might be necessary to delete
#all punctuation and special symbols (new line, tab etc.) and put all words in lower case.

#Get rid of dots, commas etc
def ClearSymbols(a):
    a = a.replace(chr(10)," ")
    for i in range(1,10): #\n == chr(10)
        a=a.replace(chr(i),"")
    for i in range(11, 32):  # space == chr(32)
        a = a.replace(chr(i), "")
    for i in range(33,48):
        a=a.replace(chr(i),"")
    for i in range(58,64):
        a=a.replace(chr(i),"")
    for i in range(91,97):
        a=a.replace(chr(i),"")
    for i in range(123,127):
        a=a.replace(chr(i),"")
    return a

#Load txt file:
f = 't.txt'
with open(f, 'r') as infile: # 'r' == read
    myText = infile.read()
    myText = ClearSymbols(myText)
    dict = {}
    space = myText.find(" ")
    word = myText[:space]
    word = word.lower()
    while space>0:
        try:
            a = dict[word]
            a = a+1
            dict[word]=a
        except:
            dict[word]=1
        finally:
            myText = myText[-len(myText)+space+1:]
            space = myText.find(" ")
            word = myText[:space]
            word = word.lower()
    try:
        a = dict[myText]
        a = a + 1
        dict[myText] = a
    except:
        dict[myText] = 1
    print(dict)


    class Triangle(Shape):
        def tri_surface(self):
            s = (self._a + self._b + self._c) / 2
            return (s * (s - self._a) * (s - self._b) * (s - self._c)) ** 0.5
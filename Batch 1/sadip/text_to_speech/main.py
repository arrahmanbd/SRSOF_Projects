import pyttsx3
import PyPDF3
book=open('ops.pdf','rb')
pdfReader=PyPDF3.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
friend=pyttsx3.init()
for num in range(7,pages):
    page= pdfReader.getPage(num)
    text= page.extractText()
    friend.say(text)
    friend.runAndWait()
    
    
    
    




import pyttsx3
import PyPDF3

with open("ops.pdf", "rb") as book:
    pdfReader = PyPDF3.PdfFileReader(book)
    friend = pyttsx3.init()
    for num in range(7, pdfReader.numPages):
        text = pdfReader.getPage(num).extractText()
        friend.say(text)
        friend.runAndWait()

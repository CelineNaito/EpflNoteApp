
from flask import Flask
from flask import request

app = Flask(__name__)

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content


@app.route("/")
def home():
    return get_html("index")


@app.route("/add")
def add():
    return get_html("add")

@app.route("/result")
def result():
    return get_html("result")

@app.route("/view")
def view():
    return get_html("view")

@app.route("/save_note")
def save_note():
    #html_page= get_html("add") est-ce que get "q" suffit à trouver la source html???
    new_note= request.args.get("q")
    notes= open("noteapp.text","a")
    notes.write(new_note+ "\n")
    notes.close()
    #print ("new note saved")il faudrait l'intégrer dans une page html
    return get_html("add")






#choice = input("what do you want to do? 1 Enter a new note; 2 Search your notes; 3 Quit the notepad ")



def enter_note():
    note = open("noteapp.txt", "a")
    new_line = input("Please enter your note: ")
    note.write (new_line + "\n")
    note.close()

def search_notes():
    noteapp= open("noteapp.text")
    #content = noteapp.read()
    #array = content.split("\n")
    #TypeError: 'str' object cannot be interpreted as an integer
    search_word = input("What word do you want to search? ")
    #result = ""
    found = False
    for line in noteapp:
        
        if line.find(search_word) != -1:
            print(line)
            found = True
        
    if found == False:       
        print("The word you searched was not found")
    noteapp.close()










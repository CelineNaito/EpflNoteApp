
from flask import Flask
from flask import request

app = Flask(__name__)

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_notes():
    notes= open("noteapp.text")
    content= notes.read()
    all_notes = content.split("\n")
    all_notes.pop(len(all_notes)-1)
    notes.close()
    return all_notes

@app.route("/")
def home():
    return get_html("index")


@app.route("/add")
def add():
    return get_html("add")

@app.route("/result")
def result():
    html_page = get_html("result")
    search_value = request.args.get("search_input") #flask is not defined!
    notes = get_notes()

    result = ""

    for note in notes:
      if note.lower().find(search_value.lower()) != -1: 
        result += "<p>" + note + "<p>"

    if result == "":
            result = "<p> no matching note </p>"

           
    return html_page.replace("§§placeholder§§", result)

@app.route("/view")
def view():
    html_page = get_html("view")
    notes_to_show = get_notes()
    actual_values= " "
    for note in notes_to_show:
        actual_values += "<li>" +note + "</li>"
    return html_page.replace ("§§notes§§", actual_values)


@app.route("/save_note")
def save_note():
    #html_page= get_html("add") est-ce que get "q" suffit à trouver la source html???
    new_note= request.args.get("q")
    notes= open("noteapp.text","a")
    notes.write(new_note+ "\n")
    notes.close()
    #print ("new note saved")il faudrait l'intégrer dans une page html
    return get_html("add")



#def enter_note():
    note = open("noteapp.txt", "a")
    new_line = input("Please enter your note: ")
    note.write (new_line + "\n")
    note.close()

#def search_notes():
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










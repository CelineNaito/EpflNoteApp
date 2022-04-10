choice = input("what do you want to do? 1 Enter a new note; 2 Search your notes; 3 Quit the notepad")



def enter_note():
    note = open("noteapp.txt", "a")
    new_line = input("Please enter your note: ")
    note.write (new_line + "\n")
    note.close()
    #the noteapp.txt file does not change...???

def search_notes():
    noteapp= open("noteapp.txt")
    content = noteapp.read()
    array = content.split("\n")
    #TypeError: 'str' object cannot be interpreted as an integer
    search_word = input("What word do you want to search? ")
    result = ""
    
    for line in array:
        if line.find(search_word) != -1:
            print(result)
        else:
            print("The word you searched was not found")
    noteapp.close()

if choice == "1":
    enter_note()
elif choice == "2":
    search_notes()
else:
    quit()








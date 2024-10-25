import os
import time
import ast
from logo import logo
bookshelf =[]

  
def loadFile():
  f = open('file.txt','r')

  for line in f.readlines():
    bookshelf.append(ast.literal_eval(line))

  f.close()

def addBook(title,author,genre):
  newBook ={'title':title,'author':author,'genre':genre}
  bookshelf.append(newBook)
  fp = open("file.txt", 'a')
  fp.write(str(newBook)+" \n")
  fp.close()

def removeBook(title):
  
  for book in bookshelf:
    if book["title"]==title:
      bookshelf.remove(book)
      print(f"The book titled '{title}' has been removed.")

def viewInventory():
  count=1
  if len(bookshelf)>0:
    print("                   CURRENT BOOK INVENTORY LIST")
    print("")
    print("    NAME OF BOOK              AUTHOR                    GENRE")
    for book in bookshelf:
      print(f"{count:2d}. {book['title']:25s} {book['author']:25s} {book['genre']}")
      count+=1
    print("")
    print(f"Total Number of Books in Inventory: {len(bookshelf)}")

def searchByAuthor(author):
  count=1
  for book in bookshelf:
    if book['author']==author:
      print(f"{count}. '{book['title']}', Genre: {book['genre']}")
      count+=1
  print(f"Total Number of Books in Inventory by {author}: {count-1}")
    
def mainMenu():
  print("Main Menu")
  print("1. Add a book")
  print("2. Search for a Book By Author")
  print("3. Remove a book by Title")
  print("4. View Book Inventory")
  print("5. Exit Program")

gameLoop =True
loadFile()
print(logo)
time.sleep(3)# create a pause of 3 seconds
while(gameLoop==True):
  os.system('clear')# clears the console
  mainMenu()
  print("")
  choice = input("Select a Choice from the Main Menu: ")
  print("")
  os.system('clear')
  if choice =='1':
    print("ADDING A BOOK TO THE INVENTORY")
    print("")
    title =input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    addBook(title,author,genre)
  elif choice =='2':
    print("SEARCHING FOR A BOOK FROM INVENTORY...")
    print("")
    author = input("Enter the author of the book: ")
    searchByAuthor(author)
  elif choice =='3':
    print("REMOVING A BOOK FROM INVENTORY...")
    print("")
    title = input("Enter the title of the book: ")
    removeBook(title)
  elif choice=='4':
    viewInventory()
  elif choice =="5":
    gameLoop =False
    print("Thank you for using the Book Inventory System. Have a nice day!")
  print("")
  input("Press 'Enter' to continue...")
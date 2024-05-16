import customtkinter
import threading as th
import cleaner

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x400")
app.title("OpenCleaner")

cleaning = False

header = customtkinter.CTkFrame(master=app, fg_color="#191919" , width=1000, height=35) 
header.pack(expand=True)
header.place(rely=0.0)

appName = customtkinter.CTkLabel(master=header, text="OpenCleaner")
appName.place(relx=0.0 , rely= 0.1)

#declaring the labels but not placing them yet
loadingLabel = customtkinter.CTkLabel(master=app, text="Cleaning...")
loadingLabel2 = customtkinter.CTkLabel(master=app, text="Please wait")

# Root directory (C: on Windows)
root_directory = 'C:\\'
def Cleaning ():
   cleaner.SearchAndDelete(root_directory)
   Finished()

def Clean():
    global cleaning
    if (cleaning is False):
     loadingLabel.place(relx = 0.5 , rely=0.8, anchor=customtkinter.CENTER)
     loadingLabel2.place(relx = 0.5 , rely=0.9, anchor=customtkinter.CENTER)
     processThread = th.Thread(target=Cleaning)
     processThread.start()
     cleaning = True

def Finished ():
       loadingLabel.configure(text="Finished")
       loadingLabel2.configure(text="")
       loadingLabel.update()
       loadingLabel2.update()
       global cleaning
       cleaning = False
   
button = customtkinter.CTkButton(master=app, text="Start cleaning", command=Clean)
button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

app.mainloop()
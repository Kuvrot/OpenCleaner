import customtkinter
import threading as th
import cleaner

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x400")

cleaning = False

header = customtkinter.CTkFrame(master=app, fg_color="#191919" , width=1000, height=35) 
header.pack(expand=True)
header.place(rely=0.0)

appName = customtkinter.CTkLabel(master=header, text="OpenCleaner")
appName.place(relx=0.1 , rely= 0.1)

# Root directory (C: on Windows)
root_directory = 'C:\\'
def Cleaning ():
   cleaner.SearchAndDelete(root_directory)

loadingLabel = customtkinter.CTkLabel(master=app, text="Cleaning...")
loadingLabel2 = customtkinter.CTkLabel(master=app, text="Please wait")

def Clean():
    cleaning = True
    if (cleaning):
     loadingLabel.place(relx = 0.5 , rely=0.8, anchor=customtkinter.CENTER)
     loadingLabel2.place(relx = 0.5 , rely=0.9, anchor=customtkinter.CENTER)
     processThread = th.Thread(target=Cleaning)
     processThread.start()

def Finishing ():
       loadingLabel.update(text="Finished")
       loadingLabel2.update(text="")
   
button = customtkinter.CTkButton(master=app, text="Start cleaning", command=Clean)
button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

app.mainloop()
import os
import shutil
from datetime import datetime
import tkinter as tki
from tkinter import filedialog, messagebox, ttk

def sort_downloads(download_folder, sort_by):
    file_list = os.listdir(download_folder)
    for file_name in file_list:
        file_full_path = os.path.join(download_folder, file_name)
        if os.path.isfile(file_full_path):
            creation_timestamp = os.path.getctime(file_full_path)
            creation_date = datetime.fromtimestamp(creation_timestamp)
            if sort_by == "Date":
                directory_name = creation_date.strftime("%Y-%m-%d")
            else:
                directory_name = os.path.splitext(file_name)[1][1:]
            directory_path = os.path.join(download_folder, directory_name)
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            shutil.move(file_full_path, os.path.join(directory_path, file_name))

def select_directory():
    global download_folder
    download_folder = filedialog.askdirectory()
    entry.delete(0, tki.END)
    entry.insert(0, download_folder)

def sort_files():
    global download_folder
    sort_by = sort_option.get()
    sort_downloads(download_folder, sort_by)
    messagebox.showinfo("Success", "Downloads sorted successfully!")

main_window = tki.Tk()
main_window.title("Files Sorter")
main_window.geometry('500x150')

customFont = (None, 12)

label = tki.Label(main_window, text="File Directory:", font=customFont)
label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

entry = tki.Entry(main_window, width=20, font=customFont)
entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

select_directory_button = tki.Button(main_window, text="Select Directory", command=select_directory, font=customFont)
select_directory_button.grid(row=0, column=2, padx=10, pady=5)

sort_option = ttk.Combobox(main_window, values=["Date", "File Type"], state="readonly", font=customFont)
sort_option.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky='w')
sort_option.set("Date")

sort_button = tki.Button(main_window, text="Sort File", command=sort_files, font=customFont)
sort_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

main_window.mainloop()

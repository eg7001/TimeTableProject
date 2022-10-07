from tkinter import *
import csv
from tkinter import filedialog
root = Tk()
root.config(background="#3c9687")
root.geometry('1060x760')
root.resizable(False, False)
root.title(" TIMETABLE  PROGRAM ")

def del_listbox():
    a = listbox.curselection()
    b = listbox.size()
    asd = []
    for i in range(0,b):
        if i in a:
            asd.append(listbox.get(i))
    listbox.delete(0,END)
    for x in asd:
        listbox.insert(END,x)
    listbox.select_set(0,len(a))

def del_all():
    listbox.delete(0,END)

def gettinv_csv():
        del_listbox()
        x = entry.get()
        with open(x, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            read_csv = []
            for i in csv_reader:
                read_csv.append(i)           
            read_csv = list(filter(lambda x: x, read_csv))  
        for i in read_csv:
            asd = i[0].split()
            z_deg = variable_deg.get()
            z_vit = variable_vit.get()
            if((z_vit==" Choose Year: " or z_vit == "All years") and (z_deg==" Choose Course: " or z_deg == 'All courses')):
                listbox.insert(END,i)
            elif (z_deg==" Choose Course: " or z_deg=='All courses'):
                if z_vit == "All courses" or z_vit == " Choose Year: ":
                    listbox.insert(END,i)
                else:
                    z_vit_int = int(variable_vit.get())*100
                    if((int(asd[1])>= z_vit_int and int(asd[1])<(z_vit_int+100))):
                        listbox.insert(END,i)
            elif (z_vit==" Choose Year: " or z_vit =='All years'):
                if(z_deg == asd[0]):
                    listbox.insert(END,i) 
            else:
                z_vit_int = int(variable_vit.get())*100
                if(asd[0]==z_deg and (int(asd[1])>= z_vit_int and int(asd[1])<(z_vit_int+100))):
                    listbox.insert(END,i)

def display():  
    try:
        gettinv_csv()
    except:
        warning_blank.insert(END,"FILE NOT FOUND")
    else:
        warning_blank.delete(0,END)

def save():
    a = listbox.curselection()
    b = listbox.size()
    asd = []
    for i in range(0,b):
        if i in a:
            asd.append((listbox.get(i)))
    abcd = []
    if len(a) > 6:
        warning_blank.delete(0,END)
        warning_blank.insert(END,"YOU HAVE SELECTED")
        warning_blank.insert(END,"MORE THAN 6 COURSES")
    else:
        warning_blank.delete(0,END)
    for i in asd:
            acdc = str(i)
            aa = acdc.split()
            abcd.append(aa[-3:])
    counter = 0
    for i in abcd:
        for j in abcd:
            if j == i:
                counter +=1
    if counter>len(a):
        warning_blank.delete(0,END)
        warning_blank.insert(END," YOU HAVE SELECTED ")
        warning_blank.insert(END," TWO COURSES THAT ")
        warning_blank.insert(END," TAKE PLACE AT THE SAME TIME")
        warning_blank.insert(END," ")
        warning_blank.insert(END," CHOOSE ANOTHER")
    if warning_blank.size() == 0:
        opened_file = filedialog.asksaveasfile(initialfile='timetable.csv')
        writer = csv.writer(opened_file)
        for i in asd:
            writer.writerow(i)        
        opened_file.close()

frame_zgjedh = Frame(root)
frame_zgjedh.grid(column=1,row=8)

variable_vit = StringVar(root)
variable_vit.set(" Choose Year: ") 
zgjedh_vitin = OptionMenu(frame_zgjedh, variable_vit, 'All years',1, 2, 3,4,5)
    
variable_deg = StringVar(root)
deget = ['All courses',
    "CHI",
    'CS',
    'ECE',
    'ECON',
    'EE',
    'EECS',
    'ENGR',
    'FRE',
    'GER',
    'IE',
    'ISE',
    'LIFE',
    'MATH',
    'MGT',
    'UNI',]
variable_deg.set(" Choose Course: ") 
zgjedh_degen = OptionMenu(frame_zgjedh, variable_deg,*deget)

blank_label1 = Label(root,bg="#3c9687",height=5)
blank_label1.grid(column=1,row=3,rowspan=3)

frame_file_path = Frame(root)
frame_file_path.grid(column=1,row=6,columnspan=3)

blank_label2 = Label(root,bg="#3c9687")
blank_label2.grid(column=1,row=7,pady=60)

blank_label3 = Label(root,bg="#3c9687")
blank_label3.grid(column=1,row=9,pady=50)

frame_button = Frame(root)
frame_button.grid(column=1,row=10)

blank_label4 = Label(root, bg='#3c9687',height=5)
blank_label4.grid(column=1,row=11,rowspan=3)

frame_per_klasat = Frame(root,bg="#3c9687")
frame_per_klasat.grid(column=3,row=14,rowspan=10)

frame_warnings = Frame(root,bg='#3c9687')
frame_warnings.grid(column=1,row=14,rowspan=1)

warning_text_label = Label(frame_warnings,text="WARNINGS: ",font=("arial",15))
warning_text_label.grid(row=0,column=0)

warning_blank = Listbox(frame_warnings,width=30,height=8)
warning_blank.grid(row=1,column=1)

label_i_emrit = Label(root,
    text=" TIMETABLE MANAGMENT PROGRAM ",
    font=("Arial",20,"bold"),
    bg="#3c9687")

label_i_emrit.grid(row=0,column=1,columnspan=3)

zgjedh_vitin.pack(side=LEFT)
zgjedh_degen.pack(side=RIGHT)

entry = Entry(frame_file_path,font=("Arial",20))
entry.grid(row=0,column=2)


label_per_input = Label(frame_file_path,text="ENTER FILE PATH: ",)
label_per_input.grid(row=0,column=1)

courses_text = Label(frame_per_klasat,text="COURSES: ",font=("arial",15))
courses_text.grid(column=0,row=0)

display_button = Button(frame_button,text="Display",command=display)
clear_button = Button(frame_button,text="Clear",command=del_all)
save_button = Button(frame_button,text="Save",command=save)

display_button.pack(side=LEFT)
clear_button.pack(side=LEFT)
save_button.pack(side=LEFT)

listbox = Listbox(frame_per_klasat,width=100,selectmode="multiple")
listbox.grid(row=1,column=1)

root.mainloop()
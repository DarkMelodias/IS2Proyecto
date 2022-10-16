from tkinter import *
from tkcalendar import Calendar 
from datetime import datetime
  
root = Tk() 
  
root.geometry("400x400") 
  
cal = Calendar(root, selectmode = 'day', 
               year = 2020, month = 5, 
               day = 22, hour = 14, minute = 0, second = 0) 
  
cal.pack(pady = 20) 
  
def grad_date(): 
    dat = cal.get_date()
    d,y,m,dater = "","","",""
    if dat[1] == "/":
        d = dat[0]
        if dat[3] == "/":
            m = dat[2]
            y = dat[4:6]
        else:
            m = dat[2:4]
            y = dat[5:7]
    else:
        d = dat[0:2]
        if dat[4] == "/":
            m = dat[3]
            y = dat[5:7]
        else:
            m = dat[3:5]
            y = dat[6:8]
    # print(d)
    # print(m)
    # print(y)
    dater = y+"/"+m+"/"+d

    # print(dater)
  
Button(root, text = "Get Date", 
       command = grad_date).pack(pady = 20) 
  
date = Label(root, text = "") 
date.pack(pady = 20) 
  
root.mainloop()


datetime.fromisoformat('2011-11-04T00:05:23')
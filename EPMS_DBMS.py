from tkinter import *
import sqlite3
#import matplotlib.pyplot as plt 
#import pandas as pd
from datetime import * 
from tkinter import messagebox

#root=Tk()
#root.configure(bg='gray27')
#root.title('EPMS')

#conn=sqlite3.connect('epms.db')

def main():
    

    def emp():

        def back():
            top.destroy()
            #print('hi')
            main()

        def new():

            def back2():
                n.destroy()
                #print('hi')
                main()

            def data_in():
                conn=sqlite3.connect('epms.db')
                c=conn.cursor()
                c.execute('SELECT MAX(oid) FROM epms')
                oidc=c.fetchall()
                for data in oidc:
                    oid=data
                    #print(oid)
                if oid[0]==None:
                    c.execute('INSERT INTO epms VALUES(:name,:des,:eno,:status)',
                {
                    'name':name.get(),
                    'des':des.get(),
                    'eno':2020+1,
                    'status':"Employed"
                })
                else:
                    c.execute('INSERT INTO epms VALUES(:name,:des,:eno,:status)',
                    {
                        'name':name.get(),
                        'des':des.get(),
                        'eno':oid[0]+2020+1,
                        'status':"Employed"
                    })
                messagebox.showinfo('Done','Employee Added')
                conn.commit()
                conn.close()
                name.delete(0,END)
                des.delete(0,END)

            n=Tk()
            n.title('New')
            top.destroy()
            n.configure(bg='gray27')
            Label(n,text="New",anchor='center',bg='gray27',font=("Courier", 100),fg='IndianRed2').grid(row=0,column=0,columnspan=3)
            Label(n,text='Full Name',bg='gray27',).grid(row=1,column=0)
            Label(n,text='Designation',bg='gray27',).grid(row=2,column=0)
            name=Entry(n,width=40,borderwidth=5)
            name.grid(row=1,column=1,columnspan=2)
            des=Entry(n,width=40,borderwidth=5)
            des.grid(row=2,column=1,columnspan=2)
            Button(n,text='Add',command=data_in,anchor='center',highlightbackground="gray27",bg='DarkOrange2',padx=40,pady=20).grid(row=3,column=2,sticky='w',rowspan=2)
            gb=Button(n,text='Go Back',bg='gray27',fg='pink',command=back2,highlightbackground="gray27")
            gb.grid(column=2,row=4,sticky='se')
            name.delete(0,END)
            des.delete(0,END)


        def ex():

            def back2():
                n.destroy()
                #print('hi')
                #emp()
                main()

            def desg():
                conn=sqlite3.connect('epms.db')
                c=conn.cursor()
                c.execute('UPDATE epms SET des==:des WHERE eno==:en',{'des':des.get(),'en':em.get()})
                conn.commit()
                conn.close()
                #print('done')
                messagebox.showinfo('Done','Designation Updated')
                des.delete(0,END)
                em.delete(0,END)

            n=Tk()
            n.title('Update Designation')
            top.destroy()
            n.configure(bg='gray27')
            Label(n,text="Update Designation",anchor='center',bg='gray27',font=("Courier", 40),fg='IndianRed2').grid(row=0,column=0,columnspan=3)
            #Label(n,text='Full Name',bg='gray27',).grid(row=1,column=0)
            Label(n,text='Designation',bg='gray27',).grid(row=2,column=0)
            Label(n,text='Employee No.',bg='gray27',).grid(row=1,column=0)
            #name=Entry(n,width=40,borderwidth=5)
            #name.grid(row=1,column=1,columnspan=2)
            des=Entry(n,width=40,borderwidth=5)
            des.grid(row=2,column=1,columnspan=2)
            em=Entry(n,width=40,borderwidth=5)
            em.grid(row=1,column=1,columnspan=2)
            Button(n,text='Update',command=desg,anchor='center',highlightbackground="gray27",bg='DarkOrange2',padx=40,pady=20).grid(row=3,column=1,rowspan=2,columnspan=2)
            gb=Button(n,text='Go Back',bg='gray27',fg='pink',command=back2,highlightbackground="gray27")
            gb.grid(column=2,row=4,sticky='se')

        def uex():
            
            def back2():
                n.destroy()
                #print('hi')
                #emp()
                main()
            def retire():
                conn=sqlite3.connect('epms.db') 
                c=conn.cursor()
                c.execute('UPDATE epms SET status="Retired" WHERE eno='+em.get())
                conn.commit()
                conn.close()
                messagebox.showinfo('Done','Status set to Retired')

            def fire():
                conn=sqlite3.connect('epms.db') 
                c=conn.cursor()
                c.execute('UPDATE epms SET status="Fired" WHERE eno='+em.get())
                conn.commit()
                conn.close()
                messagebox.showinfo('Done','Status set to Fired')
                em.delete(0,END)

            n=Tk()
            n.title('Existing')
            top.destroy()
            n.configure(bg='gray27')
            Label(n,text="Update Existing",anchor='center',bg='gray27',font=("Courier", 40),fg='IndianRed2').grid(row=0,column=0,columnspan=3)
            Label(n,text='Employee No.',bg='gray27',).grid(row=1,column=0)
            em=Entry(n,width=40,borderwidth=5)
            em.grid(row=1,column=1,columnspan=2)
            Button(n,text='Retire',command=retire,anchor='center',highlightbackground="gray27",bg='DarkOrange2',padx=40,pady=20).grid(row=2,column=1,sticky='w',rowspan=2)
            Button(n,text='Fire',command=fire,anchor='center',highlightbackground="gray27",bg='DarkOrange2',padx=40,pady=20).grid(row=2,column=2,rowspan=2)
            gb=Button(n,text='Go Back',bg='gray27',fg='pink',command=back2,highlightbackground="gray27")
            gb.grid(column=2,row=4,sticky='se')

        top=Tk()
        top.title('Update')
        root.destroy()
        top.configure(bg='gray27')
        Label(top,text="Update Employees",anchor='center',bg='gray27',font=("Courier", 100),fg='IndianRed2').grid(row=0,column=0,columnspan=3)
        be1=Button(top,text='Add New',command=new, fg="red",highlightbackground="black",bg='DarkOrange2',padx=115,pady=100,font=("Courier", 40))
        be1.grid(column=0,row=1)
        be2=Button(top,text='Update Designation',command=ex, fg="red",highlightbackground="black",bg='DarkOrange2',padx=14,pady=100,font=("Courier", 36))
        be2.grid(column=2,row=1)
        be3=Button(top,text='Update Existing',command=uex, fg="red",highlightbackground="black",bg='DarkOrange2',padx=32,pady=100,font=("Courier", 40))
        be3.grid(column=1,row=2)
        gb=Button(top,text='Go Back',bg='gray27',fg='pink',command=back)
        gb.grid(column=2,row=2,sticky='se')

    def att():

        def back():
            top.destroy()
            #print('hi')
            main()

        def start():
            today=date.today()
            now=datetime.now()
            #print(now)
            conn=sqlite3.connect('epms.db')
            c=conn.cursor()
            c.execute('SELECT end FROM shift where eno==:en AND start=(SELECT MAX(start) FROM shift where eno==:en)',{'en':em.get()})
            e=c.fetchall()
            if  len(e)==0:
                k=(1,)
            else:
                k=e[0]
            #print('hi')
            #print(k[0])
            if k[0]==0:
                #print('hi')
                root1=Tk()
                root1.withdraw()
                messagebox.showinfo('Done','Shift already started')
                root1.destroy()
            else:
                c.execute('INSERT INTO shift VALUES(:eno,:date,:start,:end)',
                {
                    'eno':em.get(),
                    'date':today,
                    'start':now,
                    'end':'0'
                })
                root1=Tk()
                root1.withdraw()
                messagebox.showinfo('Done','Shift Started')
                root1.destroy()
                em.delete(0,END)
            conn.commit()
            conn.close()

        def end():
            today=date.today()
            now=datetime.now()
            #print(now)
            conn=sqlite3.connect('epms.db')
            c=conn.cursor()
            c.execute('SELECT end FROM shift where eno==:en AND start=(SELECT MAX(start) FROM shift where eno==:en)',{'en':em.get()})
            e=c.fetchall()
            k=e[0]
            #print('hi')
            #print(k[0])
            if k[0]!=0:
                #print('hi')
                root1=Tk()
                root1.withdraw()
                messagebox.showinfo('Done','No shift started')
                root1.destroy()
            else:
                c.execute('UPDATE shift set end==:now WHERE date==:date AND start=(SELECT MAX(start) FROM shift where eno==:en)',{'now':now,'date':today,'en':em.get()})
                root1=Tk()
                root1.withdraw()
                messagebox.showinfo('Done','Shift Ended')
                root1.destroy()
                em.delete(0,END)
            conn.commit()
            conn.close()
            #print('done')
            
            

        top=Tk()
        top.title('Attendance')
        root.destroy()
        top.configure(bg='gray27')
        Label(top,text="Attendance",anchor='center',bg='gray27',font=("Courier", 100),fg='IndianRed2').grid(row=0,column=0,columnspan=3)
        Label(top,text="Employee No.",bg='gray27',font=("arial",25)).grid(row=1,column=0)
        em=Entry(top,width=40,borderwidth=5)
        em.grid(row=1,column=1,columnspan=2)
        ba1=Button(top,text='Shift Start',command=start,padx=40,pady=20,highlightbackground="gray27").grid(row=2,column=0,rowspan=2)
        ba2=Button(top,text='Shift End',command=end,padx=40,pady=20,highlightbackground="gray27").grid(row=2,column=2,rowspan=2)
        gb=Button(top,text='Go Back',bg='gray27',fg='pink',command=back,highlightbackground="gray27")
        gb.grid(column=2,row=4,sticky='se')
    
    def rec():

        def back():
            top.destroy()
            #print('hi')
            main()

        conn=sqlite3.connect('epms.db')
        c=conn.cursor()
        c.execute('SELECT *,oid FROM epms')
        records=c.fetchall()
        print_records="('Name','Designation','EmpId','Status','Oid')\n"
        for data in records:
            print_records+=str(data)+'\n'
        conn.commit()
        conn.close()
        #print(print_records)
        top=Tk()
        top.title('Records')
        root.destroy()
        top.configure(bg='gray27')
        Label(top,text="Records",anchor='center',bg='gray27',font=("Courier", 100),fg='IndianRed2').grid(row=0,column=0,columnspan=3)
        reco=Text(top,width=100,height=20,borderwidth=5,state='normal')
        reco.grid(row=1,column=0,columnspan=3,padx=10,pady=10)
        reco.insert(END,print_records)
        reco.config(state=DISABLED)
        gb=Button(top,text='Go Back',bg='gray27',fg='pink',command=back,highlightbackground="gray27")
        gb.grid(column=2,row=2,sticky='se')

    def wh():

        def back():
            top.destroy()
            #print('hi')
            main()
        
        conn=sqlite3.connect('epms.db')
        c=conn.cursor()
        c.execute('SELECT * FROM shift')
        records=c.fetchall()
        print_shifts="('Employee No.','Date','Start Time','End Time')\n"
        for data in records:
            print_shifts+=str(data)+'\n'
        #c.execute('SELECT start,end FROM shift WHERE eno=2021')##for graph
        #ti=c.fetchall()
        #tt=''
        #for tim in ti:
        #    tt+=str(tim)+'\n'
        #print(tt)
        #t1=datetime.strptime(tt[1],'%Y-%m-%d %H:%M:%S.%f')-datetime.strptime(tt[0],'%Y-%m-%d %H:%M:%S.%f')
        #print(t1)
        conn.commit()
        conn.close()
        top=Tk()
        top.title('Working Hours')
        root.destroy()
        top.configure(bg='gray27')
        Label(top,text="Working Hours",anchor='center',bg='gray27',font=("Courier", 100),fg='IndianRed2').grid(row=0,column=0,columnspan=3)
        shifts=Text(top,width=100,height=20,borderwidth=5,state='normal')
        shifts.grid(row=1,column=0,columnspan=3,padx=10,pady=10)
        shifts.insert(END,print_shifts)
        shifts.config(state=DISABLED)
        gb=Button(top,text='Go Back',bg='gray27',fg='pink',command=back,highlightbackground="gray27")
        gb.grid(column=2,row=2,sticky='se')

    

    #main function
    root=Tk()
    root.configure(bg='gray27')
    root.title('EPMS')

    conn=sqlite3.connect('epms.db')
    c=conn.cursor()
    c.execute("""
                Create TABLE IF NOT EXISTS epms(
                    name text,
                    des text,
                    eno int,
                    status text
                )""")

    c.execute("""
                Create TABLE IF NOT EXISTS shift(
                    eno int,
                    date date,
                    start datetime,
                    end datetime
                )""")

    epms=Label(root,text="EPMS",anchor='center',bg='gray27',font=("Courier", 100),fg='IndianRed2')
    epms.grid(column=0,row=0,columnspan=6,rowspan=4)

    b1= Button(root, text="Update Employees",command=emp, fg="red",highlightbackground="black",bg='DarkOrange2',padx=10,pady=100,font=("Courier", 40))
    b1.grid( column=1,row=5)

    b2 = Button(root, text="Attendance",command=att, fg="brown",highlightbackground="black",bg='DarkOrange2',padx=85,pady=100,font=("Courier", 40))
    b2.grid( column=2,row=5)

    b3= Button(root, text="Records",command=rec, fg="blue",highlightbackground="black",bg='DarkOrange2',padx=117,pady=100,font=("Courier", 40))
    b3.grid(column=3,row=5)

    b4= Button(root, text="Working Hours",command=wh, fg="black",highlightbackground="black",bg='DarkOrange2',padx=50,pady=100,font=("Courier", 40))
    b4.grid( column=2,row=6)

    Label(root,text="Created by NISHIT MEHROTRA",bg='gray27',fg='white').grid(row=6,column=3,sticky='se')
    
    conn.commit()
    conn.close()

    root.mainloop()

main()
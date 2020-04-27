from tkinter import*
import SQL


global date1
date1 = []

'''global date2
date2 = []

global date3
date3 = []'''

class ThearteSeats:
    def __init__(self, master):
        self.customerDetails = []
        master.title('Title')
        master.option_add('*Font', 'Georgia 12')
        master.option_add('*background', 'grey20')
        master.option_add('*label.Font', 'helvetica 14')
        master.geometry('1200x540+100+100')
        master.configure(bg='grey20')

        DateSelectFrame = Frame(master)
        DateSelectFrame.config(height=30, width=5,)
        DateSelectFrame.rowconfigure(0, weight=1)
        DateSelectFrame.grid(row=0, column=0)

        self.DateChoice = IntVar()
        # self.DateChoice.set('')
        radio_1 = Radiobutton(DateSelectFrame, text='03/11/20', value='1', activebackground='green', variable=self.DateChoice)
        radio_2 = Radiobutton(DateSelectFrame, text='04/11/20', value='2', activebackground='green', variable=self.DateChoice)
        radio_3 = Radiobutton(DateSelectFrame, text='05/11/20', value='3', activebackground='green', variable=self.DateChoice)
        radio_1.grid(row=0, column=0)
        radio_2.grid(row=1, column=0)
        radio_3.grid(row=2, column=0)

# type of buy
        typeofticketframe = Frame(master, highlightthickness='1', highlightbackground='white')
        typeofticketframe.config()
        typeofticketframe.grid(row=0, column=1, ipadx=5, ipady=1, sticky=W)
        self.ticketchoice = StringVar()
        self.ticketchoice.set('0')
        adult = Radiobutton(typeofticketframe, text='Adult ticket', value='1', variable=self.ticketchoice)
        child = Radiobutton(typeofticketframe, text='child ticket', value='2', variable=self.ticketchoice)
        special = Radiobutton(typeofticketframe, text='special ticket', value='3', variable=self.ticketchoice)
        gov = Radiobutton(typeofticketframe, text='govnor', value='4', variable=self.ticketchoice)
        adult.grid(row=0, column=0)
        child.grid(row=1, column=0)
        special.grid(row=0, column=1)
        gov.grid(row=1, column=1)


# Ticket types
        TicketContainer = Frame(master, highlightthickness='1', highlightbackground='white')
        TicketContainer.config(height=40, width=50)
        TicketContainer.grid(row=1, column=0, ipadx=1, ipady=60, sticky=W)

        AdultLabel = Label(TicketContainer, text='Adult ticket(£10): ', fg='green')
        AdultLabel.grid(row=0, column=0, sticky=W)
        AdultTicketShow = Entry(TicketContainer, width=2,)
        AdultTicketShow.grid(row=0, column=1, padx=5)

        Under18Label = Label(TicketContainer, text='Under18 ticket(£5): ', fg='purple')
        Under18Label.grid(row=1, column=0, sticky=W, pady=2)
        Under18TicketShow = Entry(TicketContainer, width=2,)
        Under18TicketShow.grid(row=1, column=1, padx=5, pady=2)

        SpecialLabel = Label(TicketContainer, text='Special ticket(£5): ', fg='red')
        SpecialLabel.grid(row=2, column=0, sticky=W, pady=2)
        SpecialTicketShow = Entry(TicketContainer, width=2,)
        SpecialTicketShow.grid(row=2, column=1, padx=5, pady=2)

        GovnorLabel = Label(TicketContainer, text='Govnor/staff ticket(£0): ', fg='yellow')
        GovnorLabel.grid(row=3, column=0, sticky=W, pady=2)
        GovnorTicketShow = Entry(TicketContainer, width=2,)
        GovnorTicketShow.grid(row=3, column=1, padx=5, pady=2)


# Seats-----------------------------------

        container = Frame(master)
        container.grid(row=1, rowspan=2, column=1, pady=10)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        stage = Frame(container, highlightthickness='1', highlightbackground='white')
        stage.pack(side=TOP, ipadx=350, ipady=7)
        title = Label(stage, text='Stage', fg='white', pady=2)
        title.pack()
        buttonFrame = Frame(container, highlightthickness='2', highlightbackground='red')
        buttonFrame.config(height=100, width=200)
        buttonFrame.pack(side=RIGHT, anchor=NW,  padx=10, pady=10)

        # create seats
        tracker = 0
        count = 0
        self.btn = [[]*200]
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        for i in range(10):
            for y in range(1, 21):
                self.btn.append((alphabet[i] + str(y)))

        for i in range(10):
            for y in range(1, 21):
                name = (str(alphabet[i]) + str(y))
                self.button = Button(buttonFrame, text=name, height=1, width=3, bg='grey78')
                self.button.bind('<Button-1>', self.button_func)

                self.button.grid(row=i, column=y)
                self.btn.append(self.button)
                count += 1

# Details --------------
        nameBox = Frame(master, highlightthickness='1', highlightbackground='white')
        nameBox.config(height=20)
        nameBox.grid(row=1, column=0, ipady=10, ipadx=10, sticky=SW)
        firstName = Label(nameBox, text='First name: ')
        firstName.grid(row=0, column=0, sticky=W)
        secondName = Label(nameBox, text='Second name: ')
        secondName.grid(row=1, column=0, pady=1, sticky=W)
        phoneNumber = Label(nameBox, text='Phone number: ')
        phoneNumber.grid(row=2, column=0, sticky=W)
        '''password = Label(nameBox, text='Password: ')
        password.grid(row=3, column=0, sticky=W, pady=1)
        password2 = Label(nameBox, text='Password: ')
        password2.grid(row=4, column=0, sticky=W)'''

        self.firstNameVar = StringVar()
        self.firstNameVar.set('')
        firstNameEntry = Entry(nameBox, textvariable=self.firstNameVar)
        firstNameEntry.config(width=12)
        firstNameEntry.grid(row=0, column=1, sticky=W)

        self.secondNameVar = StringVar()
        self.secondNameVar.set('')
        secondNameEntry = Entry(nameBox, textvariable=self.secondNameVar)
        secondNameEntry.config(width=12)
        secondNameEntry.grid(row=1, column=1, sticky=W, pady=1)

        self.numberVar = StringVar()
        self.numberVar.set('')
        phoneNumberEntry = Entry(nameBox, textvariable=self.numberVar)
        phoneNumberEntry.config(width=12)
        phoneNumberEntry.grid(row=2, column=1, sticky=W, pady=1)

        '''self.password1Var = StringVar()
        self.password1Var.set('')
        passwordEntry = Entry(nameBox, textvariable=self.password1Var)
        passwordEntry.config(width=12)
        passwordEntry.grid(row=3, column=1, sticky=W, pady=1)

        self.password2Var = StringVar()
        self.password2Var.set('')
        password2Entry = Entry(nameBox, textvariable=self.password2Var)
        password2Entry.config(width=12)
        password2Entry.grid(row=4, column=1, sticky=W, pady=1)'''

        confirmButton = Button(nameBox, width=10, text='Confirm', command=self.infoGet)
        confirmButton.grid(row=5, column=1, pady=3, padx=9)

        AddToDataBaseButton = Button(nameBox, width=10, text='Finalised',) # command=self.returnList())
        AddToDataBaseButton.grid(row=6, column=1)

    # Getting data
        OutputWidgets = Frame(master, highlightthickness='1', highlightbackground='white')
        OutputWidgets.grid(row=0, column=1, ipady=2, ipadx=20, padx=5, sticky=E)
        OutputWidgets.columnconfigure(0, weight=1)
        TableSearchLabel = Label(OutputWidgets, text='Table to search:')
        TableSearchLabel.grid(row=0, column=0, sticky=W)
        TableSearchBox = Frame(OutputWidgets)
        TableSearchBox.grid(row=1, column=0, sticky=W)
        self.SearchChoice = StringVar()
        self.SearchChoice.set('0')
        customer = Radiobutton(TableSearchBox, text='Customer', value='1', variable=self.SearchChoice)
        booking = Radiobutton(TableSearchBox, text='Booking', value='2', variable=self.SearchChoice)
        customer.grid(row=0, column=0, sticky=W)
        booking.grid(row=1, column=0, sticky=W)

        DateToSearchLabel = Label(OutputWidgets, text='Select Date : ')
        DateToSearchLabel.grid(row=0, column=1, padx=10, sticky=W)
        self.DateSearchChoice = IntVar()
        #self.DateSearchChoice.set('')
        Day1 = Radiobutton(OutputWidgets, text='03/11/20', value='1', activebackground='green', variable=self.DateSearchChoice)
        Day2 = Radiobutton(OutputWidgets, text='04/11/20', value='2', activebackground='green', variable=self.DateSearchChoice)
        Day3 = Radiobutton(OutputWidgets, text='05/11/20', value='3', activebackground='green', variable=self.DateSearchChoice)
        Day1.grid(row=1, column=1, sticky=S)
        Day2.grid(row=2, column=1, sticky=N)
        Day3.grid(row=3, column=1, sticky=N)

        NameSearchLabel = Label(OutputWidgets, text='Search by name: ')
        NameSearchLabel.grid(row=0, column=2, padx=2)
        self.NameSearch = StringVar()
        self.NameSearch.set('')
        NameEntry = Entry(OutputWidgets, textvariable=self.NameSearch)
        NameEntry.config(width=8)
        NameEntry.grid(row=1, column=2)

        ButtonOutputWidgetFrame = Frame(master, highlightthickness='1', highlightbackground='white')
        ButtonOutputWidgetFrame.grid(row=0, column=2)
        ConfirmSearchButton = Button(ButtonOutputWidgetFrame, width=10, text='confirm')
        ConfirmSearchButton.grid(row=0, column=0)

        ShowStatsButtonFrame = Frame(master, highlightthickness='1', highlightbackground='white')
        ShowStatsButtonFrame.grid(row=1, column=2)
        WhatToSeeRadButtonLabel = Label(ShowStatsButtonFrame, text='Select what to see: ')
        WhatToSeeRadButtonLabel.grid(row=0, pady=10)

        self.SelectedStat = StringVar()
        self.SelectedStat.set('')
        TotalTickets = Radiobutton(ShowStatsButtonFrame, text='Total Tickets Sold', value='1', variable=self.SelectedStat)
        TotalTickets.grid(row=1, sticky=W)
        RemainingTickets = Radiobutton(ShowStatsButtonFrame, text='Remaing Tickets', value='2', variable=self.SelectedStat)
        RemainingTickets.grid(row=2, sticky=W)
        TotalRev = Radiobutton(ShowStatsButtonFrame, text='Total Revenue', value='3', variable=self.SelectedStat)
        TotalRev.grid(row=3, sticky=W)

        SeeStats = Button(ShowStatsButtonFrame, width=10, text='ShowStats')
        SeeStats.grid(row=4, column=0)

    def button_func(self, button):
        BtnControl = button.widget
        choice = self.ticketchoice.get()
        Date = self.DateChoice.get

        if choice == '0':
            print('Please select ticket type')

        if choice == '1':
            BtnControl.config(bg='green')
            date1.append(BtnControl['text'])

        if choice == '2':
            BtnControl.config(bg='purple')
            date1.append(BtnControl['text'])

        if choice == '3':
            BtnControl.config(bg='red')
            date1.append(BtnControl['text'])

        if choice == '4':
            BtnControl.config(bg='yellow')
            date1.append(BtnControl['text'])

    def infoGet(self):
        '''f = open('number.txt', 'r')
        num = int(f.read())
        print(str(num))
        custID = 'C' + str(num)
        print(custID)
        f.close()
        self.customerDetails.append(str(custID))
        f = open('number.txt', 'w')
        f.write(str(num))
        f.close'''

        correctScore = 0

        firstName = self.firstNameVar.get()
        if firstName.isalpha() and len(firstName) < 20:
            correctScore += 1
        else:
            print('First name not acceptable')

        secondName = self.secondNameVar.get()
        if secondName.isalpha() and len(secondName) < 20:
            correctScore += 1
        else:
            print('second name not acceptable ')

        number = self.numberVar.get()
        if number.isdigit():
            correctScore += 1

        if correctScore != 3:
            print('re-enter Details')

        else:
            self.customerDetails.append(firstName)
            self.customerDetails.append(secondName)
            self.customerDetails.append(number)
            day = self.DateChoice.get()
            if day == 1:
                self.customerDetails.append('03/11//20')
            if day == 2:
                self.customerDetails.append('04/11//20')
            if day == 3:
                self.customerDetails.append('05/11//20')

            f = open('number.txt', 'r')
            num = f.read()
            custID = 'N' + num
            f.close()
            self.customerDetails.append(str(custID))
            f = open('number.txt', 'w')
            f.write(str(num))
            f.close

            self.customerDetails.append(date1)
            showDate = self.customerDetails[3]
            print(self.customerDetails)
            CID = 5

            Database = SQL.Data()
            Database.enter(CID, firstName, secondName, str(number), showDate)


def main():
    root = Tk()
    app = ThearteSeats(root)
    root.mainloop()


if __name__ == '__main__':
    main()

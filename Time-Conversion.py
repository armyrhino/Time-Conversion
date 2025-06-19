#! /usr/bin/python

from tkinter import *
import tkinter as Tk
from datetime import datetime
from time import *

###################################################################################
#                                Global Variables                                 #
###################################################################################

Frame = Tk()
currentTime = datetime.now()
tt = currentTime.timetuple()
year = int(tt.tm_year)
month = int(tt.tm_mon)
day = int(tt.tm_mday)
hour = int(tt.tm_hour)
minute = int(tt.tm_min)
second = int(tt.tm_sec)
epoch = int(tt.tm_yday)
color1 = 'light blue'

###################################################################################
#                                Python 3                                         #
###################################################################################
class Conversion(Frame):
    def __init__(self, parent = None, **options):
            Frame.__init__(self, parent, background = color1, **options)
            self.grid(columnspan = 10, rowspan = 16, sticky = 'NSEW')
            self.winfo_toplevel().title("Conversion Tool")
            self.widgets()

###################################################################################
#                         Face of the GUI Selections                              #
###################################################################################

    def widgets(self):
            self.STDYearSpinVar = IntVar()
            self.STDYearSpinVar.set(year)
            self.STDMonthSpinVar = IntVar()
            self.STDMonthSpinVar.set(month)
            self.STDDaySpinVar = IntVar()
            self.STDDaySpinVar.set(day)
            self.STDHourSpinVar = IntVar()
            self.STDHourSpinVar.set(hour)
            self.STDMinuteSpinVar = IntVar()
            self.STDMinuteSpinVar.set(minute)
            self.STDSecondSpinVar = IntVar()
            self.STDSecondSpinVar.set(second)
            self.JulianYearSpinVar = IntVar()
            self.JulianYearSpinVar.set(year)
            self.JulianDaySpinVar = IntVar()
            self.JulianDaySpinVar.set(epoch)
            self.STDEntryVar = StringVar()
            self.JulianEntryVar = StringVar()
            self.SSEEntryVar = StringVar()
            self.EpochEntryVar  = StringVar()
            self.CurrentDay = day
            self.UserEntry = StringVar()
            self.STDYearSpin = Spinbox(from_ = 1970, to = year, increment = 1, command=self.update_stdyearbox, textvariable = self.STDYearSpinVar, width = 4)
            self.STDYearSpin.bind('<Button-1>', self.SpinConfig)
            self.STDMonthSpin = Spinbox(from_ = 1, to = 12, increment = 1, wrap = False, command=self.update_stdmonthday, textvariable = self.STDMonthSpinVar, width = 4)
            self.STDDaySpin = Spinbox(from_ = 1, to = 31, increment = 1, wrap  = False, command=self.update_stddaybox, textvariable = self.STDDaySpinVar, width = 4)
            self.STDHourSpin = Spinbox(from_ = 0, to = 23, increment = 1, wrap = True, textvariable = self.STDHourSpinVar, width = 4)
            self.STDMinuteSpin = Spinbox(from_ = 0, to = 60, increment = 1, wrap = True, textvariable = self.STDMinuteSpinVar, width = 4)
            self.STDSecondSpin = Spinbox(from_ = 0, to = 60, increment = 1, textvariable = self.STDSecondSpinVar, width = 4)
            self.JulianYearSpin = Spinbox(from_ = 1970, to = year, increment = 1, command=self.update_julyearbox, textvariable = self.JulianYearSpinVar, width = 4)
            self.JulianYearSpin.bind('<Button-1>', self.LeapYear_event)
            self.JulianDaySpin = Spinbox(from_ = 1, to = 366, increment = 1, wrap = True, command=self.LeapYears, textvariable = self.JulianDaySpinVar, width = 4)
            self.STDSpace1 = Label(width = 5, bg = color1)
            self.STDSpace2 = Label(width = 4, bg = color1)
            self.STDEntry = Entry(width = 20, text = self.STDEntryVar)
            self.JulianEntry = Entry(width = 20, text = self.JulianEntryVar)
            self.SSEEntry = Entry(width = 20, text = self.SSEEntryVar)
            self.EpochEntry = Entry(width = 20, text = self.EpochEntryVar)
            self.PreviousSTDMonth = int(self.STDMonthSpin.get())
            self.Displaybutton = Button(text = "Display", background = 'white', command = self.Display)
            self.UserEntry = Entry(width = 20, fg = 'grey', text = self.UserEntry)
            self.UserEntry.insert(0, "yyyy:mm:dd hh:mm:ss")
            self.UserEntry.bind("<FocusIn>", self.handle_FocusIn)
            self.UserEntry.bind("<FocusOut>", self.handle_FocusOut)
            self.UserEntry.bind("<Return>", self.SubmitEntry)
            self.ExitButton = Button(text = "Exit", bg = 'red', command=self.quit)
            self.create_widgets()
            
    def create_widgets(self):
            self.UserEntry.grid(row = 1, column = 0, pady = 5, padx = 5)
            Label(text = "Local Format", bg = color1).grid(row = 2, column = 0)
            self.STDSpace1.grid(row = 2, column = 1)
            self.STDYearSpin.grid(row = 2, column = 2)
            self.STDMonthSpin.grid(row = 2, column = 3, padx = 5)
            self.STDDaySpin.grid(row = 2, column = 4)
            self.STDHourSpin.grid(row = 2, column = 5, padx = 5)
            self.STDMinuteSpin.grid(row = 2, column = 6)
            self.STDSecondSpin.grid(row = 2, column = 7, padx = 5)
            self.STDSpace2.grid(row = 2, column = 8)
            self.STDEntry.grid(row = 2, column = 9, padx = 5)
            Label(text = "Julian Format", bg = color1).grid(row = 3, column = 0, pady = 5, padx = 5)
            self.JulianYearSpin.grid(row = 3, column = 2)
            self.JulianDaySpin.grid(row = 3, column = 3)
            self.JulianEntry.grid(row = 3, column = 9)
            Label(text = "SSE Format", bg = color1).grid(row = 4, column = 0)
            self.SSEEntry.grid(row = 4, column = 9)
            Label(text = "Epoch Format", bg = color1).grid(row = 5, column = 0, pady = 5, padx = 5)
            self.EpochEntry.grid(row = 5, column = 9)
            self.Displaybutton.grid(row = 7, column = 0, pady = 10)
            self.ExitButton.grid(row = 7, column = 9)
            
    def Display(self):
            STDYear = str(self.STDYearSpin.get())
            STDMonth = str(self.STDMonthSpin.get())
            STDDay = str(self.STDDaySpin.get())
            STDHour = str(self.STDHourSpin.get())
            STDMinute = str(self.STDMinuteSpin.get())
            STDSecond = str(self.STDSecondSpin.get())
            self.JulianYear = str(self.JulianYearSpin.get())
            self.JulianDay = self.JulianDaySpin.get()
            self.JuliantoEpoch()
            self.seconds_conversion()
            JulianDay = str(self.JulianDay)
            STDTotal = STDYear + "/" + STDMonth + "/" + STDDay + " " + STDHour + ":" + STDMinute + ":" + STDSecond
            JulianTotal = self.JulianYear + "/" + JulianDay + " " + STDHour + ":" + STDMinute + ":" + STDSecond
            EpochTotal = str(self.CurrentEpochYear) + "/" + str(self.CurrentEpoch) + " " + STDHour + ":" + STDMinute + ":" + STDSecond
            self.STDEntryVar.set(STDTotal)
            self.JulianEntryVar.set(JulianTotal)
            self.EpochEntryVar.set(EpochTotal)
            self.SSEEntryVar.set(self.total_seconds)
            
####################################################################################
#                             Event Handling                                       #
####################################################################################

    def update_stdyearbox(self):
            CurrentSTDYear = self.STDYearSpin.get()
            self.JulianYearSpinVar.set(CurrentSTDYear)
            
    def update_julyearbox(self):
            CurrentEPYear = self.JulianYearSpin.get()
            self.STDYearSpinVar.set(CurrentEPYear)
            
    def handle_FocusIn(self, _):
            self.UserEntry.delete(0, END)
            self.UserEntry.config(fg = 'black')

    def handle_FocusOut(self, _):
            self.UserEntry.delete(0, END)
            self.UserEntry.config(fg = 'gray')
            self.UserEntry.insert(0, "YYYY:MM:DD HH:MM:SS")
            
    def SubmitEntry(self, _):
            Entry = self.UserEntry.get()
            try:
                Date, Time = Entry.split(" ")
                NewYear, NewMonth, NewDay = Date.split(":")
                NewHour, NewMinute, NewSecond = Time.split(":")
                self.SpinConfig(NewYear)
                self.STDYearSpinVar.set(NewYear)
                self.JulianYearSpinVar.set(NewYear)
                self.LeapYears()
                self.LeapYear = StringVar()
                self.LeapYear = self.LeapYear
                self.STDMonthSpinVar.set(NewMonth)
                self.STDDaySpinVar.set(NewDay)
                self.STDHourSpinVar.set(NewHour)
                self.STDMinuteSpinVar.set(NewMinute)
                self.STDSecondSpinVar.set(NewSecond)
                self.ValidateJulianDay()
            except ValueError or AttributeError:
                self.ErrorHandle()
                
    def ErrorHandle(self):
            error_window = Tk()
            error_window.title("Error")
            error_window.grid()
            Label(error_window, text = "Please enter the correct format: YYYY-MM-DD HH:MM:SS", bg = color1).grid(row = 0, column = 0)
            Button(error_window, text = "Close", command=error_window.destroy).grid(row = 0, column = 6)
            
    def update_stddaybox(self):
            self.CurrentSTDDay = IntVar()
            self.CurrentSTDDay = int(self.STDDaySpin.get())
            if (self.CurrentDay) > (self.CurrentSTDDay):
                self.CurrentDay = self.CurrentSTDDay
                self.JulianDaySpinVar.set(int(self.JulianDaySpin.get()) - 1)
            elif (self.CurrentDay) > (self.CurrentSTDDay):
                self.CurrentDay = self.CurrentSTDDay
                self.JulianDaySpinVar.set(int(self.JulianDaySpin.get()) + 1)
                
    def update_stdmonthday(self):
            self.LeapYear = StringVar()
            self.LeapYear = int(self.JulianYearSpin.get()) % 4
            self.LeapYear = str(self.LeapYear)
            Leap = self.LeapYear
            CurrentSTDMonth = int(self.STDMonthSpin.get())
            CurrentJulianDay = int(self.JulianDaySpin.get())
            if Leap == '0':
                if CurrentSTDMonth < self.PreviousSTDMonth:
                    if CurrentSTDMonth ==1 or CurrentSTDMonth == 12:
                        self.STDDaySpin.cong(to = 31)
                        if CurrentSTDMonth == 1:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) - 29)
                        else:
                            return
                    elif (CurrentSTDMonth == 3 or CurrentSTDMonth == 5 or CurrentSTDMonth == 8 or CurrentSTDMonth == 10 or CurrentSTDMonth == 7):
                        self.STDDaySppin.config(to = 31)
                        if CurrentSTDMonth == 7:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) - 31)
                        else:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) - 30)
                    elif (CurrentSTDMonth == 4 or CurrentSTDMonth == 6 or CurrentSTDMonth == 9 or CurrentSTDMonth == 11 or CurrentSTDMonth == 2):
                        self.JulianDaySpinVar.set(int(CurrentJulianDay) - 31)
                        if CurrentSTDMonth == 2:
                            self.STDDaySpin.config(to = 29)
                        else:
                            self.STDDaySpin.config(to = 30)
                elif (CurrentSTDMonth > self.PreviousSTDMonth):
                    if (CurrentSTDMonth == 3 or CurrentSTDMonth == 5 or CurrentSTDMonth == 7 or CurrentSTDMonth == 10 or CurrentSTDMonth == 12):
                        self.STDDaySpin.config(to = 31)
                        if CurrentSTDMonth == 3:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) + 29)
                        else:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) + 30)
                    elif (CurrentSTDMonth == 2 or CurrentSTDMonth == 4 or CurrentSTDMonth == 6 or CurrentSTDMonth == 8 or CurrentSTDMonth == 9 or CurrentSTDMonth == 11):
                        self.JulianDaySpinVar.set(int(CurrentJulianDay) + 31)
                        if CurrentSTDMonth == 2:
                          self.STDDaySpin.config(to = 29)
                        else:
                            self.STDDaySpin.config(to = 30)
                    elif CurrentSTDMonth == 1:
                        self.STDDaySpin.config(to = 31)
            else:
                if CurrentSTDMonth < self.PreviousSTDMonth:
                    if CurrentSTDMonth ==1 or CurrentSTDMonth == 12:
                        self.STDDaySpin.cong(to = 31)
                        if CurrentSTDMonth == 1:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) - 28)
                        else:
                            return
                    elif (CurrentSTDMonth == 3 or CurrentSTDMonth == 5 or CurrentSTDMonth == 8 or CurrentSTDMonth == 10 or CurrentSTDMonth == 7):
                        self.STDDaySppin.config(to = 31)
                        if CurrentSTDMonth == 7:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) - 31)
                        else:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) - 30)
                    elif (CurrentSTDMonth == 4 or CurrentSTDMonth == 6 or CurrentSTDMonth == 9 or CurrentSTDMonth == 11 or CurrentSTDMonth == 2):
                        self.JulianDaySpinVar.set(int(CurrentJulianDay) - 31)
                        if CurrentSTDMonth == 2:
                            self.STDDaySpin.config(to = 28)
                        else:
                            self.STDDaySpin.config(to = 30)
                elif (CurrentSTDMonth > self.PreviousSTDMonth):
                    if (CurrentSTDMonth == 3 or CurrentSTDMonth == 5 or CurrentSTDMonth == 7 or CurrentSTDMonth == 10 or CurrentSTDMonth == 12):
                        self.STDDaySpin.config(to = 31)
                        if CurrentSTDMonth == 3:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) + 28)
                        else:
                            self.JulianDaySpinVar.set(int(CurrentJulianDay) + 30)
                    elif (CurrentSTDMonth == 2 or CurrentSTDMonth == 4 or CurrentSTDMonth == 6 or CurrentSTDMonth == 8 or CurrentSTDMonth == 9 or CurrentSTDMonth == 11):
                        self.JulianDaySpinVar.set(int(CurrentJulianDay) + 31)
                        if CurrentSTDMonth == 2:
                          self.STDDaySpin.config(to = 28)
                        else:
                            self.STDDaySpin.config(to = 30)
                    elif CurrentSTDMonth == 1:
                        self.STDDaySpin.config(to = 31)
            self.PreviousSTDMonth = CurrentSTDMonth
            self.validateJulianDay()
            
###################################################################################
#                              Conversions                                        #
###################################################################################

    def seconds_conversion(self):
            self.total_seconds = StringVar()
            date1 = datetime(1970, 12, 20, 0, 0, 0)
            date2 = datetime(int(self.JulianYearSpinVar.get()), int(self.STDMonthSpinVar.get()), int(self.STDDaySpinVar.get()), int(self.STDHourSpinVar.get()), int(self.STDMinuteSpinVar.get()), int(self.STDSecondSpinVar.get()))
            timedelta = date2 - date1
            seconds = timedelta.total_seconds()
            self.total_seconds = seconds

    def LeapYears(self):
            self.LeapYear = StringVar()
            self.LeapYear = int(self.JulianYearSpinVar.get()) % 4
            self.LeapYear = str(self.LeapYear)
            if self.LeapYear == '0':
                self.JulianDaySpin.config(to = 366)
            else:
                self.JulianDaySpin.config(to = 365)

    def LeapYearConversions(self, LeapYear):
            self.CurrentEpoch = str(int(self.JulianDay) + 11)
            key = self.CurrentEpoch
            self.LeapYear = str(self.LeapYear)
            if self.LeapYear == '0':
                Epoch = {'366':366, '367':1, '368':2, '369':3, '370':4, '371':5, '372':6, '373':7, '374':8, '375':9, '376':10, '377':11}
                Epochkey = Epoch[key]
            else:
                Epoch = {'366':1, '367':2, '368':3, '369':4, '370':5, '371':6, '372':7, '373':8, '374':9, '375':10, '376':11}
                Epochkey = Epoch[key]
            self.CurrentEpoch = int(Epochkey)
            
    def SpinConfig(self, NewYear):
            self.STDYearSpins = str(self.STDYearSpin.get())
            if NewYear == '1970' or self.STDYearSpins == '1970':
                self.STDMonthSpin.config(from_ = 12)
                self.STDDaySpin.config(from_ = 20)
            else:
                self.STDMonthSpin.config(from_ = 1)
                self.STDDaySpin.config(from_ = 1)
                
    def LeapYears(self):
            self.LeapYear = StringVar()
            self.LeapYear = str(int(self.JulianYearSpinVar.get()) % 4)
            if self.LeapYear == '0':
                self.JulianDaySpin.config(to = 366)
            else:
                self.JulianDaySpin.config(to = 365)
                
    def LeapYear_event(self):
            self.LeapYear = StringVar()
            self.LeapYear = str(int(self.JulianYearSpinVar.get()) % 4)
            if self.LeapYear == '0':
                self.JulianDaySpin.config(to = 366)
            else:
                self.JulianDaySpin.config(to = 365)
                
    def JuliantoEpoch(self):
            self.CurrentEpochYear = self.JulianYear
            self.CurrentEpoch = IntVar()
            self.CurrentEpoch = int(self.JulianDay) + 11
            self.LeapYear = StringVar()
            self.LeapYear = int(self.JulianYearSpin.get()) % 4
            self.CurrentEpoch = str(self.CurrentEpoch)
            if str(self.CurrentEpoch) > '365':
                self.LeapYearConversion(self.LeapYear)
            
    def LeapYearConversion(self, LeapYear):
            self.LeapYear = str(self.LeapYear)
            key = str(self.CurrentEpoch)
            if self.LeapYear == '0':
                Epoch = {'366':366, '367':1, '368':2, '369':3, '370':4, '371':5, '372':6, '373':7, '374':8, '375':9, '376':10, '377':11, str(key):key}
                Epochkey = Epoch[key]
            else:
                Epoch = {'366':1, '367':2, '368':3, '369':4, '370':5, '371':6, '372':7, '373':8, '374':9, '375':10, '376':11, str(key):key}
                Epochkey = Epoch[key]
            self.CurrentEpoch = int(Epochkey)
            self.CurrentEpochYear = int(self.CurrentEpochYear)
            
###################################################################################
#                                Calendar                                         #
###################################################################################

    def ValidateJulianDay(self):
            CurrentYeartime = str(self.STDYearSpin.get())
            CurrentDaytime = str(self.STDDaySpin.get())
            CurrentMonthtime = str(self.STDMonthSpin.get())
            dates = CurrentYeartime + '-' + CurrentMonthtime + '-' + CurrentDaytime
            cal = datetime.strptime(dates, "%Y-%m-%d").strftime("%Y-%j")
            year, julian = cal.split("")
            set.JulianDaySpinVar.set(julian)
            
if __name__ == '__main__':
    Conversion().mainloop()
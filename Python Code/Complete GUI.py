from tkinter import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pyvisa as visa
import time


class App():
    def __init__(self, master):
        
        # SetPoint
        self.l3 = Label(root, text = 'SetPoint(deg C):')
        self.l3.place(x = 615, y = 70)
        self.SetpointInput = Entry(root)
        self.SetpointInput.place(x = 615, y = 100)

        # Max Voltage
        self.l1 = Label(root, text = 'Max Voltage:')
        self.l1.place(x = 615, y = 150)
        self.MaxVoltageInput = Entry(root)
        self.MaxVoltageInput.insert(END, 'XX.X')
        self.MaxVoltageInput.place(x = 615, y = 180)

        #Current Range
        self.l15 = Label(root, text = 'Current Range:')
        self.l15.place(x = 800, y = 70)
        self.l2 = Label(root, text = 'Output High:')
        self.l2.place(x = 800, y = 100)
        self.MaxCurrentInput = Entry(root)
        self.MaxCurrentInput.insert(END, 'X.XX')
        self.MaxCurrentInput.place(x = 800, y = 120)
        self.l16 = Label(root, text = 'Output Low:')
        self.l16.place(x = 800, y = 150)
        self.MinCurrentInput = Entry(root)
        self.MinCurrentInput.insert(END, '0.00')
        self.MinCurrentInput.place(x = 800, y = 170)

        # Program Outputs (temp, current, time)
        self.l17 = Label(root, text = 'Temp (deg C)')
        self.l17.place(x = 615, y = 260)
        self.TempOutput = Label(root, text = '00.0000')
        self.TempOutput.place(x = 635, y = 280)
        
        self.l18 = Label(root, text = 'Output Current')
        self.l18.place(x = 730, y = 260)
        self.CurrentOutput = Label(root, text = '0.00')
        self.CurrentOutput.place(x = 760, y = 280)

        self.l19 = Label(root, text = 'Time')
        self.l19.place(x = 865, y = 260)
        self.TimeOutput = Label(root, text = '0.0000')
        self.TimeOutput.place(x = 865, y = 280)

        self.l20 = Label(root, text = "VISA Port: Power Supply:")
        self.l20.place(x = 615, y = 30)
        self.PSVisaInput = Entry(root)
        self.PSVisaInput.insert(END, 'ASRL8::INSTR')
        self.PSVisaInput.place(x = 755, y = 32)
        
        # START Button
        self.ProgramOn = False
        self.StartButton = Button(root, text = 'PROGRAM START/STOP', bg = 'red', command = self.ProgramOnOff)
        self.StartButton.place(x = 650, y = 320, height = 100, width = 250,)


        # PID Control
        self.l4 = Label(root, text = 'PID Gains:')
        self.l4.place(x = 600, y = 480)
        self.l5 = Label(root, text = 'P:')
        self.l5.place(x = 630, y = 515)
        self.PID_PInput = Entry(root)
        self.PID_PInput.place(x = 670, y = 515)

        self.l6 = Label(root, text = 'I:')
        self.l6.place(x = 630, y = 545)
        self.PID_IInput = Entry(root)
        self.PID_IInput.place(x = 670, y = 545)

        self.l7 = Label(root, text = 'D:')
        self.l7.place(x = 630, y = 575)
        self.PID_DInput = Entry(root)
        self.PID_DInput.place(x = 670, y = 575)

        # Temp Graph
        self.l10 = Label(root, text = 'TEMPERATURE VS TIME')
        self.l10.place(x = 240, y = 1)
        self.temperature_graph()

        # Spect Graph
        self.l11 = Label(root, text = 'SPECTROMETER READING')
        self.l11.place(x = 1160, y = 1)
        self.spectrometer_graph()

        # Laser Control
        self.l12 = Label(root, text = 'GREEN LASER CONTROL')
        self.l12.place(x = 50, y = 500)
        self.l13 = Label(root, text = 'VISA Port:')
        self.l13.place(x = 5, y = 530)
        self.LaserVISAInput = Entry(root)
        self.LaserVISAInput.insert(END, 'ASRL7::INSTR')
        self.LaserVISAInput.place(x = 120, y = 530)
        self.l8 = Label(root, text = 'Laser Power(mW):')
        self.l8.place(x = 5, y = 560)
        self.LaserPowerInput = Entry(root)
        self.LaserPowerInput.insert(END, '100')
        self.LaserPowerInput.place(x = 120, y = 560)
        self.l14 = Label(root, text = 'Actual Power Output:')
        self.l14.place(x = 5, y = 590)
        self.ActualLaserPowerOutput = Label(root, text = '00000000000')
        self.ActualLaserPowerOutput.place(x = 150, y = 590)
        self.LaserOn = False
        self.LaserButton = Button(root, text = 'LASER ON/OFF', bg = 'red', command = self.LaserToggle)
        self.LaserButton.place(x = 70, y = 650, height = 50, width = 100,)
        self.my_after()
        #if self.LaserOn == True:
        #    self.my_instrument.write('POWER?')
        #    self.ActualLaserPowerOutput.config(text=str(self.my_instrument.read()))

        # File Save Path
        self.l9 = Label(root, text = 'File Path:')
        self.l9.place(x = 500, y = 700)
        self.FileSaveLocationInput = Entry(root)
        self.FileSaveLocationInput.place(x = 500, y = 730, width = 600)



    def my_after(self, event=None):
        if self.LaserOn == True:
            self.my_instrument.write('POWER?')
            self.ActualLaserPowerOutput.config(text=str(self.my_instrument.read()))
        root.after(100, my_after)

    #def ChangeLabelText(self, event=None):
    def temperature_graph(self, event=None):
        self.x = np.linspace(0, 6*np.pi, 100)
        self.y = np.sin(self.x)

        self.fig = Figure(figsize=(6,4))
        self.ax = self.fig.add_subplot(111)

        self.ax.set_ylabel("Temperature")
        self.ax.set_xlabel("Time")
        self.ax.grid()
        self.graph = FigureCanvasTkAgg(self.fig, master=root)
        self.graph.get_tk_widget().place(x = 10, y = 20)#pack(side="top",fill='none',expand=False)
        self.line1, = self.ax.plot(self.x, self.y, 'r-') # Returns a tuple of line objects, thus the comma

        # Updating plot
        #for phase in np.linspace(0, 10*np.pi, 500):
        #    self.line1.set_ydata(np.sin(self.x + phase))
        #    self.fig.canvas.draw_idle()
        #    self.fig.canvas.flush_events()

    def spectrometer_graph(self, event=None):
        self.x = np.linspace(0, 6*np.pi, 100)
        self.y = np.cos(self.x)

        self.fig = Figure(figsize=(6,4))
        self.ax = self.fig.add_subplot(111)

        self.ax.set_ylabel("Peak Intensity")
        self.ax.set_xlabel("Wavelength")
        self.ax.grid()
        self.graph = FigureCanvasTkAgg(self.fig, master=root)
        self.graph.get_tk_widget().place(x = 930, y = 20)#pack(side="top",fill='none',expand=False)
        self.line1, = self.ax.plot(self.x, self.y, 'r-') # Returns a tuple of line objects, thus the comma

    def LaserToggle(self, event=None):
        if self.LaserOn == False:
            self.LaserButton.configure(bg = 'white')
            self.LaserOn = True
            # TURN LASER ON
            self.rm = visa.ResourceManager()
            self.my_instrument = self.rm.open_resource(str(self.LaserVISAInput.get()))
            self.my_instrument.read_termination = '\r'
            self.my_instrument.write_termination = '\r'
            self.my_instrument.write('ON')
            time.sleep(.1)
            laserPower = 'POWER=' + str(self.LaserPowerInput.get())
            self.my_instrument.write(laserPower)

        else:
            self.LaserButton.configure(bg = 'red')
            self.LaserOn = False
            # TURN LASER OFF
            self.my_instrument.write('OFF')

    def ProgramOnOff(self, event=None):
        rm = visa.ResourceManager()
        my_instrument = rm.open_resource(str(self.PSVisaInput.get()))
        my_instrument.read_termination = '\r'
        my_instrument.write_termination = '\r'
        my_instrument.write('SESS00') #set to remote mode
        time.sleep(.05)

        if self.ProgramOn == False:
            self.StartButton.configure(bg = 'white')
            self.ProgramOn = True
            #TURN POWER ON
            currentLimit = 'CURR00' + str(self.MaxCurrentInput.get()).replace('.','')
            my_instrument.write(currentLimit) #sets current limit
            time.sleep(.05)
            voltageLimit = 'SOVP00' + str(self.MaxVoltageInput.get()).replace('.','')
            my_instrument.write(voltageLimit) #sets voltage limit
            time.sleep(.05)
            my_instrument.write('VOLT00010') #sets voltage output
            time.sleep(.05)
            my_instrument.write('SOUT000') #turn power supply on
            time.sleep(.05)
            
        else:
            self.StartButton.configure(bg = 'red')
            self.ProgramOn = False
            #TURN POWER OFF
            my_instrument.write('SOUT001') #turn power supply off
            time.sleep(.05)

#CHANGED SPACING ON THIS AFTER TEST, IF IT DOESNT WORK THEN GIVE IT ANOTHER TAB
def my_after():
    # UPDATES LASER POWER OUTPUT VARIABLE IF LASER IS ON
    if A.LaserOn == True:
        A.my_instrument.write('POWER?')
        A.ActualLaserPowerOutput.config(text=str(A.my_instrument.read()))

    ######               SET UP THE POWER SUPPLY TO CONSTANTLY UPDATE VOLTAGE AND CURRENT              ##############

    root.after(100, my_after)

if __name__ == '__main__':
    root = Tk()
    A = App(root)
    
    # RUNS THIS FUNCTION EVERY 100 MS, UPDATES VARIABLES
    my_after()

    root.mainloop()
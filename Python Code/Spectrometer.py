import ctypes
import clr
import os
import numpy as np
import sys

import default_settings

class MySpectro:
    # variables
    DataBuffer = []
    SpectralData = []
    DarkData = []
    WaveData = []

    IntegrationPeriod = 0
    TemperatureCompensation = 0
    chan = 1

    buffer = []
    
    
    def __init__(self):

        clr.AddReference('C:\\Users\\mckay\\Desktop\\RA\\spectrom.dll')

        from Spectro_1 import SwWrapper
        self.my_spectrometer = SwWrapper()
        #my_spectrometer.Init()
        #my_spectrometer.Close()

    def initiate_spectrometer(self):
        self.my_spectrometer.Init()
        # get default variable values
        # override cal coefficients w/ ones from spectrometer
        # fill wavedata array
        # set integration period from XTRate
        # set timer to 1/3 integration period (check 3 times)
        self.my_spectrometer.Rate(self.IntegrationPeriod)
        self.my_spectrometer.Update(default_settings.scansToAvg, default_settings.xsmooth, default_settings.tempComp)
        self.my_spectrometer.Mode(default_settings.xtrate)

    def getBWee(self, chan):
        #int i
        #int16 ec
        #int16 ea
        #string coeffbuf

        ec = np.int16(chan)
        ea = np.int16(0x80)
        if my_spectrometer.eeRead(ec, ea, buffer) == False:
            return
            
        for (i in range(14)):
            if buffer[i] < 0x20 or buffer[i] > 127:
                return

        # continue here
        

    #def update_spectrometer:

    #def close_spectrometer:
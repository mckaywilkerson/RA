import ctypes
import clr
import os
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

    #def update_spectrometer:

    #def close_spectrometer:
# NOTES: make sure that you know that VISA port for the power supply before you start this (line 45)
#        also need to make sure that the DAQ is Dev1 (line 31)

import PID
import time
import nidaqmx
import visa

system = nidaqmx.system.System.local()
targetT = 20        # Target temperature
P = 0               # Initial PID values
I = 0
D = 0

pid = PID.PID(P, I, D)
pid.SetPoint = targetT
pid.setSampleTime(.5)

def setValues():
    # set the values to use
    pid.SetPoint = 20
    pid.setKp(0.5)
    pid.setKi(0.5)
    pid.setKd(0.5)

while 1:
    setValues()

    #READS TEMP DATA FROM DAQ
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        temp = float(task.read()) * 16.562 - 12.369

    pid.update(temp, time.time())
    pidOutput = pid.output
    pidOutput = max(min( int(pidOutput), 100 ),0)       # ensures that the output is between 0-100
    pidOutput = pidOutput * 9 / 100                     # scale it down to between 0-9

    

    time.sleep(.5)

    #SETS POWER SUPPLY COMMANDS
    rm = visa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR')
    my_instrument.read_termination = '\r'
    my_instrument.write_termination = '\r'

    my_instrument.write('SESS00')   # Sets to remote mode
    my_instrument.write('SOVP00050')# Sets max voltage to 5V
    my_instrument.write('CURR00050')# Sets current to .5 Amps
    my_instrument.write('SOUT000')  # Turns power supply on
    time.sleep(1)
    my_instrument.write('SOUT001')  # Turns power supply off
    
import PID
import time
import nidaqmx

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

    #READ TEMP DATA
    temperature = 15

    pid.update(temperature, time.time())
    pidOutput = pid.output
    pidOutput = max(min( int(pidOutput), 100 ),0)       # ensures that the output is between 0-100
    pidOutput = pidOutput * 9 / 100                     # scale it down to between 0-9

    print(pidOutput)

    time.sleep(.5)

    #SET THE POWER SUPPLY COMMANDS BASED ON THIS
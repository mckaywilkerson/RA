import pyvisa as visa
import time

rm = visa.ResourceManager()
print(rm.list_resources())

my_instrument = rm.open_resource('ASRL8::INSTR')

my_instrument.read_termination = '\r'
my_instrument.write_termination = '\r'

#my_instrument.write('SOUT00')
my_instrument.write('SESS00')           # Sets power supply to remote mode (address 00)
time.sleep(.05)
my_instrument.write('VOLT00000')        # Sets Voltage output: VOLT(address = 00)(voltage = XX.X)
time.sleep(.05)         # Needs this delay to be able to have time to write (.01 was too small, but .05 seems to work.
                        # can try for shorter if I need to.)
my_instrument.write('CURR00050')        # Sets Current limit: CURR(address = 00)(current = X.XX)
time.sleep(.05)
my_instrument.write('SOUT000')
time.sleep(.05)
my_instrument.write('SOUT001')
# OTHER COMMANDS
#    SOVP<address><voltage(XX.X)> sets max voltage output
#    GETS<address> gets the set voltage and current (return will be <volage(XX.X)><current(X.XX)><0/1 (0 if in CV, 1 if in CC)>)
#    GETD<address> gets measured voltage and current (return will be <voltage><current><0/1>)
#    SOUT<address><status(0 if enable, 1 if disable)> Turn on or off the power supply
print(my_instrument.read())

import pyvisa as visa
import time

rm = visa.ResourceManager()

# print all the visa devices you have access to
print(rm.list_resources())

my_instrument = rm.open_resource('ASRL7::INSTR')

my_instrument.read_termination = '\r'
my_instrument.write_termination = '\r'

my_instrument.write('ON')
time.sleep(.1)
my_instrument.write('POWER=100') #IN MW
time.sleep(1)
# for some reason, it wont do it only once and basically skips the OFF command if right before
for x in range(100):
    my_instrument.write('POWER?')
    print(my_instrument.read())
my_instrument.write('OFF')
import visa
import time

rm = visa.ResourceManager()
print(rm.list_resources())

my_instrument = rm.open_resource('ASRL5::INSTR')

my_instrument.read_termination = '\r'
my_instrument.write_termination = '\r'

my_instrument.write('ON')
my_instrument.write('POWER=100') #IN MW
time.sleep(1)
# for some reason, it wont do it only once and basically skips the OFF command if right before
for x in range(2):
    my_instrument.write('POWER?')
    print(my_instrument.read())
my_instrument.write('OFF')
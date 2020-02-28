import pyvisa as visa
import time

rm = visa.ResourceManager()

# print all the visa devices you have access to
print(rm.list_resources())
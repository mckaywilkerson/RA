# default settings for the spectrometer

# xsmooth: smoothing using pixel boxcar averaging across spectral scan
# 0 = NONE
# 1 = 5 pixels
# 2 = 9 pixels
# 3 = 17 pixels
# 4 = 33 pixels
int xsmooth = 1

# tempComp: temperature compensation uses detector optical black region
# pixels 1-12
# 0 = NONE
# 1 = ON
int tempComp = 0

# scansToAvg: scan averaging accumulates scans then divides by
# scansToAvg (1-99)
int scansToAvg = 1

# 4 bis 65500 (differential scanning fluorimetry). Used to change
# detector integration rate in ms (4-65500)
int DSF = 30

# xtrate: has something to do with integration period (IP)
# 0 = if IP < 1, IP = 1
# 1 = if IP < 15, IP = 15
# 2 = if IP < 30, IP = 30
int xtrate = 2

# set CalCoeff values
float CalCoeff1 = 0.69379
float CalCoeff2 = 0.0001266
float CalCoeff3 = 336.09
float CalCoeff4 = 0
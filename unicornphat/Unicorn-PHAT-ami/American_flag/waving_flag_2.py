################################################################
#                    Waving Flag 2                             #
################################################################
# Description:                                                 #
# The title pretty much explains it.                           #
#                                                              #
# Author: Paul Ryan                                            #
#                                                              #
################################################################
#!/usr/bin/python
import unicornhat, signal, time, random

unicornhat.set_layout(unicornhat.PHAT)
unicornhat.brightness(0.5)
unicornhat.rotation(180)

R = (255,0,0)
W = (255, 255, 255)
B = (0,0,255)
off = (0, 0, 0)
R2 = (128, 0, 0)
W2 = (128, 128, 128)
B2 = (0, 0, 128)

flag = [
    [W, W, W, W, W, W, W, W], 
    [R, R, R, R, R, R, R, R], 
    [W, W, W, W, B, B, B, B], 
    [R, R, R, R, B, B, B, B],
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off,off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

wave0 = [
    [W, W, W, W, W, W, W, W2], 
    [R, R, R, R, R, R, R, R2], 
    [W, W, W, W, B, B, B, B2], 
    [R, R, R, R, B, B, B, B2], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

wave1 = [
    [W, W, W, W, W, W, W2, W], 
    [R, R, R, R, R, R, R2, R], 
    [W, W, W, W, B, B, B2, B], 
    [R, R, R, R, B, B, B2, B], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

wave2 = [
    [W, W, W, W, W, W2, W, W], 
    [R, R, R, R, R, R2, R, R], 
    [W, W, W, W, B, B2, B, B], 
    [R, R, R, R, B, B2, B, B], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

wave3 = [
    [W, W, W, W, W2, W, W, W], 
    [R, R, R, R, R2, R, R, R], 
    [W, W, W, W, B2, B, B, B], 
    [R, R, R, R, B2, B, B, B], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

wave4 = [
    [W, W, W, W2, W, W, W, W], 
    [R, R, R, R2, R, R, R, R], 
    [W, W, W, W2, B, B, B, B], 
    [R, R, R, R2, B, B, B, B],  
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

wave5 = [
    [W, W, W2, W, W, W, W, W], 
    [R, R, R2, R, R, R, R, R], 
    [W, W, W2, W, B, B, B, B], 
    [R, R, R2, R, B, B, B, B], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

wave6 = [
    [W, W2, W, W, W, W, W, W], 
    [R, R2, R, R, R, R, R, R], 
    [W, W2, W, W, B, B, B, B], 
    [R, R2, R, R, B, B, B, B], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]


wave7 = [
    [W2, W, W, W, W, W, W, W], 
    [R2, R, R, R, R, R, R, R], 
    [W2, W, W, W, B, B, B, B], 
    [R2, R, R, R, B, B, B, B], 
    # Don't use the 4 rows below for UnicornPHAT, use only for UnicornHAT
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off], 
    [off, off, off, off, off, off, off, off]
]

while True:
    unicornhat.set_pixels(flag)
    unicornhat.show()
    time.sleep(5.0)
    unicornhat.set_pixels(wave0)
    unicornhat.show()
    time.sleep(0.05)
    unicornhat.set_pixels(wave1)
    unicornhat.show()
    time.sleep(0.05)
    unicornhat.set_pixels(wave2)
    unicornhat.show()
    time.sleep(0.05)
    unicornhat.set_pixels(wave3)
    unicornhat.show()
    time.sleep(0.05)
    unicornhat.set_pixels(wave4)
    unicornhat.show()
    time.sleep(0.05)
    unicornhat.set_pixels(wave5)
    unicornhat.show()
    time.sleep(0.05)
    unicornhat.set_pixels(wave6)
    unicornhat.show()
    time.sleep(0.05)
    unicornhat.set_pixels(wave7)
    unicornhat.show()
    time.sleep(0.05)

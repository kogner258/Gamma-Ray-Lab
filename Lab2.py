import math as pi
import matplotlib.pyplot as plt
import numpy as np

volts = np.array([620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 1000])
amps = np.array([100, 332, 464, 660, 780, 920, 1040, 1160, 1280, 1440, 1540, 1720, 1920, 2040, 2200, 2400, 2600, 4200, 5080, 6240])
cts = np.array([0, 0, 0, 0, 0, 219, 234, 269, 221, 263, 256, 265, 293, 301, 285, 262, 302, 285, 319, 266])
ctsr = np.array([0, 0, 0, 0, 0, 21.9, 23.4, 26.9, 22.1, 26.3, 25.6, 26.5, 29.3, 30.1, 28.5, 26.2, 30.2, 28.5, 31.9, 26.6])

plt.plot(volts, ctsr, color='b', marker='o')
plt.title('Volts vs Count Rate')
plt.xlabel('Volts (mV)')
plt.ylabel('Count Rate')
plt.grid(True)
plt.show()

plt.plot(volts, amps, color="r")
plt.title('Volts vs Amplitude')
plt.xlabel("Volts (mV)")
plt.ylabel("Amps (mV)")
plt.grid(True)
plt.show()


cts2 = np.array([17, 29, 21, 25, 22, 24, 17, 18, 22, 15, 28, 26, 35, 22, 24, 22, 28, 18, 21, 19, 23, 22, 15, 20, 24, 19, 23, 29, 18, 15, 25, 32, 24, 18, 19, 33, 23, 27, 29, 30, 29, 19, 22, 22, 21, 29, 19, 22, 17, 25, 29, 24, 17, 19, 28, 23, 19, 21, 18, 22, 28, 22, 16, 32, 28, 25, 17, 26, 21, 21, 16, 31, 23, 20, 15, 24, 30, 26, 30, 25, 17, 23, 29, 28, 29, 22, 19, 22, 21, 15, 22, 16, 25, 20, 22, 32, 22, 24, 21, 28])
range = np.arange(1, 101, 1)
ctsm = np.mean(cts2)
cts3 = []
for num in cts2:
    res = np.math.factorial(num)
    cts3.append(res)

P1 = np.exp(-ctsm)*(ctsm**cts2)/cts3

plt.plot(range, P1, "go")
plt.title("Poisson Distribution of 100 Numbers")
plt.xlabel("Counts")
plt.ylabel("Number of Counts")
plt.grid(True)
plt.show()


thickness = np.array([])
bgr = 0.57
rate = np.array([])
rate = rate - bgr
        
countr = np.array([])
countre = countr*0.03
        
uncert = 1/countre
weight = 1/uncert
plt.plot(thickness, countr, color="p")
plt.title("Main Experiment Graph")
plt.xlabel("Thickness of Lead")
plt.ylabel("Count Rate of Gamma Rays")
plt.grid(True)
plt.show()
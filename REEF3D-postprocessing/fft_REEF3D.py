# Written by Widar Weizhi Wang 
# For master students at NTNU

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d 
from scipy.fftpack import fft
from scipy.ndimage import gaussian_filter1d 

# %% load the time series 
N_gauges = 14
N_headers=N_gauges+7
fsf_t = np.loadtxt('./data/REEF3D_FNPF_WSF/REEF3D-FNPF-WSF-HG.dat', skiprows=N_headers)

# %% fft 
def wave_spectrum(data,nfft,Fs):
    
    fft_s = fft(data,N)/N
    f = Fs/2*np.arange(0,1,1/nfft)
    f = np.transpose(f)
    df = f[2]-f[1]
    p = abs(fft_s[0:nfft])*2
    E = p**2/2/df
   
    return E,f

# %% get the spetrum and hs 
wave_gauge = 1 
time = fsf_t[:,0]
free_o = fsf_t[:,1:]
func_free_s = interp1d(time,free_o,axis = 0)
Fs = 50
ts = np.arange(min(time),max(time),1/Fs)
free_i = func_free_s(ts)
N = len(free_i)
nfft = int(np.floor(N/2)+1)
E, f = wave_spectrum(free_i[:,wave_gauge-1], nfft, Fs)
sig = 10
S = gaussian_filter1d(E,sig)
Hs = 4*np.sqrt(abs(np.trapz(E,f)))

fig = plt.figure()
plt.plot(f, S)
plt.xlabel('f (Hz)')
plt.ylabel('S(f) ($m^2/Hz$)')
plt.xlim([0.0, 5.0])
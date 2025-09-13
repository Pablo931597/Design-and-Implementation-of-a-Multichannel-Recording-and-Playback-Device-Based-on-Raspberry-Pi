import pyaudio
import wave
import numpy as np
import os
import tkinter
import matplotlib.pyplot as plt
from scipy.io import wavfile
from matplotlib.animation import FuncAnimation
import ventana5
import time
import Potenciometro
from gpiozero import MCP3008
#import reloj

def act_barra_volumen(output_buffer):
    
    for g in range(8):
        vol = 0
        progreso = ventana5.get_barra_volumen()
        if np.isnan(abs(np.sqrt(np.mean(np.square(output_buffer[:,g]))))):
            pass
        else:
            vol = abs(np.sqrt(np.mean(np.square(output_buffer[:,g]))))
            print(vol)
            progreso[g].set(vol)

def reproducir(file,btnCH,colores):
    #reloj.clock()
    CHUNK = 512
    volume=1
    print(file)
    wav = []
    wf = []
    factor = 0.55
    
    size = 0
    for x in range(len(file)):
        if os.path.isfile(file[x]):
            wav.append(file[x])
            wf.append(wave.open(wav[size], 'rb'))
            size = size+1
        else:
            size = size
    colors = []
    
    for y in range(8):
        for n in range(9):
            if btnCH[y].cget('background') == colores[n]:
                colors.append(n)
            else:
                pass
    print (colors)
    
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                    channels=8,
                    rate=48000,
                    output=True,
                    output_device_index=0,
                    frames_per_buffer=CHUNK)

    print("Reproduciendo audio...")
    stop = False
    finish = True
    try:
        while True:
            stop = ventana5.get_stop()
            finish = ventana5.get_finish()
            
            if finish == True:
                break
            
            while stop:
                finish = ventana5.get_finish()
                if finish == True:
                    break
                time.sleep(1)
                stop = ventana5.get_stop()
                
            data = []
            samples = []
            r = False
            for i in range(size):
                data.append(wf[i].readframes(CHUNK))
                
                if all(elemento == 0 for elemento in data[i]):
                    r = True
                    pass
                    
                else:
                    samples.append(np.frombuffer(data[i], dtype=np.int16))
            
            if r == True:
                break
            
            #num_samples = len(samples)
            num_samples = len(samples[0])
                        
            output_buffer = np.zeros((num_samples, 8), dtype=np.int16)
            
            for t in range(len(colors)):

                if  colors[t] == 0:
                    pass
                else:
                    output_buffer[:,t] = samples[colors[t]-1]
            #for i in range(8):
            try:
                for i in range(8):
                    pot = MCP3008(channel=i)
                    output_buffer[:,i] = output_buffer[:,i]*round(pot.value,1)*factor
            except Exception as e:
                break
            
            output_buffer = np.clip(output_buffer, -32768, 32767)
            
            act_barra_volumen(output_buffer)
                
            output_data = output_buffer.tobytes()

            stream.write(output_data)
            
    except KeyboardInterrupt:
        pass

    print("Finalizando...")
    stream.stop_stream()
    stream.close()
    for u in range(len(wf)):
        wf[u].close()
    p.terminate()

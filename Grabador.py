import threading
import pyaudio
import wave
import numpy as np
from datetime import datetime
import SaveFile
import ventana3
import ventana2
from tkinter import *
import tkinter
from tkinter import ttk
import Potenciometro

def act_barra_volumen(output_buffer):
    
    for g in range(8):
        vol = 0
        progreso = ventana3.get_barra_volumen()
        if np.isnan(abs(np.sqrt(np.mean(np.square(output_buffer[:,g]))))):
            pass
        else:
            vol = abs(np.sqrt(np.mean(np.square(output_buffer[:,g]))))
            print(vol)
            progreso[g].set(vol)


def iniciar_grabacion(*args):
    rec_channels = args
    to_rec = []
    for i in range(8):
        if rec_channels[i] == True:
            to_rec.append(i)
            
    print(to_rec)
    
    FORMAT = pyaudio.paInt32
    CHANNELS = 8
    RATE = 48000
    CHUNK = 512
    CANAL_GRABAR = to_rec
    audio = pyaudio.PyAudio()
    factor = 0.55
    
    frames = []
    stop = False
    stream_in = audio.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            output_device_index=1,
                            frames_per_buffer=CHUNK)

    stream_out = audio.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            output=True,
                            output_device_index=0,
                            frames_per_buffer=CHUNK)
    
    print('Grabacion iniciada...')
    while True:
        
        stop = ventana3.get_stop()
        if stop == True:
            break
        
        data = stream_in.read(CHUNK)
        
        audio_data = np.frombuffer(data, dtype=np.int16)
        audio_data = audio_data.reshape(-1, CHANNELS)
        
        #selected_channels = audio_data[:, CANAL_GRABAR]
        output_buffer = np.zeros((len(audio_data), 8), dtype=np.int16)
        try:
            for i in range (len(to_rec)):
                pot = MCP3008(channel=i)
                output_buffer[:,to_rec[i]] = audio_data[:,to_rec[i]]*round(pot.value,1)*factor
        except Exception as e:
                break
        #for i in range(8):
                #output_buffer[:,i] = output_buffer[:,i]*Potenciometro.gain(i)
        
        output_buffer = np.clip(output_buffer, -32768, 32767)
        
        act_barra_volumen(output_buffer)
        
        mono_data = np.mean(output_buffer, axis=1).astype(np.int16)
        
        frames.append(mono_data.tobytes())
        
        stream_out.write(mono_data.tobytes())
        
    stream_in.stop_stream()
    stream_in.close()
    stream_out.stop_stream()
    stream_out.close()
    audio.terminate()
    
    date = datetime.now()
    ventana3.ventana3.withdraw()
    SaveFile.mostrar_ventana(f"Record of {date}.wav")
    
    guardar = SaveFile.guardarwav()

    if guardar == True:
        wf = wave.open(f"/home/pi3/Desktop/TFG/Grabaciones/Record of {date}.wav", 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        print("Guardado correctamente")
    else:
        print("No se ha guardado")
           

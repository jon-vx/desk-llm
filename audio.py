import sounddevice as sd
import numpy
import soundfile as sf
import queue
import sys
assert numpy

device : int = 0
samplerate : int = 48000
filename : str = "test.wav"


q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

try:
    with sf.SoundFile(filename, mode='x', samplerate=samplerate, channels=1) as file:
        with sd.InputStream(samplerate=samplerate, device=device,channels=1, callback=callback):
            print("#" * 80)
            print("ctrl+c to stop recording")
            print("#" * 80)
            while True:
                file.write(q.get())
except KeyboardInterrupt:
    print('finished recording: ' + filename)



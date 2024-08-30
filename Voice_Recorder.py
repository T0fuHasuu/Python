import sys
import subprocess
import pkg_resources

# Define the required libraries
required = {'sounddevice', 'scipy', 'wavio'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

# Install missing packages
if missing:
    print(f"Installing missing packages: {missing}")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

# Import the libraries after installation
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 48000  

# Recording duration
duration = 20

# Reduce channels to 1 for mono recording
channels = 1

# Start recorder with the given values of duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=channels)

# Record audio for the given number of seconds
sd.wait()

# Save the recording to a file
write("recording0.wav", freq, recording)
wv.write("recording1.wav", recording, freq, sampwidth=2)

# Play the recording using sounddevice
print("Playing the recording...")
sd.play(recording, samplerate=freq)
sd.wait()  # Wait until playback is finished

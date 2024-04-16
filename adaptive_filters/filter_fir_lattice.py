import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
    
# 1. Read the WAV file
sample_rate, input_audio = wavfile.read("altered_gettysburg.wav")

# 2. Define the coefficients of the FIR lattice filter
coefficients = [0.1, 0.2, 0.3, 0.4, 0.5]

# 3. Apply the FIR lattice filter
output_audio, _ = signal.lfilter(coefficients, [1], input_audio, zi=np.zeros(len(coefficients)-1))

# 4. Write the filtered audio to a new WAV file
output_audio = np.round(np.clip(output_audio, -32768, 32767)).astype(np.int16) 
wavfile.write("output.wav", sample_rate, output_audio)

plt.figure(figsize=(10, 6))
plt.plot(input_audio, color='b', label='Input Signal')
plt.plot(output_audio, color='r', label='Output Signal')
plt.title('Input and Output Signals')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()
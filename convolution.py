from scipy.io import wavfile
from scipy.signal import convolve
import numpy as np
import matplotlib.pyplot as plt

# Read the input WAV file
sample_rate, input_audio = wavfile.read("altered_gettysburg.wav")

# Define the impulse response (kernel) of the convolution filter
# Example: a simple moving average filter
kernel_length = 5
kernel = np.ones(kernel_length) / kernel_length

# Perform convolution on the input audio with the defined kernel
output_audio = convolve(input_audio, kernel, mode='same')

# Write the output audio to a new WAV file
wavfile.write("output_convolved.wav", sample_rate, output_audio.astype(np.int16))

print("Convolved audio saved to 'output_convolved.wav'.")

plt.figure(figsize=(10, 6))
plt.plot(input_audio, color='b', label='Input Signal')
plt.plot(output_audio, color='r', label='Output Signal')
plt.title('Input and Output Signals')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()
#importing these libraries -> install with pip3 before running script on machine
from playsound import playsound
import matplotlib.pyplot as plt
import wave
import numpy as np

''' This script that serves as signal processing pipeline '''

# plots the audio amplititude over time
def visualizeAudio(path):
    # Open the WAV file
    with wave.open(path, 'rb') as wav_file:
        # Get the audio parameters
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        num_channels = wav_file.getnchannels()

        # Read the audio data
        audio_data = wav_file.readframes(num_frames)
        audio_data = np.frombuffer(audio_data, dtype=np.int16)

    # Close the WAV file
    wav_file.close()

    # Create a time array based on the sample rate and number of frames
    time = np.arange(0, num_frames) / sample_rate

    # Create a figure for the plot
    plt.figure(figsize=(12, 6))

    # Plot the audio data
    plt.plot(time, audio_data, color='b')

    # Label the plot
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Audio Data Visualization')
    plt.grid()

    # Show the plot
    plt.show()



def main():
    #modify this variable to read in different inputs
    inputAudioPath = '/Users/rahulnair/umd/gemstone/gettysburg10.wav'

    #function calls 
    playsound(inputAudioPath)
    visualizeAudio(inputAudioPath)

if __name__ == "__main__":
    main()


 


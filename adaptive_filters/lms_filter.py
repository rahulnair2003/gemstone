import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.io import wavfile
import scipy.io.wavfile as wav
import playsound as ps



class LMSFilter:
    def __init__(self, num_taps, mu):
        self.num_taps = num_taps
        self.mu = mu
        self.coeffs = np.zeros(num_taps)
        self.state = np.zeros(num_taps - 1)

    def process(self, input_data, reference_data):
        output_data = np.zeros_like(reference_data)
        error_data = np.zeros_like(reference_data)
        
        for i in range(len(reference_data)):
            # Compute filter output
            output_data[i] = np.dot(self.coeffs, np.concatenate(([input_data[i]], self.state)))
            # Compute error
            error_data[i] = reference_data[i] - output_data[i]
            # Update coefficients
            self.coeffs += self.mu * error_data[i] * np.concatenate(([input_data[i]], self.state))
            # Update state
            self.state = np.roll(self.state, 1)
            self.state[0] = input_data[i]
        
        return output_data, error_data

def main(input_file, output_file):
    # Read input audio file
    input_data, samplerate = sf.read(input_file)
    # Assume mono audio
    if len(input_data.shape) > 1:
        input_data = input_data[:, 0]
    
    # Initialize LMS filter
    num_taps = 32  # Example number of taps, you may need to adjust this
    mu = 0.1  # Example step size, you may need to adjust this
    lms_filter = LMSFilter(num_taps, mu)
    
    # Process audio data
    output_data, error_data = lms_filter.process(input_data, input_data)  # Using input as reference
    
    # Write output audio file
    sf.write(output_file, output_data, samplerate)

    # Plot input and output signals
    plt.figure(figsize=(10, 6))
    plt.plot(input_data, color='b', label='Input Signal')
    plt.plot(output_data, color='r', label='Output Signal')
    plt.title('Input and Output Signals')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.tight_layout()
    plt.show()

def calculate_metrics(data):
    # Signal-Noise-ratio (SNR)
    signal_power = np.sum(data ** 2) / len(data)
    noise_power = np.mean((data - np.mean(data)) ** 2)
    snr = 10 * np.log10(signal_power / noise_power)

    # Total Harmonic Distortion (THD)
    thd = np.sqrt(np.sum(data ** 2) / len(data))

    # Noise floor
    noise_floor = 10 * np.log10(np.mean(data ** 2))

    # Dynamic Range
    dynamic_range = 10 * np.log10(np.max(data) - np.min(data))

    # Crest Factor
    crest_factor = np.max(np.abs(data)) / np.sqrt(np.mean(data ** 2))

    return snr, thd, noise_floor, dynamic_range, crest_factor

if __name__ == "__main__":
    input_file = "input.wav"
    output_file = "output.wav"
    main(input_file, output_file)
    ps.playsound(output_file)
    fs_in, data_in = wav.read("input.wav")
    fs_out, data_out = wav.read("output.wav")

    # Calculate metrics for input and output
    snr_in, thd_in, noise_floor_in, dynamic_range_in, crest_factor_in = calculate_metrics(data_in)
    snr_out, thd_out, noise_floor_out, dynamic_range_out, crest_factor_out = calculate_metrics(data_out)

    # Print metrics side by side
    print("{:<25} {:<25} {:<25}".format("Metric", "Input", "Output"))
    print("-" * 75)
    print("{:<25} {:<25} {:<25}".format("Signal-Noise Ratio (SNR)", f"{snr_in:.2f} dB", f"{snr_out:.2f} dB"))
    print("{:<25} {:<25} {:<25}".format("Total Harmonic Distortion (THD)", f"{thd_in:.2f}", f"{thd_out:.2f}"))
    print("{:<25} {:<25} {:<25}".format("Noise Floor", f"{noise_floor_in:.2f} dB", f"{noise_floor_out:.2f} dB"))
    print("{:<25} {:<25} {:<25}".format("Dynamic Range", f"{dynamic_range_in:.2f} dB", f"{dynamic_range_out:.2f} dB"))
    print("{:<25} {:<25} {:<25}".format("Crest Factor", f"{crest_factor_in:.2f}", f"{crest_factor_out:.2f}"))

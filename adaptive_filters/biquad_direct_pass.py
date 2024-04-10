import numpy as np
import soundfile as sf
from scipy.io import wavfile
import scipy.io.wavfile as wav
import playsound as ps
import matplotlib.pyplot as plt


import numpy as np
import soundfile as sf


class BiquadFilter:
    def __init__(self, num_stages, coeffs):
        self.num_stages = num_stages
        self.coeffs = coeffs
        self.state = np.zeros(4 * num_stages)

    def process(self, input_data):
        output_data = np.zeros_like(input_data)

        for n in range(len(input_data)):
            acc = input_data[n]
            for stage in range(self.num_stages):
                b0, b1, b2, a1, a2 = self.coeffs[stage]
                Xn1, Xn2, Yn1, Yn2 = self.state[4*stage:4*(stage+1)]

                acc = (b0 * acc) + (b1 * Xn1) + \
                    (b2 * Xn2) - (a1 * Yn1) - (a2 * Yn2)

                self.state[4*stage+1] = Xn1
                self.state[4*stage+2] = acc
                self.state[4*stage+3] = Yn1
                self.state[4*stage] = input_data[n]

            output_data[n] = acc

        return output_data


def main(input_file, output_file):
    # Read input audio file
    input_data, samplerate = sf.read(input_file)
    # Assume mono audio
    if len(input_data.shape) > 1:
        input_data = input_data[:, 0]

    # Biquad filter coefficients (example coefficients)
    num_stages = 2  # Example number of stages
    coeffs = [
        [1.0, -0.01, 0.005, 0.01, 0.001],  # Adjusted coefficients for stage 1
        [0.5, -0.005, 0.001, 0.005, 0.0005]  # Example coefficients for stage 2
    ]

    # Initialize Biquad filter
    biquad_filter = BiquadFilter(num_stages, coeffs)

    # Process audio data
    output_data = biquad_filter.process(input_data)

    # Write output audio file
    sf.write(output_file, output_data, samplerate)
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
    snr_in, thd_in, noise_floor_in, dynamic_range_in, crest_factor_in = calculate_metrics(
        data_in)
    snr_out, thd_out, noise_floor_out, dynamic_range_out, crest_factor_out = calculate_metrics(
        data_out)

    # Print metrics side by side
    print("{:<25} {:<25} {:<25}".format("Metric", "Input", "Output"))
    print("-" * 75)
    print("{:<25} {:<25} {:<25}".format("Signal-Noise Ratio (SNR)",
          f"{snr_in:.2f} dB", f"{snr_out:.2f} dB"))
    print("{:<25} {:<25} {:<25}".format(
        "Total Harmonic Distortion (THD)", f"{thd_in:.2f}", f"{thd_out:.2f}"))
    print("{:<25} {:<25} {:<25}".format("Noise Floor",
          f"{noise_floor_in:.2f} dB", f"{noise_floor_out:.2f} dB"))
    print("{:<25} {:<25} {:<25}".format("Dynamic Range",
          f"{dynamic_range_in:.2f} dB", f"{dynamic_range_out:.2f} dB"))
    print("{:<25} {:<25} {:<25}".format("Crest Factor",
          f"{crest_factor_in:.2f}", f"{crest_factor_out:.2f}"))

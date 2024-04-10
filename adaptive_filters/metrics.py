import numpy as np
import scipy.io.wavfile as wav

def calculate_metrics(data):
    signal_power = np.sum(data ** 2) / len(data)
    noise_power = np.mean((data - np.mean(data)) ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    

    thd = np.sqrt(np.sum(data ** 2) / len(data))
    noise_floor = 10 * np.log10(np.mean(data ** 2))
    dynamic_range = 10 * np.log10(np.max(data) - np.min(data))
    crest_factor = np.max(np.abs(data)) / np.sqrt(np.mean(data ** 2))
    
    return snr, thd, noise_floor, dynamic_range, crest_factor


fs_in, data_in = wav.read("input.wav")
fs_out, data_out = wav.read("output.wav")


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

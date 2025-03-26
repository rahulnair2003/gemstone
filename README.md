# Team ECHO Benchmarking Tool Suite

## Overview

This tool suite allows users to generate structured benchmarks and evaluate audio processing models across diverse environmental conditions. Using the audio dataset, the notebooks help to process each `.wav` file through a selected model, compute evaluation metrics, and store results in a JSON format for easy comparison and visualization.

## Dataset

Download the labeled audio dataset here:  
[Google Drive – Team ECHO Dataset](https://drive.google.com/file/d/1T8BgIkIYePeYGhqIF8kHW1Nw-tcWQadU/view?usp=share_link)

After downloading, place the dataset in your project directory and update the path in the notebook as needed.

## Getting Started

1. Clone this repository
2. Download the dataset and place it in the working directory
3. Open and run `generateBenchmark.ipynb` to:
   - Load each `.wav` file from the dataset
   - Process it through your selected audio model
   - Compute the following audio quality metrics:
     - Total Harmonic Distortion (THD)
     - Signal-to-Noise Ratio (SNR)
     - Noise Floor
     - Dynamic Range
     - Crest Factor
     - Waveform Complexity Index (WCI)
   - Store the output in a structured JSON format containing:
     - Environmental metadata: `Indoors`, `Crowded`, `Speaking`, `Walking`
     - Speaker metadata: `Voice_Type`, `Voice_ID`
     - File metadata: duration, location, filename

4. Use `comparejsons.ipynb` to analyze and visualize model performance across different environments and metrics


## System Requirements

To run the benchmarking notebooks locally, ensure your system meets the following requirements:

### Python Environment
- Python Version: 3.8 – 3.11 (recommended: 3.9 or later)
- It is recommended to use a virtual environment (e.g., `venv` or `conda`) to manage dependencies.

### Required Python Packages
Install the following packages using pip:

```bash
pip install numpy pandas scipy matplotlib librosa soundfile fastdtw
```

Alternatively, install from the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Operating System Compatibility
- Compatible with Linux, macOS, and Windows

### System-Level Dependencies
Some audio libraries depend on external tools for audio decoding and file handling:

**On Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg libsndfile1
```

**On macOS (using Homebrew):**
```bash
brew install ffmpeg libsndfile
```

**On Windows:**
- Download FFmpeg from https://ffmpeg.org/download.html
- Add the FFmpeg binary folder to your system PATH
- Ensure libsndfile is installed via pip (already included with `soundfile`)

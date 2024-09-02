
# Audio Modem Samples

This repository contains examples of signal modulation via audio using FSK (Frequency Shift Keying) modulation in Python. The project is designed to transmit and receive simple messages using sounds at different frequencies.

## Requirements

To run the scripts, you need to have Python installed along with the following libraries:

- `numpy`
- `sounddevice`
- `scipy`

You can install them using the command:

```bash
pip install numpy sounddevice scipy
```

## How to Run

The project includes two main scripts:

1. **Transmitter**: `fsk_transmitter.py`
2. **Receiver**: `fsk_receiver.py`

### Steps

1. **On the transmitting computer**: Run the `fsk_transmitter.py` script to send a message via sound.
   
   ```bash
   python fsk_transmitter.py
   ```

2. **On the receiving computer**: Run the `fsk_receiver.py` script to receive and decode the transmitted message.

   ```bash
   python fsk_receiver.py
   ```

## Configuration

### Receiver (`fsk_receiver.py`)

The following variables can be adjusted for calibration as needed:

- `sample_rate`: Sampling rate (default: 48000 Hz)
- `duration`: Duration of each bit in seconds (default: 0.1 seconds)
- `freq_0`: Frequency to represent bit 0 (default: 18000 Hz)
- `freq_1`: Frequency to represent bit 1 (default: 20000 Hz)
- `tolerance`: Frequency detection tolerance (default: 80 Hz)
- `header`: Synchronization pattern (default: '10101010' - 8 alternating bits)
- `duration_seconds`: Maximum listening time (default: 20 seconds)

### Transmitter (`fsk_transmitter.py`)

The variables that can be adjusted in the transmitter include:

- `sample_rate`: Sampling rate (default: 48000 Hz)
- `duration`: Duration of each bit in seconds (default: 0.1 seconds)
- `freq_0`: Frequency to represent bit 0 (default: 18000 Hz)
- `freq_1`: Frequency to represent bit 1 (default: 20000 Hz)
- `header`: Synchronization pattern (default: '10101010' - 8 alternating bits)

## Considerations

This script is designed to record audio for a set period and then decode it. This means that communication is not in real-time but is processed after recording. If real-time communication is needed, the code would need to be adapted to support continuous streaming.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests for improvements and fixes.


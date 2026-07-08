# Hybrid Analog–Digital QRS Detector


A complete ECG heartbeat detection system that combines analog signal conditioning with digital peak detection logic. The project demonstrates how biomedical signals can be processed through a hybrid workflow, from analog filtering and amplification to digital QRS complex detection using finite state machines.



# Features

Analog front-end for ECG filtering and amplification.
Python-based ECG preprocessing and ROM generation.
Digital QRS detection using counters, subtractors, comparators, and an FSM.
Heartbeat indication through a digital pulse/LED output.
Simulated using LTspice and Logisim Evolution.


# System Overview


## Analog Stage


High-pass filtering for baseline drift removal.
Instrumentation amplification and low-pass filtering.
Precision rectification and threshold comparison.


## Python Processing


ECG data loading and resampling.
Signal normalization and 8-bit quantization.
Generation of a Logisim-compatible ROM initialization file.


## Digital Stage


Sequential reading of ROM samples.
Derivative-based slope detection.
FSM-based validation to reduce false positives.
LED pulse generation for confirmed QRS complexes.


## Tools Used


LTspice
Python (NumPy)
Logisim Evolution


## Learning Outcomes


ECG signal conditioning techniques
Active filter and instrumentation amplifier design
Digital sequential logic and FSM implementation
Biomedical signal processing workflows
Integration of analog and digital subsystems


## Future Work
FPGA implementation for real-time operation.
Adaptive thresholding for improved robustness.
Integration with live ECG acquisition hardware.




This project serves as an educational example of combining analog and digital design methodologies for biomedical instrumentation.

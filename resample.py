import numpy as np

# 1. Configuration
INPUT_FILE = "analog.txt"          # input text file
OUTPUT_FILE = "rom.txt"   # file for Logisim
TARGET_SAMPLES = 40              # Resample target
BIT_DEPTH = 8                    # 8-bit hex mapping (0 to 255)

# 2. Load and parse the file
# Assumes white-space or tab-separated values. Adjust delimiter if using commas.
data = np.loadtxt(INPUT_FILE)
time = data[:, 0]
voltage = data[:, 1]

# 3. Linear Resampling to exactly 40 points
original_indices = np.linspace(0, 1, len(voltage))
target_indices = np.linspace(0, 1, TARGET_SAMPLES)
resampled_voltage = np.interp(target_indices, original_indices, voltage)

# 4. Quantize values to Hexadecimal (00 to FF for 8-bit)
# This maps your minimum voltage to 0x00 and maximum voltage to 0xFF
v_min, v_max = resampled_voltage.min(), resampled_voltage.max()
if v_max == v_min:
    quantized_values = np.zeros(TARGET_SAMPLES, dtype=int)
else:
    max_hex_val = (2**BIT_DEPTH) - 1
    quantized_values = ((resampled_voltage - v_min) / (v_max - v_min) * max_hex_val).astype(int)

# Convert integers to 2-digit lowercase hex strings
hex_strings = [f"{val:02x}" for val in quantized_values]

# 5. Format and save to Logisim ROM format
with open(OUTPUT_FILE, "w") as f:
    f.write("v2.0 raw\n")
    f.write(" ".join(hex_strings))

print(f"Successfully converted {len(voltage)} samples to 40 samples.")
print(f"File saved as '{OUTPUT_FILE}' in Logisim ROM format.")





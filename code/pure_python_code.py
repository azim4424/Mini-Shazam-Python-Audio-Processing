import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy.fftpack import fft

def compute_fft(segment):
    spectrum = fft(segment)
    spectrum = spectrum[0:len(segment)//2]
    magnitude = np.abs(spectrum)
    return magnitude


fs, signal = wavfile.read("audio.wav")
if len(signal.shape) > 1:
    signal = signal.mean(axis=1)
signal = signal.astype(float)
print("Sampling Frequency =", fs, "Hz")
print("Length of Full Signal =", len(signal), "samples")
print("Signal Duration =", len(signal)/fs, "seconds")

time = np.arange(len(signal)) / fs
plt.plot(time, signal)
plt.title("Full Signal (Time Domain)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

start = 5
duration = 3
start_index = int(start * fs)
end_index = int((start + duration) * fs)
clip = signal[start_index:end_index]
print("Clip Length =", len(clip), "samples")
print("Original Clip Position =", start, "seconds")

clip_time = np.arange(len(clip)) / fs
plt.plot(clip_time, clip)
plt.title("Clip (Time Domain)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

clip_fft = compute_fft(clip)
frequencies = np.linspace(0, fs/2, len(clip_fft))
plt.plot(frequencies, clip_fft)
plt.title("Clip Frequency Domain")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()

window_length = len(clip)

step_size = 1000

similarity_scores = []
positions = []

for i in range(0, len(signal) - window_length, step_size):
    segment = signal[i:i + window_length]
    segment_fft = compute_fft(segment)
    numerator = np.dot(clip_fft, segment_fft)
    denominator = (
        np.linalg.norm(clip_fft)
        * np.linalg.norm(segment_fft)
    )
    similarity = numerator / denominator
    similarity_scores.append(similarity)
    positions.append(i / fs)

best_index = np.argmax(similarity_scores)
detected_time = positions[best_index]
best_score = similarity_scores[best_index]

print("Detected Position =", detected_time, "seconds")
print("Best Similarity Score =", best_score)

plt.plot(positions, similarity_scores, label='the similarity scores')
plt.axvline(start, color='green', linestyle='--', label='Actual Position')
#the above to highlight where the clip actually starts.
plt.axvline(detected_time, color='red', linestyle='--', label='Detected Position')
#the above to highlight the detected time of where clip starts.
plt.title("Similarity Score vs Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Similarity Score")
plt.legend()
plt.grid()
plt.show()

detected_index = int(detected_time * fs)
detected_segment = signal[
    detected_index : detected_index + window_length
]

plt.plot(clip_time, clip, label="Original Clip")
plt.plot(clip_time, detected_segment, label="Detected Segment", color='red', alpha=0.7)
plt.title("Clip vs Detected Segment")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.legend()
plt.grid()

plt.show()

import struct
import wave
import math

# 出力するwavファイルの設定値
# サンプルレート(Hz)
SAMPLE_RATE = 44100
# サンプル幅(ビット)
SAMPLE_WIDTH = 2
# チャンネル数
NUM_CHANNELS = 1

# A4の周波数(Hz)
A4_FREQ = 440
# 音の長さ(秒)
duration = 1.0
# 振幅
amplitude = 0.5

filename = "v1_a4.wav"
audio_data = b""

frames = int(duration * SAMPLE_RATE)
for frame in range(frames):
    time = float(frame) / SAMPLE_RATE
    value = amplitude * math.sin(2.0 * math.pi * A4_FREQ * time)
    packed_value = struct.pack("<h", int(value * 32767.0))
    audio_data += packed_value

with wave.open(filename, "wb") as f:
    f.setnchannels(NUM_CHANNELS)
    f.setsampwidth(SAMPLE_WIDTH)
    f.setframerate(SAMPLE_RATE)
    f.writeframes(audio_data)

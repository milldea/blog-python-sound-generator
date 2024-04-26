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

# 音階と周波数の対応
NOTE_FREQS = {
    "C": 130.81,
    "C#": 138.59,
    "D": 146.83,
    "D#": 155.56,
    "E": 164.81,
    "F": 174.61,
    "F#": 185.00,
    "G": 196.00,
    "G#": 207.65,
    "A": 220.00,
    "A#": 233.08,
    "B": 246.94,
}
# 音の長さ(秒)
duration = 1.0
# 振幅
amplitude = 0.5

# 演奏する音階の指定
notes = ["C", "C", "G", "G", "A", "A", "G", "F", "F", "E", "E", "D", "D", "C"]
filename = "v3_envelope.wav"
audio_data = b""

for note in notes:
    freq = NOTE_FREQS[note] * 4
    num_frames = int(duration * SAMPLE_RATE)
    for frame in range(num_frames):
        t = float(frame) / SAMPLE_RATE
        value = amplitude * math.sin(2.0 * math.pi * freq * t)
        # キラキラ感を生成
        envelope = amplitude * math.sin(10.0 * math.pi * t)
        value *= envelope
        packed_value = struct.pack("<h", int(value * 32767.0))
        audio_data += packed_value
    
with wave.open(filename, "wb") as f:
    f.setnchannels(NUM_CHANNELS)
    f.setsampwidth(SAMPLE_WIDTH)
    f.setframerate(SAMPLE_RATE)
    f.writeframes(audio_data)

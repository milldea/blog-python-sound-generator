import wave

# 出力するwavファイルの設定値
# サンプルレート(Hz)
SAMPLE_RATE = 44100
# サンプル幅(ビット)
SAMPLE_WIDTH = 2
# チャンネル数
NUM_CHANNELS = 1

filename = "v0_none.wav"
audio_data = b""

with wave.open(filename, "wb") as f:
    f.setnchannels(NUM_CHANNELS)
    f.setsampwidth(SAMPLE_WIDTH)
    f.setframerate(SAMPLE_RATE)
    f.writeframes(audio_data)

import sounddevice as sd
from scipy.io.wavfile import write
import sounddevice as sd
# 导入soundfile库用于读取音频文件
import soundfile as sf

def startRecording(duration,outupt_file):
    # 配置参数
    RATE = 44100  # 采样率
    DURATION = duration  # 录音时长（秒）
    OUTPUT_FILE = outupt_file  # 输出文件名

    print("开始录音...")
    audio = sd.rec(int(DURATION * RATE), samplerate=RATE, channels=1, dtype='int16')
    sd.wait()  # 等待录音完成
    print("录音结束")

    # 保存到 WAV 文件
    write(OUTPUT_FILE, RATE, audio)
    print(f"录音已保存到 {OUTPUT_FILE}")
    return OUTPUT_FILE

def playAudio(path):


    # 加载音频数据
    # 使用soundfile库的read函数读取音频文件 'audio_file.wav'
    # data变量存储音频数据，fs变量存储采样率
    data, fs = sf.read(path)

    # 播放音频
    # 使用sounddevice库的play函数播放音频数据
    # data参数为要播放的音频数据，fs参数为音频数据的采样率
    sd.play(data, fs)

    # 等待播放完成
    # 使用sounddevice库的wait函数等待音频播放完成
    sd.wait()


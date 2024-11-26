import sys
sys.path.insert(0, '../libs')

from TTS.api import TTS

def generateAudioFile(fileContent,savePath):
    # Get device
    device = "cpu"

    # Init TTS
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    # Run TTS
    # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
    # Text to speech list of amplitude values as output
    # wav = tts.tts(text="明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间。", speaker_wav="speaker_wav.wav", language="zh")
    # Text to speech to a file
    return tts.tts_to_file(
        text=fileContent,speaker_wav="./lib/res/speaker_wav.wav",
        language="zh", file_path=savePath)

# 单独运行时释放此方法
# if __name__ == "__main__":
#     import sys
#
#     if len(sys.argv) != 3:
#         print("Usage: python tts.py <text> <output_path>")
#         sys.exit(1)
#
#     text = sys.argv[1]
#     print(text)
#     output_path = sys.argv[2]
#     print(output_path)
#     path = generateAudioFile(text, output_path)
#     print(path)

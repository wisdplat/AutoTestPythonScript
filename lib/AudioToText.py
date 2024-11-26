import whisper


def getAudio(path):
    # 加载模型
    device = "cpu"
    model = whisper.load_model("large").to(device)

    # 加载音频并预处理
    audio = whisper.load_audio(path)
    audio = whisper.pad_or_trim(audio)

    # 生成 log-Mel spectrogram
    mel = whisper.log_mel_spectrogram(audio, n_mels=128).to(device)

    # 检测语言
    _, probs = model.detect_language(mel)
    language_code = max(probs, key=probs.get)
    print(f"Detected language: {language_code}")

    # 解码音频为文本
    options = whisper.DecodingOptions(fp16=False)  # 你可以根据需要调整fp16
    result = whisper.decode(model, mel, options)

    # 打印识别的文本
    print(result.text)
    return result.text


# 单独运行时释放此方法
# if __name__ == "__main__":
#     import sys
#
#     if len(sys.argv) != 2:
#         print("Usage: python tts.py <text> <output_path>")
#         sys.exit(1)
#     filepath = sys.argv[1]
#     getAudio(filepath)
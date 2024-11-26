from lib.AudioToText import getAudio
from lib.ExecuteCase import run
from lib.OpenCVUtils import compareImg
from lib.TestReportUtils import startRecord, addCase, generateReport
from lib.TextToAudio import generateAudioFile


# C#中代码字符串拼接后，再写入文件中
def startTest():
    print("开始测试")
    # compareImg("./resources/obj.png", "./resources/sc.png")
    generateAudioFile("测试测试,123123123", "./resources/test.wav")
    print("开始验证")
    getAudio("./test.wav")


# todo  音频处理部分需要ffmpeg
# 由此方法将C#中的参数传入python中
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("运行参数不对")
        sys.exit(1)

    print(sys.argv[1])

    path = sys.argv[1]

    # startRecord
    # for():
    #     addCase
    #
    # generateReport

    run(path)


    # startTest()







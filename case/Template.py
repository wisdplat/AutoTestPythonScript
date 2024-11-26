from lib.AudioToText import getAudio
from lib.AudioUtils import startRecording, playAudio
from lib.OpenCVUtils import compareImg
from lib.TestReportUtils import addCaseStepResult
from lib.TextOCR import getTextInImage
from lib.TextToAudio import generateAudioFile


def runCase():
    getAudio
    startRecording
    playAudio
    compareImg
    addCaseStepResult
    getTextInImage
    generateAudioFile

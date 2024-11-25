import easyocr


# 文字OCR识别
def getTextInImage(path):
    reader = easyocr.Reader(['en', 'zh'])  # 支持多语言
    result = reader.readtext("test_image.png")
    for (bbox, text, confidence) in result:
        print(f"Detected text: {text} (confidence: {confidence})")
    return result
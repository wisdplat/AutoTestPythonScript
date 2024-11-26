import cv2


def compareImg(src1: str, src2: str):
    """
    图像对比方法
    :param src1: 模板图片路径
    :param src2: 对比图片路径
    :return: 匹配结果 (最匹配点的坐标) 或 None
    """
    # 读取图片
    src_img1 = cv2.imread(src1, cv2.IMREAD_COLOR)
    src_img2 = cv2.imread(src2, cv2.IMREAD_COLOR)

    if src_img1 is None or src_img2 is None:
        print("无法读取图片文件。")
        return None

    # 创建 SIFT 对象
    sift = cv2.SIFT_create()

    # 计算特征点和描述符
    keypoints1, descriptors1 = sift.detectAndCompute(src_img1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(src_img2, None)


    # 创建 FlannBasedMatcher
    index_params = dict(algorithm=1, trees=5)  # 使用 KDTree 算法
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # 进行 KNN 匹配
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    # 筛选匹配结果，应用 Lowe's Ratio Test

    good_matches = []
    for m, n in matches:
        if m.distance < 0.3 * n.distance:  # 阈值为 0.3
            good_matches.append(m)

    # 绘制匹配结果
    result = cv2.drawMatches(src_img1, keypoints1, src_img2, keypoints2, good_matches, None,
                             flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # 显示结果
    scale = 0.5
    resized_result = cv2.resize(result, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Match Result", resized_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 如果没有匹配点，则返回 None
    if (not good_matches) or len(good_matches) < 5:
        return False,None

    # 获取最匹配点（模板图片中的点）
    best_match = good_matches[0]  # 最好的匹配点
    point1 = keypoints1[best_match.queryIdx].pt  # 获取坐标 (x, y)

    print(f"最匹配点的坐标: ({point1[0]}, {point1[1]})")

    return True,point1
import cv2

if __name__ == '__main__':

    # 画像の読み込み
    img_src1 = cv2.imread("background_image.jpg", 1)
    img_src2 = cv2.imread("frontground_image.jpg", 1)

    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

    fgmask = fgbg.apply(img_src1)
    fgmask = fgbg.apply(img_src2)

    # 表示
    cv2.imshow('frame',fgmask)

    # 検出画像
    bg_diff_path  = './diff.jpg'
    cv2.imwrite(bg_diff_path,fgmask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


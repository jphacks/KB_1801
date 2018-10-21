#!/usr/local/bin/python
#! -*- coding: utf-8 -*-

import cv2
import numpy as np
import pickle



# 指定した画像(path)の物体を検出し、外接矩形の画像を出力します


def detect_contour_num_staff(path, num_staff):

  # 画像を読込
  src = cv2.imread(path, cv2.IMREAD_COLOR)
  
  # グレースケール画像読み込み
  gray0 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  #gray0 = cv2.GaussianBlur(src, (5, 5), 0)
  img = cv2.medianBlur(gray0, 5)
  gray = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                              cv2.THRESH_BINARY, 11, 2)
  #gray = cv2.GaussianBlur(gray, (5, 5), 0)



  # 2値化
  #retval, bw = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  #エッジング　
  bw = cv2.Canny(gray, 10, 100)
  #bw = cv2.Sobel(gray, cv2.CV_8UC1,1, 0, ksize = 3)
  cv2.imwrite('edging.jpg', bw)

  # 輪郭を抽出
  #   contours : [領域][Point No][0][x=0, y=1]
  #   cv2.CHAIN_APPROX_NONE: 中間点も保持する
  #   cv2.CHAIN_APPROX_SIMPLE: 中間点は保持しない

  image, contours, hierarchy = cv2.findContours(

      bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
  # 矩形検出された数（デフォルトで0を指定）
  detect_count = 0

  #長方形の面積を大きい順に入れる配列
  #(中心座標x, y), (長さw, y)), (面積)
  lectangle_areaArray_temp = []
  counter_lectangle_array = 0
  # 各輪郭に対する処理
  for i in range(0, len(contours)):

    # 輪郭の領域を計算
    area = cv2.contourArea(contours[i])

    # ノイズ（小さすぎる領域）と全体の輪郭（大きすぎる領域）を除外
    if 1e3 < area:
      continue

    # 外接矩形
    if len(contours[i]) > 0:
      rect = contours[i]
      x, y, w, h = cv2.boundingRect(rect)

      lectangle_areaArray_temp.append([])
      lectangle_areaArray_temp[counter_lectangle_array].append((x, y))
      lectangle_areaArray_temp[counter_lectangle_array].append((w, h))
      lectangle_areaArray_temp[counter_lectangle_array].append(h*w)
      counter_lectangle_array += 1

  #大きい長方形のみを残す
  lectangle_areaArray_temp = sorted(
      lectangle_areaArray_temp, key=lambda x: x[2], reverse=True)
  lectangle_areaArray_new = [lectangle_areaArray_temp[i] for i in range(num_staff)]

  #長方形
  for i in range(len(lectangle_areaArray_new)):
    """
    # 外接矩形毎に画像を保存
    cv2.imwrite('./gaikei/' + str(detect_count) +
                '.jpg', src[y:y + h, x:x + w])
    detect_count = detect_count + 1
    """
    cv2.rectangle(src, (lectangle_areaArray_new[i][0][0], lectangle_areaArray_new[i][0][1]), (
        lectangle_areaArray_new[i][0][0] + lectangle_areaArray_new[i][1][0], lectangle_areaArray_new[i][0][1] + lectangle_areaArray_new[i][1][1]), (0, 255, 0), 2)

  # 外接矩形された画像を表示
  cv2.imwrite('output2.png', src)
  
  """
  #整理するものの位置、重さ情報を保存
  f = open('./info/sort_staff_list.txt', 'w')
  for line in lectangle_areaArray_new:
    f.write(str(line) + "\n")
  f.close()
  """

  with open('./info/sort_staff_list.pickle', mode='wb') as fo:
    pickle.dump(lectangle_areaArray_new, fo)


  for i in range(len(lectangle_areaArray_new)):
    print(lectangle_areaArray_new[i][1])
  f = open('./info/judge.txt', 'w')  # 書き込みモードで開く
  f.write('0')  # 引数の文字列をファイルに書き込む
  f.close()  # ファイルを閉じる

  # 終了処理
  #cv2.destroyAllWindows()


def detect_contour_threshold(path, threshold):

  # 画像を読込
  src = cv2.imread(path, cv2.IMREAD_COLOR)
  # グレースケール画像読み込み
  gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

  # 2値化
  #retval, bw = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  #エッジング　
  bw = cv2.Canny(gray, 10, 500)
  #bw = cv2.Sobel(gray, cv2.CV_8UC1,1, 0, ksize = 3)

  cv2.imwrite('edgingMove.jpg', bw)
  # 輪郭を抽出
  #   contours : [領域][Point No][0][x=0, y=1]
  #   cv2.CHAIN_APPROX_NONE: 中間点も保持する
  #   cv2.CHAIN_APPROX_SIMPLE: 中間点は保持しない

  image, contours, hierarchy = cv2.findContours(

      bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
  # 矩形検出された数（デフォルトで0を指定）
  detect_count = 0

  #長方形の面積を大きい順に入れる配列
  #(中心座標x, y), (長さw, y)), (面積)
  lectangle_areaArray_new = []
  counter_lectangle_array = 0
  # 各輪郭に対する処理
  for i in range(0, len(contours)):

    # 輪郭の領域を計算
    area = cv2.contourArea(contours[i])

    # ノイズ（小さすぎる領域）と全体の輪郭（大きすぎる領域）を除外
    if area < 1e2 or 1e5 < area:
      continue

    # 外接矩形
    if len(contours[i]) > 0:
      rect = contours[i]
      x, y, w, h = cv2.boundingRect(rect)
      if h*w > threshold:
        lectangle_areaArray_new.append([])
        lectangle_areaArray_new[counter_lectangle_array].append((x, y))
        lectangle_areaArray_new[counter_lectangle_array].append((w, h))
        lectangle_areaArray_new[counter_lectangle_array].append(h*w)
        counter_lectangle_array += 1

        cv2.rectangle(src, (x, y), (
            x + w, y + h), (0, 255, 0), 2)

  

  # 外接矩形された画像を表示
  cv2.imwrite('output3.png', src)

  
  """
  #整理するものの位置、重さ情報を保存
  f = open('./info/sort_staff_list.txt', 'w')
  for line in lectangle_areaArray_new:
    f.write(str(line) + "\n")
  f.close()
  """

  with open('./info/sort_staff_list.pickle', mode='wb') as fo:
    pickle.dump(lectangle_areaArray_new, fo)

  for i in range(len(lectangle_areaArray_new)):
    print(lectangle_areaArray_new[i][1])
  # 終了処理
  #cv2.destroyAllWindows()
  
  

if __name__ == '__main__':
  #並べる物の数
  num_staff = 2
  threshold = 30000
  detect_contour_num_staff('./images2/correct.JPG', num_staff)


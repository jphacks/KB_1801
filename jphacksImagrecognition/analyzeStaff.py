#!/usr/local/bin/python
#! -*- coding: utf-8 -*-

import cv2
import numpy as np
import pickle


# 指定した画像(path)の物体を検出し、外接矩形の画像を出力します
def remove_same_area(lectangle_areaArray_temp, judgement_coefficient):
  eliminate_index = []
  result = []
  for index_org in range(len(lectangle_areaArray_temp)):
    for inidex_compare in range(index_org + 1, len(lectangle_areaArray_temp)):
      if -(lectangle_areaArray_temp[index_org][0][1] + lectangle_areaArray_temp[index_org][1][1])*judgement_coefficient + (lectangle_areaArray_temp[inidex_compare][0][1] + lectangle_areaArray_temp[inidex_compare][1][1]) > 0 or \
          -(lectangle_areaArray_temp[inidex_compare][0][1] + lectangle_areaArray_temp[inidex_compare][1][1])*judgement_coefficient + (lectangle_areaArray_temp[index_org][0][1] - lectangle_areaArray_temp[index_org][1][1]) > 0 or \
          -(lectangle_areaArray_temp[index_org][0][0] + lectangle_areaArray_temp[index_org][1][0])*judgement_coefficient + (lectangle_areaArray_temp[inidex_compare][0][0] + lectangle_areaArray_temp[inidex_compare][1][0]) > 0 or \
              -(lectangle_areaArray_temp[inidex_compare][0][0] + lectangle_areaArray_temp[inidex_compare][1][0])*judgement_coefficient + (lectangle_areaArray_temp[index_org][0][0] - lectangle_areaArray_temp[index_org][1][0]) > 0:
        #print(index_org)
        eliminate_index.append(index_org)
  #print(eliminate_index)
  for index in range(len(lectangle_areaArray_temp)):
    if index != eliminate_index[0]:
      result.append(lectangle_areaArray_temp[index])
      eliminate_index.pop(0)

  return result

def analyze_staff(path, judgement_coefficient):
	with open('./info/sort_staff_list.pickle', mode='rb') as fi:
		correct_lectangle_areaArray = pickle.load(fi)
		num_staff = len(correct_lectangle_areaArray)


		# 画像を読込
		src = cv2.imread(path, cv2.IMREAD_COLOR)
		# グレースケール画像読み込み
		gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

		# 2値化
		#retval, bw = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

		#エッジング　
		bw = cv2.Canny(gray, 10, 100)
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
		observed_lectangle_areaArray_temp = []
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

				observed_lectangle_areaArray_temp.append([])
				observed_lectangle_areaArray_temp[counter_lectangle_array].append((x, y))
				observed_lectangle_areaArray_temp[counter_lectangle_array].append((w, h))
				observed_lectangle_areaArray_temp[counter_lectangle_array].append(h*w)
				counter_lectangle_array += 1

		#大きい長方形のみを残す
		observed_lectangle_areaArray_temp = sorted(observed_lectangle_areaArray_temp, key=lambda x: x[2])
		remove_same_area(observed_lectangle_areaArray_temp, judgement_coefficient)
		observed_lectangle_areaArray_new = [observed_lectangle_areaArray_temp[i] for i in range(
                    len(observed_lectangle_areaArray_temp) - 1, len(observed_lectangle_areaArray_temp) - num_staff - 1, -1)]

		#ここからモノがちゃんと片付けられているかどうか確認

		candidate_mach_lectangle = []
		number_mach_lectangle = 0
		
		#正解画像と観察画像に含まれている数が同じかどうか
		#同じ
		if len(observed_lectangle_areaArray_new) != num_staff:
			print("片付けろぉぉ！！")
			#To do ここで、textに0or1を書き込む
			f = open('./info/judge.txt', 'w')  # 書き込みモードで開く
			f.write('1')
			f.close()  # ファイルを閉じる


		#違う
		else:
			for index_correct, line in enumerate(correct_lectangle_areaArray):
				for index_observed, line in enumerate(observed_lectangle_areaArray_new):
					if abs(observed_lectangle_areaArray_new[index_observed][0][0] - correct_lectangle_areaArray[index_correct][0][0]) <= observed_lectangle_areaArray_new[index_observed][1][0] - correct_lectangle_areaArray[index_correct][1][0] \
							and abs(observed_lectangle_areaArray_new[index_observed][0][1] - correct_lectangle_areaArray[index_correct][0][1]) <= observed_lectangle_areaArray_new[index_observed][1][1] - correct_lectangle_areaArray[index_correct][1][1]:
							candidate_mach_lectangle.append(index_observed)
				#２個以上対象物の候補があるかどうか
				number_of_candidate = len(candidate_mach_lectangle)
				#とりあえず絶対ありえない値を入れる
				#Todoここを変える
				candidate_areasquare_measuresize = correct_lectangle_areaArray[index_correct][2]
				correct_lectangle_areasquare_measuresize = correct_lectangle_areaArray[index_correct][2]
				if number_of_candidate >= 2:
					for index_candidate in range(number_of_candidate):
						if candidate_areasquare_measuresize > abs(correct_lectangle_areasquare_measuresize - observed_lectangle_areaArray_new[index_observed][2]):
							candidate_index = index_observed
							candidate_areasquare_measuresize = abs(correct_lectangle_areasquare_measuresize - observed_lectangle_areaArray_new[index_observed][2])
				else:
					candidate_index = index_observed

				#候補観察画像と正解画像とがマッチするかどうか確認
				#上下左右がそれぞれjudgement_coefficient倍した観察画像の領域内に入っているかどうか
				if (correct_lectangle_areaArray[index_correct][0][1] + correct_lectangle_areaArray[index_correct][1][1]*judgement_coefficient) - (observed_lectangle_areaArray_new[candidate_index][0][1] + observed_lectangle_areaArray_new[candidate_index][1][1]) > 0 and \
				(observed_lectangle_areaArray_new[candidate_index][0][1] + observed_lectangle_areaArray_new[candidate_index][1][1]) - (correct_lectangle_areaArray[index_correct][0][1] - correct_lectangle_areaArray[index_correct][1][1]*judgement_coefficient) > 0 and \
				(correct_lectangle_areaArray[index_correct][0][0] + correct_lectangle_areaArray[index_correct][1][0]*judgement_coefficient) - (observed_lectangle_areaArray_new[candidate_index][0][0] + observed_lectangle_areaArray_new[candidate_index][1][0]) > 0 and \
				(observed_lectangle_areaArray_new[candidate_index][0][0] + observed_lectangle_areaArray_new[candidate_index][1][0]) - (correct_lectangle_areaArray[index_correct][0][0] - correct_lectangle_areaArray[index_correct][1][0]*judgement_coefficient) > 0:
								number_mach_lectangle += 1
				else:
					print("片付けろおぉぉ！！！！")
					f = open('./info/judge.txt', 'w')  # 書き込みモードで開く
					f.write('1')  # 引数の文字列をファイルに書き込む
					f.close()  # ファイルを閉じる

			if number_mach_lectangle == num_staff:
				print("Okkkkk")
				f = open('./info/judge.txt', 'w')  # 書き込みモードで開く
				f.write('0')  # 引数の文字列をファイルに書き込む
				f.close()  # ファイルを閉じる

		
		


if __name__ == '__main__':
  judgement_coefficient = 1.2  
  analyze_staff('./images2/ok4.JPG', judgement_coefficient)

setStaff.pyがキレイな状態をセットするプログラムです
ping2.pngが物体認識した後のものになります
setStaff.pyは片付いているかどうかチェックするプログラムです。
片付いているかどうかは、infoの中のjudge.txtに0と書いていたら片付いている、1だったら汚いとなっています

setStaff.pyの195行目detect_contour_num_staff('./images2/correct.JPG', num_staff)
の部分がキレイな状態の画像になります

analyzeStaff.pyの132行目 analyze_staff('./images2/IMG_5339.JPG', judgement_coefficient)のファイル名を変えてください。
これは、チェックするプログラムです。
image2の中に画像があり、okと書いているファイル名はokで認識されるものです、dameと書いているファイルは汚いと認識されるものです

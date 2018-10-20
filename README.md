# 片付けRIZAP
~　まだ片付けで消耗してるの？　~

[![Product Name](image.png)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要
### 「片付け」 X 「Tech」

### 背景（製品開発のきっかけ、課題等）
「部屋の片付けのしつけ」は親にとって重要な仕事です．
一方で，こどもの片付けの状態に「とても満足している」親はたった５％，　約７割の親が満足できていません［１］．
子供が楽しんで片付けをできるように〇〇にしつけを任せませんか？
私達は「片付け」と「テクノロジー」を掛け合わせたプロダクトを開発しました．

- 今回のプロダクトの開発に至った背景
片付けという基本的な考え方をしつけるのが思ったよりも困難だというデータをみかけたため．

- 着目した顧客・顧客の課題・現状
女性の社会進出が進み，　子供のしつけにかけられる時間が少なくなっている．
子供がうまいこと片付けができないことからネグレクトなどに発展するケースなども報告されている［2]


［１］　子供の片付けに関するアンケート　（野村不動産アーバンネット株式会社）　http://www.nomura-un.co.jp/page/news/pdf/20150903.pdf
[2]


### 製品説明（具体的な製品の説明）
こちらに製品の概要・特徴について説明を記載してください。

### 特長

#### 1. 特長1
部屋の投影面積から「ちらかり度合い」を算出する．

#### 2. 特長2

#### 3. 特長3

### 解決出来ること
この製品を利用することによって最終的に解決できることについて記載をしてください。

### 今後の展望
![image](https://user-images.githubusercontent.com/21073221/47256803-7fef5200-d4c0-11e8-9e7a-364dd6e5bfda.png)
今回は実現できなかったが、今後改善すること、どのように展開していくことが可能かについて記載をしてください。


## 開発内容・開発技術
![image](https://user-images.githubusercontent.com/21073221/47256694-1753a580-d4bf-11e8-8d9a-6fc8924f095f.png)

### 活用した技術
#### API・データ
* [Messging API (LINE様)](https://developers.line.me/ja/services/messaging-api/)
* Clova Extention Kit (CEK) (LINE様)

#### フレームワーク・ライブラリ・モジュール
* Python(Raspberry Piのクライアント)
* [Open CV(画像処理)](https://opencv.org/)

#### デバイス
* [Raspberry pi Zero WH](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
* Raspberry Pi カメラモジュール

### 研究内容・事前開発プロダクト（任意）
ご自身やチームの研究内容や、事前に持ち込みをしたプロダクトがある場合は、こちらに実績なども含め記載をして下さい。

* 関連する研究やプロダクトは特になし

### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* RasPiによる画像の自動解析
* 物体認識（被覆率の算出）
* LINEAPIを用いた片付け結果の通知
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください（任意）

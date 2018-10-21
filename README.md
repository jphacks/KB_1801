# 片付けRIZAP  -まだ片付けで消耗してるの？-
![image](https://user-images.githubusercontent.com/21073221/47261384-0760b380-d509-11e8-9e17-7ba1fab4ad18.png)

# プロモーションビデオ
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/21073221/47262029-d340bf00-d517-11e8-99de-264e7d1e4a1a.png)](https://youtu.be/UL3A2Y659nU)
## 製品概要
### 「片付け」 X 「Tech」

### このテーマに着目した背景
机の片付けほど一人でマネジメントすることが難しいことはない．実際に「整理」「整頓」などのキーワードを用いたビジネス書は毎年のように出版されており，人々がいかに学習できていないかがわかる．実際，オフィスで働く人女性の７0%以上がデスクの書類や文房具等の整理整頓に困っていることが報告されており[1]，また，ビジネスマンを対象とした調査では，９割以上のビジネスマンが片付けと仕事には関係があると考えている[2]．更に，OECDデータによると日本の時間あたりの労働生産性はOECD加盟国３５カ国中２０位という低水準である[3]．  
### **そして何よりも，チームメンバー全員が圧倒的に片付けを苦手としている．**　
### **エントロピー増大の法則に立ち向かい，日本の生産性向上に寄与するために我々はこの困難な課題に立ち向かった．．．．．**　

![image](https://user-images.githubusercontent.com/21073221/47262239-d9d23500-d51d-11e8-8767-8f34a005bf81.png)



[[1]](http://www.watashimigaki.com/community/enquete/archives_000814) 株式会社カウネット「働く女性の『オフィスの収納・整理』に関するアンケート」    
[[2]](https://president.jp/articles/-/9462) PRESIDENT Online「年収1500万vs500万の整理術」  
[[3]](https://www.jpc-net.jp/intl_comparison/) 公益財団法人日本生産性本部「労働生産性の国際比較」　  　


### 製品説明（具体的な製品の説明）
こちらに製品の概要・特徴について説明を記載してください。

### 特長
![image](https://user-images.githubusercontent.com/21073221/47262430-c4600980-d523-11e8-82bc-f24bab95e403.png)

#### 1. 特長1 机ライフログ
Raspberry Piでスケジュール撮影した結果を用いて「机の被覆率」と「机の散らかり度」を算出し，デイリーレポートとして結果をLINEに通知するサービスを提供します．　　
また，こちらからLINEにて「最近，片付けできてるやろ？」等のメッセージを送ることによってその時点でのデイリーレポートを提供します．　　
体重計の結果のログを可視化するだけで人は痩せるということが報告されており[4]，　机においても同様の効果が期待されます．

[[４]](https://allabout.co.jp/gm/gc/411617/) All About Beauty 「ダイエット成功のカギ”可視化”を楽しく実現！」　  　


#### 2. 特長2

#### 3. 特長3

### 解決出来ること
この製品を利用することによって最終的に解決できることについて記載をしてください。

### 今後の展望
![image](https://user-images.githubusercontent.com/21073221/47256803-7fef5200-d4c0-11e8-9e7a-364dd6e5bfda.png)
今回は実現できなかったが、今後改善すること、どのように展開していくことが可能かについて記載をしてください。

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


## 開発内容・開発技術
![image](https://user-images.githubusercontent.com/21073221/47256694-1753a580-d4bf-11e8-8d9a-6fc8924f095f.png)

### 活用した技術
#### API・データ
* [Messging API (LINE様)](https://developers.line.me/ja/services/messaging-api/)
* [Clova Extention Kit (CEK) (LINE様)](https://clova-developers.line.me/#/)

#### フレームワーク・ライブラリ・モジュール
* Python(Raspberry Piのクライアント)
* [Open CV(画像処理)](https://opencv.org/)
* Amazon Web Services ※未実装

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

# 片付けRIZAP  -まだ片付けで消耗してるの？-
![image](https://user-images.githubusercontent.com/21073221/47261384-0760b380-d509-11e8-9e17-7ba1fab4ad18.png)

# プロモーションビデオ
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/21073221/47262029-d340bf00-d517-11e8-99de-264e7d1e4a1a.png)](https://youtu.be/El6NWfqYYBk)
## 製品概要
### ちゃんと片付けTech（「片付け」X「Tech」）

### このテーマに着目した背景
机の片付けほど一人でマネジメントすることが難しいことはない．実際に「整理」「整頓」などのキーワードを用いたビジネス書は毎年のように出版されており，人々がいかに学習できていないかがわかる．実際，オフィスで働く人女性の７0%以上がデスクの書類や文房具等の整理整頓に困っていることが報告されており[1]，また，ビジネスマンを対象とした調査では，９割以上のビジネスマンが片付けと仕事には関係があると考えている[2]．更に，OECDデータによると日本の時間あたりの労働生産性はOECD加盟国３５カ国中２０位という低水準である[3]．  
### **そして何よりも，チームメンバー全員が圧倒的に片付けを苦手としている．**　
### **エントロピー増大の法則に立ち向かい，日本の生産性向上に寄与するために我々はこの困難な課題に立ち向かった．．．．．**　

![image](https://user-images.githubusercontent.com/21073221/47262239-d9d23500-d51d-11e8-8767-8f34a005bf81.png)



[[1]](http://www.watashimigaki.com/community/enquete/archives_000814) 株式会社カウネット「働く女性の『オフィスの収納・整理』に関するアンケート」    
[[2]](https://president.jp/articles/-/9462) PRESIDENT Online「年収1500万vs500万の整理術」  
[[3]](https://www.jpc-net.jp/intl_comparison/) 公益財団法人日本生産性本部「労働生産性の国際比較」　  　


### 製品説明（具体的な製品の説明）
机上部に「片付けRIZAPくん（RaspberryPI+PiCameraで構成されたモジュール）」を設置し，机を綺麗にした状態で基準となる画像を撮影する（撮影はLINEのメッセンジャーで「基準値撮って！」などのメッセージを送ると対応してくれる※未実装）．「片付けRAIZAP君」は定期的に机の画像をスケジュール撮影し，その結果をAWSに送る（デモでは，無料サーバーにアップしている）．

### 特長
![image](https://user-images.githubusercontent.com/21073221/47262430-c4600980-d523-11e8-82bc-f24bab95e403.png)

#### 【特長1】 机ライフログ
RaspberryPiでスケジュール撮影した結果を用いて「机の被覆率」と「机の散らかり度」を算出し，デイリーレポートとして結果をLINEに通知するサービスを提供します．また，こちらからLINEにて「最近，片付けできてるやろ？」等のメッセージを送ることによってその時点でのデイリーレポートを提供します．体重計の結果のログを可視化するだけで人は痩せるということが報告されており[4]，机においても同様の効果が期待されます．

[[４]](https://allabout.co.jp/gm/gc/411617/) All About Beauty 「ダイエット成功のカギ”可視化”を楽しく実現！」    　

#### 【特長2】 机お叱りアラート
机の汚さがある一定の閾値を下回ると，LINEのメッセージで叱ってくれるサービスを提供します．
いくら，ログが可視化されてもなおらない自制心の弱いユーザーでも安心して使えます．

#### 【特長3】 机メンタリング
机お叱りアラートをいくらしても改善がみられないようなユーザーには，人によるメンタリング制度を提案する予定です．
機械と人との対応では怠けてしまうユーザーも人（コーチ）が介在することによって机を綺麗にすることができます．
このサービスを用いると，デイリーレポートを実際に人が目視で確認して対応してくれます．
この「片付けRIZAP」はフリーミアムモデルの採用を検討しており，この「机メンタリング」のサービスによってマネタイズすることを考えています．
※「机ライフログ」と「机お叱りアラート」は機器代金以外は無料を想定しています．

### 解決出来ること
このテクノロジーを用いることで「机が綺麗な状態を維持できる人，生産性の高い人」に変わることができます．
更に，「机ライフログ」という新しいデータセットの概念は，人の生産性や性格，几帳面さにも影響すると考えており，  
今後はこの「机ライフログ」を用いた信用評価システムなどにも展開できると考えています．

### 今後の展望（事業展開）
![image](https://user-images.githubusercontent.com/21073221/47263218-072bdc80-d538-11e8-8528-ce94e2d036d0.png)

#### 事業展開１（「子供の片付けのしつけ」に展開）
「部屋の片付けのしつけ」は親にとって重要な仕事です．一方で，こどもの片付けの状態に「とても満足している」親はたった５％，約７割の親が満足できていません［5］．子供が楽しんで片付けをできるようにLINE株式会社のClovaを用いた教育プラットフォームに展開する予定です．

[[５]](hhttp://www.nomura-un.co.jp/page/news/pdf/20150903.pdf) 子供の片付けに関するアンケート　（野村不動産アーバンネット株式会社） 

#### 事業展開２（「ファーストフード店における掃除レビュー」に展開）
ファミリーレストランなどにおいて，お客様が来た際のテーブルの綺麗さを定量的に評価する仕組みをつくることでBtoBにも進出する予定です．

## 開発内容・開発技術
![image](https://user-images.githubusercontent.com/21073221/47262791-f6c23480-d52c-11e8-8783-f983efd47851.png)

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
* 関連する研究やプロダクトは特になし  
(４人のメンバー中，非情報系の理系大学院生がメンバーの３人を占めています．)

### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* RasPiによる画像の自動解析
* 物体認識（被覆率の算出と、ゆとりを持たせた物体位置の正誤判定）
* LINEAPIを用いた片付け結果の通知
* 特に力を入れた部分のファイルリンク（画像処理による散らかり度解析）
https://github.com/jphacks/KB_1801/tree/master/jphacksImagrecognition

![image](https://user-images.githubusercontent.com/21073221/47262947-9df49b00-d530-11e8-9535-9ba56a529333.png)


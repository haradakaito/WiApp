# NexmonによるCSIを用いたスマートデバイス状態推定  
## 0. はじめに
　IEEE 802.11規格の無線周波数Wi-Fiは, 携帯電話やラップトップPC, ゲーム機, テレビ等の様々なデバイスの通信に使用される無線LANとして普及している. 近年のWi-Fiは, デバイス通信ではなく, 人間活動認識(HAR)等の新しいセンシング手法として注目を集めている.   
　HARの既存研究として, RGB-Dカメラや加速度センサー等のウェアラブルデバイスを用いた手法が盛んに行われているが, これらは接触型センシング手法であり, 対象者によっては注察感を与えてしまい, プライバシーに関する問題に直面する可能性を否定できない.   
　Wi-Fiを用いたセンシング手法は, 従来の接触型のセンシング手法の代替となる非接触型のセンシング手法となる可能性がある. また, 今後更なる情報化に伴ってスマートデバイスが遍在化することも想定できるため, 実用化の容易性の点でも優れている.Wi-Fiでは, CSI(Chanel State Information)という無線送信信号の振幅と位相に関する情報で構成されたデータが送受信機間でやり取りされている. CSIデータを分析することで, Wi-Fi通信環境下における様々な要因による時間的環境変化を捉えることが可能になる. 
 
<img align="right" width="350" alt="image" src="https://github.com/haradakaito/NexmonCSI/assets/75819611/07cc38a8-7a66-4718-8d47-8cf2c3d251d1">  
　しかし, CSIデータは多くのWi-Fiチップメーカーは外部からのアクセス不可能にしていることが多く, CSIデータへのアクセスは容易ではない. 加えて, CSIデータへのアクセスを可能にするためのハードウェアとソフトウェアは共に高価であり, CSIデータを収集するにあたる制限が強い.そこで[[1]](https://github.com/haradakaito/NexmonCSI/blob/main/README.md#7-%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)の論文中に示されるような, Nexmonと呼ばれるオープンソースのCSI収集用ファームウェアパッチを用いて, 比較的安価なデバイスでCSI収集を行う. Nexmonを用いることで従来のCSIが抱えるハードウェアとソフトウェア制限の強さを解消したCSI収集システムを構築することが可能である.   
　本研究では, Nexmonを用いて(デバイスに対して)汎用性の高いCSI収集システムを構築し, スマートデバイスの状態推定という比較的局所的なパターンの分類タスクに対しての有効性を検証する. 

## 1. 既存研究
  Wi-Fiセンシングに関するサーベイ論文として[[2]](https://github.com/haradakaito/NexmonCSI/blob/main/README.md#7-%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)があるが, 
- 既存研究1
  
## 2. 実験環境
### 2.1 実験デバイス  
- CSI収集デバイス：RaspberryPi 4B  
- Wi-Fiルーター：ASUS RT-AC86U  
- Ping送信デバイス：dynabook GX83/MLE
- スマートデバイス：iphone12
  
### 2.2 通信条件  
- 帯域：2.4 / 5.0 [GHz]
- 帯域幅：20 / 40 / 80 [MHz]
- チャネル：任意
- Ping送信デバイスとスマートデバイスの接続帯域が異なる

## 3. データ収集フェーズ
### 3.1 収集条件
- Ping送信間隔：10 [Ping/s]
- Ping送信方法：Ping送信プログラム(.py)
- 収集時間：18000 [Ping]
- サンプリングレート：1 / 5 / 10 [Sample/s]
    
### 3.2 スマートデバイス状態
- LINE
- Instagram
- YouTube
- TikTok
- X(Twitter)
- Facebook
- Amazon
- Minecraft
- パズル&ドラゴンズ
- モンスターストライク
- eFootball
- 荒野行動
- ピッコマ
- Tetris
  
## 4. 信号処理フェーズ
### 4.1 pcap→csv変換
- 変換方法：CSI Extracterプログラム(.py)

### 4.2 ノイズ除去アルゴリズム
- 移動平均フィルター  
  ウィンドウサイズ(SL:1)：1 / 5 / 10 / 20  
  ウィンドウサイズ(SL:5)：2 / 10 / 20 / 40  
  ウィンドウサイズ(SL:10)：10 / 50 / 100 / 200  
- ガウシアンフィルター
- Savitzky-Golayフィルター
  
### 4.3 データ分割
- Train：Val：Test = 6 : 2 : 2

### 4.4 ウィンドウサイズ
ウィンドウサイズは, 1~60[s]スケールになるように設定
- ウィンドウサイズ(SL:1)：1 / 5 / 10 / 20 / 30 / 40 / 50 / 60
- ウィンドウサイズ(SL:5)：2 / 10 / 20 / 40 / 60 / 80 / 100 / 120
- ウィンドウサイズ(SL:10)：10 / 50 / 100 / 200 / 300 / 400 / 500 / 600
  
## 5. 学習・評価フェーズ
### 5.1 学習器
- SVM
- RandomForest
- LSTM
- LSTM-FCN
- 1D-CNN
- ResNet
- Transformer

## 6. 今後の展望
- 個人差の検討
- 環境差の検討
- 損失関数
- ソフトラベル

## 7. 参考文献
**[[1]](https://dl.acm.org/doi/10.1145/3349623.3355477)** GRINGOLI, Francesco, et al. Free your CSI: A channel state information extraction platform for modern Wi-Fi chipsets. In: Proceedings of the 13th International Workshop on Wireless Network Testbeds, Experimental Evaluation & Characterization. 2019. p. 21-28.  
**[[2]](https://dl.acm.org/doi/abs/10.1145/3310194)** MA, Yongsen; ZHOU, Gang; WANG, Shuangquan. WiFi sensing with channel state information: A survey. ACM Computing Surveys (CSUR), 2019, 52.3: 1-36.

## Nexmonのセットアップ


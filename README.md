
# NexmonによるCSIを用いたスマートデバイス状態認識  
## 0. はじめに
### 0.1 Wi-Fi(CSI)センシングの動機
　IEEE 802.11規格の無線周波数Wi-Fiは, 携帯電話やラップトップPC, ゲーム機, テレビ等の様々なデバイスの通信に使用される無線LANとして普及している. 近年のWi-Fiは, デバイス通信ではなく, 人間活動認識(HAR)等の新しいセンシング手法として注目を集めている.   
　HARの既存研究として, RGB-Dカメラや加速度センサー等のウェアラブルデバイスを用いた手法が盛んに行われているが, これらは接触型センシング手法であり, 対象者によっては注察感を与えてしまい, プライバシーに関する問題に直面する可能性を否定できない.   
　Wi-Fiを用いたセンシング手法は, 従来の接触型のセンシング手法の代替となる非接触型のセンシング手法となる可能性がある. また, 今後更なる情報化に伴ってスマートデバイスが遍在化することも想定できるため, 実用化の容易性の点でも優れている.
 Wi-Fiでは, CSI(Chanel State Information)という無線送信信号の振幅と位相に関する情報で構成されたデータが送受信機間でやり取りされている. CSIデータを分析することで, Wi-Fi通信環境下における様々な要因による時間的環境変化を捉えることが可能になる.   
### 0.2 Nexmonへの注目
　CSIデータは多くのWi-Fiチップメーカーは外部からのアクセス不可能にしていることが多く, CSIデータへのアクセスは容易ではない. 加えて, CSIデータへのアクセスを可能にするためのハードウェアとソフトウェアは共に高価であり, CSIデータを収集するにあたる制限が強い.そこで[[1]](https://github.com/haradakaito/NexmonCSI/blob/main/README.md#7-%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)の論文中に示されるような, Nexmonと呼ばれるオープンソースのCSI収集用ファームウェアパッチを用いて, 比較的安価なデバイスでCSI収集を行う. Nexmonを用いることで従来のCSIが抱えるハードウェアとソフトウェア制限の強さを解消したCSI収集システムを構築することが可能である.   
### 0.3 本研究のモチベーション
　Wi-Fi(CSI)センシングに関するサーベイ論文として[[2]](https://github.com/haradakaito/NexmonCSI/blob/main/README.md#7-%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)がある. [2]Fig.1には, Wi-Fiセンシングの概要について示されており, Wi-Fiセンシングは3つのセクションで大別され, 各セクションが更に3種類のアプローチで構成されている. 以下に, 各セクションとアプローチを示す. 

| Section  | Approach |
| ------------- | ------------- |
| Signal Processing(信号処理) | Noise Reduction(ノイズ低減), Signal Transform(信号変換), Signal Extraction(信号抽出) |
| Algorithm(アルゴリズム)  | Modeling-Based(数式モデルベース), Learning-Based(学習ベース), Hybrid(ハイブリッド) |
| Application(アプリケーション)  | Detection(検出), Recognition(認識), Estimation(推定) |

　本研究では, Nexmonを用いて(デバイスに対して)汎用性の高いCSI収集システムを構築し, スマートデバイスの状態推定(特に, 操作アプリケーション)という比較的局所的なパターンの分類タスクに対しての, Nexmon及びそれを用いたCSI収集・分析システムの有効性を検証する.   

## 1. 既存研究
　本研究のセクション属性は以下のようになる.  
 
- Signal Processing(信号処理)：Noise Reduction(ノイズ低減) / Signal Transform(信号変換) / Signal Extraction(信号抽出)
- Algorithm(アルゴリズム)：Learning-Besed(学習ベース)
- Application(アプリケーション)：Recognition(認識)

　Signal Procesingセクションに関しては, 単一のアプローチとは限らないため, AlgorithmとApplicationセクションにおいて, Learning-Based(学習ベース)のRecognition(認識)タスクを設定している研究の動向を調査した.   
### 1.1 Wi-Fi信号(CSI)を用いた局所的なジェスチャ認識[[3]](https://github.com/haradakaito/NexmonCSI/blob/main/README.md#7-%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)  

  
## 2. 実験環境
### 2.1 実験デバイス  
- CSI収集デバイス：RaspberryPi 4B  
- Wi-Fiルーター：ASUS RT-AC86U  
- Ping送信デバイス：dynabook GX83/MLE
- スマートデバイス：iphone12
  
### 2.2 通信条件  
- 無線規格：IEEE 802.11n / ac
- 帯域：2.4 / 5 [GHz]
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
- 変換方法：CSI Extractor(csi_changer.py)
```  
$ cd CSI_changer
$ python csi_changer.py
```
- 入力例(帯域幅:20Mhzで収集されたApp.pcapの0~100パケット部分をcsvファイルに変換)
```
Pcap File Name: App
Band Width: 20
> 0-100
```

### 4.2 ノイズ除去アルゴリズム
- NR(Noise Reduction)  
　・ローパスフィルター  
　　・バターワース型  
　・CFO(Carrier Frequency Offset)  
　・ウェーブレットフィルター  
　・Hampelフィルター  
　・移動平均フィルター  

- ST(Signal Transform)  
　・DWT(Discrete Wavelet Transform)  
　・高速フーリエ変換(FFT)  

- SE(Signal Extraction)  
　・閾値  
　・主成分分析(PCA)  
　・特徴量抽出  
　・ローパスフィルター  
　　・バターワース型  
　・BPF(Band Pass Filter)  
　　・バターワース型  

### 4.3 データ分割
- ダウンサンプリング
- シーケンス単位でシャッフル
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
**[[3]](https://dl.acm.org/doi/abs/10.1145/2999572.2999582)** ZHANG, Ouyang; SRINIVASAN, Kannan. Mudra: User-friendly fine-grained gesture recognition using WiFi signals. In: Proceedings of the 12th International on Conference on emerging Networking EXperiments and Technologies. 2016. p. 83-96.  

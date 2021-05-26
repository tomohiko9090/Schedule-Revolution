# 制作物名：「ちょっと部長！今週パツってます。」  

## 開発物概要
**言語**：Python 3.9.4  
**フレームワーク**：Django 3.1.7  
**ページのリンク**：http://45.76.98.152/list/  
**開発環境**：MacOS  
**外部サーバー(OS)**：vultur(ubuntu)  
**DB**：外部サーバー上ではPostgreSQLを使用  

## 
**メイン機能**：  
・部下にとって仕事の内容をどのように捉えているのか可視化できる(matplotlibを使用)  
・一週間のスケジュールの自動で作成できる   


**開発経緯**：  
・仕事量が多く、その人にとっては辛い仕事である時、上司がその状況に気がつき仕事の割り振り方を変えることができれば、チームとして成果を上げることができると考えたから。  
・毎週１週間の予定を組み立てる作業を自動化し、たくさんやることがあって何から手をつけていいのか分からない状態をなくしたいと考えたから。  


**工夫した点**:   
・「7つの習慣」の緊急重要マトリクスを用いて、人生にとって大切である「重要であり緊急でないもの」を実行できる予定の組み方にした点。  
・作成した一週間のスケジュールをpdfでダウンロードできるようにした点。  

## アプリの使用方法
1. このリポジトリをclone
2. 以下を実行
以下を実行
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsurperuser
python3 manage.py runserver
```



# Auto AnimeFace Cropping

入力イメージからAnimeFaceを検出して設定パラメータに従いキャラクタを切り抜きます。GPUは使わず、CPUのみで動きます。

## インストール

git clone 

python3 -m venv aseg

source aseg/bin/activate

cd anime-crop

pip install requirements.txt

ウエイトのダウンロード

https://huggingface.co/UZUKI/Scalable-tkh/tree/main

から

isnetis.ckpt

realesr-animevideov3.pth

ssd_best8.pth

をダウンロードし、weights　ディレクトリにコピー

## 利用方法

python anime_face_seg.py

gradioが起動するのでブラウザーからアクセス

### 変数

Image Type　入力画像がpillow形式かOpenCV形式かを選択

Height　クロップ後画像の貼り付け用キャンバスサイズの高さ

Width　　クロップ後画像の貼り付け用キャンバスサイズの幅

Top Space　クロップしたキャラクタを貼り付けいる時の上部位置

Head size　FaceDitection時のバウンディングboxの大きさの指定。入力画像のキャラクタの大きさに関わらず出力キャラクタの顔がこの大きさになり、キャラクタ全体の大きさも同時に拡大・縮小されます。

FaceDetection confidence lebel　FaceDitection時の推論精度指定　大きくするほど厳しく判定し、小さくすると甘くなります。大きくすると検出不能が生じ、小さくするとご検出が発生します。


Flag　クリックでflaggedディレクトリが作成され画像が保存されます。

このソフトウエアが以下のaiを利用しています。

背景削除

https://github.com/SkyTNT/anime-segmentation

アップスケール

https://github.com/xinntao/Real-ESRGAN

Face detection

SSD





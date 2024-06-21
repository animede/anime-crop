# Auto AnimeFace Cropping

入力イメージからAnimeFaceを検出して設定パラメータに従いキャラクタを切り抜きます。GPUは使わず、CPUのみで動きます。

## インストール

Ubuntuの場合はターミナル

Windowsの場合はWindowsシステムのコマンドプロンプト

### リポジトリのクローン

git clone https://github.com/animede/anime-crop.git

Windows==>git または　Github Desktopをインストールしてリポジトリをクローンする

git　==>https://gitforwindows.org/

参考　https://qiita.com/T-H9703EnAc/items/4fbe6593d42f9a844b1c

### 仮想環境の準備

python -m venv aseg

source aseg/bin/activate

Windows==>aseg\Script\activate

### 環境構築

cd anime-crop

pip install -r requirements.txt

インストールされないモジュールがあるので以下手動でインストール

pip install gradio

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

pip install pip install opencv-python

pip install basicsr

pip install numpy==1.26.3

pip install pytorch_lightning

### basicSRの修正

インストールしたままではエラーになるので以下対処

==>　https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/13985

\aseg\Lib\site-packages\basicsr\data\degradations.py　line7を

from torchvision.transforms.functional_tensor import rgb_to_grayscale

から

from torchvision.transforms.functional import rgb_to_grayscale

に変更

### ウエイトのダウンロード

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

## このソフトウエアは以下のAIを利用しています。

背景削除

https://github.com/SkyTNT/anime-segmentation

アップスケール

https://github.com/xinntao/Real-ESRGAN

Face detection

SSD





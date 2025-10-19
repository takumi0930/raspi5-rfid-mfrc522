# raspi5-rfid-mfrc522
This repository contains files related to operating the MFRC522 RFID module on Raspberry Pi 5.

SunFounder コードダウンロードでは，Raspberry pi 5でMFRC522 RFIDモジュールを動作できるプログラムが公開されている，

SunFounder コードダウンロード
https://github.com/sunfounder/davinci-kit-for-raspberry-pi
/python-pi5/ にある以下の3つのファイル
- MFRC522.py (import spidev, signal, time)
- 2.2.10_read.py (import MFRC522, signal, time)
- 2.2.10_write.py (import MFRC522, signal, time)
(RPi.GPIOが使われていないので，Raspberry pi 5でも動作できる)


ここでは，上記の3つのファイルを基に，自分のプログラム用に使いやすくしたプログラムを共有する．

- MFRC522.py
元のMFRC522.pyにおいて，MFRC522_Read(self, blockAddr)の中の，print文をコメントアウトにした．その他の変更はなし．
- rfid_read.py
2.2.10_read.pyを基に作成した．
RFIDタグをリーダーにかざすと，そのRFIDタグのuidと保存されているtextをコマンドラインに表示する.
- rfid_write.py
2.2.10_write.pyを基に作成した．
RFIDタグをリーダーにかざして，書き込みたい文字を入力すると，そのuidのRFIDタグに書き込みができる.

また，フォルダ構成と依存関係を示す．

- フォルダ構成
MFRC522.py, rfid_read.py, rfid_write.pyを同じディレクトリに置く
- Requires（依存関係）
MFRC522.py: spidev, signal, time.py
rfid_read.py: MFRC522.py, time.py
rfid_write.py: MFRC522.py, time.py

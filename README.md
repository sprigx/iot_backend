# iot_backend

ラズパイを使った赤外線スマートリモコンのバックエンドAPIサーバー

## 使用ハードウェア
- Raspberry Pi Zero
- 赤外線LEDユニット: https://qiita.com/takjg/items/e6b8af53421be54b62c9
- 大気計測センサー: BME680

## パッケージ
- FastAPI
- uvicorn
- bme680
- pigpio

## API DOC
|                     | method | URI  | request  | response  |
| ------------------  | ---- | ------- | ------- |------- |
| 赤外線信号を送出     | POST | /control | {"target": "command"} | {"status": "ok"または"failed"}
| 大気の状態を取得する | GET | /air      | |  {"status": "ok", "temperature": "", "pressure": "", "humidity": "", "gas_resistance": ""} |
| 動作確認 | GET | /test      | |  {"status": "ok"} |

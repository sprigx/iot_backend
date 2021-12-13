# iot_backend

ラズパイを使った赤外線スマートリモコンのバックエンドAPIサーバー

## usage

```
$ python3 main.py
```

## Hardware
<img width="300" alt="pi_zero" src="https://user-images.githubusercontent.com/46306618/145812585-cf625fe5-1a6a-4661-970e-ef35a1695332.png">

- Raspberry Pi Zero
- 赤外線LEDユニット(参考記事): https://qiita.com/takjg/items/e6b8af53421be54b62c9
- 大気計測センサー: BME680

## Python packages
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

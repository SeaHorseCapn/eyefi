# ESP32 Setup Guide

## Recommended Hardware

| Component | Model | Cost |
|-----------|-------|------|
| ESP32 Board | ESP32-S3-DevKitC-1 | $8-12 |
| USB-C Cable | Quality data cable | $3-5 |
| Antenna (optional) | 2.4GHz WiFi | $2-4 |

**Total per node**: ~$12-20

## Step-by-Step Flashing

1. Install Arduino IDE 2.x
2. Add ESP32 board support (https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json)
3. Select Board: ESP32S3 Dev Module
4. Open examples/esp32_csi_capture.ino
5. Upload

## Verification

Open Serial Monitor (115200 baud). You should see:
```
eyefi ESP32 CSI ready
CSI_DATA,...
```

## Troubleshooting

- Use data cable (not charging only)
- Correct baud rate (115200)
- Proper board selection

Full guide at: https://github.com/SeaHorseCapn/eyefi
from __future__ import annotations

"""
eyefi.hardware.esp32
Real ESP32 CSI capture implementation.

Copyright (c) 2026 eyefi Contributors
SPDX-License-Identifier: MIT
"""

import serial
import time
import numpy as np
from typing import Iterator, Optional
from dataclasses import dataclass

@dataclass
class CSIFrame:
    timestamp: float
    amplitude: np.ndarray
    phase: np.ndarray
    node_id: str = "default"

class ESP32CSISensor:
    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        self.serial_conn = None
    
    def connect(self):
        self.serial_conn = serial.Serial(self.port, 115200, timeout=1)
        time.sleep(2)
        print("Connected to ESP32")
    
    def stream_frames(self):
        while True:
            line = self.serial_conn.readline().decode().strip()
            if line.startswith("CSI_DATA"):
                yield line
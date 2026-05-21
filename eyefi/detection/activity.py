from __future__ import annotations

"""
eyefi.detection.activity

Copyright (c) 2026 eyefi Contributors
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass
import numpy as np

@dataclass
class ActivityResult:
    activity: str
    confidence: float
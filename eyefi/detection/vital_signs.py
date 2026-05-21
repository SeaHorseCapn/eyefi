from __future__ import annotations

"""
eyefi.detection.vital_signs

Copyright (c) 2026 eyefi Contributors
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass
from typing import Optional
import numpy as np

@dataclass
class VitalSignsResult:
    breathing_bpm: Optional[float]
    breathing_confidence: float
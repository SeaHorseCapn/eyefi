from __future__ import annotations

"""
eyefi.detection.presence

Copyright (c) 2026 eyefi Contributors
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass
from typing import Dict
import numpy as np

@dataclass
class PresenceResult:
    is_present: bool
    confidence: float
    score: float
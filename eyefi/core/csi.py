from __future__ import annotations

"""
eyefi.core.csi
Elegant Channel State Information (CSI) handling.

Copyright (c) 2026 eyefi Contributors
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass
import numpy as np

@dataclass
class CSIFrame:
    timestamp: float
    amplitude: np.ndarray
    phase: np.ndarray
    node_id: str = "default"
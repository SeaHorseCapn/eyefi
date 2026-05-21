from __future__ import annotations

"""
eyefi.fusion.multi_node

Copyright (c) 2026 eyefi Contributors
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass

@dataclass
class NodeReading:
    node_id: str
    presence_confidence: float
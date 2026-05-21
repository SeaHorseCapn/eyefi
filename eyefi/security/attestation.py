from __future__ import annotations

"""
eyefi.security.attestation

Copyright (c) 2026 eyefi Contributors
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass

@dataclass
class Attestation:
    measurement_hash: str
    signature: str
    node_id: str
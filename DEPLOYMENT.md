# eyefi Production Deployment Guide

## Overview

eyefi is designed for production deployment in secure environments.

## Recommended Architecture

```
└─── ESP32 Nodes ────▶ eyefi API (FastAPI) ────▶ Dashboard
                               │
                               ▼
                        Attestation + Logging
```

## Docker Production Deployment

```bash
docker-compose up -d
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| EYEFI_NODE_ID | eyefi-node | Unique node identifier |
| EYEFI_LOG_LEVEL | INFO | Logging level |

## Security Recommendations

1. Run behind reverse proxy with TLS
2. Enable attestation on all measurements
3. Use HSM for private keys in high-security environments
4. Network isolation
5. Regular calibration audits

## Compliance

- GDPR (no personal imagery)
- HIPAA (non-intrusive vital signs)
- Classified environments (attestation + audit logging)
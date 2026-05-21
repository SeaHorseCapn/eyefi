# eyefi Production Deployment Guide

Full guide at: https://github.com/SeaHorseCapn/eyefi

## Quick Start (Docker)

```bash
docker-compose up
```

## Security Recommendations
- Run behind reverse proxy with TLS
- Enable attestation
- Use HSM for private keys in high-security environments
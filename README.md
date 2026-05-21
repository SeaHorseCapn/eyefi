# eyefi

<p align="center">
  <a href="https://github.com/SeaHorseCapn/eyefi/stargazers">
    <img src="https://img.shields.io/github/stars/SeaHorseCapn/eyefi?style=social" alt="GitHub stars">
  </a>
  <a href="https://github.com/SeaHorseCapn/eyefi/network/members">
    <img src="https://img.shields.io/github/forks/SeaHorseCapn/eyefi?style=social" alt="GitHub forks">
  </a>
  <a href="https://github.com/SeaHorseCapn/eyefi/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/SeaHorseCapn/eyefi" alt="License">
  </a>
</p>

```
███████╗██╗   ██╗███████╗███████╗██╗
██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝██║
█████╗   ╚████╔╝ █████╗  █████╗  ██║
██╔══╝    ╚██╔╝  ██╔══╝  ██╔══╝  ██║
███████╗   ██║   ███████╗██║     ██║
╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
```

**Radio Vision — Elegant, Secure, Production-Grade Sensing Using Commodity Radio Waves**

eyefi turns ordinary WiFi signals into a powerful, camera-free sensing system capable of detecting presence, breathing, heart rate, falls, and activity — all without capturing a single pixel.

Designed from first principles for **reliability, elegance, and security**, eyefi is built to the standard expected by state actors, critical infrastructure operators, and professional security teams.

## Philosophy

- **Elegance over complexity**: Clean architecture, minimal dependencies, beautiful code.
- **Security by design**: Cryptographic attestation, zero-trust data handling, audit-ready logging.
- **Scientific rigor**: Proper calibration, statistical confidence scoring, validated signal processing.
- **Production readiness**: Type-safe, well-documented, extensible, and deployable at scale.
- **Hardware agnostic**: Works with ESP32 today, designed for future specialized radio hardware.

## Core Capabilities (v3)

- **Presence Detection** — Sub-second, high-confidence detection even through walls
- **Vital Signs** — Breathing rate + heart rate estimation with confidence intervals
- **Activity Recognition** — Walking, sitting, falling, with severity scoring
- **Multi-Node Fusion** — Coherent sensing across distributed radio nodes
- **Secure Attestation** — Every measurement can be cryptographically verified
- **Real-time & Edge** — Low-latency processing suitable for embedded deployment

## Quick Start

```bash
pip install eyefi
eyefi demo
eyefi dashboard
```

## Architecture

eyefi follows a clean layered architecture:

```
Physics → Signal Processing → Feature Extraction → Detection → Fusion → Intelligence → Interface
```

All layers are modular, testable, and independently extensible.

## Advanced Features (v3)

- **Multi-Node Fusion** — Coherent sensing across distributed radio nodes with spatial awareness
- **Cryptographic Attestation** — Ed25519 signed measurements for non-repudiation
- **Advanced Activity Recognition** — Walking, sitting, falling, sudden movement detection
- **Hardware Abstraction** — Clean support for ESP32 and future radio hardware
- **Alerting System** — Configurable real-time alerts
- **3D Visualization Ready** — Scene data generator for Three.js / Plotly
- **Full REST API + Python SDK** — Production-ready integration

## Security & Privacy

- No video or identifiable imagery ever captured
- Optional end-to-end encryption of measurements
- Cryptographic witness chains for data integrity
- Designed for GDPR, HIPAA, and classified environments

## Use Cases

- Secure facilities & critical infrastructure monitoring
- Elder care & assisted living (non-intrusive)
- Defense & intelligence applications
- Smart buildings & energy optimization
- Research into radio-based perception

## Status

**Current Version**: 3.0 (First Principles Redesign)

This is a ground-up redesign focused on elegance, security, and professional-grade reliability.

---

*Built with precision. Designed for those who need to see without being seen.*
# Self-Hosting Trivena Meet

Deploy Trivena Meet on a single VPS with Docker (backend, frontend, Socket.io, workers, MariaDB, Redis, Nginx, Certbot, and Mediasoup SFU).

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/TrivenaCloud/trivena-meet/develop/deploy/install.sh | bash
```

By default the installer creates a `trivena-meet` directory:

```bash
cd trivena-meet
```

Follow the script prompts for domain and SSL. When finished, Meet is available at `https://YOUR_DOMAIN`.

## Update

Re-run the installer / compose update flow from the deploy directory to pull the latest images and restart services.

## Links

- Repo: [TrivenaCloud/trivena-meet](https://github.com/TrivenaCloud/trivena-meet)
- Cloud: [cloud.trivena.tech](https://cloud.trivena.tech)

# Trivena Meet SFU Server

Mediasoup-based Selective Forwarding Unit (SFU) for Trivena Meet.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/TrivenaCloud/trivena-meet/develop/sfu-server/deploy/install.sh | bash
```

## Configuration

| Variable | Description |
| --- | --- |
| `JWT_SECRET` | Shared secret with the Meet site (`openssl rand -base64 32`) |

Add the matching secret to the site’s `site_config.json` so the backend can authorize SFU traffic.

## Links

- Repo: [TrivenaCloud/trivena-meet](https://github.com/TrivenaCloud/trivena-meet)

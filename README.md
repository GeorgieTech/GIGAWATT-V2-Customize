# Gigawatt V2 — Customize

Repo: [`GIGAWATT-V2-Customize`](https://github.com/GeorgieTech/GIGAWATT-V2-Customize)

This is the **web UI skins** tree. Halloween, sports-fan, and other looks live here so the product firmware stays clean.

**Product firmware (buyers, eBay, shipped units):** [`GIGAWATT-V2`](https://github.com/GeorgieTech/GIGAWATT-V2)

This project is **not affiliated with Savant Systems**.

## What this repo is for

`crypt.css` already uses color tokens (`--ember`, `--void`, `--card`, …). A skin is a second stylesheet that reassigns those tokens. Playing, Library, Karaoke, Report, and Settings all pick it up.

Shipped examples:

| Skin | File | Look |
|---|---|---|
| Stock | `host-webui/skins/stock.css` | Product Gigawatt |
| Halloween | `host-webui/skins/halloween.css` | Orange / bone / void |
| Sports | `host-webui/skins/sports.css` | Field green / stadium gold |

Add a club or season by copying a CSS file:

```sh
cp host-webui/skins/sports.css host-webui/skins/your-team.css
# edit --ember / --void / --card
```

Settings → **Look** lists every `host-webui/skins/*.css`. Details: [docs/SKINS.md](docs/SKINS.md).

## Lab vs a shipped unit

Lab jack for preview: **192.168.1.142**. A shipped unit takes **DHCP** — pass that IP.

```sh
scripts/push-host.sh 192.168.1.142
```

Pushing **this** checkout replaces `/data/www` on that chassis, including the Look picker. It is not the product image. Restore stock firmware from [`GIGAWATT-V2`](https://github.com/GeorgieTech/GIGAWATT-V2):

```sh
cd ../GIGAWATT-V2
scripts/push-host.sh 192.168.1.142
```

Pull product updates into this tree:

```sh
git fetch upstream
git merge upstream/main
```

`upstream` is `https://github.com/GeorgieTech/GIGAWATT-V2.git`.

## Docs

- Skins: [docs/SKINS.md](docs/SKINS.md)
- Hardware (lab): [docs/HOST-142.md](docs/HOST-142.md)
- Directories: [docs/LAYOUT.md](docs/LAYOUT.md)
- Deploy: [docs/DEPLOY.md](docs/DEPLOY.md)

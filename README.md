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
| LA Rams V1 | `host-webui/skins/la-rams.css` | Rams Royal / Sol / Bone |
| Las Vegas Raiders V1 | `host-webui/skins/lv-raiders.css` | Silver / Black |
| Philadelphia Eagles V1 | `host-webui/skins/phi-eagles.css` | Midnight Green / Silver |
| Dallas Cowboys V1 | `host-webui/skins/dal-cowboys.css` | Navy / Silver / White |
| Buffalo Bills V1 | `host-webui/skins/buf-bills.css` | Royal Blue / Red / White |
| San Francisco 49ers V1 | `host-webui/skins/sf-49ers.css` | Scarlet / Gold / Black |
| Seattle Seahawks V1 | `host-webui/skins/sea-seahawks.css` | College Navy / Action Green / Wolf Grey |
| Arizona Cardinals V1 | `host-webui/skins/ari-cardinals.css` | Cardinal Red / Desert Gold / White / Black |
| Tampa Bay Buccaneers V1 | `host-webui/skins/tb-buccaneers.css` | Buccaneers Red / Pewter / Orange / White |
| New Orleans Saints V1 | `host-webui/skins/no-saints.css` | Old Gold / Black / White |

Add a club or season by copying a CSS file:

```sh
cp host-webui/skins/sports.css host-webui/skins/your-team.css
# edit --ember / --void / --card
```

Settings → **Look** is a dropdown of every `host-webui/skins/*.css`. Details: [docs/SKINS.md](docs/SKINS.md).

Latest themed release: **[New Orleans Saints V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/no-saints-v1)**. Also [Tampa Bay Buccaneers V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/tb-buccaneers-v1), [Arizona Cardinals V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/ari-cardinals-v1), [Seattle Seahawks V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/sea-seahawks-v1), [San Francisco 49ers V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/sf-49ers-v1), [Buffalo Bills V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/buf-bills-v1), [Dallas Cowboys V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/dal-cowboys-v1), [Philadelphia Eagles V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/phi-eagles-v1), [Las Vegas Raiders V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/lv-raiders-v1), and [LA Rams V1](https://github.com/GeorgieTech/GIGAWATT-V2-Customize/releases/tag/la-rams-v1). Fan looks, not official NFL products. This checkout ships with Saints selected (`host-webui/skins/active`). Switch in Settings → Look.

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

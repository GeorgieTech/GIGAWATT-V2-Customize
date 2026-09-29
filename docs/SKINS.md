# Web UI skins

This tree (`GIGAWATT-V2-Customize`) is for **looks**. Product firmware stays in [`GIGAWATT-V2`](https://github.com/GeorgieTech/GIGAWATT-V2).

Skins are CSS overlays on `host-webui/crypt.css`. Pages load `/crypt.css` then `/skin.css`. A skin should mostly reassign the `:root` tokens (`--ember`, `--void`, `--card`, …) so Playing, Library, Karaoke, Report, and Settings all change together.

## Files

| Path | Role |
|---|---|
| `host-webui/skins/<id>.css` | Overlay. `id` is lowercase `a-z0-9-` |
| `host-webui/skins/active` | Default if the jack has no saved choice |
| `/data/crypt/skin.json` | Last pick from Settings → Look (survives a push) |

Shipped examples: **stock** (product look), **halloween**, **sports**.

## Add a skin

1. Copy `host-webui/skins/sports.css` to `host-webui/skins/your-team.css`.
2. Change `--ember` / `--void` / `--card` to the club colors.
3. Push this checkout. Settings → Look lists every `*.css` in that folder.

Do not fork HTML for a color swap. Only add extra rules when a token is not enough (gradients, letter-spacing, button fill).

## Preview on a jack

`scripts/push-host.sh 192.168.1.142` (or the unit’s current DHCP IP) **replaces** `/data/www` with this tree, including the skin picker. The product repo does not have skins. Push [`GIGAWATT-V2`](https://github.com/GeorgieTech/GIGAWATT-V2) again to restore stock firmware.

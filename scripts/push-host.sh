#!/bin/bash
# Copy this checkout onto one Gigawatt host and install.
# Usage: scripts/push-host.sh <ip>
# Lab jack: scripts/push-host.sh 192.168.1.142
# Shipped unit: pass the current DHCP address, not the lab IP.
# SSH user is RPM. Do not put the password in this file.
set -euo pipefail
HOST="${1:-}"
if [ -z "$HOST" ]; then
  echo "usage: scripts/push-host.sh <ip>" >&2
  echo "example: scripts/push-host.sh 192.168.1.142" >&2
  exit 2
fi
case "$HOST" in
  192.168.1.40|192.168.1.178|192.168.1.179|192.168.1.180)
    echo "refusing $HOST" >&2
    exit 2
    ;;
esac
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
UI="$ROOT/host-webui"
LIST="$UI/FILES"
if [ ! -f "$LIST" ]; then
  echo "missing $LIST" >&2
  exit 1
fi
FILES=()
while IFS= read -r name; do
  [ -z "$name" ] && continue
  case "$name" in
    \#*) continue ;;
  esac
  FILES+=("$UI/$name")
done < "$LIST"
SSH=(ssh -o IPQoS=none -o ConnectTimeout=30)
SCP=(scp -O -o IPQoS=none -o ConnectTimeout=30)
echo "push $(cat "$UI/VERSION") -> RPM@$HOST"
"${SCP[@]}" "${FILES[@]}" "RPM@$HOST:/tmp/"
"${SSH[@]}" "RPM@$HOST" rm -rf /tmp/gigawatt-airplay /tmp/gigawatt-nas /tmp/gigawatt-skins
"${SCP[@]}" -r "$UI/airplay" "RPM@$HOST:/tmp/gigawatt-airplay"
"${SCP[@]}" -r "$UI/nas" "RPM@$HOST:/tmp/gigawatt-nas"
"${SCP[@]}" -r "$UI/skins" "RPM@$HOST:/tmp/gigawatt-skins"
"${SSH[@]}" "RPM@$HOST" sudo env bash /tmp/install-on-host.sh
"${SSH[@]}" "RPM@$HOST" cat /data/www/VERSION

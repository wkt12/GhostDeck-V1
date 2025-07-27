🔑 Step 1: Launcher Script — arena_launcher.sh
`bash
!/bin/bash
echo "[Arena] Stealth loading..."
sleep 1
python3 HUD/terminal_flicker.py &
bash modules/hydra_hook.sh &
sleep 2
echo "[Arena] Active. Cluster will report false positives until node label mismatch."
`

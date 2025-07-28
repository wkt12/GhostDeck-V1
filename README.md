# GhostDeck-V1


Project Structure — “GhostDeck v1”

GhostDeck/
├── arena_launcher.sh # Termux-ready launcher (stealth entry)
├── challenge_pack.json # Mutation trap challenge config
├── modules/
│ ├── hydra_hook.sh # Hydra post-auth bloom trigger
│ ├── friday_bloom.yaml # Friday module for auto-deploy
│ └── metasploit_fingerprint.rb # Misdirected sidecar fingerprint mod
├── payloads/
│ ├── drop.sh # Bloom detonator script (curl + shell)
│ └── ghost_bloom.py # Python-based HUD with visual flickers
├── HUD/
│ └── terminal_flicker.py # Glitchwave HUD display engine
├── cloak/
│ └── container_indexer.yaml # Docker container with bait labels
│ └── postdeploy.sh # Silent trigger on label fingerprint
└── ghost.eviction.sh # Self-delete script post-mutation

Every component is modular, pentest-grade, and flavorfully deceptive

<img width="1024" height="1024" alt="1000044418" src="https://github.com/user-attachments/assets/7df02b25-a597-4fca-8069-d48ae1c09ca7" />

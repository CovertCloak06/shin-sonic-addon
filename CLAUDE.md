# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Custom Minecraft Bedrock addon called "Shin Sonic" - a Huggy Wuggy-style horror character for the user's daughter to play on Nintendo Switch via Realms.

## Current Status

- **Addon:** COMPLETE - `shin_sonic_addon/shin_sonic_addon.mcaddon`
- **GitHub:** Pushed to https://github.com/CovertCloak06/shin-sonic-addon
- **Windows To Go:** Created on 1TB USB drive
- **Next Steps:** User needs to boot into Windows, install Minecraft Bedrock, import addon, set up Realms, then daughter plays on Switch

## Key Files

```
shin_sonic_addon/
├── shin_sonic_addon.mcaddon       # Final packaged addon (import this)
├── behavior_pack/
│   ├── entities/shin_sonic.json   # Entity with 4 growth phases
│   ├── spawn_rules/shin_sonic.json
│   └── manifest.json
└── resource_pack/
    ├── textures/entity/shin_sonic/phase1-4.png
    ├── models/entity/shin_sonic.geo.json
    ├── render_controllers/shin_sonic.json
    └── entity/shin_sonic.entity.json
```

## Shin Sonic Features

- **4 Growth Phases** - grows bigger after killing players/mobs
  - Phase 1: 1.0x scale, 50 HP, 6 damage
  - Phase 2: 1.5x scale, 100 HP, 10 damage
  - Phase 3: 2.2x scale, 200 HP, 16 damage
  - Phase 4: 3.5x scale, 500 HP, 25 damage, BOSS bar, darkens sky
- Hunts players, villagers, animals
- Custom textures per phase (creepier as grows)
- Spawn egg included
- Summon command: `/summon shinsonic:shin_sonic`

## Build Commands

```bash
# Rebuild the .mcaddon package
cd shin_sonic_addon
cd behavior_pack && zip -r ../shin_sonic_bp.mcpack . && cd ..
cd resource_pack && zip -r ../shin_sonic_rp.mcpack . && cd ..
zip shin_sonic_addon.mcaddon shin_sonic_bp.mcpack shin_sonic_rp.mcpack
rm shin_sonic_bp.mcpack shin_sonic_rp.mcpack
```

## Target Platform

- **Minecraft Bedrock Edition** (not Java)
- Tested for: Android, Windows 10/11, Nintendo Switch (via Realms)
- Format version: 1.20.0+

## Related Guides

- `PROJECT_STATUS.md` - Full status and next steps
- `REALMS_SETUP_GUIDE.md` - How to set up Realms for Switch
- `SWITCH_SETUP_GUIDE.md` - Local hosting alternative
- `CPM_INSTALL_GUIDE.md` - Custom Player Models (Java Edition alternative)

## User Context

Building this for the user's daughter. She plays Minecraft on Nintendo Switch. The addon needs to be accessible via Realms since Switch can't directly install addons.

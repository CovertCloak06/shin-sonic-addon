#!/usr/bin/env python3
"""
Cursed Sonic Minecraft Skin Generator
Creates a 64x64 Minecraft skin based on the nightmare Sonic meme
"""

from PIL import Image, ImageDraw

# Create 64x64 RGBA image
skin = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
draw = ImageDraw.Draw(skin)

# Colors
BLUE_DARK = (20, 50, 180, 255)      # Dark blue fur
BLUE_MID = (30, 80, 200, 255)       # Mid blue
BLUE_LIGHT = (50, 100, 220, 255)    # Light blue highlights
SKIN_TAN = (210, 170, 140, 255)     # Mouth/muzzle area
SKIN_DARK = (180, 140, 110, 255)    # Darker skin tone
WHITE = (255, 255, 255, 255)        # Teeth/eyes
OFF_WHITE = (240, 235, 230, 255)    # Teeth
BLACK = (10, 10, 10, 255)           # Pupils/nose
PINK = (180, 100, 110, 255)         # Inner mouth/tongue
GUM_PINK = (200, 130, 140, 255)     # Gums
RED = (200, 50, 50, 255)            # Shoes
YELLOW = (230, 200, 50, 255)        # Shoe buckle

# ============ HEAD (8x8x8 cube) ============
# Head front: x=8-15, y=8-15
# Head back: x=24-31, y=8-15
# Head top: x=8-15, y=0-7
# Head bottom: x=16-23, y=0-7
# Head right: x=0-7, y=8-15
# Head left: x=16-23, y=8-15

def draw_head_front():
    """Draw the front of the head with the creepy face"""
    # Base blue face
    for y in range(8, 16):
        for x in range(8, 16):
            skin.putpixel((x, y), BLUE_MID)

    # Lighter blue top area (forehead)
    for y in range(8, 10):
        for x in range(8, 16):
            skin.putpixel((x, y), BLUE_LIGHT)

    # Tan muzzle/mouth area (bottom half)
    for y in range(12, 16):
        for x in range(9, 15):
            skin.putpixel((x, y), SKIN_TAN)

    # Eyes - white with small black pupils (wide creepy eyes)
    # Left eye
    skin.putpixel((9, 10), WHITE)
    skin.putpixel((10, 10), WHITE)
    skin.putpixel((9, 11), WHITE)
    skin.putpixel((10, 11), BLACK)  # Pupil

    # Right eye
    skin.putpixel((13, 10), WHITE)
    skin.putpixel((14, 10), WHITE)
    skin.putpixel((14, 11), WHITE)
    skin.putpixel((13, 11), BLACK)  # Pupil

    # Black nose
    skin.putpixel((11, 11), BLACK)
    skin.putpixel((12, 11), BLACK)

    # THE TEETH - the iconic horrifying grin
    # Upper teeth row
    for x in range(9, 15):
        skin.putpixel((x, 13), OFF_WHITE)

    # Lower teeth row
    for x in range(9, 15):
        skin.putpixel((x, 14), OFF_WHITE)

    # Mouth outline/gums
    skin.putpixel((9, 12), SKIN_DARK)
    skin.putpixel((14, 12), SKIN_DARK)

    # Pink tongue/inner mouth hint
    skin.putpixel((11, 15), PINK)
    skin.putpixel((12, 15), PINK)

def draw_head_sides():
    """Draw sides, top, bottom of head"""
    # Head right side (x=0-7, y=8-15)
    for y in range(8, 16):
        for x in range(0, 8):
            skin.putpixel((x, y), BLUE_MID)
    # Some tan showing on side
    for y in range(12, 16):
        for x in range(5, 8):
            skin.putpixel((x, y), SKIN_TAN)

    # Head left side (x=16-23, y=8-15)
    for y in range(8, 16):
        for x in range(16, 24):
            skin.putpixel((x, y), BLUE_MID)
    # Tan on side
    for y in range(12, 16):
        for x in range(16, 19):
            skin.putpixel((x, y), SKIN_TAN)

    # Head top (x=8-15, y=0-7) - blue fur spikes
    for y in range(0, 8):
        for x in range(8, 16):
            if y < 2:
                skin.putpixel((x, y), BLUE_DARK)
            elif y < 4:
                skin.putpixel((x, y), BLUE_MID)
            else:
                skin.putpixel((x, y), BLUE_LIGHT)

    # Head bottom (x=16-23, y=0-7) - under chin, tan
    for y in range(0, 8):
        for x in range(16, 24):
            skin.putpixel((x, y), SKIN_TAN)

    # Head back (x=24-31, y=8-15) - blue
    for y in range(8, 16):
        for x in range(24, 32):
            skin.putpixel((x, y), BLUE_DARK)
    # Blue quills/spikes pattern
    for x in [25, 27, 29]:
        skin.putpixel((x, 8), BLUE_LIGHT)
        skin.putpixel((x, 9), BLUE_MID)

# ============ BODY (8x12x4) ============
# Body front: x=20-27, y=20-31
# Body back: x=32-39, y=20-31

def draw_body():
    """Draw the torso"""
    # Body front (x=20-27, y=20-31)
    for y in range(20, 32):
        for x in range(20, 28):
            if x >= 22 and x <= 25 and y >= 22 and y <= 29:
                # Tan belly
                skin.putpixel((x, y), SKIN_TAN)
            else:
                skin.putpixel((x, y), BLUE_MID)

    # Body back (x=32-39, y=20-31)
    for y in range(20, 32):
        for x in range(32, 40):
            skin.putpixel((x, y), BLUE_DARK)

    # Body right side (x=16-19, y=20-31)
    for y in range(20, 32):
        for x in range(16, 20):
            skin.putpixel((x, y), BLUE_MID)

    # Body left side (x=28-31, y=20-31)
    for y in range(20, 32):
        for x in range(28, 32):
            skin.putpixel((x, y), BLUE_MID)

    # Body top (x=20-27, y=16-19)
    for y in range(16, 20):
        for x in range(20, 28):
            skin.putpixel((x, y), BLUE_LIGHT)

    # Body bottom (x=28-35, y=16-19)
    for y in range(16, 20):
        for x in range(28, 36):
            skin.putpixel((x, y), BLUE_DARK)

# ============ ARMS ============
# Right arm: x=40-55, y=16-31 (front at 44-47)
# Left arm (slim): x=32-47, y=48-63

def draw_arms():
    """Draw both arms - blue"""
    # Right arm outer (x=40-43, y=20-31)
    for y in range(20, 32):
        for x in range(40, 44):
            skin.putpixel((x, y), BLUE_MID)

    # Right arm front (x=44-47, y=20-31)
    for y in range(20, 32):
        for x in range(44, 48):
            if y >= 28:  # Hands - tan/skin
                skin.putpixel((x, y), SKIN_TAN)
            else:
                skin.putpixel((x, y), BLUE_MID)

    # Right arm inner (x=48-51, y=20-31)
    for y in range(20, 32):
        for x in range(48, 52):
            skin.putpixel((x, y), BLUE_DARK)

    # Right arm back (x=52-55, y=20-31)
    for y in range(20, 32):
        for x in range(52, 56):
            skin.putpixel((x, y), BLUE_DARK)

    # Right arm top (x=44-47, y=16-19)
    for y in range(16, 20):
        for x in range(44, 48):
            skin.putpixel((x, y), BLUE_LIGHT)

    # Left arm (x=32-47, y=48-63) - similar pattern
    # Left arm outer (x=32-35, y=52-63)
    for y in range(52, 64):
        for x in range(32, 36):
            skin.putpixel((x, y), BLUE_MID)

    # Left arm front (x=36-39, y=52-63)
    for y in range(52, 64):
        for x in range(36, 40):
            if y >= 60:
                skin.putpixel((x, y), SKIN_TAN)
            else:
                skin.putpixel((x, y), BLUE_MID)

    # Left arm inner (x=40-43, y=52-63)
    for y in range(52, 64):
        for x in range(40, 44):
            skin.putpixel((x, y), BLUE_DARK)

    # Left arm back (x=44-47, y=52-63)
    for y in range(52, 64):
        for x in range(44, 48):
            skin.putpixel((x, y), BLUE_DARK)

    # Left arm top (x=36-39, y=48-51)
    for y in range(48, 52):
        for x in range(36, 40):
            skin.putpixel((x, y), BLUE_LIGHT)

# ============ LEGS ============
# Right leg: x=0-15, y=16-31
# Left leg: x=16-31, y=48-63

def draw_legs():
    """Draw legs - blue with red shoes"""
    # Right leg front (x=4-7, y=20-31)
    for y in range(20, 32):
        for x in range(4, 8):
            if y >= 28:  # Red shoes
                skin.putpixel((x, y), RED)
            else:
                skin.putpixel((x, y), BLUE_MID)
    # Shoe stripe
    skin.putpixel((5, 29), WHITE)
    skin.putpixel((6, 29), WHITE)

    # Right leg outer (x=0-3, y=20-31)
    for y in range(20, 32):
        for x in range(0, 4):
            if y >= 28:
                skin.putpixel((x, y), RED)
            else:
                skin.putpixel((x, y), BLUE_MID)

    # Right leg inner (x=8-11, y=20-31)
    for y in range(20, 32):
        for x in range(8, 12):
            if y >= 28:
                skin.putpixel((x, y), RED)
            else:
                skin.putpixel((x, y), BLUE_DARK)

    # Right leg back (x=12-15, y=20-31)
    for y in range(20, 32):
        for x in range(12, 16):
            if y >= 28:
                skin.putpixel((x, y), RED)
            else:
                skin.putpixel((x, y), BLUE_DARK)

    # Right leg top (x=4-7, y=16-19)
    for y in range(16, 20):
        for x in range(4, 8):
            skin.putpixel((x, y), BLUE_MID)

    # Right leg bottom - shoe sole (x=8-11, y=16-19)
    for y in range(16, 20):
        for x in range(8, 12):
            skin.putpixel((x, y), (80, 80, 80, 255))  # Gray sole

    # LEFT LEG (x=16-31, y=48-63)
    # Left leg front (x=20-23, y=52-63)
    for y in range(52, 64):
        for x in range(20, 24):
            if y >= 60:
                skin.putpixel((x, y), RED)
            else:
                skin.putpixel((x, y), BLUE_MID)
    skin.putpixel((21, 61), WHITE)
    skin.putpixel((22, 61), WHITE)

    # Left leg outer (x=16-19, y=52-63)
    for y in range(52, 64):
        for x in range(16, 20):
            if y >= 60:
                skin.putpixel((x, y), RED)
            else:
                skin.putpixel((x, y), BLUE_MID)

    # Left leg inner (x=24-27, y=52-63)
    for y in range(52, 64):
        for x in range(24, 28):
            if y >= 60:
                skin.putpixel((x, y), RED)
            else:
                skin.putpixel((x, y), BLUE_DARK)

    # Left leg back (x=28-31, y=52-63)
    for y in range(52, 64):
        for x in range(28, 32):
            if y >= 60:
                skin.putpixel((x, y), RED)
            else:
                skin.putpixel((x, y), BLUE_DARK)

    # Left leg top (x=20-23, y=48-51)
    for y in range(48, 52):
        for x in range(20, 24):
            skin.putpixel((x, y), BLUE_MID)

# ============ HAT/HEAD OVERLAY (for fur texture) ============
def draw_overlay():
    """Add overlay layer for fur texture on head"""
    # Hat overlay area: x=32-63, y=0-15
    # This adds spiky fur texture

    # Overlay front (x=40-47, y=8-15)
    # Add some fur spikes on top
    for x in [41, 43, 45]:
        skin.putpixel((x, 8), BLUE_LIGHT)

    # Eyebrow furrows for angry/creepy look
    skin.putpixel((41, 10), BLUE_DARK)
    skin.putpixel((46, 10), BLUE_DARK)

# Build the skin
draw_head_front()
draw_head_sides()
draw_body()
draw_arms()
draw_legs()
draw_overlay()

# Save
output_path = '/home/gh0st/minecraft-custom-project/skins/characters/cursed_sonic_v1.png'
skin.save(output_path)
print(f"Skin saved to: {output_path}")

# Also save to exports
export_path = '/home/gh0st/minecraft-custom-project/skins/exports/cursed_sonic.png'
skin.save(export_path)
print(f"Export saved to: {export_path}")

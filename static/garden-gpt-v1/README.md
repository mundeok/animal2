# Garden and explorer artwork v1

Generated with the built-in GPT image generation tool on 2026-10-13.
Source atlases are preserved here. Runtime PNGs are mechanically cropped and
nearest-neighbor resized from those atlases, not drawn in SVG or Python.
Explorer frames share a 64×80 canvas and aligned foot baseline.

## Generation prompt set

Tiles: A tightly aligned square 4×4 tileset atlas for a top-down children's
nature exploration RPG, original late-1990s handheld pixel-art feel. No text,
gutters or grid. Row 1: four subtle seamless lawn variations. Row 2: same lawn
with white, yellow, pink and lavender flowers. Row 3: four warm tan dirt path
variations. Row 4: bush, rounded deciduous tree, burrow and mixed flower bed.
Cohesive muted greens, warm tan, pastel flowers; crisp pixel clusters; no blur.

Explorer: Transparent 4×4 sprite sheet, same friendly child explorer with blue
cap, red-orange shirt, olive backpack, blue shorts and brown shoes. Rows face
down, left, right and up. Columns are standing, left-foot step, standing and
right-foot step. Identical scale and aligned feet, alternating arms and legs,
compact large-headed handheld pixel-art style. No shadows, text or grid.

## Integration

Garden terrain uses deterministic texture variants and grouped flower patches.
Collision, animal encounters and portal positions are retained.
Walking advances on a continuous 105ms pose clock instead of replaying four
frames and resetting the pose on every tile. Tile travel takes 180ms.
Other habitat terrain and the separate battle trainer illustration are unchanged.

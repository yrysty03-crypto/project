# tools.py

from collections import deque

def flood_fill(surface, x, y, new_color, width, height):
    """Flood fill using BFS"""

    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    queue = deque([(x, y)])

    while queue:
        px, py = queue.popleft()

        if px < 0 or px >= width or py < 0 or py >= height:
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        queue.append((px + 1, py))
        queue.append((px - 1, py))
        queue.append((px, py + 1))
        queue.append((px, py - 1))
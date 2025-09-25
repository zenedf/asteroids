def display_coords(screen, font, obj, color="yellow", offset_y=-40):
    """Display coordinates above any object type.
    
    Args:
        screen: pygame screen surface
        font: pygame font object
        obj: can be a sprite (with .position), pygame.mouse module, or (x,y) tuple
        color: text color (default "yellow")
        offset_y: vertical offset above the object (default -40)
    """
    # Handle different object types
    if hasattr(obj, 'position'):
        # Sprite object with .position attribute
        x, y = obj.position.x, obj.position.y
    elif hasattr(obj, 'get_pos'):
        # pygame.mouse object
        x, y = obj.get_pos()
    elif isinstance(obj, (tuple, list)) and len(obj) == 2:
        # Direct (x, y) coordinates
        x, y = obj
    else:
        # Try to treat as an object with x, y attributes
        try:
            x, y = obj.x, obj.y
        except AttributeError:
            raise ValueError(f"Object {obj} doesn't have recognizable position attributes")
    
    # Create and display the text
    coord_text = f"({int(x)}, {int(y)})"
    text_surface = font.render(coord_text, True, color)
    text_width = text_surface.get_width()
    screen.blit(text_surface, (x - text_width // 2, y + offset_y))
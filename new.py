def percent_to_graph(percent: float, length: int = 20) -> str:
    """
    Converts a percentage (0.0 to 1.0) into a graphical representation of hashes and spaces.

    Args:
        percent (float): Percentage value between 0.0 and 1.0.
        length (int): Length of the graph.

    Returns:
        str: Graphical representation of hashes and spaces.
    """
    # Calculate the number of hashes, using max to ensure it's at least 0
    hashes = int(percent * (length - 2))  # Subtract 2 to account for the brackets
    # Calculate the number of spaces to fill the remaining length
    spaces = length - 2 - hashes  # Remaining space after the hashes
    
    # Ensure spaces is non-negative (in case of large percent values)
    if spaces < 0:
        spaces = 0

    # Return the graphical representation with brackets, ensuring total length is correct
    return f"[{'#' * hashes}{' ' * spaces}]"


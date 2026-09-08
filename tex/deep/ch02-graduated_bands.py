def graduated_bands(routes):
    """Ideal lengths by occurrence; no intensities, efficiencies or gel model."""
    bands = {v: set() for v in range(1, 7)}
    for route in routes:
        if not route or route[0] != START or set(route) - set(VERTICES):
            raise ValueError("routes must begin at 0 and use known vertices")
        for position, vertex in enumerate(route):
            if vertex != START:
                bands[vertex].add(20 * (position + 1))
    return {str(v): sorted(xs) for v, xs in bands.items()}

def hanoi_tower_algorithm(n, x, y, z):
    if n == 1:
        print(f"Diski {x} çubuğundan {z} çubuğuna koy")
    else:
        hanoi_tower_algorithm(n-1, x, z, y)
        hanoi_tower_algorithm(1, x, y, z)
        hanoi_tower_algorithm(n-1, y, x, z)
    # ndisc = Number of Disc
hanoi_tower_algorithm(5, "A", "B", "C")
# TODO: make more patterns
# and draw them in comments
# TODO: make own complex patterns from existing:
# e.g. explosions or population growth patterns etc.
# TODO: save all interesting random generated patterns
# from the running game
patterns = {
    "block": [(0, 0),
              (0, 1),
              (1, 0),
              (1, 1)],

    # Penta-decathlon
    # period: 15
    "penta": [(3, 4),
              (4, 4),
              (6, 4),
              (7, 4),
              (8, 4),
              (9, 4),
              (11, 4),
              (12, 4),
              (5, 3),
              (5, 5),
              (10, 3),
              (10, 5)],

    # Light-weight spaceship
    "lwss": [(0, 1),
             (0, 2),
             (1, 0),
             (1, 1),
             (1, 2),
             (1, 3),
             (2, 0),
             (2, 1),
             (2, 3),
             (2, 4),
             (3, 2),
             (3, 3)]
}

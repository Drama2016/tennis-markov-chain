def prob_win_game(p):
    """
    Probability of winning a service game given p = probability of winning a single point.
    Uses the standard tennis scoring structure (win by 2, deuce at 3-3).
    """
    win_4_0 = p**4
    win_4_1 = 4 * p**4 * (1 - p)
    win_4_2 = 10 * p**4 * (1 - p)**2
    reach_deuce = 20 * p**3 * (1 - p)**3
    win_from_deuce = p**2 / (p**2 + (1 - p)**2)

    return win_4_0 + win_4_1 + win_4_2 + (reach_deuce * win_from_deuce)

def penalize_update_rank_and_xp(rank, xp, penalty):   
    total_points = rank * 100 + xp
    updated_points = total_points - penalty
    if updated_points <= 0:
        new_rank = 0
        new_xp = 0
    elif updated_points > 0:
        new_rank = updated_points // 100
        new_xp = updated_points % 100
    return new_rank, new_xp
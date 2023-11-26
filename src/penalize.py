def penalize_update_rank_and_xp(rank, xp, penalty):   

    deduct_from_rank = penalty // 100
    deduct_from_xp = penalty % 100
           
    new_rank = max(rank - deduct_from_rank, 0)  
    new_xp = xp - deduct_from_xp

    if new_xp < 0 and new_rank == 0:
        new_rank = 0
        new_xp = 0
    elif new_xp < 0 and new_rank > 0:
        new_rank -= 1
        new_xp = 100 - abs(new_xp)
    return new_rank, new_xp

print(penalize_update_rank_and_xp(2, 90, 90)) # (0, 95)
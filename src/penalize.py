def penalize_update_rank_and_xp(rank, xp, penalty):   

    total_points = rank * 100 + xp
    #print(total_points)
    #deduct_from_rank = penalty // 100
    #deduct_from_xp = penalty % 100
    updated_points = total_points - penalty
    #print(updated_points)       
    #new_rank = max(rank - deduct_from_rank, 0)  
    #new_xp = xp - deduct_from_xp
    if updated_points <= 0:
        new_rank = 0
        new_xp = 0
    elif updated_points > 0:
        new_rank = updated_points // 100
        new_xp = updated_points % 100
    # if new_xp < 0 and new_rank == 0:
    #     new_rank = 0
    #     new_xp = 0
    # elif new_xp < 0 and new_rank > 0:
    #     new_rank -= 1
    #     new_xp = 100 - abs(new_xp)
    return new_rank, new_xp

print(penalize_update_rank_and_xp(3, 90, 400)) # (0, 95)
def award_update_rank_and_xp(rank, current_xp, awarded_xp):
    quotient, remainder = divmod(awarded_xp, 100)
    rank += quotient
    current_xp += remainder
    
    if current_xp >= 100:
        quotient, remainder = divmod(current_xp, 100)
        rank += quotient
        current_xp = remainder
    
    return rank, current_xp

rank, current_xp = award_update_rank_and_xp(4, 35, 375)
print("Updated Rank:", rank)
print("Updated Current XP:", current_xp)

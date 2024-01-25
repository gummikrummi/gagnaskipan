def veldi(base, exp): #recursive 
    if exp == 0: #base case
        return 1 #ef veldi er 0 þá er svarið 1
    return base * veldi(base, exp-1) #kallar aftur á sig með minna exp þangað til exp er 0 og þá er svarið 1
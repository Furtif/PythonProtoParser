def formatDefenders(gym_json):
    defenders = []
    fortData = []
    ## Seperate out for the fort Proto for ID, Team##
    FortProto = gym_json['gymStatusAndDefenders']['pokemonFortProto']
    fort_id = getKeyValue(FortProto,'id')
    fort_name = getKeyValue(gym_json,'name')
    fort_team = getKeyValue(FortProto,'ownedByTeam')

    ## Create a dict{} for all the fort data for the final output
    fortDict = {'fort_id': fort_id,'fort_name': fort_name, 'fort_team': fort_team}
    
    ## Create List of the gymDefender Proto responses to iterate over for data ##
    defenderList = gym_json['gymStatusAndDefenders']['gymDefender']
    
    for defender in defenderList:
        tmp = defender['motivatedPokemon']['pokemon']
        pokemon_id = getKeyValue(tmp,'pokemonId')
        owner_name = getKeyValue(tmp,'ownerName')
        nickname = getKeyValue(tmp,'nickname')
        cp = getKeyValue(tmp,'cp')
        stamina = getKeyValue(tmp,'stamina')
        stamina_max = getKeyValue(tmp,'stamina_max')
        atk_iv = getKeyValue(tmp,'individualAttack')
        def_iv = getKeyValue(tmp,'individualDefense')
        sta_iv = getKeyValue(tmp,'individualStamina')
        move1 = getKeyValue(tmp,'move1')
        move2 = getKeyValue(tmp,'move2')
        battles_attacked = getKeyValue(tmp,'battles_attacked')
        battles_defended = getKeyValue(tmp,'battles_defended')
        num_upgrades = getKeyValue(tmp, 'num_upgrades')

        defenderDict = {"pokemon_id":pokemon_id, "owner_name":owner_name, "nickname":nickname, "cp":cp, "stamina":stamina,
                        "stamina_max":stamina_max, "atk_iv":atk_iv, "def_iv":def_iv, "sta_iv":sta_iv, "move1":move1, "move2":move2, \
                        "battles_attacked":battles_attacked, "battles_defended":battles_defended,"num_upgrades":num_upgrades}

        defenders.append(defenderDict)

    defenderCount = len(defenders)
    out = { 'fortData': fortDict, 'defenderCount': defenderCount, 'defenderData': defenders}
    return(out)

import json
import random
import os


allowed_moves = [1, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33,
                34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
                 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89,
                 90, 91, 92, 93, 94, 95, 97, 98, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 113, 114,
                 115, 116, 118, 120, 122, 123, 124, 126, 127, 129, 133, 135, 136, 137, 138, 139, 141, 143, 144, 147,
                 150, 151, 152, 153, 154, 156, 157, 160, 161, 162, 163, 164, 165, 166, 167, 168, 172, 173, 174, 175,
                 176, 177, 178, 179, 180, 181, 182, 183, 184, 186, 187, 188, 189, 191, 192, 194, 195, 196, 197, 198,
                 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 217, 219, 220,
                 221, 223, 224, 225, 226, 227, 229, 230, 231, 232, 234, 235, 236, 238, 239, 240, 241, 242, 243, 244,
                 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 262, 263, 264, 266,
                 268, 269, 270, 271, 272, 273, 275, 276, 278, 280, 281, 282, 283, 284, 285, 286, 291, 292, 294, 295,
                 296, 297, 298, 299, 303, 304, 305, 306, 307, 308, 309, 310, 311, 313, 314, 315, 317, 319, 321, 322,
                 323, 325, 326, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344,
                 345, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 359, 360, 361, 362, 364, 365, 366, 367, 368,
                 369, 370, 371, 372, 374, 379, 380, 383, 384, 385, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396,
                 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416,
                 417, 418, 419, 420, 421, 422, 423, 424, 425, 427, 428, 430, 432, 433, 434, 435, 436, 437, 438, 439,
                 440, 441, 442, 444, 446, 447, 449, 450, 451, 452, 453, 454, 455, 457, 458, 459, 460, 461, 463, 467,
                 468, 469, 470, 471, 472, 473, 474, 476, 478, 479, 482, 483, 484, 486, 487, 488, 489, 490, 491, 492,
                 493, 494, 495, 496, 497, 499, 500, 501, 502, 503, 504, 505, 506, 508, 509, 510, 511, 512, 513, 514,
                 515, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 532, 533, 534, 535, 538, 539,
                 540, 541, 542, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 562, 564, 565,
                 566, 568, 570, 571, 572, 573, 574, 575, 576, 577, 580, 581, 583, 584, 585, 586, 587, 589, 590, 591,
                 592, 593, 594, 595, 596, 597, 598, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 618, 619, 620,
                 621, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 672, 675, 676, 678, 679, 680, 681,
                 682, 683, 684, 686, 688, 689, 690, 691, 692, 693, 694, 705, 706, 707, 709, 710, 711, 713, 714, 715,
                 716, 722, 744, 745, 746, 747, 748, 749, 750, 751, 752, 756, 775, 776, 777, 778, 780, 781, 782, 783,
                 784, 785, 786, 787, 788, 789, 790, 791, 793, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806,
                 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826,
                 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846,
                 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866,
                 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886,
                 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906,
                 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919]


banned_pokemon = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 29, 30, 31, 32, 33, 34, 35, 41, 42, 46, 47, 63,
                  64, 65, 66, 67, 77, 78, 83, 95, 98, 99, 104, 105, 108, 114, 115, 118, 119, 120, 121, 122, 124, 127,
                  138, 139, 140, 141, 142, 165, 166, 169, 175, 176, 177, 178, 201, 202, 208, 213, 222, 223, 224, 226,
                  238, 241, 251, 263, 264, 265, 266, 267, 268, 269, 276, 277, 290, 291, 292, 293, 294, 295, 300, 301,
                  303, 304, 305, 306, 309, 310, 315, 318, 319, 320, 321, 327, 337, 338, 343, 344, 345, 346, 347, 348,
                  351, 352, 359, 360, 363, 364, 365, 366, 367, 368, 369, 399, 400, 406, 407, 412, 413, 414, 420, 421,
                  427, 428, 431, 432, 439, 441, 451, 452, 455, 458, 463, 465, 468, 494, 504, 505, 506, 507, 508, 509,
                  510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 524, 525, 526, 527, 528, 531, 535, 536,
                  537, 538, 539, 543, 544, 545, 554, 555, 556, 557, 558, 561, 562, 563, 564, 565, 566, 567, 568, 569,
                  582, 583, 584, 587, 588, 589, 592, 593, 597, 598, 599, 600, 601, 605, 606, 616, 617, 618, 621, 626,
                  631, 632, 649, 659, 660, 674, 675, 676, 679, 680, 681, 682, 683, 684, 685, 688, 689, 694, 695, 696,
                  697, 698, 699, 710, 711, 716, 717, 718, 746, 755, 756, 759, 760, 767, 768, 771, 772, 773, 776, 777,
                  780, 781, 785, 786, 787, 788, 793, 794, 795, 796, 797, 798, 799, 802, 803, 804, 805, 806, 807, 808,
                  809, 824, 825, 826, 827, 828, 829, 830, 831, 832, 835, 836, 850, 851, 852, 853, 864, 865, 866, 867,
                  880, 881, 882, 883]
# abilities are any number between 1 and 298, inclusive
banned_abilities = [278, 307]  # Zero to Hero and Tera Shift banned
randomize_abilities = 0
randomize_moves = 0


def check_banned_ability(index):
    if index in banned_abilities:
        return True
    return False


# Double check this function to ensure other forms are added later on
def get_alt_form(index: int):
    has_alt = [25,  # pikachu
                26, #raichu
                27, #sandshrew
                28, #sandslash
               29, #vulpix
               30, #ninetails
                50, #diglett
                51, #dugtrio
                52, #meowth, has two
                53, #persian
                58, #growlithe
                59, #arcanine
               74,  #geodude
               75,  #graveler
               76,  #golem
                79, #slowpoke
                80, #slowbro, seems to be form id 2
                88, #grimer
                89, #muk
                100, #voltorb
                101, #electrode
               103,  #exeggutor
               110,  # weezing
                128, #tauros, 3 form possible 1 2 3
                144, #articuno
                145, #zapdos
                146, #moltres
                157, #typhlosion
                194, #wooper
                199, #slowking
                211, #qwilfish
                215, #sneasel
               386,  #Deoxys
                422, #shellos
                423, #gastrodon
                479, #rotom: 5 forms 0 1 2 3 4 5
                483, #dialga
                484, #palkia
                487, #giratina
               492,  #shaymin
               493,  #arceus
                503, #samurott
                549, #lilligant
                550, #basculin
                570, #zorua
                571, #zoroark
               585,  #deerling
               586,  #sawsbuck
                628, #braviary
                641, #tornadus
                642, #thundurus
                645, #landorus
               646,  #Kyurem
                648, #meloetta
               658,  # greninja - added for future proofing and not forget it
               664,  #scatterbug
               665,  #sweppa
               666,  #vivillon - flabebe/floette/florges 0-4 (floette 5 but ot present)
               669,  #flabebe
               670,  #floette - 5 is eternal flower not in game
               671,  #florges
               678,  # meowstic
                705, #sligoo
                706, #goodra
                713, #avalugg
                720, #hoopa
                724, #decidueye
                741, #oricorio, 3 forms 0 1 2 3
                744, #rockruff
                745, #lycanroc: 2 forms 0 1 2
               774,  #minior
               778,  #mimikyu
               800,  #necrozma: 2 - 3 not in game
               801,  #magearna
               845,  #cramorant
                849, #toxtricity
               854,  #sineastea
               855,  # plteageist
               869,  #alcremie 8 forms
               875,  #Eiscue
               876,  #indeedee
               877,  #morpeko
               888,  #Zacian
               889,  #Zamazenta
                892, #urshifu
                893, #zarude
                898, #calyrex, 2 forms 0 1 2
               901,  #Ursaluna
               902,  #basculegion
               905,  #enamorus
               916,  #Oinkolonge
               917,  #Dudunsparce
               934,  #Palafin
               946,  #Mausehold
               952,  #tatsugiri: 2 forms 0 1 2
               960,  #squakabily: 3 forms 0 1 2 3
               976,  #gimmighoul - 998 koraidon test, 999 miraidon test [0-4]
               1011, #ogerpon - 0 [Teal], 1[wellspring], 2[heartflame], 3[rock]; 4-7 is teraform
               1021, #terapagos
               1024, #poltchageist
               1025, #sinistcha
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 25:
                choice = random.randint(0, 9)
                # form 8 not in the game (Partner Let's Go Pikachu)
                while choice == 8:
                    choice = random.randint(0, 9)
                return choice
            case 52:
                choice = random.randint(0, 2)
                return choice
            case 80:
                choice = random.randint(0, 2)
                # form 1 not in the game (Mega Slowbro)
                while choice == 1:
                    choice = random.randint(0, 2)
                return choice
            case 128:
                choice = random.randint(0, 3)
                return choice
            case 386:
                choice = random.randint(0, 3)
                return choice
            case 479:
                choice = random.randint(0, 5)
                return choice
            case 493:
                choice = random.randint(0, 17)
                return choice
            case 550:
                choice = random.randint(0, 2)
                return choice
            case 585:
                choice = random.randint(0, 3)
                return choice
            case 586:
                choice = random.randint(0, 3)
                return choice
            case 646:
                choice = random.randint(0, 2)
                return choice
            case 664:
                choice = random.randint(0, 19)
                return choice
            case 665:
                choice = random.randint(0, 19)
                return choice
            case 666:
                choice = random.randint(0, 19)
                return choice
            case 669:
                choice = random.randint(0, 4)
                return choice
            case 670:
                choice = random.randint(0, 5)
                while choice == 5:
                    choice = random.randint(0, 5)
                return choice
            case 671:
                choice = random.randint(0, 4)
                return choice
            case 741:
                choice = random.randint(0, 3)
                return choice
            case 745:
                choice = random.randint(0, 2)
                return choice
            case 774: # includes shield downs form
                choice = random.randint(0, 13)
                return choice
            case 800:
                choice = random.randint(0, 3)
                while choice == 3:
                    choice = random.randint(0, 3)
                return choice
            case 845:
                choice = random.randint(0, 2)
                return choice
            case 869:
                choice = random.randint(0, 8)
                return choice
            case 898:
                choice = random.randint(0, 2)
                return choice
            case 952:
                choice = random.randint(0, 2)
                return choice
            case 960:
                choice = random.randint(0, 3)
                return choice
            case 1011:
                choice = random.randint(0, 3)
                return choice
            case _:
                choice = random.randint(0, 1)
                return choice
    else:
        return 0


def randomizeAbilities(pokemon):
    if pokemon['is_present'] is True:
        if pokemon['species']['species'] == 934:
            choice = random.randint(1, 310)
            while check_banned_ability(choice) is True:
                choice = random.randint(1, 298)
            pokemon['ability_hidden'] = choice
        elif pokemon['species']['species'] == 1021 and pokemon['species']['form'] != 0:
            i = 1
            while i < 4:
                choice = random.randint(1, 310)
                while check_banned_ability(choice) is True:
                    choice = random.randint(1, 310)
                else:
                    if i != 3:
                        pokemon["ability_" + str(i)] = choice
                    else:
                        pokemon['ability_hidden'] = choice
                    i = i + 1
        elif pokemon['species']['species'] == 1021 and pokemon['species']['form'] == 0:
            pass
        else:
            i = 1
            while i < 4:
                choice = random.randint(1, 310)
                while check_banned_ability(choice) is True:
                    choice = random.randint(1, 310)
                else:
                    if i != 3:
                        pokemon["ability_" + str(i)] = choice
                    else:
                        pokemon['ability_hidden'] = choice
                    i = i + 1
    return pokemon


def randomizeMoveset(pokemon):
    current_moveset = []
    if pokemon['is_present'] is True:
        for move in pokemon['levelup_moves']:
            index = random.randint(0, len(allowed_moves) - 1)
            if allowed_moves[index] not in current_moveset:
                move['move'] = allowed_moves[index]
                current_moveset.append(allowed_moves[index])

    return pokemon


def randomizeTypes(pokemon):
    if pokemon['is_present'] is True:
        pokemon['type_1'] = random.randint(0, 17)
        pokemon['type_2'] = random.randint(0, 17)

    return pokemon


def randomizeEvolutions(pokemon):
    for evo in pokemon['evolutions']:
        choice = random.randint(1, 1025)
        while choice in banned_pokemon:
            choice = random.randint(1, 1025)
        evo['species'] = choice
        evo['form'] = get_alt_form(choice)

    return pokemon


def forceTeraBlast(pokemon):
    teraBlastForced = {
        "move": 851,
        "level": 5
    }
    pokemon['levelup_moves'].append(teraBlastForced)

    currentlevel = 5
    while currentlevel < 105:
        teraBlastForced["level"] = teraBlastForced["level"] + 5
        pokemon['levelup_moves'].append(teraBlastForced)
        currentlevel = currentlevel + 5

    return pokemon

def randomizeEvolutionsEveryLevel():
    template_evolution = {
        "level": 0,
        "condition": 0,
        "parameter": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "species": 0,
        "form": 0
    }

    evoList = []
    for i in range(1, 101):
        template_evolution['level'] = i
        template_evolution['condition'] = 4
        species_choice = random.randint(1, 1025)
        while species_choice in banned_pokemon:
            species_choice = random.randint(1, 1025)
        template_evolution['species'] = species_choice
        template_evolution['form'] = get_alt_form(species_choice)
        evoList.append(template_evolution)

        template_evolution = {
            "level": 0,
            "condition": 0,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 0,
            "form": 0
        }

    return evoList


# To be completed - Trying to figure out how to keep
# same total.
def randomizeBaseStatsWeighted(pokemon):
    total = 0
    total = total + pokemon['base_stats']['hp']
    total = total + pokemon['base_stats']['atk']
    total = total + pokemon['base_stats']['def']
    total = total + pokemon['base_stats']['spa']
    total = total + pokemon['base_stats']['spd']
    total = total + pokemon['base_stats']['spe']

    if pokemon['species']['species'] == 0:
        return pokemon
    # add hard check for shedninja once back in the game
    # to have it hard coded to 1 for HP
    newstats = [15]*6
    total = total - (15*6)

    # Loop to ensure all stats are always correctly randomized
    randomizeStats = True
    while randomizeStats:
        statschecked = []
        while total != 0:
            no_infite_loop = 1
            checktotal = total
            changinStat = random.randint(0,5)

            while changinStat in statschecked:
                changinStat = random.randint(0, 5)
                if no_infite_loop == 6:
                    break
                no_infite_loop = no_infite_loop + 1
            if no_infite_loop == 6:
                break

            statschecked.append(changinStat)

            new_base_stat = random.randint(0, 240)
            while checktotal - new_base_stat < 0:
                new_base_stat = random.randint(0, total)
            while newstats[changinStat] + new_base_stat > 255:
                new_base_stat = random.randint(0, 240)

            newstats[changinStat] = newstats[changinStat] + new_base_stat
            total = total - new_base_stat
            if total == 0:
                randomizeStats = False

    pokemon['base_stats']['hp'] = newstats[0]
    pokemon['base_stats']['atk'] = newstats[1]
    pokemon['base_stats']['def'] = newstats[2]
    pokemon['base_stats']['spa'] = newstats[3]
    pokemon['base_stats']['spd'] = newstats[4]
    pokemon['base_stats']['spe'] = newstats[5]

    return pokemon


def randomizeBaseStatsTotal(pokemon):
    pokemon['base_stats']['hp'] = random.randint(15, 255)
    pokemon['base_stats']['atk'] = random.randint(15, 255)
    pokemon['base_stats']['def'] = random.randint(15, 255)
    pokemon['base_stats']['spa'] = random.randint(15, 255)
    pokemon['base_stats']['spd'] = random.randint(15, 255)
    pokemon['base_stats']['spe'] = random.randint(15, 255)

    return pokemon


def randomize(config, configglobal):
    file = open(os.getcwd() + "/Randomizer/PersonalData/" +"personal_array_clean.json", "r")
    data = json.load(file)
    file.close()

    if config['ban_wonder_guard'] == "yes":
        banned_abilities.append(25)

    for pokemon in data['entry']:
        if config['randomize_stats_with_same_total'] == "yes":
            pokemon = randomizeBaseStatsWeighted(pokemon)
        if config['randomize_stats_with_different_total'] == "yes":
            pokemon = randomizeBaseStatsTotal(pokemon)
        if config['randomize_abilities'] == "yes":
            pokemon = randomizeAbilities(pokemon)
        if config['randomize_movesets'] == "yes":
            pokemon = randomizeMoveset(pokemon)
        if config['randomize_evolutions'] == "yes" and configglobal['limit_generation']['evolution_limiter'] == "no":
            pokemon = randomizeEvolutions(pokemon)
        if config['let_pokemon_evolve_every_level'] == "yes" and configglobal['limit_generation']['evolution_limiter'] == "no":
            pokemon['evolutions'] = randomizeEvolutionsEveryLevel()
        if config['randomize_types'] == "yes":
            pokemon = randomizeTypes(pokemon)
        pokemon = forceTeraBlast(pokemon)

    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/PersonalData/" +"personal_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation Of Stats/Abilities/Moves/Evos Done !")


def main():
    randomize()


if __name__ == "__main__":
    main()
    
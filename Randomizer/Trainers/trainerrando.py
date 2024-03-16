import csv
import json
import random
import os

def fetch_devname(index: int, csvdata):
    #print(csvdata[index])
    return str.strip(csvdata[index])

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


legends = [144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480,
           481, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646,
           647, 648, 649, 716, 717, 718, 719, 720, 721, 785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808,
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 994, 995, 996, 997, 998, 999, 1011, 1014,
           1015, 1016, 1021, 1022]
paradox = [978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 998, 999, 1021,
           1017, 1018, 1019, 1020]
legends_and_paradox = [
           144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480,
           481, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646,
           647, 648, 649, 716, 717, 718, 719, 720, 721, 785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808,
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 978, 979, 980, 981, 982, 983, 984, 985, 986,
           987, 988, 989, 990, 991, 992, 993, 1017, 1018, 1019, 1020, 994, 995, 996, 997, 998, 999, 1011, 1014, 1015,
           1016, 1021, 1022]
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
tera_types = ['normal', 'kakutou', 'hikou', 'doku', 'jimen', 'iwa', 'mushi', 'ghost', 'hagane', 'honoo', 'mizu', 'kusa',
              'denki', 'esper', 'koori', 'dragon', 'aku', 'fairy', 'niji']
average_level = 0

'''
normal = normal
kakutou = fightning
hikou = flying
doku = poison
jimen = ground
iwa = rock
mushi = bug
ghost = ghost
hagane = steel
honoo = fire
mizu = water
kusa = grass
denki = electric
esper = psychic
koori = ice
dragon = dragon
aku = dark
fairy = fairy (yousei everywhere else)
niji = stellar
'''

# trid == rival_01_hono
# ...._kusa
# ...._mizu


def make_poke(pokeEntry, index: str, csvdata, config, beginner: bool):
    chosenmon = random.randint(1, 1025)
    while chosenmon in banned_pokemon:
        chosenmon = random.randint(1, 1025)
    if config['only_legends'] == "yes":
        chosenmon = legends[random.randint(0, len(legends)-1)]
        while chosenmon in banned_pokemon:
            chosenmon = legends[random.randint(0, len(legends) - 1)]
    if config['only_paradox'] == "yes":
        chosenmon = paradox[random.randint(0, len(paradox)-1)]
        while chosenmon in banned_pokemon:
            chosenmon = paradox[random.randint(0, len(paradox) - 1)]
    if config['only_legends_and_paradoxes'] == "yes":
        chosenmon = legends_and_paradox[random.randint(0, len(legends_and_paradox)-1)]
        while chosenmon in banned_pokemon:
            chosenmon = legends_and_paradox[random.randint(0, len(legends_and_paradox) - 1)]

    while chosenmon in banned_pokemon:
        chosenmon = random.randint(1, 1025)
    pokeEntry['poke' + index]['devId'] = fetch_devname(chosenmon, csvdata)
    alt_form_choosen = get_alt_form(chosenmon)
    pokeEntry['poke' + index]['formId'] = alt_form_choosen
    pokeEntry['poke' + index]['sex'] = "DEFAULT"
    pokeEntry['poke' + index]['level'] = pokeEntry['poke1']['level']
    if beginner is False:
        choice = random.randint(1,4)
        pokeEntry['poke' + index]['level'] = pokeEntry['poke'+ index]['level'] + choice
    pokeEntry['poke' + index]['wazaType'] = "DEFAULT"
    pokeEntry['poke' + index]['waza1']['wazaId'] = "WAZA_TERABAASUTO"
    pokeEntry['poke' + index]['waza2']['wazaId'] = "WAZA_NULL"
    pokeEntry['poke' + index]['waza3']['wazaId'] = "WAZA_NULL"
    pokeEntry['poke' + index]['waza4']['wazaId'] = "WAZA_NULL" #6 mons on gyms, elite 4 champ
    if config['force_perfect_ivs'] == "yes":
        talentvalue = {
            "hp": 31,
            "atk": 31,
            "def": 31,
            "spAtk": 31,
            "spDef": 31,
            "agi": 31
        }
        pokeEntry['poke' + index]['talentValue'] = talentvalue
    if config['randomize_fixed_tera_type'] == "yes" and pokeEntry['poke' + index]['gemType'] != "DEFAULT":
        pokeEntry['poke' + index]['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()
    if config['randomize_all_tera_type'] == "yes":
        pokeEntry['poke' + index]['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()
    if config['allow_trainers_shiny_pokemon'] == "yes":
        shinychance = random.randint(0, 15)
        if shinychance == 7:
            pokeEntry['poke' + index]['rareType'] = "RARE"
        else:
            pokeEntry['poke' + index]['rareType'] = "NO_RARE"

    # Add check for ogerpon later
    match chosenmon:
        case 1011:
            match alt_form_choosen:
                case 0:
                    pokeEntry['poke' + index]['gemType'] = "KUSA"
                    pass
                case 1:
                    pokeEntry['poke' + index]['gemType'] = "MIZU"
                    pass
                case 2:
                    pokeEntry['poke' + index]['gemType'] = "HONOO"
                    pass
                case 3:
                    pokeEntry['poke' + index]['gemType'] = "IWA"
                    pass
        case 1021:
            pokeEntry['poke' + index]['gemType'] = "NIJI"


# "trid": "raid_assist_NPC_1", - skip them if wanted (for sure for double battles though) [for 1.0.6]
def randomize(config):
    #load information
    file = open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/Trainers/" +"pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    for entry in data['values']:
        # Counter to see how many pokemon there are to randomize originally
        counter = 1
        for j in range(0, 6):
            t = j+1
            if entry['poke' + str(t)]['devId'] != "DEV_NULL":
                counter = counter + 1
        pokemon_to_randomize = counter

        if config['give_trainers_extra_mons'] == "yes":
            new_counter = 1
            # Counter to see how many free slots there are
            for j in range(2, 6):
                if entry['poke' + str(j)]['devId'] == "DEV_NULL":
                    new_counter = new_counter + 1
            # If none then just randomize all 6
            if new_counter == 0:
                pokemon_to_randomize = 6
            else:
                # if some then choose a random number between 1 and itself
                pokemon_to_randomize = random.randint(1, new_counter)
                pokemon_to_randomize = pokemon_to_randomize + counter
                if pokemon_to_randomize > 6:
                    pokemon_to_randomize = 6
        if config['force_6_pokemons_on_trainers'] == "yes":
            # If user wants all 6 then set to all 6
            pokemon_to_randomize = 6

        # a way to prevent any errors
        beginner = False
        if pokemon_to_randomize > 6:
            pokemon_to_randomize = 6
        elif pokemon_to_randomize < 1:
            # get exact number if its less than 1 (should never happen)
            counter = 1
            for j in range(0, 6):
                t = j + 1
                if entry['poke' + str(t)]['devId'] != "DEV_NULL":
                    counter = counter + 1
            pokemon_to_randomize = counter

        if entry['trid'] == "rival_01_hono" or entry['trid'] == "rival_01_kusa" or entry['trid'] == "rival_01_mizu":
            pokemon_to_randomize = 1
            beginner = True

        i = 1
        while i <= pokemon_to_randomize:
            make_poke(entry, str(i), csvdata, config, beginner)
            i = i + 1

        if config['make_ai_smart_for_all_trainers'] == "yes" and beginner is False:
            entry['aiBasic'] = True
            entry['aiHigh'] = True
            entry['aiExpert'] = True
            entry['aiChange'] = True
        if config['allow_all_trainers_to_terastalize'] == "yes" and beginner is False:
            entry['changeGem'] = True
        if "raid_assist_NPC" not in entry['trid']:
            if config['randomnly_choose_single_or_double'] == "yes" and beginner is False:
                battleformat = random.randint(1, 2)
                if battleformat == 2 and pokemon_to_randomize < 2:
                    make_poke(entry, str(2), csvdata, config, beginner)
                if battleformat == 2:
                    entry['aiDouble'] = True
                type_of_battle = f"_{battleformat}vs{battleformat}"
                entry['battleType'] = type_of_battle
            if config['only_double'] == "yes" and beginner is False:
                entry['battleType'] = "_2vs2"
                entry['aiDouble'] = True
                if pokemon_to_randomize < 2:
                    make_poke(entry, str(2), csvdata, config, beginner)

    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation of Trainers done !")


def main():
   randomize()


if __name__ == "__main__":
    main()

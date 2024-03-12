import csv
import json
import random
import os

def fetch_devname(index: int, csvdata):
    #print(csvdata[index])
    return str.strip(csvdata[index])

def get_alt_form(index: int):
    has_alt = [26, #raichu
    50, #diglett
    51, #dugtrio
    52, #meowth, has two
    53, #persian
    58, #growlithe
    59, #arcanine
    79, #slowpoke
    80, #slowbro, seems to be form id 2
    88, #grimer
    89, #muk
    100, #voltorb
    101, #electrode
    128, #tauros, 3 form possible 1 2 3
    144, #articuno
    145, #zapdos
    146, #moltres
    157, #typhlosion
    194, #wooper
    199, #slowking
    211, #qwilfish
    215, #sneasel
    422, #shellos
    423, #gastrodon
    479, #rotom: 5 forms 0 1 2 3 4 5
    483, #dialga: force it to be origin
    484, #palkia: force it to be origin
    487, #giratina
    #fuck arceus
    503, #samurott
    549, #lilligant
    550, #basculin, form 2
    570, #zorua
    571, #zoroark
    #fuck deerling
    628, #braviary
    641, #tornadus
    642, #thundurus
    645, #landorus
    648, #meloetta
    705, #sligoo
    706, #goodra
    713, #avalugg
    720, #hoopa
    724, #decidueye
    741, #oricorio, 3 forms 0 1 2 3
    744, #rockruff
    745, #lycanroc: 2 forms 0 1 2
    849, #toctricity
    892, #urshifu
    893, #zarude
    898, #calyrex, 2 forms 0 1 2 
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 52:
                choice = random.randint(0, 2)
                #forms = [1, 2]
                return choice
            case 80:
                choice = random.randint(0, 100)
                if choice < 49:
                    return 2
                else:
                    return 0
            case 128:
                choice = random.randint(0, 3)
                #forms = [0,1,2,3]
                #choice = [0] #only base tauros is not present
                #form_index = form_index + 1
                return choice
            case 194:
                choice = random.randint(0, 100)
                if choice < 49:
                    return 1
                else:
                    return 0
                #return [0] #base wooper is not in the encounter table
            case 479:
                choice = random.randint(0,5)
                forms = [1,2,3,4,5]
                return choice
            case 550:
                choice = random.randint(0, 100)
                if choice < 49:
                    return 2
                else:
                    return 0
            case 745: #all forms already in the table
                 choice = random.randint(0, 2)
            #    forms = [0,1,2]
            #    choice = forms[form_index]
            #    form_index = form_index + 1
                 return choice
            case 898:
                choice = random.randint(0, 2)
                #forms = [1,2]
                return choice
            case _:
                choice = random.randint(0, 100)
                if choice < 49:
                    return 0
                else:
                    return 1
    else:
        return  0


banned_pokemon = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 29, 30, 31, 32, 33, 34, 35, 41, 42, 46, 47, 63,
                  64, 65, 66, 67, 77, 78, 83, 95, 98, 99, 104, 105, 108, 114, 115, 118, 119, 120, 121, 122, 124, 127,
                  138, 139, 140, 141, 142, 165, 166, 169, 175, 176, 177, 178, 201, 202, 208, 213, 222, 223, 224, 226,
                  238, 241, 251, 263, 264, 265, 266, 267, 268, 269, 276, 277, 290, 291, 292, 293, 294, 295, 300, 301,
                  303, 304, 305, 306, 309, 310, 315, 318, 319, 320, 321, 327, 337, 338, 343, 344, 345, 346, 347, 348,
                  351, 352, 359, 360, 363, 364, 365, 366, 367, 368, 369, 399, 400, 406, 407, 412, 413, 414, 420, 421,
                  427, 428, 431, 432, 439, 441, 451, 452, 455, 458, 463, 465, 468, 494, 504, 505, 506, 507, 508, 509,
                  510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 524, 525, 526, 527, 528, 531, 526, 537,
                  538, 539, 543, 544, 545, 554, 555, 556, 557, 558, 561, 562, 563, 564, 565, 566, 567, 568, 569, 582,
                  583, 584, 587, 588, 589, 592, 593, 597, 598, 599, 600, 601, 605, 606, 616, 617, 618, 621, 626, 631,
                  632, 649, 659, 660, 674, 675, 676, 679, 680, 681, 682, 683, 684, 685, 688, 689, 694, 695, 696, 697,
                  698, 699, 710, 711, 716, 717, 718, 746, 755, 756, 759, 760, 767, 768, 771, 772, 773, 776, 777, 780,
                  781, 785, 786, 787, 788, 793, 794, 795, 796, 797, 798, 799, 802, 803, 804, 805, 806, 807, 808, 809,
                  824, 825, 826, 827, 828, 829, 830, 831, 832, 835, 836, 850, 851, 852, 853, 864, 865, 866, 867, 880,
                  881, 882, 883]
tera_types = ['normal', 'kakutou', 'hikou', 'doku', 'jimen', 'iwa', 'mushi', 'ghost', 'hagane', 'honoo', 'mizu', 'kusa',
              'denki', 'esper', 'koori', 'dragon', 'aku', 'fairy', 'niji']
average_level = 0

# trid == rival_01_hono
# ...._kusa
# ...._mizu


def make_poke(pokeEntry, index: str, csvdata, config, beginner: bool):
    chosenmon = random.randint(1, 1025)
    while chosenmon in banned_pokemon:
        chosenmon = random.randint(1, 1025)
    pokeEntry['poke' + index]['devId'] = fetch_devname(chosenmon, csvdata)
    pokeEntry['poke' + index]['formId'] = get_alt_form(chosenmon)
    pokeEntry['poke' + index]['sex'] = "DEFAULT"
    if beginner is False:
        pokeEntry['poke' + index]['level'] = pokeEntry['poke'+ index]['level'] + 3
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

    # Add check for ogerpon later
    if chosenmon == 1021:
        pokeEntry['poke' + index]['gemType'] = 'NIJI'


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
            if entry['poke' + str(t)] != "DEV_NULL":
                counter = counter + 1
        pokemon_to_randomize = counter

        if config['force_6_pokemons_on_trainers'] == 'no' and config['give_trainers_extra_mons'] == "yes":
            new_counter = 1
            # Counter to see how many free slots there are
            for j in range(2, 6):
                if entry['poke' + str(j)] == "DEV_NULL":
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
        elif config['force_6_pokemons_on_trainers'] == "yes":
            # If user wants all 6 then set to all 6
            pokemon_to_randomize = 6

        # a way to prevent any errors
        beginner = False
        if pokemon_to_randomize > 6 or pokemon_to_randomize < 1:
            pokemon_to_randomize = 6

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
        if config['randomnly_choose_single_or_double'] == "yes" and beginner is False:
            battleformat = random.randint(1, 2)
            if battleformat == 2 and pokemon_to_randomize < 2:
                make_poke(entry, str(2), csvdata, config, beginner)
            type_of_battle = f"_{battleformat}vs{battleformat}"
            entry['battleType'] = type_of_battle
        if config['only_double'] == "yes" and beginner is False:
            entry['battleType'] = "_2vs2"
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

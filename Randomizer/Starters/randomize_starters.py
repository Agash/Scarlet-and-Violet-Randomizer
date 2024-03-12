import json
import random
import os
import shutil

picked_starters = []
tera_types = ['normal','kakutou', 'hikou', 'doku', 'jimen', 'iwa', 'mushi', 'ghost', 'hagane', 'honoo', 'mizu', 'kusa',
              'denki', 'esper', 'koori', 'dragon', 'aku', 'fairy', 'niji']
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


def fetch_devname(index: int, csvdata):
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
        return 0


def flip_starter_texture(starter_num: int):
    file = open(os.getcwd() + "/Randomizer/Starters/" +"pokemon_to_file.txt", "r")
    names = []
    for name in file:
        names.append(name)
    pokemon_file = fetch_devname(starter_num, names)
    print(starter_num)
    print(pokemon_file)
    # _00 - male
    # _01 - female
    # _51 and _52 - mega/primal forms
    # _61 - Alolan Form
    # _81 - GMAX form
    # _XX_31 - Galarian form
    # _XX_41 - Hisuian
    # _XX_51 - Paldean
    # _71_XX - Noble
    # --------------- 1X is only for non-regional forms
    # _11 - form0
    # _12 - form1
    # _13 - form2
    # _14 - form3
    # _XY - formZ./pokemon_clean/{pokemon_file}
    # Copies files of pokemon needed. Right now gets all - later only form specific
    shutil.copytree(os.getcwd() + "\\Randomizer\\Starters\\" +f'pokemon_clean\\{pokemon_file}',
                 os.getcwd() + "\\Randomizer\\Starters\\" +f'output\\romfs\\pokemon\\data\\{pokemon_file}')
    current_check = os.getcwd() + "\\Randomizer\\Starters\\" +f'output\\romfs\\pokemon\\data\\{pokemon_file}'
    i = 0
    for pokemonfolder in os.listdir(current_check):
        # print(pokemonfolder)
        pokemontextures_animations = current_check + "\\" + pokemonfolder

        for files in os.listdir(pokemontextures_animations):
            if "rare" in files:
                # print(files)
                # print(files.replace("_rare", ''))
                replacedfile = files.replace("_rare", '')
                ogfiledir = pokemontextures_animations + "\\" + f'{files}'
                newfiledir =pokemontextures_animations + "\\" + f'{replacedfile}'
                #print(f'OG File Dir: {ogfiledir}')
                #print(f'New File Dir: {newfiledir}')
                shutil.copy2(ogfiledir, newfiledir)


def randomize(config):
    if os.path.exists(os.getcwd() + "\\Randomizer\\Starters\\" +f'output'):
        shutil.rmtree(os.getcwd() + "\\Randomizer\\Starters\\" +f'output')

    file = open(os.getcwd() + "/Randomizer/Starters/" +"eventAddPokemon_array_clean.json", "r")
    data = json.load(file)
    file.close()
    file = open(os.getcwd() + "/Randomizer/Starters/" +"pokemon_to_id.txt", "r")
    names = []
    for name in file:
        names.append(name)
    file.close()
    i = 1
    for entry in data['values']:
        if config['randomize_all_gifts'] == "no":  # only starters
            if "common_0065_" in entry['label']:
                choice = random.randint(1, 1025)
                while choice in banned_pokemon or choice in picked_starters:
                    choice = random.randint(1, 1025)
                if choice not in picked_starters:
                    entry['pokeData']['devId'] = fetch_devname(choice, names)
                    entry['pokeData']['formId'] = get_alt_form(choice)
                    if choice == 1021:
                        entry['pokeData']['gemType'] = "NIJI"

                    if config['all_shiny'] == "yes":
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    elif config['higher_shiny_chance'] == "yes":
                        chance = random.randint(1, 10)
                        if chance == 10:
                            entry['pokeData']['rareType'] = "RARE"
                            if config['shiny_overworld'] == "yes":
                                flip_starter_texture(choice)
                        else:
                            entry['pokeData']['rareType'] = "NO_RARE"
                    picked_starters.append(choice) 
        else:  # everything plus starters
            choice = random.randint(1, 1025)
            while choice in banned_pokemon:
                choice = random.randint(1, 1025)
            if config['all_shiny'] == "yes":
                entry['pokeData']['rareType'] = "RARE"
            elif config['higher_shiny_chance'] == "yes":
                chance = random.randint(0, 10)
                if chance == 10:
                    entry['pokeData']['rareType'] = "RARE"
                else:
                    entry['pokeData']['rareType'] = "NO_RARE"
            entry['pokeData']['devId'] = fetch_devname(choice, names)
            entry['pokeData']['formId'] = get_alt_form(choice)
        if config['randomize_tera_type'] == "yes":
            entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()
        entry['pokeData']['wazaType'] = "DEFAULT"
        entry['pokeData']['waza1']['wazaId'] = "WAZA_NULL"
        entry['pokeData']['waza2']['wazaId'] = "WAZA_NULL"
        entry['pokeData']['waza3']['wazaId'] = "WAZA_NULL"
        entry['pokeData']['waza4']['wazaId'] = "WAZA_NULL"


    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/Starters/" +"eventAddPokemon_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation Of Starter Pokemon Done !")


def main():
   randomize()


if __name__ == "__main__":
    main()

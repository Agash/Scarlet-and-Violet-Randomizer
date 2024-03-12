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
                #choice = random.randint(0, 2)
                forms = [1, 2]
                return forms
            case 80:
                #choice = random.randint(0, 100)
                #if choice < 49:
                return [2]
                #else:
                #    return 0
            case 128:
                #choice = random.randint(0, 3)
                #forms = [0,1,2,3]
                choice = [0] #only base tauros is not present
                #form_index = form_index + 1
                return choice
            case 194:
                return [0] #base wooper is not in the encounter table
            case 479:
                #choice = random.randint(0,5)
                forms = [1,2,3,4,5]
                return forms
            case 550:
                #choice = random.randint(0, 100)
                #if choice < 49:
                return [2]
                #else:
                #    return 0
            #case 745: #all forms already in the table
            #    #choice = random.randint(0, 2)
            #    forms = [0,1,2]
            #    choice = forms[form_index]
            #    form_index = form_index + 1
            #    return choice
            case 898:
                #choice = random.randint(0, 2)
                forms = [1,2]
                return forms
            case _:
                #choice = random.randint(0, 100)
                #if choice < 49:
                #    return 0
                #else:
                return [1]
    else:
        return [0]


# ## Utility functions for biomes ## #
def pick_random_biome1():
    possible_biomes = ["GRASS", "FOREST", "SWAMP", "LAKE", "TOWN", "MOUNTAIN", "BAMBOO", "MINE", "CAVE", "OLIVE",
                       "UNDERGROUND", "RIVER", "ROCKY", "BEACH", "SNOW", "OSEAN", "RUINS", "FLOWER",]
    choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
    chosen_biomes.append(choice)
    return choice


def pick_random_biomerest():
    possible_biomes = ["GRASS", "FOREST", "SWAMP", "LAKE", "TOWN", "MOUNTAIN", "BAMBOO", "MINE", "CAVE", "OLIVE",
                       "UNDERGROUND", "RIVER", "ROCKY", "BEACH", "SNOW", "OSEAN", "RUINS", "FLOWER", "NONE"]
    choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
    while choice in chosen_biomes:
        choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
        if len(chosen_biomes) > 4:
            break
    chosen_biomes.append(choice)
    return choice


def generate_lot_value_for_biome(biome_type: str):
    if biome_type == "NONE":
        return 0
    else:
        return random.randint(1, 50)


def generate_area():
    return(random.sample(range(1, 27), 10))


def generate_area_list():
    return(str(generate_area()).replace('[','"').replace(']','"').replace(' ',''))


# ## Utility function because otherwise, randomize() would be fucked up
def make_template(new_template, index, csvdata, form=0):
    new_template['devid'] = fetch_devname(index, csvdata)
    new_template['formno'] = form
    new_template['minlevel'] = 2
    new_template['maxlevel'] = 99
    new_template['lotvalue'] = random.randint(1, 50)
    new_template['biome1'] = pick_random_biome1()
    new_template['biome2'] = pick_random_biomerest()
    new_template['biome3'] = pick_random_biomerest()
    new_template['biome4'] = pick_random_biomerest()
    new_template['lotvalue1'] = generate_lot_value_for_biome(new_template['biome1'])
    new_template['lotvalue2'] = generate_lot_value_for_biome(new_template['biome2'])
    new_template['lotvalue3'] = generate_lot_value_for_biome(new_template['biome3'])
    new_template['lotvalue4'] = generate_lot_value_for_biome(new_template['biome4'])
    chosen_biomes.clear()
    new_template['area'] = generate_area_list()
    new_template['locationName'] = ""
    new_template['enabletable']['land'] = True
    new_template['enabletable']['up_water'] = True
    new_template['enabletable']['underwater'] = True
    new_template['enabletable']['air1'] = True
    new_template['enabletable']['air2'] = True
    new_template['timetable']['morning'] = True
    new_template['timetable']['noon'] = True
    new_template['timetable']['evening'] = True
    new_template['timetable']['night'] = True
    new_template['flagName'] = ""
    new_template['versiontable']['A'] = True
    new_template['versiontable']['B'] = True
    new_template['bringItem']['itemID'] = "ITEMID_NONE"
    new_template['bringItem']['bringRate'] = 0
    return new_template


# ## Global variables ## #
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
legends = [998, 999, 493, 487, 483, 484, 382, 383, 384, 150, 151, 144, 146, 145, 720, 721, 719, 889, 888, 890, 897, 896, 898, 894, 895, 893]
recreated_species = []
recreated_altforms = []
chosen_biomes = []


### Actual shit going on here ###
def randomize(config):
    # print(os.getcwd())
    # load information
    file = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    # recreate data entries so all mons are present.
    # simplest way of doing it, is to edit all existing entries to have devid's ascending from allowed species, and simply paste another entry with the new ids n shti
    # copy an entry
    template_entry = data['values'][0].copy()

    i = len(data) - 1
    # edit existing entries
    for entry in data['values']:
        # entry['devid'] = fetch_devname(allowed_species[i])
        # entry['sex'] = "DEFAULT"
        recreated_species.append(entry['devid'])
        if entry['formno'] != 0:
            recreated_altforms.append(entry['devid'])
        entry['minlevel'] = 2
        entry['maxlevel'] = 99
        entry['lotvalue'] = random.randint(1, 50)
        entry['biome1'] = pick_random_biome1()
        entry['biome2'] = pick_random_biomerest()
        entry['biome3'] = pick_random_biomerest()
        entry['biome4'] = pick_random_biomerest()
        entry['lotvalue1'] = generate_lot_value_for_biome(entry['biome1'])
        entry['lotvalue2'] = generate_lot_value_for_biome(entry['biome2'])
        entry['lotvalue3'] = generate_lot_value_for_biome(entry['biome3'])
        entry['lotvalue4'] = generate_lot_value_for_biome(entry['biome4'])
        chosen_biomes.clear()
        entry['area'] = generate_area_list()
        entry['locationName'] = ""
        entry['enabletable']['land'] = True
        entry['enabletable']['up_water'] = True
        entry['enabletable']['underwater'] = True
        entry['enabletable']['air1'] = True
        entry['enabletable']['air2'] = True
        entry['timetable']['morning'] = True
        entry['timetable']['noon'] = True
        entry['timetable']['evening'] = True
        entry['timetable']['night'] = True
        entry['flagName'] = ""
        entry['versiontable']['A'] = True
        entry['versiontable']['B'] = True
        entry['bringItem']['itemID'] = "ITEMID_NONE"
        entry['bringItem']['bringRate'] = 0
    # add in mons that were not present previously
    # i shoudl really cleanup this bullshit later
    for index in range(1, 1025):
        if index in banned_pokemon:
            continue
        if config['exclude_legendaries'] == "yes":
            if index in legends:
                pass
            else:
                if fetch_devname(index, csvdata) not in recreated_species:
                    new_template = template_entry.copy()
                    recreated_species.append(fetch_devname(index, csvdata))
                    new_template = make_template(new_template, index, csvdata)
                    data['values'].append(new_template)
                    i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index != 128 and index != 194:
                            break  # NOT ALLOWED !!!
                        else:
                            # print(form_template)
                            data['values'].append(form_template)
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
        else:
            if fetch_devname(index, csvdata) not in recreated_species:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
            forms = get_alt_form(index)
            for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                # so aside from 128 and 194, all 0's should be ignored
                form_template = template_entry.copy()  # gotta copy again the template from the start
                form_template = make_template(form_template, index, csvdata,
                                              form)  # randomize the template before changing the formno
                if form == 0:
                    if index != 128 and index != 194:
                        break  # NOT ALLOWED !!!
                    else:
                        # print(form_template)
                        data['values'].append(form_template)
                else:  # should let pass 0's if correct id's
                    # print(form_template)
                    data['values'].append(form_template)

    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation - Paldea done !")


def randomize_teal(config):
    # print(os.getcwd())
    # load information
    file = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su1_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    # recreate data entries so all mons are present.
    # simplest way of doing it, is to edit all existing entries to have devid's ascending from allowed species, and simply paste another entry with the new ids n shti
    # copy an entry
    template_entry = data['values'][0].copy()

    i = len(data) - 1
    # edit existing entries
    for entry in data['values']:
        # entry['devid'] = fetch_devname(allowed_species[i])
        # entry['sex'] = "DEFAULT"
        recreated_species.append(entry['devid'])
        if entry['formno'] != 0:
            recreated_altforms.append(entry['devid'])
        entry['minlevel'] = 2
        entry['maxlevel'] = 99
        entry['lotvalue'] = random.randint(1, 50)
        entry['biome1'] = pick_random_biome1()
        entry['biome2'] = pick_random_biomerest()
        entry['biome3'] = pick_random_biomerest()
        entry['biome4'] = pick_random_biomerest()
        entry['lotvalue1'] = generate_lot_value_for_biome(entry['biome1'])
        entry['lotvalue2'] = generate_lot_value_for_biome(entry['biome2'])
        entry['lotvalue3'] = generate_lot_value_for_biome(entry['biome3'])
        entry['lotvalue4'] = generate_lot_value_for_biome(entry['biome4'])
        chosen_biomes.clear()
        entry['area'] = generate_area_list()
        entry['locationName'] = ""
        entry['enabletable']['land'] = True
        entry['enabletable']['up_water'] = True
        entry['enabletable']['underwater'] = True
        entry['enabletable']['air1'] = True
        entry['enabletable']['air2'] = True
        entry['timetable']['morning'] = True
        entry['timetable']['noon'] = True
        entry['timetable']['evening'] = True
        entry['timetable']['night'] = True
        entry['flagName'] = ""
        entry['versiontable']['A'] = True
        entry['versiontable']['B'] = True
        entry['bringItem']['itemID'] = "ITEMID_NONE"
        entry['bringItem']['bringRate'] = 0
    # add in mons that were not present previously
    # i shoudl really cleanup this bullshit later
    for index in range(1, 1025):
        if index in banned_pokemon:
            continue
        if config['exclude_legendaries'] == "yes":
            if index in legends:
                pass
            else:
                if fetch_devname(index, csvdata) not in recreated_species:
                    new_template = template_entry.copy()
                    recreated_species.append(fetch_devname(index, csvdata))
                    new_template = make_template(new_template, index, csvdata)
                    data['values'].append(new_template)
                    i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index != 128 and index != 194:
                            break  # NOT ALLOWED !!!
                        else:
                            # print(form_template)
                            data['values'].append(form_template)
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
        else:
            if fetch_devname(index, csvdata) not in recreated_species:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
            forms = get_alt_form(index)
            for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                # so aside from 128 and 194, all 0's should be ignored
                form_template = template_entry.copy()  # gotta copy again the template from the start
                form_template = make_template(form_template, index, csvdata,
                                              form)  # randomize the template before changing the formno
                if form == 0:
                    if index != 128 and index != 194:
                        break  # NOT ALLOWED !!!
                    else:
                        # print(form_template)
                        data['values'].append(form_template)
                else:  # should let pass 0's if correct id's
                    # print(form_template)
                    data['values'].append(form_template)

    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su1_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation - Teal done !")


def randomize_indigo(config):
    # print(os.getcwd())
    # load information
    file = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su2_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    # recreate data entries so all mons are present.
    # simplest way of doing it, is to edit all existing entries to have devid's ascending from allowed species, and simply paste another entry with the new ids n shti
    # copy an entry
    template_entry = data['values'][0].copy()

    i = len(data) - 1
    # edit existing entries
    for entry in data['values']:
        # entry['devid'] = fetch_devname(allowed_species[i])
        # entry['sex'] = "DEFAULT"
        recreated_species.append(entry['devid'])
        if entry['formno'] != 0:
            recreated_altforms.append(entry['devid'])
        entry['minlevel'] = 2
        entry['maxlevel'] = 99
        entry['lotvalue'] = random.randint(1, 50)
        entry['biome1'] = pick_random_biome1()
        entry['biome2'] = pick_random_biomerest()
        entry['biome3'] = pick_random_biomerest()
        entry['biome4'] = pick_random_biomerest()
        entry['lotvalue1'] = generate_lot_value_for_biome(entry['biome1'])
        entry['lotvalue2'] = generate_lot_value_for_biome(entry['biome2'])
        entry['lotvalue3'] = generate_lot_value_for_biome(entry['biome3'])
        entry['lotvalue4'] = generate_lot_value_for_biome(entry['biome4'])
        chosen_biomes.clear()
        entry['area'] = generate_area_list()
        entry['locationName'] = ""
        entry['enabletable']['land'] = True
        entry['enabletable']['up_water'] = True
        entry['enabletable']['underwater'] = True
        entry['enabletable']['air1'] = True
        entry['enabletable']['air2'] = True
        entry['timetable']['morning'] = True
        entry['timetable']['noon'] = True
        entry['timetable']['evening'] = True
        entry['timetable']['night'] = True
        entry['flagName'] = ""
        entry['versiontable']['A'] = True
        entry['versiontable']['B'] = True
        entry['bringItem']['itemID'] = "ITEMID_NONE"
        entry['bringItem']['bringRate'] = 0
    # add in mons that were not present previously
    # i shoudl really cleanup this bullshit later
    for index in range(1, 1025):
        if index in banned_pokemon:
            continue
        if config['exclude_legendaries'] == "yes":
            if index in legends:
                pass
            else:
                if fetch_devname(index, csvdata) not in recreated_species:
                    new_template = template_entry.copy()
                    recreated_species.append(fetch_devname(index, csvdata))
                    new_template = make_template(new_template, index, csvdata)
                    data['values'].append(new_template)
                    i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index != 128 and index != 194:
                            break  # NOT ALLOWED !!!
                        else:
                            # print(form_template)
                            data['values'].append(form_template)
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
        else:
            if fetch_devname(index, csvdata) not in recreated_species:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
            forms = get_alt_form(index)
            for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                # so aside from 128 and 194, all 0's should be ignored
                form_template = template_entry.copy()  # gotta copy again the template from the start
                form_template = make_template(form_template, index, csvdata,
                                              form)  # randomize the template before changing the formno
                if form == 0:
                    if index != 128 and index != 194:
                        break  # NOT ALLOWED !!!
                    else:
                        # print(form_template)
                        data['values'].append(form_template)
                else:  # should let pass 0's if correct id's
                    # print(form_template)
                    data['values'].append(form_template)

    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su2_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation - Indigo done !")


def main():
    randomize()
    randomize_teal()
    randomize_indigo()


if __name__ == "__main__":
    main()

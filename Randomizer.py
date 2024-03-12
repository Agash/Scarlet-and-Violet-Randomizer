import json
import os
import Randomizer.WildEncounters.wildrando as WildRandomizer
import Randomizer.Trainers.trainerrando as TrainerRandomizer
import Randomizer.PersonalData.personal_randomizer as PersonalRandomizer
import Randomizer.Starters.randomize_starters as StarterRandomizer
import Randomizer.StaticSpawns.statics as StaticRandomizer
import Randomizer.Scenes.patchscene as PatchScene
import Randomizer.FileDescriptor.fileDescriptor as FileDescriptor
import shutil
import subprocess


# thanks zadenowen for the function
def generateBinary(schema: str, json: str, path: str):
    flatc = "flatc/flatc.exe"
    outpath = os.path.abspath("output/romfs/" + path)
    # print(outpath)
    proc = subprocess.run(
        [os.path.abspath(flatc),
        "-b",
        "-o",
        outpath,
        os.path.abspath(schema),
        os.path.abspath(json)
        ], capture_output=True
    )
    return proc


def open_config():
    file = open("config.json", "r")
    config = json.load(file)
    file.close()
    return config


def create_modpack():
    if os.access("output/romfs", mode=777) == True: #exists
        shutil.rmtree("output/romfs")
    os.makedirs("output/romfs", mode=777, exist_ok=True)


paths = {
    "wilds": "world/data/encount/pokedata/pokedata",
    "wilds_su1": "world/data/encount/pokedata/pokedata_su1",
    "wilds_su2": "world/data/encount/pokedata/pokedata_su2",
    "trainers": "world/data/trainer/trdata",
    "gifts": "world/data/event/event_add_pokemon/eventAddPokemon",
    "personal": "avalon/data",
    "statics": "world/data/field/fixed_symbol/fixed_symbol_table",
    "tms": "world/data/item/itemdata",
    "catalog": "pokemon/catalog/catalog",
    "scenes": "world/scene/parts/event/event_scenario/main_scenario/common_0070_",
    "shiny_scenes": "pokemon/data/",
    "trpfd": "arc"
}


def randomize():
    config = open_config()
    create_modpack()
    if config['wild_randomizer']['is_enabled'] == "yes":  # Updated for 3.0.1
        WildRandomizer.randomize(config['wild_randomizer'])
        WildRandomizer.randomize_teal(config['wild_randomizer'])
        WildRandomizer.randomize_indigo(config['wild_randomizer'])
        generateBinary("Randomizer/WildEncounters/pokedata_array.bfbs", "Randomizer/WildEncounters/pokedata_array.json", paths["wilds"])
        generateBinary("Randomizer/WildEncounters/pokedata_su1_array.bfbs", "Randomizer/WildEncounters/pokedata_su1_array.json",
                       paths["wilds_su1"])
        generateBinary("Randomizer/WildEncounters/pokedata_su2_array.bfbs",
                       "Randomizer/WildEncounters/pokedata_su2_array.json",
                       paths["wilds_su2"])
    if config['trainer_randomizer']['is_enabled'] == "yes":  # Updated for 3.0.1
        TrainerRandomizer.randomize(config['trainer_randomizer'])
        generateBinary("Randomizer/Trainers/trdata_array.bfbs", "Randomizer/Trainers/trdata_array.json", paths["trainers"])
    if config['personal_data_randomizer']['is_enabled'] == "yes":  # Updated to 3.0.1
        PersonalRandomizer.randomize(config['personal_data_randomizer'])
        generateBinary("Randomizer/PersonalData/personal_array.fbs", "Randomizer/PersonalData/personal_array.json", paths["personal"])
    if config['starter_randomizer']['is_enabled'] == "yes":  # Updated to 3.0.1
        StarterRandomizer.randomize(config['starter_randomizer'])
        generateBinary("Randomizer/Starters/eventAddPokemon_array.bfbs", "Randomizer/Starters/eventAddPokemon_array.json", paths["gifts"])
    if config['static_randomizer']['is_enabled'] == "yes":  # Updated to 3.0.1
        StaticRandomizer.randomize(config['static_randomizer'])
        generateBinary("Randomizer/StaticSpawns/fixed_symbol_table_array.bfbs", "Randomizer/StaticSpawns/fixed_symbol_table_array.json", paths["statics"])
    if config['starter_randomizer']['is_enabled'] == "yes" and config['starter_randomizer']['show_starters_in_overworld'] == "yes": # Updated for 3.0.1
        PatchScene.patchScenes()
        generateBinary("Randomizer/Scenes/poke_resource_table.fbs", "Randomizer/Scenes/poke_resource_table.json", paths['catalog'])
        os.makedirs("output/romfs/" + paths['scenes'], mode=777, exist_ok=True)
        shutil.copyfile("Randomizer/Scenes/common_0070_always_0.trsog", "output/romfs/" + paths['scenes'] + '/common_0070_always_0.trsog')
        shutil.copyfile("Randomizer/Scenes/common_0070_always_1.trsog", "output/romfs/" + paths['scenes'] + '/common_0070_always_1.trsog')
    if config['patch_trpfd'] == "yes":
        FileDescriptor.patchFileDescriptor()
        generateBinary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json", paths['trpfd'])
        shutil.make_archive("output/randomizer", "zip", "output/")
        if os.path.exists(os.getcwd() + "\\randomizer-patched"):
            shutil.rmtree(os.getcwd() + "\\randomizer-patched")
        shutil.copytree('output/', 'randomizer-patched/')
        shutil.move('output/randomizer.zip', 'randomizer-patched/randomizer.zip')
        if config['starter_randomizer']['shiny_overworld'] == "yes":
            if os.path.exists(os.getcwd() + "\\Randomizer\\Starters\\" + f'output'):
                shutil.copytree(os.getcwd() + "\\Randomizer\\Starters\\output\\romfs\\pokemon\\data",
                                "output/romfs/" + paths['shiny_scenes'])
                FileDescriptor.patchFileDescriptor()
                generateBinary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json",
                               paths['trpfd'])
                shutil.make_archive("output/randomizer-shiny-overworld", "zip", "output/")
                if os.path.exists(os.getcwd() + "\\randomizer-shiny"):
                    shutil.rmtree(os.getcwd() + "\\randomizer-shiny")
                shutil.copytree('output/', 'randomizer-shiny/')
                shutil.move('output/randomizer-shiny-overworld.zip', 'randomizer-shiny/randomizer-shiny-overworld.zip')
    else:
        shutil.make_archive("output/randomizer", "zip", "output/romfs/")

        if config['starter_randomizer']['shiny_overworld'] == "yes":
            if os.path.exists(os.getcwd() + "\\Randomizer\\Starters\\" + f'output'):
                shutil.copytree(os.getcwd() + "\\Randomizer\\Starters\\output\\romfs\\pokemon\\data",
                                "output/romfs/" + paths['shiny_scenes'])
                shutil.make_archive("output/randomizer-shiny-overworld", "zip", "output/romfs/")
            else:
                print('No Shiny starter')


def test():
    create_modpack()


def main():
    randomize()


if __name__ == "__main__":
    main()

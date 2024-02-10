#!/usr/bin/env python3
import argparse
import json
import copy

class FixSkillMissing():
    def __init__(self):
        self.skill_list = []
        self.skill_unique_list = []
        self.skill_tree_list = {}
        self.level_sav = {}
        self.pals_data = []

    def init_skill_list(self):
        with open("./skill_list.json") as fd:
            self.skill_list = json.load(fd)
        pass

    def init_unique_skill(self):
        with open("./skill_unique_list.json") as fd:
            self.skill_unique_list = json.load(fd)
        pass

    def init_skill_tree_list(self):
        with open("./skill_tree_list.json") as fd:
            self.skill_tree_list = json.load(fd)
        pass

    def get_pals_data(self, save_path):
        with open(save_path) as fd:
            self.level_sav = json.load(fd)
            self.pals_data = self.level_sav["properties"]["worldSaveData"]["value"]["CharacterSaveParameterMap"]["value"]
        pass

    def build_mastered_skill(self, skill_list):
        obj = {
                "array_type": "EnumProperty",
                "id": None,
                "value": {
                    "values": skill_list
                },
                "type": "ArrayProperty"
            }
        return obj

    def start(self, save_path, mode):
        self.init_skill_list()
        self.init_unique_skill()
        self.init_skill_tree_list()
        self.get_pals_data(save_path)
        size = len(self.pals_data)
        index = 0
        for pal_data in self.pals_data:
            index += 1
            print(f'processing... {index}/{size}   {pal_data["key"]["InstanceId"]["value"]}')
            if "IsPlayer" in pal_data["value"]["RawData"]["value"]["object"]["SaveParameter"]["value"]:
                continue
            if "UniqueNPCID" in pal_data["value"]["RawData"]["value"]["object"]["SaveParameter"]["value"]:
                continue

            pal_mastered_skill = pal_data["value"]["RawData"]["value"]["object"]["SaveParameter"]["value"]
            pal_name = pal_data["value"]["RawData"]["value"]["object"]["SaveParameter"]["value"]["CharacterID"]["value"]
            pal_name = pal_name.lower()
            if pal_name.startswith("boss"):
                pal_name = pal_name.split("boss_")[1]

            if mode == "base":
                pal_mastered_skill["MasteredWaza"] = self.build_mastered_skill(copy.deepcopy(self.skill_tree_list[pal_name]))
                continue

            if mode == "extend":
                old_mastered_skill_list = copy.deepcopy(pal_mastered_skill["MasteredWaza"]["value"]["values"])
                new_mastered_skill_list = copy.deepcopy(self.skill_tree_list[pal_name])
                for skill in old_mastered_skill_list:
                    if skill not in new_mastered_skill_list:
                        new_mastered_skill_list.append(skill)
                pal_mastered_skill["MasteredWaza"] = self.build_mastered_skill(new_mastered_skill_list)
                continue

            if mode == "all":
                new_mastered_skill_list = copy.deepcopy(self.skill_tree_list[pal_name])
                for skill in self.skill_list:
                    if skill not in new_mastered_skill_list:
                        new_mastered_skill_list.append(skill)
                pal_mastered_skill["MasteredWaza"] = self.build_mastered_skill(new_mastered_skill_list)
                continue

            if mode == "extra":
                new_mastered_skill_list = copy.deepcopy(self.skill_tree_list[pal_name])
                for skill in self.skill_list:
                    if skill not in new_mastered_skill_list:
                        new_mastered_skill_list.append(skill)
                for skill_unique in self.skill_unique_list:
                    if skill_unique not in new_mastered_skill_list:
                        new_mastered_skill_list.append(skill_unique)
                pal_mastered_skill["MasteredWaza"] = self.build_mastered_skill(new_mastered_skill_list)
                continue

        print("writing json file.")
        with open("./Level_new.sav.json", "w") as fd:
            json.dump(self.level_sav, fd, indent=2)
        pass

        print("Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_path", help="level.save.json path", required=True)
    parser.add_argument("-m", "--mode", type=str, default="extend", choices=["base", "extend", "all", "extra"],
                        help="base: only original skills, extend: base + learned skills, all: base + all learnable skills, extra: all + all unique skills.")

    args = parser.parse_args()
    if args.file_path:
        main = FixSkillMissing()
        main.start(args.file_path, args.mode)
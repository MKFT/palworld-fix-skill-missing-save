# palworld-fix-skill-missing-save

Fix pal skill missing issue

ENGLISH / [中文](./README_CH.md)

## Requirement
- [palworld-save-tools](https://github.com/cheahjs/palworld-save-tools)

## Usage
Use `palworld-save-tools` to get the `Level.sav.json` file
> [!WARNING]
> ALWAYS MAKE SURE TO BACKUP YOUR SAVE FILES

### Windows GUI

Drag and drop the `Level.sav.json` file into `fix_skill_{MODE}.cmd` for the mode you want to run.

### Terminal
```shell
python3 ./fix_skill_missing.py -f YOUR_JSON_PATH -m MODE

options:
  -h, --help              Print help
  -f, --file_path <PATH>  Level.sav.json path(file location)
  -m, --mode              base: only original skills
                          extend(default): base + learned skills
                          all: base + all learnable skills
                          extra: all + all unique skills
```
You will get `Level_new.sav.json` after run fix, use `palworld-save-tools` convert json to sav.

Rename to `Level.sav` and overwrite file.

Enjoy your game.
> [!NOTE]
> Nothing happens when using skills that are not unique to pal.

## License

[MIT](./LICENSE)
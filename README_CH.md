# palworld-fix-skill-missing-save

修復帕魯技能消失問題

[ENGLISH](./README.md) / 中文

## Requirement
- [palworld-save-tools](https://github.com/cheahjs/palworld-save-tools)

## Usage
使用`palworld-save-tools`將`Level.json`轉成`Level.sav.json`
> [!WARNING]
> 請確保你有備份紀錄檔案

```shell
python3 ./fix_skill_missing.py -f YOUR_JSON_PATH -m MODE

options:
  -h, --help              印出說明/印出幫助
  -f, --file_path <PATH>  Level.sav.json 的檔案位置
  -m, --mode              base: 只有該帕魯原本會學會的技能(包含自己的專屬技能)
                          extend(預設值): base + 修正前擁有的技能
                          all: base + 專屬技能以外的所有技能
                          extra: all + 所有其他帕魯的專屬技能
```
執行修復後會得到 `Level_new.sav.json`, 使用`palworld-save-tools`將sav轉回json

重新命名為`Level.sav`後覆蓋原本的檔案

享受你的遊戲
> [!NOTE]
> 使用不是該帕魯專屬的專屬技能將不會發生任何事情

## License

[MIT](./LICENSE)
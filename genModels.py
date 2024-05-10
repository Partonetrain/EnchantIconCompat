import glob
import os
import re
from pathlib import Path

print('Model generator for EnchantIconCompat')

current_directory = os.getcwd()

pngs = glob.glob(current_directory + '/**/*.png', recursive=True)
print("Found the following PNGs: " + str(pngs))

enchant_icon_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(pngs[0])))) #\assets\enchant_icon
print("Base directory: " + enchant_icon_dir)
model_dir = enchant_icon_dir + "\\models\\enchant"
print("Model directory: " + model_dir)
texture_dir = enchant_icon_dir + "\\textures\\enchant_icon\\"
print("Texture directory: " + model_dir)

count = 0
for p in pngs:
    skip = False
    enchantName = os.path.basename(p).removesuffix(".png")
    enchantNamespace = os.path.dirname(p).removeprefix(texture_dir)
    if("unsorted" in enchantNamespace):
        skip = True
        print("Skipped " + enchantNamespace + ":" + enchantName + " because it was in unsorted folder")
    if(not skip):
        print("Enchantment ID is " + enchantNamespace + ":" + enchantName)
        modelFileDir = model_dir + "\\" + enchantNamespace
        modelFilePath = model_dir + "\\" + enchantNamespace + "\\" + enchantName + ".json"
        Path(modelFileDir).mkdir(parents=True, exist_ok=True)
        f = open(modelFilePath, "w+")
        modelFileContents = "{\"parent\": \"minecraft:item/generated\", \"textures\": {\"layer0\": \"enchant_icon:enchant_icon/" + enchantNamespace + "/" + enchantName + "\"}}"
        f.write(modelFileContents)
        f.close()
        print("Generated model file for " + enchantNamespace + ":" + enchantName)
        count = count + 1

print("Done! Generated " + str(count) + " model files")
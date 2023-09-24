import bpy
import json

shapeKeys = bpy.data.objects["Body"].data.shape_keys.key_blocks
facialTrackingLibraryJson = open('E:\\2023_09_09 - OverlayFox MagPie\\05 Script\\shapeKeyReplacer RexToAdjerry91 UN.json', 'r')
facialTrackingLibrary = json.load(facialTrackingLibraryJson)
facialTrackingLibraryJson.close()


for shapeKey in shapeKeys:
    if shapeKey.name != "Basis":
        for key in facialTrackingLibrary:
            if shapeKey.name == key['oldKeyName']:
                try:
                    shapeKey.name = key['newKeyName']
                    print(f'Renamed: {key["oldKeyName"]}')
                except:
                    pass
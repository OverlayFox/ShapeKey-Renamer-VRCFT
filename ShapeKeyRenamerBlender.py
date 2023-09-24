import bpy
import json

shapeKeys = bpy.data.objects["Body"].data.shape_keys.key_blocks
facialTrackingLibraryJson = open('.\\jsons\\MagPieV6_to_UnifiedExpressions.json', 'r')
facialTrackingLibrary = json.load(facialTrackingLibraryJson)
facialTrackingLibraryJson.close()

for shapeKey in shapeKeys:
    if shapeKey.name != "Basis":
        for key in facialTrackingLibrary:
            if shapeKey.name == key['oldKeyName']:
                try:
                    shapeKey.name = key['newKeyName']
                    print(f'Renamed: {key["oldKeyName"]} to {shapeKey.name}')
                except:
                    pass
import arcpy
import os

# Koordinatsion tizimni tanlash
output_coord_system = arcpy.SpatialReference(3857)  # WGS_1984_Web_Mercator_Auxiliary_Sphere
#WKID: 3857 Authority: EPSG

# Qatlamlar joylashgan papka
input_folder = r'C:\path\to\your\layers'

# Chiqarish papkasi
output_folder = r'C:\path\to\output\layers'

# Papkada mavjud bo'lgan barcha shapefile'larni ko‘rish
for filename in os.listdir(input_folder):
    if filename.endswith(".shp"):  # Shapefile formatida
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)

        # Proyeksiya o‘zgartirish
        arcpy.Project_management(input_file, output_file, output_coord_system)

print("Barcha qatlamlar muvaffaqiyatli o‘zgartirildi!")

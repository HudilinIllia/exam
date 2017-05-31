import arcpy
import os
arcpy.env.workspace = r'D:\Modul2\p3'
arcpy.env.overwriteOutput = True
amenities = ['school','hospital','place_of_worship']
country = 'El Salvador'
# создание векторного сло€ из входного класа
arcpy.MakeFeatureLayer_management('CentralAmerica.shp','temply','"NAME" =  ' +"'"+country+"'")
#вырезание объекта
arcpy.Clip_analysis('OSMpoints.shp','temply','clip.shp')
#создание файловой базы геоданых в папке
arcpy.CreateFileGDB_management(arcpy.env.workspace,'yourGDB.gdb')
for i in amenities:
    name='point'+i
    arcpy.MakeFeatureLayer_management('clip.shp',name,'"amenity" =  ' +"'"+i+"'")
    #копирует объекты с входного класа или сло€ в новый клас объектов
    arcpy.CopyFeatures_management('point'+i,arcpy.env.workspace+r'\yourGDB.gdb'+r'\point'+i)
    #добавл€ет новое поле в таблицу
    arcpy.AddField_management('yourGDB.gdb\\'+'point'+i,'source',"TEXT")
    arcpy.AddField_management('yourGDB.gdb\\'+'point'+i,'GID',"DOUBLE")
    #изменение свойст пол€
    arcpy.AlterField_management('yourGDB.gdb\\'+'point'+i,'GID')
    #UpdateCursor устанавливает доступ дл€ чтени€ и записи к запис€м,возвращ€емым из класа объектов или таблицы
    with arcpy.da.UpdateCursor('yourGDB.gdb\\'+'point'+i, ('source','GID','id')) as cursor:
        for row in cursor:
                row[0]='OpenStreetMap'
                row[1]=row[2]
                cursor.updateRow(row)

print 'script complete'

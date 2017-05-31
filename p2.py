import arcpy
#модуль для роботы с ОС
import os
arcpy.env.workspace = r'D:\Modul2'
#список класов объектов в рабочей области
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    #возвращает объект функции describe
    desc = arcpy.Describe(fc)
    # определение картографичной проекции
    if desc.spatialReference.name!=arcpy.Describe(r'D:\Modul2\Lesson2\CityBoundaries.shp').spatialReference.name:
        outfc=desc.name[:-4]+'_projected.shp'
        #проецирование координат с одной системы в другую
        arcpy.Project_management(fc,os.path.join(arcpy.env.workspace,outfc),arcpy.Describe(r'D:\Modul2\Lesson2\CityBoundaries.shp').spatialReference)
    #arcpy.AddMessage(desc.spatialReference.name)

print "Script completed"

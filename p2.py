import arcpy
#������ ��� ������ � ��
import os
arcpy.env.workspace = r'D:\Modul2'
#������ ������ �������� � ������� �������
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    #���������� ������ ������� describe
    desc = arcpy.Describe(fc)
    # ����������� �������������� ��������
    if desc.spatialReference.name!=arcpy.Describe(r'D:\Modul2\Lesson2\CityBoundaries.shp').spatialReference.name:
        outfc=desc.name[:-4]+'_projected.shp'
        #������������� ��������� � ����� ������� � ������
        arcpy.Project_management(fc,os.path.join(arcpy.env.workspace,outfc),arcpy.Describe(r'D:\Modul2\Lesson2\CityBoundaries.shp').spatialReference)
    #arcpy.AddMessage(desc.spatialReference.name)

print "Script completed"

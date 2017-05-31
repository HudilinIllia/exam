import arcpy
from arcpy.sa import *
arcpy.env.workspace=r'D:\Modul2'
arcpy.CheckOutExtension("Spatial")
#��������� ���������� �����
arcpy.env.overwriteOutput = True
#����� ������������
a=Idw(r'D:\Modul2\Lesson1\Precip2008Readings.shp','RASTERVALU')
#��������������
b=Reclassify(a,'Value',RemapRange([[27715,55521,1],[55521,83326,2],[83326,111133,3]]))
#����������� ��������� ����� � ������������� ������
arcpy.RasterToPolygon_conversion(b,r'D:\Modul2\Lesson1\p1.shp',"NO_SIMPLIFY",'VALUE')
#��������� �������
arcpy.Clip_analysis(r'D:\Modul2\Lesson1\p1.shp',r'D:\Modul2\Lesson1\Nebraska.shp',r'D:\Modul2\Lesson1\p1clip.shp')

print 'sctipt complete' 

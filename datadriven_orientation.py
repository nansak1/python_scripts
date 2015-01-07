#-------------------------------------------------------------------------------
# Name:        House Mapbook
# Purpose: Creates landscape or portrait district maps as PDF files of each House district
# The template needs to set to data driven pages, the title needs to be dynamic text, do not use maplex for labels
# the visibility of the layers needs to be set prior to running this script
# Author:      nnayate
#
# Created:     01/05/2014
# Copyright:   (c) nnayate 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

from arcpy import env
env.workspace = "q:\\path\\to\\folder"

sCur = arcpy.SearchCursor("q:\\path\\to\\shapfile\\test.shp")

# Fetch each feature from the cursor and examine the extent properties

# loops through each row in the shapefile
for row in sCur:

# print columns
    print row.FID
    print row.DISTRICT

# for each row in the shapefile find the extent
    geom = row.shape
    ext = geom.extent



# calculate if extent is portrait or landscape
    xlength = ext.XMax - ext.XMin
    ylength = ext.YMax - ext.YMin

# if landscape
    if xlength > ylength:
        print"x>y, map should be landscape"

# set the landscape template mxd
        mxd = arcpy.mapping.MapDocument(r"q:\path\to\landscape\mapbook\template\landscape.mxd")
        pageID = mxd.dataDrivenPages.getPageIDFromName(str(row.DISTRICT))
        mxd.dataDrivenPages.currentPageID = pageID

# keeps track of exported pdf files
        print "Exporting landscape page {0} of {1}".format(str(row.FID+1), str(mxd.dataDrivenPages.pageCount))
        arcpy.mapping.ExportToPDF(mxd, r"q:\path\to\landscape\pdf\folder\landscape_" + str(row.DISTRICT) + ".pdf",resolution=150)

        del mxd

# if portrait
    else:
        print"x<y, map should be port"
# set the portrait template mxd
        mxd = arcpy.mapping.MapDocument(r"q:\path\to\portrait\mapbook\template\portrait.mxd")
        pageID = mxd.dataDrivenPages.getPageIDFromName(str(row.DISTRICT))
        mxd.dataDrivenPages.currentPageID = pageID

# keeps track of exported pdf files
        print "Exporting portrait page {0} of {1}".format(str(row.FID +1), str(mxd.dataDrivenPages.pageCount))
        arcpy.mapping.ExportToPDF(mxd, r"q:\path\to\portrait\mapbook\template\portrait_" + str(row.DISTRICT) + ".pdf",resolution=150)

        del mxd

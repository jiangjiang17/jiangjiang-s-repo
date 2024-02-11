import rasterio
import matplotlib.pyplot as plt
import numpy as np
from glob import glob

dir='/geos/netdata/oosa/week3/sentinel-2/L2A_T30VVH_A020126_20210112T113447_2021-01-12'
fileList=glob(dir+"/*"+".jp2")

band4name=list(filter(lambda x: x.endswith("B04.jp2"), fileList))[0]
band8name=list(filter(lambda x: x.endswith("B08.jp2"), fileList))[0]

band4name=rasterio.open(band4name)
band8name=rasterio.open(band8name)


# read the rasters and scale to be in relfectance
band4=band4name.read(1)/10000
band8=band8name.read(1)/10000
# remove missing data
band4[band4>1.0]=-999.0
band8[band8>1.0]=-999.0
# calculate ndvi
ndvi=(band8-band4)/(band8+band4)
# filter out missing data
ndvi[ndvi>1]=-999.0
ndvi[ndvi<-1]=-999.0

# open a new dataset ready to write, with the same dimensions as the above data
outName='sentinel2.ndvi.tif'
new_dataset=rasterio.open(outName,'w',driver='GTiff',height=band4name.height,
              width=band4name.width,count=1,dtype=ndvi.dtype,crs=band4name.crs,transform=band4name.transform)
new_dataset.write(ndvi, 1)
new_dataset.nodata = -999.0
new_dataset.close()
print("NDVI written to",outName)
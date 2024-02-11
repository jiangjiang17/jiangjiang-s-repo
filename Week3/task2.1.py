
'''
Example of opening and 
displaying a raster with
rasterio
'''

# This example was inspired by:
# https://rasterio.readthedocs.io/en/latest/quickstart.html

# import packages needed
import rasterio
import matplotlib.pyplot as plt

#################################


if __name__ == "__main__":
  '''Main block'''

  # set a file
  filename8='/geos/netdata/oosa/week3/sentinel-2/L2A_T30VVH_A020126_20210112T113447_2021-01-12/T30VVH_A020126_20210112T113447_B08.jp2'
  filename6='/geos/netdata/oosa/week3/sentinel-2/L2A_T30VVH_A020126_20210112T113447_2021-01-12/T30VVH_A020126_20210112T113447_B06.jp2'
  filename4='/geos/netdata/oosa/week3/sentinel-2/L2A_T30VVH_A020126_20210112T113447_2021-01-12/T30VVH_A020126_20210112T113447_B04.jp2'

  # open it as a rasterio object
  dataset8=rasterio.open(filename8)
  dataset6=rasterio.open(filename6)
  dataset4=rasterio.open(filename4)

  # print out some properties of it
  print("The image is",dataset8.width,"by",dataset8.height,"pixels")
  print("The projection is",dataset8.crs)
  print("The image is",dataset6.width,"by",dataset6.height,"pixels")
  print("The projection is",dataset6.crs)
  print("The image is",dataset4.width,"by",dataset4.height,"pixels")
  print("The projection is",dataset4.crs)

  # read the raster data into RAM
  bandLayer8=dataset8.read(1)
  bandLayer6=dataset6.read(1)
  bandLayer4=dataset4.read(1)

  # print to the screen
  plt.imshow(bandLayer8)
  plt.show()
  plt.imshow(bandLayer6)
  plt.show()
  plt.imshow(bandLayer4)
  plt.show()
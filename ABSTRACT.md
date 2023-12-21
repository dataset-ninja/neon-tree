The authors of the **RGB** part of the **NeonTreeEvaluation Benchmark** dataset aimed to address the challenges associated with broad-scale remote sensing for building forest inventories combining RGB, LiDAR, and hyperspectral sensor data from the USA National Ecological Observatory Network's Airborne Observation Platform. The dataset includes over 6,000 image-annotated crowns, 400 field-annotated crowns, and 3,000 canopy stem points, covering a diverse range of forest types. An R package is provided to standardize evaluation metrics, facilitating method comparisons. Additionally, the dataset offers more than 10,000 training crowns for optional use. 

## RGB data

The RGB data were obtained using a D8900 camera with a format of 8,984 x 6,732 pixels. Individual images underwent color rectification, orthorectification, and mosaicking to generate a single raster image with a pixel size of 0.1 m^2. Mosaic tiles, available as 1000m x 1000m geoTIFF files, are named based on the UTM coordinate at the northwest origin. The high spatial resolution of RGB data allows the observation of individual canopy trees, discerning crown boundaries, and revealing color differences reflecting taxonomy and health status.

To ensure spatial overlap between LiDAR and RGB data, NEON staff superimposed the 0.1m spatial resolution RGB tile on a 1m spatial resolution LiDAR-derived surface height model. 

## LiDAR Point Cloud data

The LiDAR data consist of 3D coordinates (~5 points/m^2) providing detailed information about canopy crown shape and height. Stored as 1000m x 1000m .laz files, these files include x, y, z coordinates for each return, along with metadata on return intensity and point classification. The boundaries of individual canopy crowns often become apparent due to gaps among neighboring trees or variations in height among overlapping crowns.Notably, the point density of NEON LiDAR clouds is considerably lower than the densities (8–1000 pt/m^2) used in many studies of crown detection models.

<img src="https://github.com/dataset-ninja/neon-tree-evaluation/assets/78355358/652e6f0c-7699-4381-bde1-165d317d7041" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Normalized LIDAR point cloud for evaluation plot **SJER_064** from the San Joaquin Experimental Range, California (left) and **MLBS_071** from Mountain
Lake Biological Station, Virginia. Points are colored by height above ground.</span>

## Hyperspectral surface reflectance data

NEON's hyperspectral sensor captures reflected light across the visible and infrared spectrum (approximately 420–2500 nm) with a spectral sampling interval of 5nm, yielding a total of 426 bands. Orthorectified hyperspectral images, with a pixel size of 1 m^2 in 1000m x 1000m tiles aligning with RGB and LiDAR file conventions, are provided. Hyperspectral data, particularly in the infrared spectrum, proves valuable for distinguishing tree species based on spectral differences related to leaf chemistry and canopy structure. All hyperspectral data were collected during the same field campaign as RGB data, except for the UNDE site, where 2017 flight data was used due to the unavailability of 2019 RGB data.

<img src="https://github.com/dataset-ninja/neon-tree-evaluation/assets/78355358/6e606ae2-85cc-401c-be73-a401a1b2b8e8" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Composite hyperspectral image (left) and corresponding RGB image (right) for the MLBS site. The composite image contains near infrared (940nm), red (650nm), and blue (430nm) channels. Trees that are difficult to segment in RGB imagery may be more separable in hyperspectral imagery due to the differing foliar chemical and structural properties of co-occurring trees.</span>

## Ecosystem Structure

The 'Ecosystem Structure' data product, provided by the authors of the dataset, represents a LiDAR-derived height raster at 1m spatial resolution, commonly referred to as a 'canopy height model' (CHM). The raster values denote the normalized height above ground for each grid cell. This dataset proves valuable for distinguishing crowns in three dimensions and for eliminating crowns below the 3m threshold utilized in this benchmark for minimum tree height. 

## Woody Plant Vegetation Structure

In conjunction with sensor data, the authors collect information on trees within fixed plots at each NEON site. This dataset includes data from two plot types: 'distributed' plots (20m x 20m fully sampled) and 'Tower' plots (40m x 40m with two sampled 20m x 20m quadrants). While the distinction between distributed and tower plots may prove useful for users familiar with NEON’s sampling regime, it is not essential for most uses of the benchmark dataset. The mapping and recording of all trees in sampled areas with a stem diameter exceeding 10cm are carried out, providing key tree metadata such as stem position, size, and estimated tree height.

## Evaluation Annotations

The objective of this benchmark, as set by the authors of the dataset, is to evaluate algorithms for canopy tree detection and delineation. The term 'canopy crown detection' is adopted to differentiate between the tasks of 'tree detection,' involving the identification of the crown center of individual trees, and 'crown delineation' or 'crown segmentation,' often defined as identifying the boundary edge of individual crowns. The term ‘canopy’ is often implicitly assumed in most studies, given that optical data and low-density LiDAR data can only reflect the structure in the upper canopy. The evaluation of detection methods in this benchmark dataset involves assessing detections using three types of evaluation data: 1) image-annotated crown bounding boxes for 22 sites in the NEON network, 2) field-annotated crown polygons for two sites in the NEON network (Table 2), and 3) field-collected stem points from 14 sites from the NEON Woody Vegetation Structure dataset. For each of these data types, the authors outline how the data were collected and the evaluation procedure for canopy crown detection.

## Image-Annotated Crowns

The authors selected airborne imagery from 22 sites surveyed by the NEON AOP. The sites were chosen based on the availability of the three types of sensor data, as well as representation of forest conditions across the US, including diversity in species composition, stand age, and canopy openness. The evaluation images were carefully annotated by comparing the RGB, LiDAR, and hyperspectral data. Using all three products facilitated more accurate distinction of neighboring trees by simultaneously assessing visual patterns (RGB), utilizing variation in spectral signatures to distinguish different species (hyperspectral), and considering the three-dimensional structure of the tree (LiDAR). The evaluation plot overlaps with a NEON 40m x 40m plot. Within each of these plots, NEON field crews survey a 20x20 subplot; therefore, while field data are available for most plots in the dataset, they do not cover every tree in the image.


<img src="https://github.com/dataset-ninja/neon-tree-evaluation/assets/78355358/59588358-a9af-4443-932d-28275d07227a" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Image-annotated tree crowns for the evaluation data set for two sites in the National Ecological Observation Network. Using the RGB, LiDAR and hyperspectral products together contributes to more careful crown annotation. For some sites, such as MLBS (top row), the RGB and hyperspectral data are useful for differentiating overlapping crowns. For other sites, such as OSBS (bottom row) the LiDAR point cloud, shown as a rasterized height image, is most useful in capturing crown extent. The RGB-stretch image was produced by transforming the RGB data in the three principal components space. To create a three-band hyperspectral image, we used channels from the red, blue and infrared spectrum to capture changes in reflectance not apparent in the RGB imagery.</span>


## Field-Annotated Crowns

Individual trees were annotated by visiting two NEON sites and mapping the tree crown boundaries as polygons in the remote sensing images using a field tablet and GIS software while looking at each tree from the ground. False-color composites from the hyperspectral data, RGB, and LiDAR canopy height model were loaded onto tablet computers that were equipped with GPS receivers. While in the field, researchers digitized crown boundaries based on the location, size, and shape of the crown. Only alive trees with leaf-on vegetation were selected. Trees were mapped in 2014 and 2015, and all polygons were manually checked against the most recent NEON imagery. Adjustments to crown shape and position were refined after examining multiple years of RGB imagery. No adjustments to the polygons were made due to crown expansion.

## Training Annotations

During their research on canopy crown detection algorithms, the authors annotated geographic tiles separate from the evaluation data. The training sites were selected to capture a range of forest conditions, including oak woodland (NEON site: SJER), mixed pine (TEAK), alpine forest (NIWO), riparian woodlands (LENO), southern pinelands (OSBS), and eastern deciduous forest (MLBS). The training tiles were chosen at random from the NEON data portal.
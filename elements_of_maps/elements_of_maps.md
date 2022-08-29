<!--

author:   Elizabeth Drellich
email:    drelliche@chop.edu
version:  0.0.1
module_template_version: 2.0.1
language: en
narrator: UK English Female
title: The Elements of a Map
comment:  This is a general overview of ways that geospatial data can be communicated visually using maps.
long_description: Raw geospatial data can be particularly tricky for humans to read. However the shapes, colors, sizes, symbols, and language that make up a good map can effectively communicate a variety of detailed data even to readers looking at the map with only minimum specialized background knowledge. This module will demystify how raw data becomes a map and explain common components of maps. It is appropriate for anyone considering making maps from geospatial data.
estimated_time: 45 minutes

@learning_objectives  

After completion of this module, learners will be able to:

- understand the latitude and longitude coordinate system
- recognize the elements of maps
- name types of maps that focus on particular elements.

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# The Elements of a Map

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**
None

**Learning Objectives**

@learning_objectives

</div>

## Locations on Earth

Before we can talk about locations all over the earth, we have to establish the locations of a few very special points. The first two are the **North Pole** and the **South Pole**. If you imagine a line going straight through the planet connecting the two poles, this is the axis around which the Earth rotates creating night and day.

The **equator** is the circle around the surface of the earth that is exactly half way between the north and south poles. Any celestial body, like a planet or a star, that spins on an axis has two poles and an equator. Imagine a flat surface containing the equator and dividing the planet into a northern hemisphere and southern hemisphere. That flat surface is called the **equatorial plane**.

A **meridian** is a straight line on the surface of the earth connecting the poles. The third point we need is the location of the [Greenwich Observatory](https://www.rmg.co.uk/royal-observatory) in London, England. The meridian running through the observatory is called the **Prime Meridian**. Unlike the poles, which are fixed points determined by the astronomical fact that the earth is spinning on an axis, the location of the Prime Meridian was a human decision made for [historical](https://greenwichmeantime.com/articles/history/navy/) rather than geographical reasons.

Now that we have established the poles, the equator, and the prime meridian, we can use those to to create a coordinate system that will specify and point on earth!

**Latitude and Longitude**
==========================

**Latitude** is a measure of how far north or south a location is from the equator. Given a point on the surface of the earth, imagine a straight line to the center of the earth. The angle that line makes with the equatorial plane, measured in degrees (denoted $ {}^\circ $), is the point's latitude. Since that angle could be either above or below the equatorial plane, we have to specify which angle we are talking about. The horizontal line on the picture below corresponding to 30 degrees north, or +30$ {}^\circ $, goes through the United States, while the line representing 30 degrees south, or -30$ {}^\circ $, runs through Chile and Argentina.

![Earth with the poles, the equator, and latitudes marked at 30 degree increments ranging from -90 at the South Pole to 90 at the North Pole.](media/latitude.png)

**Longitude** is similarly an angular measurement, but rather than measuring relative to the equatorial plane, it measures relative to the prime meridian. Positive angles correspond to locations to the east of the prime meridian, while negative angles refer to points west of it. The meridian on the exact opposite side of the world from the prime meridian is, by convention, +180$ {}^\circ $ or 180$ {}^\circ $ East, even though it could just as accurately be described as -180$ {}^\circ $ or 180$ {}^\circ $ West.

![Earth with the prime meridian and longitude lines at 30 degree increments ranging from -150 to 180. Not shown is -180 degrees longitude which is the same as  180 degrees.](media/longitude.png)

Together, latitude and longitude form a (spherical) coordinate system that can specify any point on the planet, with high precision.

The Roberts Center for Pediatric Research at the Children's Hospital of Philadelphia, for example, is located at 39.94583795815241, -75.18659130245932. These numbers actually have far more significant digits than are appropriate, and correspond to a particular spot in the building's lobby.

<div class = "learnmore">

The location data produced today by satellites has no problem with long decimal numbers, but the first accurate measurements of longitude depended on the ability to accurately measure time.

While most of your geospatial data will likely use decimal degrees (DD), like the location for the Roberts Center above did, there is another way to specify smaller angles, using [degrees, minutes, and seconds (DMS)](https://gisgeography.com/decimal-degrees-dd-minutes-seconds-dms/). If you find yourself working with nautical data you may have to get comfortable with DMS measurements, but since most biomedical data deals with locations on land, we will leave this as a topic for you to explore further if interested.

</div>

<div class = "warning">

It is important to remember that this coordinate system is measuring angles, not distance. The points (0N,90E) and (0N, 90W) are directly across the planet from each other, as a far away as two points can get (over 20,000 km). However (89N, 90E) and (89N, 90W) are both in the arctic circle, less than 240 km away from each other.

</div>


## Shapes

<div class = "warning">

Although a map can be an extremely effective way of sharing your data, be aware that as a visual medium, maps will be inaccessible to members of your audience who are visually impaired. While we are focusing on the visual aspects in this module, it is important to provide text summaries of your findings as well.

</div>

Interpreting the geospatial data presented by a map is one thing, but if you want to make a map, you need to know how geospatial data becomes a map.

The following map shows the city of Philadelphia, along with a few specific attributes:

- zip codes divide the city into regions,
- two train lines, the Broad Street Line (in orange) and the Market Frankfort Line (in dark blue) are also pictured,
- train stations along those two train lines are shown as black and white dots.


![Map of Philadelphia highspeed train lines.](media/Philadelphia_highspeed_trains.jpg)




How did the data about stations, train lines (from [SEPTA](https://septaopendata-septa.opendata.arcgis.com/search?tags=Highspeed)), and zip codes (from [OpenDataPhilly](https://www.opendataphilly.org/dataset/zip-codes)) become a map? Each of those attributes was stored as text, a string of numbers representing one of the following types:

- Points (and Multipoints)
- Lines (and Mulitlines)
- Polygons (and Multipolygons)

<div class = "important">

Raw location data is stored as a set of points. This set of points is called a **geometry**.

In a tidy, tabular data array, you will have a column for the object name and a column for the geometry of that object. The names and geometries of the stations used for the map above are shown below:

![Tabular location data for train stations. The first column contains station names and the second column, titled geometry, contains each station's location as a point with longitude and latitude coordinates.](media/station_data.png)<!-- style = "max-width:400px;" border = 5px solid -->

</div>

Points
------

A point is a single location given by its latitude and longitude coordinates. On the map above, individual train stations are represented as points. The southernmost (bottom) station on the Broad Street Line, the NRG station has geometry `POINT (-75.17394 39.90543)`. A point has no length or width and therefore no area.

What objects are represented as points can depend on both the source of the geospatial data and the purpose of a particular map. For example if you are studying the health and safety of the city's unhoused population, representing a station that has multiple entrances as a single point could be insufficient. Alternatively if you are looking at national or global populations, the entire city of Philadelphia might be represented as a single point.

Lines
------

A line is an ordered sequence of points and all of the line segments connecting adjacent points. On the map above, the Market-Frankford and Broad Street train routes are represented as lines (actually multilines, which we will address that shortly). A line has legnth, but no width.

Since lines are made up of straight line segments, twists and turns a line require a lot of small line segments to accurately represent their geometry. While the Broad Street Line might look straight enough on the map, it is comprised of over 200 line segments!

Much like with points, which objects are represented as lines can depend on both the available data and the goal of your research. A road might be represented as a line when you are studying how children commute to school on a bus and are interested in the distance they travel. A similar study looking at children crossing large streets on the way to school might need additional information on how wide each street is. In that case, it could be helpful to represent streets not as lines but as polygons.

Polygons
-------

A polygon is a region encircled by a line that starts and ends at the same point. Each of the grey regions in the map above, representing zip codes, is a polygon. While the boundaries of these regions look curved, they are in fact made up of hundreds of straight line segments. A polygon has an inside and an outside. Its boundary is a line and it is possible to calculate the area of the polygon.

In theory, and with enough location data, you could represent every feature as a polygon. However this is extremely computationally intensive and might add a lot of work (for both the computer and the person operating it) without much added benefit. Even if the footprint of each train station were available for the map above, using those polygons would not improve the quality of this map since they would be too small to be visible.

Multipoints, Multilines, and Multipolygons
----------

Geospatial data doesn't always cleanly fit into a single point, line, or polygon. The orange Broad Street Line on the map above actually has a small loop at its northern end, and a "spur" just north of where it meets the Market-Frankford Line. These attributes can't be stored as a single ordered sequence of line segments, so they appear in the data files as multilines.

![Broad Street Line](media/broad_street_line.jpg)

A **multiline** is a collection of two or more lines that make up a single geographic feature. Many rivers are multilines to account for tributaries flowing into the main river.

Similar to multilines are multipolygons. A **multipolygon** is a collection of two or more polygons that form a single geographic region. The US state of Michigan is usually represented as a multipolygon since it is separated into two parts by the Great Lakes and no single line could enclose both parts.

A **multipoint** is a collection of two or more points. Multipoints can be an extremely helpful data structure for some of the more complicated geographic analyses. For example if you want to know how far an address is from a subway station, you could create a multipoint of all of the stations and find the distance from that multipoint to the address. Without the multipoint, you would need to find the distance from the address to each of the stations and then find the minimum distance.

<div class = "learnmore">

Software programs sometimes use different names for some shapes. For example QGIS calls a line containing more than two points a [polyline](https://docs.qgis.org/3.22/en/docs/gentle_gis_introduction/vector_data.html#polyline-features-in-detail).

</div>

## Displaying Data

Now that you know what goes into the outlines of a map, you likely want to use a map to display your data. Perhaps you have data on the locations of car accidents, or household income by neighborhood, or maybe you have addresses of households in which children have childhood asthma. You will need to use other elements to communicate the data you care about.

Before we look at other ways to communicate data, let's take a look at what we can see with just shapes:

Dot Distribution Map
-----------------
A dot distribution map lets you display the location of many individual, related events. Using data from [OpenDataPhilly](https://www.opendataphilly.org/dataset/vehicular-crash-data) we can plot every reported vehicular crash from 2019:

![Philadelphia is outlined in grey and covered in tiny blue dots. The dots are most concentrated along large roadways and trace out partial street map of the city.](media/2019_crashes.jpg)

In this section we will discuss other elements of maps, and learn about types of maps that use these elements to display data.


### Colors


<div class = "warning">

Not everyone can distinguish colors. While colors can be a powerful tool, if colors are the only way your are distinguishing features on your map, those differences will be invisible to some of your audience.

</div>

While color isn't universally accessible, it is still an important way tool for distinguish features from each other on a map.

Hue
------

When choosing what color a certain feature should be, it is important to consider the larger context of the map. Our map of Philadelphia made the two train lines orange and blue, which are the colors used on both the signs and the train cars on those lines. While our map could have used other colors, that might have been visually confusing for people familiar with these trains.  

A more universal example is the convention that bodies of water are colored blue. Unless you have a good reason to use other colors, stick to this convention to avoid confusing your audience.


Intensity
---------

You can convey a lot of information with a single color by varying its intensity. A map showing ocean depth might be a deeper, darker blue where the water is deep, and a lighter shade where the water is shallow.

Using color intensity rather than changing hues to show differences can make a map more accessible to some readers.

---

**Two types of maps that rely primarily on color for displaying data are heat maps and choropleth maps.**

Heat Maps
---------

A heat map is a useful way to show how points cluster together. This heat map uses the same Philadelphia vehicle [crash data](https://www.opendataphilly.org/dataset/vehicular-crash-data) from 2019 from before:

![Zip code boundaries of Philadelphia are outlined in black and bright colors, ranging from red to blue, blur into each other across the map. A large red region appears in the center, as do smaller reddish-orange regions in the upper right, and lower left of the city, with several orange and yellow regions scattered throughout. In between, the color fades to greens and blues, with the edge of the map surrounded by light blue.](media/2019_crashes_heat_map.png)


Instead of showing each individual crash, this map assigns colors based on how many of the crash locations are within a fixed distance. The brighter red you see on the map, the more crashes were close to that point. Green and blue colors are near to fewer crashes.

This map can show us interesting information, and also mislead if it isn't in the proper context. We are only looking at crashes inside the city, so this heat map may lead to the mistaken assumption that there are fewer crashes near the edge of the city because even though based on the data from within the city those areas are lighter colors. On the other hand, the redder region in the lower left of the map is where several highways converge near the Philadelphia airport, so that concentration of crashes might be a real observation.

Choropleth Maps
-----------
A choropleth map (pronounced "koro-pleth") colors map regions based on data. These maps may be familiar as they are frequently used by news organizations to display both political news, like election results, and public health news, like rates of Covid-19.



### Sizes
Graduated symbol maps
--------------
(https://gisgeography.com/dot-distribution-graduated-symbols-proportional-symbol-maps/#:~:text=Graduated%20symbol%20maps%20and%20proportional%20symbol%20maps%20scale%20the%20size,instead%20of%20scaling%20them%20larger.)

Proportional symbol maps
--------------

Cartograms
------------
(kind of a weird one...)

### Language

Words
numbers
Legends and keys

### Reference tables

This page is meant to summarize the vocabulary and concepts of this section.

Elements of Maps
--------------


Types of Maps
--------------

Dot Distribution
Heat Map
Choropleth
Graduated Symbol Map
Proportional Symbol Map
Cartogram

## Quiz

Which of the following statements about latitude and longitude are TRUE?

[[X]] Every location on Earth can be described using latitude and longitude.
[[ ]] The location of equator was an arbitrary decision made by historical map makers.
[[X]] Locations north of the equator are represented by positive latitudes and locations south of the equator are represented by negative latitudes.
[[ ]] Locations east of the prime meridian are represented by positive longitudes and locations west of the prime meridian are represented by negative longitudes.
***

<div class = "answer">

Every location on Earth can be described using latitude and longitude. Positive latitudes are north of the equator and positive longitudes are east of the prime meridian while negative latitudes and longitudes are to the south and west, respectively. While the location of the prime meridian was chosen for historical reasons, the location of the equator is fixed by the planet's rotation.

</div>
***


Which types of geometry might be appropriate to represent a hospital? Select all possibilities.

[[X]] Point
[[X]] Multipoint
[[ ]] Line
[[ ]] Multiline
[[X]] Polygon
[[X]] Multipolygon
***
<div class = "answer">

The type of geometry depends on both the structure of the hospital, and the reason you are interested in it.

If you care about where the hospital is located in a city or country, a point might be an appropriate geometry. If the hospital has multiple locations, a multipoint could capture all of those locations.

If you are studying how the hospital building interacts with the surrounding neighborhood, it may be better to use a polygon representation of the footprint of the hospital. If the hospital has several buildings, a mulitpolygon geometry can include all of the buildings.

</div>
***

## Additional Resources

The last section of the module content should be a list of additional resources, both ours and outside sources, including links to other modules that build on this content or are otherwise related.

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Elements+of+Maps%22)!

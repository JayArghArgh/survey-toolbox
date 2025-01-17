# Survey Toolbox
> Coordinate mathematics and tools for surveyors and game-makers (currently) working in flat plane.

Simple mathematics library for working with coordinates.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Installation

Python:

```sh
pip install surveyor-toolbox
```

## Usage example

```python
# Declare some constants.
from surveytoolbox.config import EASTING, NORTHING, ELEVATION, BEARING, DIST_2D, DIST_3D

# Import functions.
from surveytoolbox.PointStore import NewPointStore
from surveytoolbox.SurveyPoint import NewSurveyPoint

from surveytoolbox.bdc import bearing_distance_from_coordinates
from surveytoolbox.cbd import coordinates_from_bearing_distance
from surveytoolbox.fmt_dms import format_as_dms

# Start a point store so you can track your points.
pointStore = NewPointStore()

# Create some points and add to point store.
point_1 = NewSurveyPoint("JRR")
pointStore.set_new_point(point_1)

point_2 = NewSurveyPoint("JayArghArgh")
pointStore.set_new_point(point_2)

# Start playing
point_1.set_vertex(
    {
        EASTING: 100,
        NORTHING: 100,
        ELEVATION: 30
    }
)

point_2.set_vertex(
    {
        EASTING: 200,
        NORTHING: 100,
        ELEVATION: 30
    }
)

# Calculate and print the bearing and distance between two points.
target_loc = bearing_distance_from_coordinates(point_1.get_vertex(), point_2.get_vertex())
print(
    f"Bearing: {format_as_dms(target_loc[BEARING])}"
    f"\nDistance (2d): {target_loc[DIST_2D]}"
    f"\nDistance (3d): {target_loc[DIST_3D]}"
)

# Create a new point using the provided bearing and distance (it shoudl duplicate point 2)
point_3 = NewSurveyPoint("JRR2110141000")
pointStore.set_new_point(point_3)

point_3.set_vertex(
    coordinates_from_bearing_distance(
        point_1.get_vertex(),
        target_loc[BEARING],
        target_loc[DIST_2D]
    )
)

# Uncomment this for an example of listing specific information for all points.
current_points = pointStore.get_point_store()
for k, v in current_points.items():
    print(
        f"{current_points[k].get_point_name()}: {current_points[k].get_vertex()}"
    )

```
Here's a bearing example
```python
from surveytoolbox.config import EASTING, NORTHING, ELEVATION, BEARING

# Import functions

from surveytoolbox.SurveyPoint import NewSurveyPoint
from surveytoolbox.bdc import bearing_distance_from_coordinates
from surveytoolbox.fmt_dms import format_as_dms

point_1 = NewSurveyPoint("JRR")
point_2 = NewSurveyPoint("JayArghArgh")

point_1.set_vertex(
    {
        EASTING: 100,
        NORTHING: 100,
        ELEVATION: 30
    }
)

point_2.set_vertex(
    {
        EASTING: 200,
        NORTHING: 300,
        ELEVATION: 30
    }
)


# Calculate and print the bearing and distance between two points.
target_loc = bearing_distance_from_coordinates(point_1.get_vertex(), point_2.get_vertex())
print(
    target_loc
)

print(format_as_dms(target_loc[BEARING]))
```


_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History
* 0.0.3
    * Removed python-math... actually doesn't require it (DOH!)
* 0.0.2
    * Fix python-math import in setup.
* 0.0.1
    * Work in progress

## Meta

Justin – [@hopBuddyHop](https://twitter.com/hopBuddyHop) – jayarghargh @ gee mail

Distributed under the MIT license. See [MIT LICENCE](LICENCE-URL) for more information.

[https://github.com/JayArghArgh](https://github.com/JayArghArgh)

## Contributing

1. Fork it (<https://github.com/JayArghArgh/surveytoolbox/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->

[comment]: <> ([npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square)
[comment]: <> ([npm-url]: https://npmjs.org/package/datadog-metrics)
[comment]: <> ([npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square)
[comment]: <> ([travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square)
[comment]: <> ([travis-url]: https://travis-ci.org/dbader/node-datadog-metrics)
[licence-url]: https://opensource.org/licenses/MIT
[wiki]: https://github.com/JayArghArgh/surveytoolbox/wiki

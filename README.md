# General Midway Equalization #

Python implementation of general midway equalization using arbitrary number of grayscale images.

Example runs using N={2,3,4} grayscale images avaliable in jypitor notebook

`general_midway_equalization.ipynb`

It is a requirement that all images have same dimensions.

## Very short intuitions behind code ##


For further describtions and alternative methods I refer [[1]](#1).

Refer to `utils/functions.py` for detail implementation.

## How to run existing code ##

* __Step 1__: Open `general_midway_equalization.ipynb`.
* __Step 2__: Load N number grayscale images and make sure they all have same dimension. Stack them on top of each others either in a list or array.
* __Step 3__: Run codes from `utils/functions.py` and plot results.

Try it out yourself, and if you have any question don't hesitates to create an issue. Cheers!


## References ##

<a id="1">[1]</a> 
Thierry Guillemot and Julie Delon. _Implementation of the Midway Image Equalization_. In: "Image Processing On Line", 6 (2016), pp. 114-129. DOI: [10.5201/ipol.2016.140](http://www.ipol.im/pub/art/2016/140/?utm_source=doi "Named link title")

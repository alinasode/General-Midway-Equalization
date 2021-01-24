# General Midway Equalization #

Python implementation of general midway equalization using arbitrary number of grayscale images.

Example runs using N={2,3,4} grayscale images avaliable in jypitor notebook

`general_midway_equalization.ipynb`

It is a requirement that all images have same dimensions.

## Very short intuitions behind code ##




The midway specification method can be generalized to N arbitrary number of images. Specifically,

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cvarphi%20%28x%29%20%3D%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum_%7Bp%3D1%7D%5E%7BN%7D%20C_%7Bp%7D%5E%7B-1%7D%28x%29%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\varphi (x) = \frac{1}{N} \sum_{p=1}^{N} C_{p}^{-1}(x)" width="165" height="54" />


where <img src="http://www.sciweavers.org/tex2img.php?eq=%5Ctilde%7BI%7D_p%20%3D%20%5Cvarphi%20%5Cbig%28%20C_p%20%28I_p%29%20%5Cbig%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\tilde{I}_p = \varphi \big( C_p (I_p) \big)" width="114" height="24" />


I Refer to `utils/functions.py` for detail implementation. And for further describtions and alternative methods I refer [[1]](#1).

## How to run existing code ##

* __Step 1__: Open `general_midway_equalization.ipynb`.
* __Step 2__: Load N number grayscale images and make sure they all have same dimension. Stack them on top of each others either in a list or array.
* __Step 3__: Run codes from `utils/functions.py` and plot results.

Try it out yourself, and if you have any question don't hesitates to create an issue. Cheers!


## References ##

<a id="1">[1]</a> 
Thierry Guillemot and Julie Delon. _Implementation of the Midway Image Equalization_. In: "Image Processing On Line", 6 (2016), pp. 114-129. DOI: [10.5201/ipol.2016.140](http://www.ipol.im/pub/art/2016/140/?utm_source=doi "Named link title")

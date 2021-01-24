# General Midway Equalization #

Python implementation of general midway equalization using arbitrary number of grayscale images, <img src="https://render.githubusercontent.com/render/math?math=N \geq 2">.

Example runs using <img src="https://render.githubusercontent.com/render/math?math=N=\{2,3,4\}"> grayscale images avaliable in the following jypitor notebook

```
general_midway_equalization.ipynb
```

It is a requirement that all images have same dimensions.

## Very short intuition behind code ##

Let <img src="https://render.githubusercontent.com/render/math?math=C"> denotes the normalized culumative histogram of a grayscale image, <img src="https://render.githubusercontent.com/render/math?math=I">, and <img src="https://render.githubusercontent.com/render/math?math=C^{-1}"> the pseudo-inverse of <img src="https://render.githubusercontent.com/render/math?math=C">.
 
The midway specification method can be generalized to _N_ arbitrary number of images. Specifically

<img src="https://render.githubusercontent.com/render/math?math=\varphi (x) = \frac{1}{N} \sum_{p=1}^{N} C_{p}^{-1}(x)">

where <img src="https://render.githubusercontent.com/render/math?math=\tilde{I}_n = \varphi \big( C_n (I_n) \big)"> for <img src="https://render.githubusercontent.com/render/math?math=n \in \{1,...,N \}"> and  <img src="https://render.githubusercontent.com/render/math?math=p \in \{1,...,N \}">.

I refer to `utils/functions.py` for detailed implementation. 
For further describtions and alternative methods I refer to [[1]](#1).

## How to run existing code ##

* __Step 1__: Open `general_midway_equalization.ipynb`.
* __Step 2__: Load _N_ number grayscale images and make sure they all have same dimension. Stack them on top of each others either in a list or array.
* __Step 3__: Run codes from `utils/functions.py` and plot results.

Try it out yourself, and if you have any question don't hesitates to create an issue. Cheers!


## References ##

<a id="1">[1]</a> 
Thierry Guillemot and Julie Delon. _Implementation of the Midway Image Equalization_. In: "Image Processing On Line", 6 (2016), pp. 114-129. DOI: [10.5201/ipol.2016.140](http://www.ipol.im/pub/art/2016/140/?utm_source=doi "Named link title")

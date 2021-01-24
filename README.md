require 'kramdown'

# General Midway Equalization #

Python implementation of general midway equalization using arbitrary number of grayscale images.

Example runs using N={2,3,4} grayscale images avaliable in jypitor notebook

`general_midway_equalization.ipynb`

It is a requirement that all images have same dimensions.

## Very short intuitions behind code ##

$$
M = \left( \begin{array}{ccc}
x_{11} & x_{12} & \ldots \\
x_{21} & x_{22} & \ldots \\
\vdots & \vdots & \ldots \\
\end{array} \right)
$$


The midway specification method can be generalized to N arbitrary number of images. Specifically

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cvarphi%20%28x%29%20%3D%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum_%7Bp%3D1%7D%5E%7BN%7D%20C_%7Bp%7D%5E%7B-1%7D%28x%29%0A%0Awhere%20%24%5Ctilde%7BI%7D_n%20%3D%20%5Cvarphi%20%5Cbig%28%20C_n%20%28I_n%29%20%5Cbig%29%24%2C%20for%20%24n%20%5Cin%20%5C%7B1%2C...%2CN%20%5C%7D%24%20and%20%24p%20%5Cin%20%5C%7B1%2C...%2CN%20%5C%7D%24.&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\varphi (x) = \frac{1}{N} \sum_{p=1}^{N} C_{p}^{-1}(x)where $\tilde{I}_n = \varphi \big( C_n (I_n) \big)$, for $n \in \{1,...,N \}$ and $p \in \{1,...,N \}$." width="518" height="96" />

 $$C$$ denotes the normalized culumative histogram of a grayscale image and $C^{-1}$ the pseudo-inverse of $C$.

I Refer to `utils/functions.py` for detailed implementation. And for further describtions and alternative methods I refer [[1]](#1).

## How to run existing code ##

* __Step 1__: Open `general_midway_equalization.ipynb`.
* __Step 2__: Load N number grayscale images and make sure they all have same dimension. Stack them on top of each others either in a list or array.
* __Step 3__: Run codes from `utils/functions.py` and plot results.

Try it out yourself, and if you have any question don't hesitates to create an issue. Cheers!


## References ##

<a id="1">[1]</a> 
Thierry Guillemot and Julie Delon. _Implementation of the Midway Image Equalization_. In: "Image Processing On Line", 6 (2016), pp. 114-129. DOI: [10.5201/ipol.2016.140](http://www.ipol.im/pub/art/2016/140/?utm_source=doi "Named link title")

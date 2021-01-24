import numpy as np

def cumHist(Img):
    """
    Takes as input a gray scale image.
    Returns its normalized cumulative histogram.
    """
    pdf, _ = np.histogram(Img, bins=range(257))
    cdf = np.cumsum(pdf).astype(float)
    cdf = cdf / np.sum(pdf)
    return cdf

def psuedo_inv(CDF, val):
    """
    Takes as input any cumulative histogram (CDF) defined on interval {0, ..., 255}, 
    and some value in [0,1].
    Returns the pseudo-inverse of any given CDF.
    """
    res = np.min(np.where(CDF >= val))
    return res

def fp_img(Img, CDF):
    """
    Takes as input a grayscale image, and its cumulative histogram (CDF).
    Returns its floating-point image C(I) where the intensity at each pixel (i, j) is CDF(I(i, j)).
    """
    new_Img = np.zeros_like(Img)
    new_Img = CDF[Img]
    return new_Img

def general_midway_equalization(N_imgs):
    """
    Input: Takes as input arbitrary number, N, of gray scale images appended in a list or numpy array.
           Requirement for all images to have same dimensions. 
    
    Output: Returns the midway equalization between all those images stacked in a
            numpy array (N, height, width), as well as their equalizated CDF's, also in a numpy array.
    """
    
    # compute the corresponding cumulative histograms (CDFs) of all N images:
    CDFs = []
    for k in range(len(N_imgs)):
        CDFs.append(cumHist(N_imgs[k]))

    res_N_imgs = []
    for x in range(len(N_imgs)):
        res = 0
        for p in range(len(N_imgs)):
            # compute psedu inverse
            inv_CDF = np.empty_like(CDFs[p])
            for i in range(255):
                inv_CDF[i] = psuedo_inv(CDFs[p], CDFs[x][i])
            
            # compute midway equalization (using floating-point):
            res += fp_img(N_imgs[x], inv_CDF)
        res *=  1 / len(N_imgs)
    
        # append to list:
        res_N_imgs.append(res)
    
    # compute corresponding equalizated CDF's:
    res_CDFs = []
    for k in range(len(res_N_imgs)):
        res_CDFs.append(cumHist(res_N_imgs[k]))
        
    return np.array(res_N_imgs), np.array(res_CDFs)
import numpy as np
import pytest
from scipy.signal import convolve2d
from scipy import ndimage as ndi
from skimage._shared.testing import fetch
from skimage.color import rgb2gray
from skimage.data import astronaut, camera
from skimage import restoration, util
from skimage.restoration import uft

test_img = util.img_as_float(camera())


def test_wiener():
    psf = np.ones((5, 5)) / 25
    data = convolve2d(test_img, psf, 'same')
    np.random.seed(0)
    data += 0.1 * data.std() * np.random.standard_normal(data.shape)
    deconvolved = restoration.wiener(data, psf, 0.05)

    path = fetch('restoration/tests/camera_wiener.npy')
    np.testing.assert_allclose(deconvolved, np.load(path), rtol=1e-3)

    _, laplacian = uft.laplacian(2, data.shape)
    otf = uft.ir2tf(psf, data.shape, is_real=False)
    deconvolved = restoration.wiener(data, otf, 0.05,
                                     reg=laplacian,
                                     is_real=False)
    np.testing.assert_allclose(np.real(deconvolved),
                               np.load(path),
                               rtol=1e-3)


def test_unsupervised_wiener():
    psf = np.ones((5, 5)) / 25
    data = convolve2d(test_img, psf, 'same')
    np.random.seed(0)
    data += 0.1 * data.std() * np.random.standard_normal(data.shape)
    deconvolved, _ = restoration.unsupervised_wiener(data, psf)

    path = fetch('restoration/tests/camera_unsup.npy')
    np.testing.assert_allclose(deconvolved, np.load(path), rtol=1e-3)

    _, laplacian = uft.laplacian(2, data.shape)
    otf = uft.ir2tf(psf, data.shape, is_real=False)
    np.random.seed(0)
    deconvolved = restoration.unsupervised_wiener(
        data, otf, reg=laplacian, is_real=False,
        user_params={"callback": lambda x: None})[0]
    path = fetch('restoration/tests/camera_unsup2.npy')
    np.testing.assert_allclose(np.real(deconvolved),
                               np.load(path),
                               rtol=1e-3)


def test_image_shape():
    """Test that shape of output image in deconvolution is same as input.

    This addresses issue #1172.
    """
    point = np.zeros((5, 5), float)
    point[2, 2] = 1.
    psf = ndi.gaussian_filter(point, sigma=1.)
    # image shape: (45, 45), as reported in #1172
    image = util.img_as_float(camera()[65:165, 215:315]) # just the face
    image_conv = ndi.convolve(image, psf)
    deconv_sup = restoration.wiener(image_conv, psf, 1)
    deconv_un = restoration.unsupervised_wiener(image_conv, psf)[0]
    # test the shape
    np.testing.assert_equal(image.shape, deconv_sup.shape)
    np.testing.assert_equal(image.shape, deconv_un.shape)
    # test the reconstruction error
    sup_relative_error = np.abs(deconv_sup - image) / image
    un_relative_error = np.abs(deconv_un - image) / image
    np.testing.assert_array_less(np.median(sup_relative_error), 0.1)
    np.testing.assert_array_less(np.median(un_relative_error), 0.1)


def test_richardson_lucy():
    psf = np.ones((5, 5)) / 25
    data = convolve2d(test_img, psf, 'same')
    np.random.seed(0)
    data += 0.1 * data.std() * np.random.standard_normal(data.shape)
    deconvolved = restoration.richardson_lucy(data, psf, 5)

    path = fetch('restoration/tests/camera_rl.npy')
    np.testing.assert_allclose(deconvolved, np.load(path), rtol=1e-3)


@pytest.mark.parametrize('dtype_image', [np.float32, np.float64])
@pytest.mark.parametrize('dtype_psf', [np.float32, np.float64])
def test_richardson_lucy_filtered(dtype_image, dtype_psf):
    if dtype_image == np.float64:
        atol = 1e-8
    else:
        atol = 1e-5
    test_img_astro = rgb2gray(astronaut())

    psf = np.ones((5, 5), dtype=dtype_psf) / 25
    data = convolve2d(test_img_astro, psf, 'same')
    data = data.astype(dtype_image, copy=False)

    deconvolved = restoration.richardson_lucy(data, psf, 5,
                                              filter_epsilon=1e-6)
    assert deconvolved.dtype == data.dtype

    path = fetch('restoration/tests/astronaut_rl.npy')
    np.testing.assert_allclose(deconvolved, np.load(path), rtol=1e-3,
                               atol=atol)


if __name__ == '__main__':
    from numpy import testing
    testing.run_module_suite()

import pickle
import blosc
import numpy

COMPRESS_FASTEST = 0
COMPRESS_BEST = 1


def compress(data, compress_type=COMPRESS_FASTEST, nthreads=blosc.ncores):
    assert isinstance(data, bytes)
    blosc.set_nthreads(nthreads)

    compressor = "lz4" if compress_type == COMPRESS_FASTEST else "zstd"
    level = 1 if compress_type == COMPRESS_FASTEST else 5
    return blosc.compress(data, cname=compressor, clevel=level)


def decompress(binary):
    assert isinstance(binary, bytes)
    return blosc.decompress(binary)


def compress_ndarray(vectors, compress_type=COMPRESS_FASTEST, nthreads=blosc.ncores):
    assert isinstance(vectors, numpy.ndarray)
    blosc.set_nthreads(nthreads)

    compressor = "lz4" if compress_type == COMPRESS_FASTEST else "zstd"
    level = 1 if compress_type == COMPRESS_FASTEST else 5
    buffer = blosc.compress_ptr(
        vectors.__array_interface__['data'][0],
        vectors.size,
        vectors.dtype.itemsize,
        clevel=level,
        cname=compressor,
        shuffle=blosc.BITSHUFFLE

    )
    return pickle.dumps([buffer, vectors.dtype, vectors.shape])


def decompress_ndarray(binary):
    buffer, dtype, shape = pickle.loads(binary)
    arr = numpy.empty(shape, dtype)
    blosc.decompress_ptr(buffer, arr.__array_interface__['data'][0])
    return arr

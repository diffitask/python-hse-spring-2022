import numbers
import numpy as np


class AddToFileMixin:
    def add_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.__str__())


class MakeStrMixin:
    def to_str(self):
        return self.value.__str__()

class GetterSetterMixin:
    @property
    def data(self):
        return self.data

    @property
    def size(self):
        return self.size

    @property
    def real(self):
        return self.real

    @data.setter
    def data(self, other_value):
        self.value = other_value

class MatrixNumpy(np.lib.mixins.NDArrayOperatorsMixin, MakeStrMixin, AddToFileMixin, GetterSetterMixin):
    def __init__(self, value):
        self.value = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MatrixNumpy,)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, MatrixNumpy) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, MatrixNumpy) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.value)

    def __str__(self):
        return self.to_str()
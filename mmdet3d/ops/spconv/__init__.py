# Copyright (c) OpenMMLab. All rights reserved.
from .overwrite_spconv.write_spconv2 import register_spconv2

try:
    import spconv
    # import spconv.pytorch as spconv
except ImportError:
    IS_SPCONV2_AVAILABLE = False
else:
    if hasattr(spconv, '__version__') and spconv.__version__ >= '2.0.0':
        IS_SPCONV2_AVAILABLE = register_spconv2()
    else:
        IS_SPCONV2_AVAILABLE = False
print(IS_SPCONV2_AVAILABLE)
__all__ = ['IS_SPCONV2_AVAILABLE']

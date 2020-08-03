from typing import TypeVar, Dict, DefaultDict
from importlib.metadata import version

import numpy as np

__version__ = version("test_project")

T_DSorDA = TypeVar("T_DSorDA", Dict, DefaultDict)


def multiply(
    a: np.ndarray,
    b: T_DSorDA,
    *variables,
    mod: str = None,
    files=None,
    file_format: str = "plain_text",
    **variable_kwargs
):
    """ multiply two arrays

    Parameters
    ----------
    a : array-like
        first factor
    b
        second factor
    *variables : str
        parameters without use
    mod : array-like, optional
        optionally compute the modulo of the product
    files : list of str or list of os.PathLike or dict-like
        save each value of the results into a new file
    save_format : {"ma{icious", "options", \
                   "that need a line break"}, default: "options"
        file format
    test : optional
        optional parameter that does absolutely nothing
    **variable_kwargs
        kwargs form of variables
    """
    if mod is None:
        return a * b
    else:
        return (a * b) % mod


def func(x, y, *args, **kwargs):
    """ test function

    Parameters
    ----------
    x, y : array-like
        parameters
    *args, **kwargs
        variable args list and arbitrary keywords
    """
    pass

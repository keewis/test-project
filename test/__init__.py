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

    Returns
    -------
    array-like
        the dot product of the input values
    """
    pass


def func2(x, y):
    """ second test function

    Parameters
    ----------
    x : int, float or complex
        first factor
    y : int, float or complex
        second factor

    Raises
    ------
    ValueError
        if both are 0

    Returns
    -------
    product : int, float or complex
        the product of x and y
    sum : int, float or complex
        the sum of x and y

    See Also
    --------
    pandas.DataFrame.sum, xarray.Dataset.sum, pandas.Series.sum, xarray.DataArray.sum
    """
    if x == 0 and y == 0:
        raise ValueError

    return x * y, x + y


class MyClass:
    def method1(self, x):
        """ first test method

        Parameters
        ----------
        x : int
            description of x

        See Also
        --------
        MyClass.method2, func, func2, DataFrame.sum
        """
        return x

    def method2(self, y):
        """ second test method

        Parameters
        ----------
        y : float
            description of y

        See Also
        --------
        MyClass.method1, func, func2
        """
        return y

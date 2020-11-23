from typing import TypeVar, Dict, DefaultDict
from importlib.metadata import version

import numpy as np

try:
    __version__ = version("test_project")
except Exception:
    __version__ = "999"

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


def lock(timeout, requested_key) -> str:
    """Establish a shared lock to the resource.

    Parameters
    ----------
    timeout : Union[float, Literal["default"]], optional
        Absolute time period (in milliseconds) that a resource waits to get
        unlocked by the locking session before returning an error.
        Defaults to "default" which means use self.timeout.
    requested_key : Optional[str], optional
        Access key used by another session with which you want your session
        to share a lock or None to generate a new shared access key.

    Returns
    -------
    str
        A new shared access key if requested_key is None, otherwise, same
        value as the requested_key

    """


def dump_model(self, num_iteration=None, start_iteration=0, importance_type='split'):
    """Dump Booster to JSON format.

    Parameters
    ----------
    num_iteration : int or None, optional (default=None)
        Index of the iteration that should be dumped.  If None, if the best
        iteration exists, it is dumped; otherwise, all iterations are dumped.
        If <= 0, all iterations are dumped.
    start_iteration : int, optional (default=0)
        Start index of the iteration that should be dumped.
    importance_type : string, optional (default="split")
        What type of feature importance should be dumped.  If "split", result
        contains numbers of times the feature is used in a model.  If "gain",
        result contains total gains of splits which use the feature.
    Returns
    -------
    json_repr : dict
        JSON format of Booster.
    """

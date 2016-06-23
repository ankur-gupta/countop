countop
--------

Count the number of operations in your algorithm implementation.
For example, you can use to determine exactly how many comparisons are
required by a sorting algorithm. See
`Jupyter notebook example <https://github.com/ankur-gupta/countop/blob/master/countop/examples/selection_sort.ipynb>`_
that verifies the complexity of selection sort.


============
Installation
============

This package exists on `PyPI <https://pypi.python.org/pypi/countop>`_.
You can install it using `pip`::

    pip install countop

============
Demo
============

Here is a quick demo of how this package works::

    >>> from countop import Integer
    >>> print Integer.reset_counts()
    >>> print Integer.additions()
    # 0
    >>> a = Integer(1)
    >>> b = a + 1
    >>> print Integer.additions()
    # 1


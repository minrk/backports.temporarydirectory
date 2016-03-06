# Backport of Python 3 tempfile.TemporaryDirectory

Backports Python 3 [tempfile.TemporaryDirectory](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory)

## Usage

```python
try:
    from tempfile import TemporaryDirectory
except ImportError:
    from backports.temporarydirectory import TemporaryDirectory
```

Pyvolve
============

Pyvolve is an open-source Python module for simulating sequences along a phylogenetic tree according to continuous-time Markov models of sequence evolution. **Please ensure you are using the most up-to-date version of Pyvolve! The current version is 1.1.0.**

> **Note:** This is a Python 3.13-compatible fork of the original [sjspielman/pyvolve](https://github.com/sjspielman/pyvolve) repository, updated with modern packaging standards and full support for Python 3.8-3.13.

A detailed user manual for Pyvolve is available [here](https://github.com/sjspielman/pyvolve/raw/master/user_manual/pyvolve_manual.pdf), and API documentation for Pyvolve is available at [https://sjspielman.github.io/pyvolve](https://sjspielman.github.io/pyvolve).

Pyvolve has several dependencies:
* [Biopython](http://biopython.org/wiki/Download) (>= 1.80)
* [Scipy](http://www.scipy.org/install.html) (>= 1.9.0)
* [Numpy](http://www.scipy.org/install.html) (>= 1.23.0)

**Python Version Support:** Pyvolve supports Python 3.8+ including the latest Python 3.13. The following examples assume Python3 (which you may have on your computer named as `python3` and not `python`!)

## Installation

### Install from PyPI (Original Version)
To install the original version from PyPI:
```bash
pip install pyvolve
```

### Install from This Fork (Python 3.13 Compatible)
To install this Python 3.13-compatible fork directly from GitHub:
```bash
pip install git+https://github.com/cbsither/pyvolve.git
```

### Install from Source (Development)
To install from source for development:
```bash
git clone https://github.com/cbsither/pyvolve.git
cd pyvolve
pip install -e .
```

### Running Tests
To run the test suite:
```bash
python -m unittest discover -s tests -p "*_test.py"
```

## Issues and Support

For issues related to this Python 3.13-compatible fork, please file issues at: [https://github.com/cbsither/pyvolve/issues](https://github.com/cbsither/pyvolve/issues)

For issues with the original version, please visit: [https://github.com/sjspielman/pyvolve/issues](https://github.com/sjspielman/pyvolve/issues)

## Citation

*If you use Pyvolve in your research, please cite the following:* <br>
Spielman, SJ and Wilke, CO. 2015. [**Pyvolve: A flexible Python module for simulating sequences along phylogenies**](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0139047). PLOS ONE. 10(9): e0139047.

```bibtex
@article{SpielmanWilke2015,
author = {Spielman, S. J. and Wilke, C. O.},
title = {Pyvolve: A Flexible Python Module for Simulating Sequences along Phylogenies},
journal = {PLOS ONE},
year = {2015},
volume = 10,
pages = {e0139047}
}
```

## What's New in This Fork

- ✅ Full Python 3.8-3.13 support
- ✅ Modern packaging with `pyproject.toml` (PEP 517/518)
- ✅ Updated dependencies (numpy>=1.23.0, scipy>=1.9.0, biopython>=1.80)
- ✅ Fixed deprecated unittest methods
- ✅ GitHub Actions CI/CD for automated testing
- ✅ Enhanced documentation



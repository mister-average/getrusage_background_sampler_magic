from setuptools import setup, find_packages
import site

setup(
    name='getrusage_background_sampler_magic',
    version='0.0.1',
    description='Jupyter cell magic that uses psutil in a background process to collect performance info and plotly and pandas to display it.',
    url='http://github.com/mister-average/getrusage_background_sampler_magic',
    author='mister-average',
    author_email='mister_person@averageaddress.com',
    license='BSD',
    data_files=[('/', ['getrusage_background_sampler_magic.ipynb'])],
    python_requires='>=3.9'
)

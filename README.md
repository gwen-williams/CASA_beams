A script to read the beam information from a fits file using CASA.

The script manages the case where the fits file contains just one beam entry, or for some cubes for example where a beam is defined per channel. In the latter, the script returns the minimum, maximum and mean beam information.

## Dependencies

* numpy

## Usage

In CASA, one must first define the name of the .fits file like:

``` python

imagename = 'your_first_file.fits'

```

Then, to run the script, run:
'execfile("beams_script.py")'




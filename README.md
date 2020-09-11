TheEggCounter
=============

(c) 2014, 2020 Jorge Tornero, http://imasdemase.com @imasdemase

A tiny but effective application for counting objects over an image

What is it?
===========

TheEggCounter is a simple application for counting objects over a image. This involves placing markers over the object to visually ease the count so the objects are not counted twice.

The user is able to mark/unmark the objects, thus increasing/decreasing the count. After counting, the user is able to record the number of items and create a copy of the original image with the number of items counted on it.

History and motivation
----------------------
Counting objects on images, despite being a pretty simple task, usually involves the usage of complicated/expensive image analysis software, which usually carry licenses or hardware keys that makes difficult to share the software among many users. Using OSS software like ImageJ doesn't make it better because in both cases software is complicated for a simple task as counting objects over the image.

During the processing of the samples of a Daily Egg Production Method Survey on the European anchovy of the Gulf of Cadiz carried out in summer 2014, I realized that a very simple application for counting the hydrated eggs of the female hydrated gonads (a key step in the DEPM spawning biomass estimation proccess) could be the solution for the bottlenecks caused by having to share the image analysis system with other research groups, freeing the system of trivial tasks like counting eggs in favor of other activities, mainly taking pictures or performing complex analysis.

TheEggCounter can't beat automated counting of objects but **it is very appropiated where automated counting is not possible,** for instance in samples where segmentation is difficult or not posible at all. You can appreciate this difference with the image samples provided in this repository. While DEPM samples are difficult to perform an automated count, the flock image seems appropiate for such a task instead of using TheEggCounter.

Help
----

The operation is fairly simple: just click over an object to count it. A marker will we deployed over and the count increased. Right-click over a marker removes it from the image and decreases the count of objects. For more information check _About..._ in TheEggCounter menu. 

License
=======
TheEggCounter ir **released under GPL V3.0 license.** For further information please see http://www.gnu.org/licenses/gpl-3.0.html

Donations/Fees
==============
No donations/fees are required for the use of this software. However, if you want to reward me in some way, you can send me a postcard from where you live. It will be fun to show it to my kids!! In that case, you can mail me to get my postal address.
If you have money to burn, I'm sure you can help people around you, or donate some to your preferred charity/NGO. 

Translation
===========
English as well as Spanish translation for the GUI are provided. Feel free to contribute with your own translation if you want.

Installation
============
Dependencies
------------
To be able to run TheEggCounter from source you will need:

- Python 3.x, tested with 3.8
- PyQt5 libraries installed in your system

However, you can download a binary executable from the [latest release.](https://github.com/jtornero/TheEggCounter/releases/latest)

Installation
------------
In case you want to run TheEggCounter from source, download the files to a folder of your choice.

Then you can issue

    python3 TheEggCounter.py

to run TheEggCounter.

If yo downloaded a binary executable, just double click on it.

Citation
========
If you use TheEggCounter in a scientific research work, you could cite it as

Jorge Tornero (2014, 2020). TheEggCounter: A tiny but effective application for counting objects over an image. ZENODO. 10.5281/zenodo.4022391


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4022391.svg)](https://doi.org/10.5281/zenodo.4022391)



# Pixel Art App
This python program is made to emulate a pixel art android phone. It is intended to be used in [pydroid3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&gl=US) on android phones, other usages might be possible as well.

## Overview
This is an attempt to create an android app in python. Since there isn't a good way to convert pygame programs to an *.apk file, running directly on an interpreter is the way to go (such as termux with vnc or pydroid).
This app was made with pydroid in mind.

## Installation
Since pydroid comes with pygame, and since pygame is the only requirement (for now, check [Requirements](#requirement)), which comes preinstalled on pydroid3, you only need to have pydroid3 app installed on your phone.

## Usage
It is pretty simple, you have a board on the bottom with buttons on it, you can:
* Zoom in and out using the + and - buttons
* Move around in the zoomed in space.
* Choose a color from the box down
* Change the tool being used (more information will be provided regarding this, but for now feel free to experiment).
* Color a pixel or a number of pixels based on what mode you are using.
* Make a random image using "R".

## Screenshots
![icecream](/screenshots/icecream.jpg) ![cloud_9](/screenshots/cloud_9.jpg) ![test](/screenshots/test.jpg) ![random](/screenshots/random.jpg)
## Requirements
For now, the only requirement is pygame, although numpy will be needed in the future since it is crucial for some functionalities that will be added in the future.

## To-do
* Make use of auto screen scaling in pygame (so that the code is independent from resolution)
* Fix "bucket fill" functionality.
* Make better documentation.

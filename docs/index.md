# Documentation of movie consumption

Most of us watch a lot of movies. Concepts and key lines are used for cultural reference. Many of my friends refer to movies quite often, so I decided to review my [on consumption](https://hofkoh.de/2014/10/filmliste/). Starting in 2013 I recorded every movie I watched. Published [October 2014](https://hofkoh.de/2015/06/medienkonsum-die-zweite/). For some movies I could remember to have seen them in the cinema. This is a graph of recent movies according to their release year and the year I watched them:

![movies 2020](movies2020.png)

There is more to come ...

RFID reader for 125 kHz with 1602 display on Arduino. This is how our setup at the American International School Vietnam looks like:

<img src="../rfid/IMG_7966.jpg" width="45%"> <img src="IMG_7968.jpg" width="45%">

### The display encourages you to ...

<img src="display.jpg" width="45%">

And that's all the Arduino behind it. Next time we use plexiglas to be more transparent :)
<img src="backside.jpg" width="45%">


Find the code here:
(https://github.com/kreier/rfid-125/blob/master/arduino/rfid-125.ino)

## Materials

All materials were ordered at [CỬA HÀNG IC ĐÂY RỒI](https://icdayroi.com/). Total cost: 231.000₫ (10 US$). This is the list:

## Building steps

* Connect the RFID kit to the Arduino, as well as the 1602 with the I2C adapter and 4 wires
* Connections according to __link will follow__
* Upload the software found in the link above. Don't forget the library for the hd44780 controller and the hd44780_I2C expansion set. Files are located under library.

Got to [the wiki](https://github.com/matthiaskreier/rfid-125/wiki) for further details. We work on a new RTL-SDR to visualize the communication between the cards on the 125 kHz and 13.56 MHz frequency.

## Old pictures from 2018

![RFID reader](window.jpg)

The display encourages you to ...
![](https://github.com/matthiaskreier/rfid-125/blob/master/docs/display.jpg)

And that's all the Arduino behind it. Next time we use plexiglas to be more transparent :)
![](https://github.com/matthiaskreier/rfid-125/blob/master/docs/backside.jpg)

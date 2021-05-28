# Ranging using Ultrasonic Range Sensor and localization using arrows

## Ranging - Description
For autonomous vehicles, the perception subsystem typically consists of a camera, radar, sonar and lidar sensors. We have already discussed the role of Camera in our previous module. Now, we will discuss how to detect an obstacle ahead using an [Ultrasonic ranging sensor MAX3232](http://www.ti.com/lit/ds/symlink/max3232.pdf).

<div align="center">

![](_images/ultra.png)
*Ultrasonic Range sensor MAX3232- Texas Instruments*

</div>
<p> Please refer the datasheet for choosing resistors and connections </p>

# Pipeline
- Installing packages on RPi - PiCam.
- Record still image using picamera.
- Use MAX3232 to record 10 successive distance measurements between Pi and the object.
- Load the green arrow and read image.
- Take HSV masking for the arrow and detect the green part. After this, we write the code to detect corners.
- Based on count of number of vertices, we can estimate the direction in which the arrow is pointing.

<div align="center">

![](_images/ForAssignment4.png)

*Images with distances in consideration.*

</div>

<div align="center">

![](_images/hw4arrow.JPG)

*Green arrow (not the hero).*

</div>

<div align="center">

![](_images/direction.png)

*Direction detection.*

</div>


# Deliverable
- Final [YouTube video](https://youtu.be/iDpYUZIM0c0) to ensure RPi can properly track green color. We will further explore this in our later projects.

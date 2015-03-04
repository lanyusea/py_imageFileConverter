## A python image<->file converter

[idea source](http://www.zhihu.com/question/23188097/answer/24646217)

`我用python将二进制数据转化为图像，每个像素点可以表示3个字节，再将图像外围增加宽度为1的黑色边框，外面再增加宽度为1像素的白色边框，作为图像边界的标识符。`

This is a file to image and image to file converter that can be used to download code using screen capture when you work on remote desktop, from which you are forbidden to download file directly.

File will be read byte by byte and each byte will be stored into the r,g,b values of a pixel. Every pixel expresses one byte of file data(not three). Beyond the data area, which is a square there is a 1-pixel-length black boundary and a 1-pixel-length while boundray to identify the starting position of the data area.

---

1. Run on server side: <br>
`python encode.py filename image.png`

2. Do screen capture to store the image from server (Don't scale the image, keep it 100% size)
![image](https://cloud.githubusercontent.com/assets/2766729/6484419/bdd860ae-c2b6-11e4-98d9-c341559b8326.jpg)

3. Run on client: <br>
`python decode.py image.png filename`

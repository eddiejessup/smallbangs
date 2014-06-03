Title: Concatenate multiple png files into an x264-encoded movie
Date: 2013-06-04
Category: Programming
Tags: Shell, Movies

If you have a bunch of png files you want to convert into a movie, this is how you can do it via the video conversion tool mencoder, which comes with [mplayer](http://www.mplayerhq.hu):

```bash
mencoder mf://@fnames.txt -mf w=800:h=600:fps=24:type=png -ovc x264 -x264encopts crf=20 -oac copy -o output.avi
```

`fnames.txt` is a file containing a list of images to movie-fy, in sorted order. `w` and `h` are the pixel width and height of the input images, `fps` is the number of input images to show per second, and `crf` is a quality factor -- lower means better quality, bigger files. 20-30 is in the range of sensible values.

A benefit of using an input file is that you can sort your files beforehand, which is handy if they're named numerically without zero padding (`9.png`, `10.png`, `11.png` etc.), since bash's glob expansion doesn't sort these correctly -- if you used `*.png` as your input, the files would be processed out of order. Piping through sort,

```bash
ls *.png | sort -n > fnames.txt
```

solves the problem. `sort -n` is a numeric sort.

There's similar examples in mencoder's documentation, but they use lavc as the encoder instead of x264, which is less good.

Mencoder detects the desired container from the output extension, so if you'd rather it handed you an mkv, replace `mkv` with `avi` above.

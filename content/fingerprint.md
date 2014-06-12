Title: Can you fingerprint a sausage?
Date: 2013-06-20
Category: Programming
Tags: Geometry, Maths, Python

About a year ago I helped out teaching a first-year undergrad course on programming. One of the projects they could try was an interesting algorithm for generating patterns. The idea is that you have a set of fixed points in space, ${r_j}$, and you have a moveable point, $x(i)$ (at some initial position $x(0)$, whose value is not usually important). At each iteration, $i$, you pick an index, $j$, and move $x$ towards $r_j$ by some constant fraction, $d$, of the separation vector between $x$ and $r_j$,

$$ \mathbf{x}(i+1) = \mathbf{x}(i) + \mathrm{d} (\mathbf{r}_j - \mathbf{x}(i)) $$

After you've iterated this algorithm long enough, you can look at the probability distribution of $x$, and hopefully it will be something with more structure than mess.

So the choices you have are:

- The number and positions of ${r_j}$
- The method of picking $j$
- The value of $d$

# Triangle

This may sound quite abstract, so here's an example (the first example the students were asked to implement, in fact):

- 3 fixed points, placed so as to define an equilateral triangle
- Pick $j$ randomly and uniformly
- $d = 0.5$

Shown below is a colour plot of the spatial probability distribution of $x$. The fixed points are also shown as black circles,

![Sierpìnski Triangle](/images/sierpinski.png)

Hey it's a [Sierpiński triangle](http://en.wikipedia.org/wiki/Serpinski_triangle)! $x$ never goes in the triangles, and is otherwise uniformly distributed.

# Genetics

The final part of the project had the students use 4 points defining a square for ${r_j}$, with $d=0.5$. If $j$ is picked randomly, the result is a uniform distribution,

![Square for d=0.5](/images/square_uniform.png)

which is fairly interesting in itself. But what if instead of picking $j$ randomly, it's chosen by reading a text file containing characters representing the DNA bases of a genome? Each character is associated with a point $r_j$, and at each iteration $j$ is determined by reading the next character in the file. Doing this exposes the genomic structure in a remarkable way, showing visually the frequency of particular sequences of bases,

![Human genome fingerprint](/images/genetics.png)

# Literature

So since I had to implement this stuff myself for the purposes of teaching the course, I thought I might try to do a bit more with the code I had. I associated each point of a square with the roman letters *a*, *e*, *i* and *o*, and fed in lumps of text in place of the genome. My rough idea was that a distinctive 'fingerprint' might be identifiable for a particular author, date and/or language, when there's a large enough body of text available. Let's compare the complete works of Shakespeare to James Joyce's Ulysses. Because Ulysses is shorter than T.C.W.O.S, I truncated the latter in the interests of fairness.

Shakespeare:

![Shakespeare's fingerprint](/images/shakespeare.png "Shakespeare's fingerprint")

Ulysses:

![Joyce's fingerprint](/images/ulysses.png "James Joyce's Ulysses' fingerprint")

It might be reasonable to assume that the uniformity of the distribution is correlated with the variety of vocabulary used, since text consisting only of repeated insistences that 'The cat sat on the mat' would contain only a few vowel sequences, and the distribution would be very non-uniform, whereas a sequence of every permutation of every dictionary word would contain a large number of vowel sequences, and would be very long. To demonstrate this, if we feed in many paragraphs of [Lorem Ipsum](http://en.wikipedia.org/wiki/Lorem_ipsum), as an approximation of the complete works of a dull but determined writer, we get,

![Loreum Ipsum's fingerprint](/images/lorem_ipsum.png)

This has a standard deviation of $\sigma_w=37$, and appears highly non-uniform.

Adjusting for text length, Ulysses has a standard deviation $\sigma_w=4$, while Shakespeare's stuff gets $\sigma_w=13$: In the vocabulary battle of the North-West European isles, Ireland wins.

You can find the code used to generate these images [on my github page](https://github.com/eddiejessup/Sourdough).

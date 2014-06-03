Title: Voronoi diagram for a range of distance metrics
Date: 2013-06-04
Category: Programming
Tags: Python, Maths, Geometry

I've been reading about [Voronoi diagrams](http://en.wikipedia.org/wiki/Voronoi_diagram) recently, they seem pretty interesting. If you have a set of points, the Voronoi diagram of those points is made by colouring regions of space according to which point in the set is nearest (see the link for some example images).

Then I got onto reading about [distance metrics](http://en.wikipedia.org/wiki/Distance_metric), which are functions used to define the distance between two points. For example, the Euclidean metric is where you take the square root of the sum of the squares of the distance between the points along each axis. This is usually the distance definition that's useful, but others exist.

An alternative distance metric is the Manhattan distance, where you just add up the absolute value of the distance between points along each axis. If you're in an urban area that's arranged in a grid-like pattern ([Milton Keynes](http://en.wikipedia.org/wiki/Milton_keynes)), this is the distance you'd actually have to travel to get from A to B ([Arbrook Avenue to Bossiney Place](https://maps.google.co.uk/maps?q=arbrook+avenue+to+bossiney+place&saddr=arbrook+avenue&daddr=bossiney+place&hl=en&ll=52.039993,-0.75664&spn=0.011602,0.033023&sll=52.043556,-0.769107&sspn=0.011601,0.033023&geocode=FR8fGgMdpkP0_ympIiI3nqp3SDE3XaCeJ4lqLg%3BFWQFGgMdm5P0_yk9S0BXvqp3SDHFy511Rv088g&t=h&z=16)). So non-Euclidean metrics do actually have their uses.

It seemed like it might be interesting to investigate what a Voronoi diagram would look like as you changed the distance metric used to find the nearest point. The $L_p$ metric is a class of metric,

$$ \|\mathbf{x}\|_p= \left( \sum \limits_i |x_i|^p \right)^{1 / p} $$

which has a single real parameter, $p$, so this seemed like the kind of thing I could play with. It actually seems to be the only sensible distance metric that exists (or that I can find on Wikipedia), so I had less choice in the matter than I thought.

It turns out the $L_p$ metric is equivalent to the Manhattan metric when $p=1$, and the Euclidean metric when $p=2$. There's also another case when $p \to \infty$, which is called the Chebyshev metric. Wikipedia says this is useful in warehouse logistics.

So I wrote a little script to generate the Voronoi diagram with a particular $L_p$ metric, for a fixed set of randomly distributed points, and ran it for a range of values of $p$. The result is shown below, with the metric shown at the top of the figure. The diagram starts off with the Manhattan metric, moves through the Euclidean, then goes off towards the Chebyshev.

<iframe width="420" height="315" src="//www.youtube.com/embed/21IHHDssWxM" frameborder="0" allowfullscreen></iframe>

I find it really interesting that the Chebyshev metric gives sensible results, and yet the universe doesn't use it for most of its admin -- surely it's more elegant to have a nice parameterless measure than one where you're writing $2$ everywhere?

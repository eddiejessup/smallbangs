Title: Raindrops keep falling on my Delauney-triangulated polygon mesh
Date: 2013-08-08
Category: Programming
Tags: Python, Simulation

If you're not familiar with numerically solving differential equations via finite differencing, it essential involves taking the infinitesimal quantity $\delta$ in an equation, and replacing it with a finite quantity Δ, then solving this equation algebraically. [Go look on Wiki](http://en.wikipedia.org/wiki/Finite_difference_method).

Anyway, the other day I woke up in a cold sweat realising I'd never finite-differenced the wave equation,

$$ \dfrac{\partial^2 u(t, x)}{\partial t^2} = c^2 \nabla^2 u(t, x) $$

because I was scared of the double time derivative, and thought it would cause me trouble. The spatial analogue to this time quantity is the laplacian, whose usual first-order approximation in one dimension is,

$$ \dfrac{\partial^2 u(t, x)}{\partial t^2} \approx \dfrac{u(t - \Delta t, x) - 2u(t, x) + u(t + \Delta t, x)}{\Delta t^2} $$

So given this, the naïve implementation for time would be,

$$ \dfrac{\partial^2 u(t, x)}{\partial t^2} \approx \dfrac{u(t - \Delta t, x) - 2u(t, x) + u(t + \Delta t, x)}{\Delta t^2} $$

Applying the finite difference to $t$ instead of $x$. But time only really likes to go in one direction, unlike the 3 space amigos, so evaluating the last term on the RHS is more difficult. A solution to this that doesn't require time travel is just to use a more rubbish approximation, by stepping back one more time-step,

$$ \dfrac{\partial^2 u(t, x)}{\partial t^2} \approx \dfrac{u(t - 2\Delta t, x) - 2u(t - \Delta t, x) + u(t, x)}{\Delta t^2} $$

This approximation requires no time travel, only that you remember the system state at the last time-step and also the one before. Using this, and our friendly spatial approximation, we have as our approximate wave equation:

$$ \dfrac{u(t - 2\Delta t, x) - 2u(t - \Delta t, x) + u(t, x)}{\Delta t^2} = c^2 \dfrac{u(t - \Delta t, x - \Delta x) - 2u(t - \Delta t, x) + u(t - \Delta t, x + \Delta x)}{\Delta x^2} $$

The one of those we want is $u(t,x)$, so solving for that we get,

$$u(t, x) = \dfrac{c^2 \Delta t^2}{\Delta x^2} [ u(t - \Delta t, x - \Delta x) - 2u(t - \Delta t, x) + u(t - \Delta t, x + \Delta x) ] + u(t - 2\Delta t, x) - 2u(t - \Delta t, x) $$

Ugly, but solvable -- just what computers were made for. Now you can walk along $x$ at each time-step and calculate your new $u$ by plugging in the values which you already know into the RHS of the above equation.

Anyway the upshot is, I implemented this, with a bit of code that adds $\delta(x - x_0, t - t_0)$ to $u(t,x)$ for a random and uniformly sampled set of $x_0$ and $t_0$ (read: I made it rainy), and got a pretty video:

<iframe width="640" height="360" src="//www.youtube.com/embed/2TGzuh_BGEg?feature=player_embedded" frameborder="0" allowfullscreen></iframe>

You can find the code used to generate this video [on my github page](https://github.com/eddiejessup/Anpan).

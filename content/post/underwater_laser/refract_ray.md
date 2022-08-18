# refract ray

here is comment in `Triangulate.refractRay()`
of project `underwater-camera-calibration`

```python
# - 'rayDir' is the vector of the incoming ray
# - 'planeNormal' is the plane normal of the refracting interface
# - 'n1' is the refraction index of the medium the ray travels >FROM<
# - 'n2' is the refractio index of the medium the ray travels >TO<
```

## table of symbol

|    smybol    |                      meaning                      |
| :----------: | :------------------------------------------------: |
|   $v_1$   |            unit direction vector (FROM)            |
|   $v_2$   |             unit direction vector (TO)             |
|    $n$    | unit normal vector of interface plane (FROM / TO ) |
|   $n_1$   |              refraction index (FROM)              |
|   $n_2$   |               refraction index (TO)               |
| $\theta_1$ |                    angle (FROM)                    |
| $\theta_2$ |                     angle (TO)                     |

## analysis

We should notice that $n$ is opposed to the incoming ray direction $v_1$:

$$
v_1 ^\top  n < 0, v_1^\top  v_1=v_2^\top  v_2 = n^\top  n =1
$$

Now that we know all the parameters except $v_2$,
we need derive the expression of $v_2$ with other variables $v_1, n, n_1, n_2$

## reconstruct vector

and notice cross product matrix $n\times n\times=nn^\top -I$ and $n^\top  n =1$:

$$
\begin{aligned}
|v_1| \cos\theta_1 &\equiv \frac{-v_1^\top  n}{|n|}
= -v_1^\top  n\\
|v_1|^2 \sin^2\theta_1 &\equiv \Bigg|v_1 -(-n)\frac{(-n^\top v_1)}{n^\top  n}\Bigg|^2 
=\Bigg|v_1 -\frac{nn^\top }{n^\top  n} v_1\Bigg|^2
=|(I-nn^\top ) v_1|^2\\
&= |-n\times (n\times v_1)|^2 = v_1^\top  (I-nn^\top )^\top (I-nn^\top )v_1 \\
&= v_1^\top  (I-nn^\top )(I-nn^\top )v_1 \\
&= v_1^\top  (I-nn^\top )v_1 = v_1^\top  [-n\times n\times v_1] v_1\\
&= v_1^\top  v_1 - [v_1^\top n]^2\\

v_1 &\equiv nn^\top v_1 + (I-nn^\top )v_1 = n(n^\top v_1) -n\times (n\times v_1)\\
&= (-n) |v_1| \cos\theta_1 + \frac{[-n\times (n\times v_1)]}{|-n\times (n\times v_1)|}|v_1|\sin\theta_1
\end{aligned}
$$

Use $v_1^\top  v_1=1$:

$$
\sin\theta_1 =\sqrt{\frac{v_1^\top  v_1 - [v_1^\top n]^2}{v_1^\top  v_1} } = \sqrt{1-[v_1^\top n]^2}\\
v_1 = (-n)\cos\theta_1 + \frac{[-n\times (n\times v_1)]}{|-n\times (n\times v_1)|}\sin\theta_1
$$

For the same reason, $v_2^\top v_2=1$,
and $v_1, v_2, n$ in the same plane: $n\times v_1, n\times v_2$ are linear related,
and $v_1^\top  n < 0, v_2^\top  n < 0$:

$$
\frac{[-n\times (n\times v_1)]}{|-n\times (n\times v_1)|}
= \frac{[-n\times (n\times v_2)]}{|-n\times (n\times v_2)|}
$$

We want to reconstruct $v_2$ with $n, v_1$, similarly:
here is decomposition of orthogonal basis,
because $n^\top [n\times n\times v_1]=n^\top [nn^\top -I]v_1=0^\top v_1=0$

$$
v_2 = (-n)\cos\theta_2 + \frac{[-n\times (n\times v_2)]}{|-n\times (n\times v_2)|}\sin\theta_2\\
= (-n)\cos\theta_2 + \frac{[-n\times (n\times v_1)]}{|-n\times (n\times v_1)|}\sin\theta_2
$$

## Snell's Law

From previous formula, only things are missing to reconstruct $v_2$ is $\sin\theta_2, \cos\theta_2$

$$
n_1 \sin\theta_1 = n_2 \sin\theta_2
$$

We want to express $\theta_1, \theta_2$ with parameters that we know $v_1, n, n_1, n_2$,

$$
\begin{aligned}
\cos\theta_1 &= -v_1^\top n \\
\sin\theta_1 &=\sqrt{\frac{v_1^\top  v_1 - [v_1^\top n]^2}{v_1^\top  v_1} } = \sqrt{1-[v_1^\top n]^2}\\
\sin\theta_2 &= \frac{n_1}{n_2} \sin\theta_1 = \frac{n_1}{n_2} \sqrt{1-[v_1^\top n]^2}\\
\cos\theta_2 &= \sqrt{1-(\frac{n_1}{n_2})^2 (1-[v_1^\top n]^2)}
\end{aligned}
$$

Represent $\frac{[-n\times (n\times v_1)]}{|-n\times (n\times v_1)|}$ with $v_1, n$:

$$
\begin{aligned}
\frac{[-n\times (n\times v_1)]}{|-n\times (n\times v_1)|}
&= \frac{v_1 + n\cos\theta_1}{\sin\theta_1}\\
\frac{[-n\times (n\times v_1)]}{|-n\times (n\times v_1)|} \sin\theta_2 
&= v_1 \frac{\sin\theta_2}{\sin\theta_1} + n \frac{\sin\theta_2}{\sin\theta_1} \cos\theta_1\\
&= v_1 (\frac{n_1}{n_2}) - n n^\top v_1(\frac{n_1}{n_2}) \\
&= (I-nn^\top )v_1 (\frac{n_1}{n_2})\\
&= -n\times (n\times v_1) (\frac{n_1}{n_2})
\end{aligned}
$$

Eventually, represent $v_2$ with $v_1, n, n_1, n_2$

$$
\begin{aligned}
v_2 &= (-n)\cos\theta_2 + \frac{[-n\times (n\times v_1)]}{|-n\times (n\times v_1)|}\sin\theta_2 \\
&= n\Bigg[-\sqrt{1-(\frac{n_1}{n_2})^2 (1-[v_1^\top n]^2)}\Bigg] + v_1 (\frac{n_1}{n_2}) - n \Big[ n^\top  v_1(\frac{n_1}{n_2}) \Big]\\
&= n\Bigg[(\frac{n_1}{n_2})[-n^\top  v_1]-\sqrt{1-(\frac{n_1}{n_2})^2 (1-[v_1^\top  n]^2)}\Bigg] + v_1 (\frac{n_1}{n_2})
\end{aligned}
$$

## Consider all the possible values of v1

If the family of vector $v_1$ are always on the same plane,
the unit normal vector of this plane is $\pi$, always holds:

$$
\pi^\top  v_1 = 0
$$

We want to prove always exist $A, B\neq 0$ for any $v_1$ that holds $\pi^\top  v_1 =0$, make sure

$$
\begin{aligned}
(A\pi + B n)^\top  v_2 &= 0\\
&= A [\pi^\top  n]\Bigg[(\frac{n_1}{n_2})[-n^\top v_1]-\sqrt{1-(\frac{n_1}{n_2})^2 (1-[v_1^\top n]^2)}\Bigg]\\
&- B\sqrt{1-(\frac{n_1}{n_2})^2 (1-[v_1^\top n]^2)}\\

&= A [\pi^\top  n](\frac{n_1}{n_2})[-n^\top v_1]\\
&- \Big[ A [\pi^\top  n]+B \Big] \sqrt{1-(\frac{n_1}{n_2})^2 (1-[v_1^\top n]^2)}\\

\frac{A [\pi^\top  n]+B}{A [\pi^\top  n]} &= \frac{(\frac{n_1}{n_2})[-n^\top v_1]}{\sqrt{1-(\frac{n_1}{n_2})^2 (1-[v_1^\top n]^2)}}
\end{aligned}
$$

So, constant $A, B$ don't exist when $v_1$ keeps changing

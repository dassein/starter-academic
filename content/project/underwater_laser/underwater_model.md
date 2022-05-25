# under-water model

The unit vector on the laser plane $v_{m}$


$$
v_{m} = c_1 \pi + c_2 n\\
\pi^\top  v_{m} = \pi^\top  (c_1 \pi + c_2 n) =c_1 + c_2(\pi^\top  n)= 0\\
v^\top _{m} v_{m} = (c_1^2 + c_2^2) + 2c_1 c_2 (\pi^\top  n) =1
$$

Then we can have that
$$
c_1 = - c_2 (\pi^\top  n)\\
[1+(\pi^\top  n)^2] c^2_2 - 2 (\pi^\top  n)^2 c^2_2 = 1
$$

Then we solve
$$
c_2 = \frac{-1}{\sqrt{1-(\pi^\top  n)^2}}\\
c_1 = \frac{(\pi^\top  n)}{\sqrt{1-(\pi^\top  n)^2}}\\

v_{m} = \pi [\frac{(\pi^\top  n)}{\sqrt{1-(\pi^\top  n)^2}}]
+ n [\frac{-1}{\sqrt{1-(\pi^\top  n)^2}}]
$$

## expression of r, r'

Consider replace symbol of refraction:
* replace $v_1$ with $r$ to represent unit direction vector (FROM)
* replace $v_2$ with $r'$ to represent unit direction vector (TO)

Here $r_{\theta}$ is the unit vector   
after rotating $v_m$ around rotaion axis $\pi$ for angle $\theta$:

$$
\begin{aligned}
r_{\theta} &= R_{\theta} v_m\\
&= [\cos\theta I + \sin\theta (\pi\times) + (1-\cos\theta) \pi\pi^\top ] v_m\\
&= [\cos\theta I + \sin\theta (\pi\times) + (1-\cos\theta) \pi\pi^\top ] 
\Big( \pi [\frac{(\pi^\top  n)}{\sqrt{1-(\pi^\top  n)^2}}] + n [\frac{-1}{\sqrt{1-(\pi^\top  n)^2}}] \Big)\\
&= \cos\theta \Big( \pi [\frac{(\pi^\top  n)}{\sqrt{1-(\pi^\top  n)^2}}] + n [\frac{-1}{\sqrt{1-(\pi^\top  n)^2}}] \Big)\\
&+ \sin\theta (\pi\times n) [\frac{-1}{\sqrt{1-(\pi^\top  n)^2}}]\\

\end{aligned}
$$


After refraction, the formula of $r'_{\theta}$ is:

$$
r'_{\theta} = n\Bigg[(\frac{n_1}{n_2})[-n^\top r_{\theta}]-\sqrt{1-(\frac{n_1}{n_2})^2 (1-[r_{\theta}^\top n]^2)}\Bigg] + r_{\theta} (\frac{n_1}{n_2})
$$

Here, the inner product, is a function of angle $\theta$: 

$$
[-n^\top  r_{\theta}] = \cos\theta \sqrt{1-(\pi^\top  n)^2}
$$

Thus

$$
\begin{aligned}
r'_{\theta} &= 
n\Bigg[-(\frac{n_1}{n_2})[\cos\theta \frac{(\pi^\top  n)^2}{\sqrt{1-(\pi^\top  n)^2}}]-\sqrt{1-(\frac{n_1}{n_2})^2 \Big(1-\cos^2\theta [1-(\pi^\top  n)^2]\Big)}\Bigg]\\
&+ \sin\theta (\pi\times n)(\frac{n_1}{n_2}) [\frac{-1}{\sqrt{1-(\pi^\top  n)^2}}]\\
&+ \cos\theta\space\pi (\frac{n_1}{n_2})[\frac{(\pi^\top  n)}{\sqrt{1-(\pi^\top  n)^2}}] 
\end{aligned}
$$


## find intersection I

set the interface plane

$$
n^\top  I = h
$$

Here it must on the ray, all start from laser point $P$:
$$
I_{\theta} = P + k_\theta r_\theta
$$

Solve $k_\theta, I_\theta$ respectively

$$
n^\top  P - k_\theta \cos\theta \sqrt{1-(\pi^\top  n)^2} = h\\
k_\theta = \frac{n^\top P -h}{\cos\theta \sqrt{1-(\pi^\top  n)^2}}\\
I_\theta = P + [n^\top P-h]
\Bigg[
\pi [\frac{(\pi^\top  n)}{1-(\pi^\top  n)^2}] + n [\frac{-1}{1-(\pi^\top  n)^2}]
\Bigg]
+ [n^\top P-h] \tan\theta(\pi\times n) [\frac{-1}{1-(\pi^\top  n)^2}]
$$

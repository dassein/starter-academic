# triangulate

Consider replace symbol of refraction:
* replace $v_1$ with $r$ to represent unit direction vector (FROM)
* replace $v_2$ with $r'$ to represent unit direction vector (TO)

Then the formula of $r'$ becomes:

$$
r' = n\Bigg[(\frac{n_1}{n_2})[-n^\top r]-\sqrt{1-(\frac{n_1}{n_2})^2 (1-[r^\top n]^2)}\Bigg] + r (\frac{n_1}{n_2})
$$


## symbol table

| smybol |                 meaning                  |
| :----: | :--------------------------------------: |
| $r'_1$ | unit direction vector of ray 1 in water  |
| $r'_2$ | unit direction vector of ray 2 in water  |
| $I_1$  | intersection point of interface plane and ray 1 |
| $I_2$  | intersection point of interface plane and ray 2 |
| $M_1$  |     closest point of ray 1 to ray 2      |
| $M_2$  |     closest point of ray 2 to ray 1      |
|  $M$   |       mid point of $M_1$ and $M_2$       |
| $k_1$  |    scalar factor from $I_1$ to $M_1$     |
| $k_2$  |    scalar factor from $I_2$ to $M_2$     |


Our goal is to express $M$ with what we know $r'_1, r'_2, I_1, I_2$

<div STYLE="page-break-after: always;"></div>

## analysis

Defination of $M_1, M_2$,  
the closest point pair $M_1-M_2$ must be perpendicular to $r'_1, r'_2$:

$$
{r'}_1^\top (M_1 -M_2) = 0\\
{r'}_2^\top (M_1 -M_2) = 0\\
$$

Definition of $k_1, k_2$:

$$
k_1 r'_1 \equiv M_1 - I_1\\
k_2 r'_2 \equiv M_2 - I_2\\
$$


Replace $M_1, M_2$ with unknow $k_1, k_2$  
and what we know $r'_1, r'_2, I_1, I_2$,  
To solve $k_1, k_2$ firstly

$$
{r'}_1^\top \Big([I_1 -I_2] + k_1 r'_1 - k_2 r'_2 \Big) = 0\\
{r'}_2^\top \Big([I_1 -I_2] + k_1 r'_1 - k_2 r'_2 \Big) = 0\\
$$

It is equivalent to 

$$
[{r'}_1^\top  r'_1] k_1 -[{r'}_1^\top  r'_2] k_2 = - {r'}_1^\top  [I_1 -I_2]\\
-[{r'}_2^\top  r'_1] k_1 + [{r'}_2^\top  r'_2] k_2 = {r'}_2^\top  [I_1 -I_2]\\
$$

In matrix form

$$
\begin{pmatrix}
[{r'}_1^\top  r'_1] & -[{r'}_1^\top  r'_2]\\
-[{r'}_1^\top  r'_2] & [{r'}_2^\top  r'_2]
\end{pmatrix}

\begin{bmatrix} k_1\\ k_2  \end{bmatrix}
= \begin{pmatrix} - {r'}_1^\top  [I_1 -I_2]\\ {r'}_2^\top  [I_1 -I_2]  \end{pmatrix}
$$

With Cramer's rule

$$
\begin{aligned}
k_1 &= \frac{
\begin{vmatrix}
- {r'}_1^\top  [I_1 -I_2] & -[{r'}_1^\top  r'_2]\\
{r'}_2^\top  [I_1 -I_2] & [{r'}_2^\top  r'_2]
\end{vmatrix}
}{
\begin{vmatrix}
[{r'}_1^\top  r'_1] & -[{r'}_1^\top  r'_2]\\
-[{r'}_1^\top  r'_2] & [{r'}_2^\top  r'_2]
\end{vmatrix}
}
= \frac{
[-{r'}_2^\top  r'_2{r'}_1^\top  + {r'}_2^\top  r'_1{r'}_2^\top ] [I_1 -I_2]
}{
1 - [{r'}_1^\top  r'_2]^2
}\\
&= {r'}_2^\top   \Bigg[ \frac{1}{1 - [{r'}_1^\top  r'_2]^2} 
\Big(r'_1{r'}_2^\top  - r'_2{r'}_1^\top  \Big) [I_1 -I_2] \Bigg ]\\


k_2 &= \frac{
\begin{vmatrix}
[{r'}_1^\top  r'_1] & - {r'}_1^\top  [I_1 -I_2]\\
-[{r'}_1^\top  r'_2] & {r'}_2^\top  [I_1 -I_2]
\end{vmatrix}
}{
\begin{vmatrix}
[{r'}_1^\top  r'_1] & -[{r'}_1^\top  r'_2]\\
-[{r'}_1^\top  r'_2] & [{r'}_2^\top  r'_2]
\end{vmatrix}
}
= \frac{
[{r'}_1^\top  r'_1{r'}_2^\top  - {r'}_1^\top  r'_2{r'}_1^\top ] [I_1 -I_2]
}{
1 - [{r'}_1^\top  r'_2]^2
}\\
&= {r'}_1^\top   \Bigg[ \frac{1}{1 - [{r'}_1^\top  r'_2]^2} 
\Big(r'_1{r'}_2^\top  - r'_2{r'}_1^\top  \Big) [I_1 -I_2] \Bigg ]\\

\end{aligned}
$$



## expression of M

Definition of $M$ is

$$
\begin{aligned}
M &\equiv \frac{M_1 + M_2}{2} 
= \frac{I_1 + I_2}{2} + \frac{k_1 r'_1 + k_2 r'_2}{2} \\
&= \frac{I_1 + I_2}{2} + \frac{1}{2} 
\Big(r'_1{r'}_2^\top  + r'_2{r'}_1^\top \Big)
\Bigg[ \frac{1}{1 - [{r'}_1^\top  r'_2]^2} 
\Big(r'_1{r'}_2^\top  - r'_2{r'}_1^\top  \Big) [I_1 -I_2] \Bigg ]\\
&= \frac{I_1 + I_2}{2} + \frac{1}{2} \frac{1}{1 - [{r'}_1^\top  r'_2]^2}
\Bigg[  \Big(r'_1{r'}_2^\top  + r'_2{r'}_1^\top \Big)
\Big(r'_1{r'}_2^\top  - r'_2{r'}_1^\top  \Big) \Bigg ]
[I_1 -I_2]\\
&= \frac{I_1 + I_2}{2} + \frac{1}{2} \frac{1}{1 - [{r'}_1^\top  r'_2]^2}
\Bigg[ 
r'_1 [{r'}_2^\top  r'_1] {r'}_2^\top  - r'_2 [{r'}_1^\top  r'_2] {r'}_1^\top  \Bigg ]
[I_1 -I_2]\\
&= \frac{I_1 + I_2}{2} + \frac{1}{2} \frac{[{r'}_1^\top  r'_2]}{1 - [{r'}_1^\top  r'_2]^2}
\Big( r'_1 {r'}_2^\top  - r'_2  {r'}_1^\top  \Big)
[I_1 -I_2]\\
\end{aligned}
$$


Consider the cross product, and its cross product matrix form

$$
a \times b = 
\begin{bmatrix} 
a_2 b_3 - a_3 b_2\\
a_3 b_1 - a_1 b_3\\
a_1 b_2 - a_2 b_1
\end{bmatrix}\\

(a \times b)\times =
\begin{bmatrix} 
0 & -[a_1 b_2 - a_2 b_1] & a_3 b_1 - a_1 b_3\\
a_1 b_2 - a_2 b_1 & 0 & -[a_2 b_3 - a_3 b_2]\\
-[a_3 b_1 - a_1 b_3] & a_2 b_3 - a_3 b_2 & 0
\end{bmatrix}\\
= \begin{bmatrix} 
0 & a_2 b_1 -a_1 b_2  & a_3 b_1 - a_1 b_3\\
a_1 b_2 - a_2 b_1 & 0 &  a_3 b_2 -a_2 b_3\\
a_1 b_3 -a_3 b_1 & a_2 b_3 - a_3 b_2 & 0
\end{bmatrix}\\
= \begin{bmatrix} 
a_1 b_1 & a_2 b_1 & a_3 b_1\\
a_1 b_2 & a_2 b_2 & a_3 b_2\\
a_1 b_3 & a_2 b_3 & a_3 b_3
\end{bmatrix}
- \begin{bmatrix} 
a_1 b_1 & a_1 b_2 & a_1 b_3\\
a_2 b_1 & a_2 b_2 & a_2 b_3\\
a_3 b_1 & a_3 b_2 & a_3 b_3
\end{bmatrix}\\
= b a^\top  - a b^\top 
$$

Similarly, we have

$$
\Big( r'_1 {r'}_2^\top  - r'_2  {r'}_1^\top  \Big) = 
- (r'_1 \times r'_2) \times\\
M = \frac{I_1 + I_2}{2} - \frac{1}{2} \frac{[{r'}_1^\top  r'_2]}{1 - [{r'}_1^\top  r'_2]^2}
(r'_1 \times r'_2) \times
[I_1 -I_2]\\
$$

---
title: Lecture 2- State Space Representation
toc: true
categories: [控制原理, PNW课件]
tags:
  - control system
  - math
---


# Lecture 2
Lecture 2- State Space Representation
<!--more-->

## symbols

$$\dot{X}(t) = AX(t) + BU(t)$$
$$Y(t) = CX(t) + DU(t)$$

$\dot{X}(t)$ derivative of state vector

$X(t)$ state vector | nx1

$Y(t)$ output vector | px1

$U(t)$ input/control vector | mx1

$A$ system matrix | nxn

$B$ input matrix | nxm

$C$ output matrix | pxn

$D$ feedforward matrix | pxm

set $X(t)|_{t=0} = 0$, do Laplace Transform
$$sX(s) = AX(s) + BU(s)$$
$$Y(s) = CX(s) + DU(s)$$

so,
$$X(s) = (sI-A)^{-1} BU(s) = \frac{adj(sI-A)B}{det(sI-A)} U(s)$$
$$Y(s) = [\frac{Cadj(sI-A)B}{det(sI-A)} + D] U(s)$$

thus, transfer function $G(s)$
$$G(s) \equiv \frac{Y(s)}{U(s)} = \frac{Cadj(sI-A)B}{det(sI-A)} + D$$



if $X(t)|_{t=0} = X(0)$
$$
sX(s)-X(0) = AX(s) + BU(s)\\
Y(s) = CX(s) + DU(s)
$$
then
$$
Y(s) = C(sI-A)^{-1}X(0) + C(sI-A)^{-1}BU(s) + DU(s)
$$
Here set $\Phi(t) \equiv L[(sI-A)^{-1}] = e^{At} = \sum_{k=0}^{\infty} \frac{t^k A^k}{k!}$

In another way 
$$
(sI-A)^{-1} = \Bigg\{
\begin{aligned}
-A^{-1}(I-sA^{-1})^{-1} = -A^{-1}[\sum^{\infty}_{k=0}s^kA^{-k}]  && |s|< \lambda_{min}\\
s^{-1}(I-\frac{A}{s})^{-1} = \frac{1}{s}[\sum^{\infty}_{k=0}s^{-k}A^{k}]  && |s|> \lambda_{max}\\

\end{aligned}
$$


Here $\frac{1}{s^{k+1}} = L^{-1}[\frac{t^k}{k!}]$

So we can obtain $(sI-A)^{-1}|_{s=0} = -A^{-1}, \lim_{s\to \infty} s(sI-A)^{-1}=I$


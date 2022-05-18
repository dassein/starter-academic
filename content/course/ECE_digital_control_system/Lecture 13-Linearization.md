---
title: Lecture 13-Linearization
toc: true
categories: [控制原理, PNW课件]
tags:
  - control system
  - math
---

# Chap 2: Linearization
<!--more-->

$$
y-y_0 = y_0'(x-x_0)
$$


## example 1

consider such a nonlinear model: $i_r = e^{V_r}$
$$
C \frac{dV}{dt} + i_r -i(t) - 2 = 0
$$

consider a small Perturbation on the Equilibrium
$$
V = V_0 + \delta V\\
i_r = e^{V_r} = e^{V_0 + \delta V}
$$
Let $C = 1$, we have
$$
\frac{d\delta V}{dt} + e^{V_0 + \delta V} - 2 = i(t)
$$
substitute $e^{V_0 + \delta V} \approx e^{V_0} + e^{V_0} \delta V$, then
$$
\frac{d\delta V}{dt} + e^{V_0} + e^{V_0} \delta V - 2 = i(t)
$$
Thus means
$$
\frac{d\delta V}{dt} + e^{V_0} \delta V = i(t) + 2 - e^{V_0}
$$
Because $i_r|_{V_r = V_0} = e^{V_0} = 2, V_0 = \ln(2) = 0.693$, we obtain
$$
\frac{d\delta V}{dt} + 2 \delta V = i(t)
$$
Laplace transform $\mathbb{L}$

$$
(s+2)\delta V(s) - \delta V(0_-) = I(s)
$$

that is because of the property of Laplace transform
$$
\int_{0_-}^{\infty} \frac{df(t)}{dt}e^{-st}dt
= e^{-st} f(t)|_{0_-}^{\infty} + s \int_{0_-}^{\infty} f(t)e^{-st}dt\\
\mathbb{L}[\frac{df(t)}{dt}] = s\mathbb{L}[f(t)] - f(0_-)
$$

## example 2

$$
M \frac{d^2 y(t)}{dt^2} = Mg - \frac{i^2(t)}{y(t)}\\

V(t) = R i(t) + L \frac{d i(t)}{dt}
$$

$V(t)$ is input, now choose the names of variables as
$$
\begin{aligned}
X_1 &= y(t)\\
X_2 &= \frac{dy(t)}{dt}\\
X_3 &= i(t)
\end{aligned}
$$
thus, we obtain

$$
\begin{aligned}
\dot{X_1} &= X_2\\
\dot{X_2} &= -\frac{X_3^2}{MX_1} + g\\
\dot{X_3} &= - \frac{R}{L} X_3 + L^{-1} V(t)
\end{aligned}
$$

suppose input $V(t) = V_0 + \Delta V(t), i(t) = i_0 + \Delta i(t), y(t) = y_0 + \Delta y(t)$, then let $\dot{X} = 0$
$$
\begin{aligned}
0 &= \frac{dy(t)}{dt} |_{y(t) = y_0}\\
0 &= Mg- \frac{i_0^2}{y_0}\\
0 &= -R i_0 + V_0
\end{aligned}
$$
we can write down the equilibrium for input $V_0$
$$
\begin{aligned}
i_0 &= \frac{V_0}{R}\\
y_0 &= \frac{i_0^2}{Mg} = \frac{V_0^2}{R^2 Mg}
\end{aligned}
$$

It implies that
$$
\begin{aligned}
X_{10} &= y_0 = \frac{V_0^2}{R^2 Mg}\\
X_{20} &= \frac{dy(t)}{dt} |_{y(t) = y_0} = 0\\
X_{30} &= i_0 = \frac{V_0}{R}
\end{aligned}
$$
now define $\delta X \equiv X - X_0, \delta V = V - V_0$

$$
\begin{aligned}
\dot{\delta} X_1&= \delta X_2\\
\dot{\delta} X_2&= \frac{\partial[-\frac{X_3^2}{MX_1}]}{\partial X_1}|_{X=X_0} \delta X_1 + \frac{\partial[-\frac{X_3^2}{MX_1}]}{\partial X_3}|_{X=X_0} \delta X_3\\
&= [\frac{X_3^2}{MX_1^2}]|_{X=X_0} \delta X_1 + [-\frac{2X_3}{MX_1}]|_{X=X_0} \delta X_3\\
&= \frac{R^2Mg^2}{V_0^2}\delta X_1 + [\frac{-2Rg}{V_0}] \delta X_3\\
\dot{\delta} X_3 &= - \frac{R}{L} \delta X_3 + \delta V(t)
\end{aligned}
$$

therefore
$$
\dot{\delta} X = 
\begin{bmatrix}
0 & 1 & 0\\
\frac{R^2Mg^2}{V_0^2} & 0 & \frac{-2Rg}{V_0}\\
0 & 0 & - \frac{R}{L}
\end{bmatrix}
\delta X +
\begin{bmatrix}
0\\ 0\\ 1
\end{bmatrix}
\delta V
$$

Then calculate the poles of linearized model: if poles are all in left plane <=> the model is stable!!!

Is it Controllable or Not?
$$
|C_M| =[B \quad AB \quad A^2B]\

=\begin{bmatrix}

0 & 0 & \frac{-2Rg}{V_0}\\

0 & \frac{-2Rg}{V0} & \frac{2R^2g}{LV0}\\

1 & - \frac{R}{L} & \frac{R^2}{L^2}

\end{bmatrix}

\neq 0
$$
If so, we could control it to ensure the model stable
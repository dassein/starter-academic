---
title: Appendix-settling and peak time
toc: true
categories: [控制原理, PNW课件]
tags:
  - control system
  - math
---

# Peak time $T_p$, Settling time $T_s$, Overshoot $\%$
<!--more-->
$$
\begin{aligned}
G(s) &= \frac{\omega_n^2}{s^2 + 2 \zeta \omega_n s + \omega_n^2} \\ 
&= \frac{\omega_n^2}{(s+\zeta\omega_n + j \sqrt{1-\zeta^2}\omega_n)(s+\zeta\omega_n - j \sqrt{1-\zeta^2}\omega_n)}\\
&= \frac{A}{s+\zeta\omega_n + j \sqrt{1-\zeta^2}\omega_n}
- \frac{A}{s+\zeta\omega_n - j \sqrt{1-\zeta^2}\omega_n}
\end{aligned}
$$

Where $-2A j \sqrt{1-\zeta^2}\omega_n = \omega_n^2 \Leftrightarrow A = \frac{j\omega_n}{2\sqrt{1-\zeta^2}}$. So
$$
\begin{aligned}
G(s) &= \frac{j\omega_n}{2\sqrt{1-\zeta^2}} 
\left[\frac{1}{s+\zeta\omega_n + j \sqrt{1-\zeta^2}\omega_n}
- \frac{1}{s+\zeta\omega_n - j \sqrt{1-\zeta^2}\omega_n}\right]\\
g(t) &= \frac{j\omega_n}{2\sqrt{1-\zeta^2}}
[e^{-(\zeta\omega_n + j \sqrt{1-\zeta^2}\omega_n)t}
-e^{-(\zeta\omega_n - j \sqrt{1-\zeta^2}\omega_n)t}]\\
&= \frac{j\omega_n}{2\sqrt{1-\zeta^2}}e^{-\zeta\omega_n t} 
[-2j\sin(\sqrt{1-\zeta^2}\omega_n t)]\\
&= \frac{\omega_n}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_n t}
\sin(\sqrt{1-\zeta^2}\omega_n t)
\end{aligned}
$$


So, the output $y(t)$ with $y(0_-) =0$ would be
$$
\begin{aligned}
Y(s) = \frac{1}{s} G(s) \Leftrightarrow y(t) = u(t) * g(t) = \int^t_{0_-} g(\tau) d\tau\\
\mathbb{L}[y'(t)] = sY(s) - y(0_-) = sY(s) = G(s)\\
y'(t) = g(t) = \frac{\omega_n}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_n t}
\sin(\sqrt{1-\zeta^2}\omega_n t)
\end{aligned}
$$

Consider such an integral, where $\tan(\phi) = \frac{b}{a}$
$$
\begin{aligned}
\int^t_0 e^{-a\tau}\sin(b\tau) d\tau
&= \int^t_0 \text{Im}\left[e^{(-a+jb)\tau}\right] d\tau
= \text{Im}\left[ \int^t_0 e^{(-a+jb)\tau} d\tau \right]\\
&= \text{Im}\left[ \frac{a+jb}{a^2 + b^2} [1-e^{-at}\cos(bt)
-je^{-at}\sin(bt)]  \right]\\
&= \frac{1}{a^2+b^2} [-ae^{-at}\sin(bt) + b - be^{-at}\cos(bt)]\\
&= \frac{b}{a^2+b^2} - \frac{e^{-at}}{a^2+b^2} \sqrt{a^2+b^2}\sin(bt+\phi)
\end{aligned}
$$

substitute $a, b \leftarrow \zeta\omega_n, \sqrt{1-\zeta^2}\omega_n$, we can derive the expression for $y(t)$
$$
\begin{aligned}
y(t) &= \int^t_{0_-} g(\tau) d\tau
= \frac{\omega_n}{\sqrt{1-\zeta^2}} 
\int^t_{0_-} e^{-\zeta\omega_n \tau}
\sin(\sqrt{1-\zeta^2}\omega_n \tau) d\tau\\
&= \frac{\omega_n}{\sqrt{1-\zeta^2}} 
\left[ \frac{\sqrt{1-\zeta^2}\omega_n}{\omega_n^2} - 
\frac{e^{-\zeta\omega_n t}}{\omega_n}
\sin(\sqrt{1-\zeta^2}\omega_n t + \phi) \right]\\
&= 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}
\sin(\sqrt{1-\zeta^2}\omega_n t + \phi)
\end{aligned}
$$

where $\tan(\phi) = \frac{b}{a} = \frac{\sqrt{1-\zeta^2}}{\zeta}, \sin(\phi) = \sqrt{1-\zeta^2}, \cos(\phi) = \zeta$


## Calculate $T_s$
$$
T_s = \frac{4}{\zeta \omega_n} \Leftrightarrow e^{-\zeta\omega_n T_s} = e^{-4} \approx 0.02
$$

## Calculate overshoot $\%$ and $T_p$
by let $y'(t)|_{t=T_p} = 0$
$$
y'(t)|_{t=T_p} = \frac{\omega_n}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_n T_p}
\sin(\sqrt{1-\zeta^2}\omega_n T_p) = 0\\
\sqrt{1-\zeta^2}\omega_n T_p = \pi \Leftrightarrow T_p = \frac{\pi}{\sqrt{1-\zeta^2}\omega_n}
$$

consider the overshoot $\%$ at $t=T_p$
$$
\begin{aligned}
1 + \% &\equiv  y(t)|_{t=T_p} 
= 1 - \frac{e^{-\zeta\omega_n T_p}}
{\sqrt{1-\zeta^2}}
\sin(\sqrt{1-\zeta^2}\omega_n T_p + \phi)\\
&= 1 - \frac{e^{-\zeta\omega_n T_p}}
{\sqrt{1-\zeta^2}}
\sin(\pi + \phi)
= 1 + \frac{e^{-\zeta\omega_n T_p}}
{\sqrt{1-\zeta^2}} \sqrt{1-\zeta^2}\\
&= 1 + e^{-\zeta\omega_n T_p}
= 1 + e^{-\pi \frac{\zeta}{\sqrt{1-\zeta^2}}}
\end{aligned}
$$

So, we find the relationship between the overshoot $\%$ and $\zeta$
$$
\% = e^{-\pi \frac{\zeta}{\sqrt{1-\zeta^2}}} 
\Leftrightarrow -\frac{\ln(\%)}{\pi} = \frac{\zeta}{\sqrt{1-\zeta^2}}\\
\frac{-\ln(\%)}{\sqrt{\pi^2 + \ln^2(\%)}} = \zeta
$$

## Summary

$$
\begin{aligned}
\zeta &= \frac{-\ln(\%)}{\sqrt{\ln(\%)^2+\pi^2}}\\
T_s &= \frac{4}{\zeta \omega_n}\\
T_p &= \frac{\pi}{\sqrt{1-\zeta^2} \omega_n}
\end{aligned}
$$

where $T_s$ represents settling time, $T_p$ represents peak time. consider $s^2 + 2\zeta \omega_n s + \omega_n^2$, we can determine the coefficients for $s, 1$ by
$$
\begin{aligned}
2\zeta \omega_n &= \frac{8}{T_s} = \frac{-2 \ln(\%)}{T_p}\\
\omega_n^2 &= \frac{16 (\ln(\%)^2+\pi^2)}{\ln(\%)^2 T_s^2}
= \frac{\ln(\%)^2+\pi^2}{T_p^2}
\end{aligned}
$$


---
title: Lecture 4-Stability and Steady Error
toc: true
categories: [控制原理, PNW课件]
tags:
  - control system
  - math
---

### Steady Error

<!--more-->

assumption: it has been verified to be stable by the method of Routh-Hurwitz Criterion

if D = 0

$$
\begin{aligned}
e_{ss}

&= \mathop{\text{lim}} \limits_{t\to+\infty} [r(t) - c(t)]\\

&=  \mathop{\text{lim}} \limits_{s\to 0+} s[R(s) - C(s)]\\

&=  \mathop{\text{lim}} \limits_{s\to 0+} sR(s) [1 - T(s)]\\

&=  \mathop{\text{lim}} \limits_{s\to 0+} sR(s) [1 - C(sI-A)^{-1}B ]\\
\end{aligned}
$$

if $r(t)=u(t)$, step function, $R(s) = \frac{1}{s}$


$$
\begin{aligned}
e_{ss} &=  \mathop{\text{lim}} \limits_{s\to 0+}  [1 - C(sI-A)^{-1}B ]\\

&=   [1 - C(0\cdot I-A)^{-1}B ]\\

&= [1+ C A^{-1}B]
\end{aligned}
$$


if $r(t) = tu(t)$, here $R(s) = \frac{1}{s^2}$ only when $[1+ C A^{-1}B]=0$, the Steady Error $e_{ss}$ exists


$$
\begin{aligned}
e_{ss} &=  \mathop{\text{lim}} \limits_{s\to 0+}  \frac{[1 - C(sI-A)^{-1}B ]}{s}\\

&= \mathop{\text{lim}} \limits_{s\to 0+}  \frac{[1 - C(-A)^{-1}B ]}{s} - \frac{[C(sI-A)^{-1}B - C(-A)^{-1}B ]}{s}\\

&= \mathop{\text{lim}} \limits_{s\to 0+}  \frac{[1 + CA^{-1}B ]}{s} - C\mathop{\text{lim}} \limits_{s\to 0+} \frac{[(sI-A)^{-1} - (-A)^{-1}]}{s} B\\

&= \mathop{\text{lim}} \limits_{s\to 0+}  \frac{[1 + CA^{-1}B ]}{s} - C\mathop{\text{lim}} \limits_{s\to 0+} \frac{d(sI-A)^{-1}}{ds} B\\

&= \mathop{\text{lim}} \limits_{s\to 0+}  \frac{[1 + CA^{-1}B ]}{s} + C\mathop{\text{lim}} \limits_{s\to 0+} (sI-A)^{-2} B\\

&= \mathop{\text{lim}} \limits_{s\to 0+}  \frac{[1 + CA^{-1}B ]}{s} + CA^{-2} B\\
\end{aligned}
$$


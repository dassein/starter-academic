# Z transform

## Sampling
sampling interval T
$$
f_T(t) \equiv \sum_{k=0}^{\infty} f(kT) \delta(t-kT)
$$

## Laplace Transform
Let's' try to derive Z transform from Laplace transform
$$
\begin{aligned}
F_T(s) 
&\equiv \int_{0_{-}}^{\infty} f_T(t) e^{-st} dt = \sum_{k=0}^{\infty} f(kT) \int_{0_{-}}^{\infty} \delta(t-kT) e^{-st} dt\\
&= \sum_{k=0}^{\infty} f(kT) [e^{-Ts}]^k\\

f_T^{*}(t) 
&\equiv \frac{1}{2\pi j} \int_{\beta-j\infty}^{\beta+j\infty} F_T(s) e^{s t} ds
= \sum_{k=0}^{\infty} f(kT) \frac{1}{2\pi j} \int_{\beta-j\infty}^{\beta+j\infty} [e^{(t-kT)}]^s ds\\
&= \sum_{k=0}^{\infty} e^{(t-kT)\beta} f(kT) \{ \frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-jkT\omega} e^{j\omega t} d\omega \}\\
&= \sum_{k=0}^{\infty} e^{(t-kT)\beta} f(kT) \delta(t-kT)\\
&= \sum_{k=0}^{\infty} f(kT) \delta(t-kT)
\end{aligned}
$$

think about $\frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-jkT\omega} e^{j\omega t} d\omega$, introduce the parameter $a$, then
$$
\begin{aligned}
\frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-jkT\omega} e^{j\omega t} d\omega

&= \lim_{a\to 0} \frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{j(t-kT)\omega}  e^{-a\omega^2} d\omega\\

&= \lim_{a\to 0} e^{-\frac{(t-kT)^2}{4a}}
\frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-a[\omega - j\frac{(t-kT)}{2a}]^2} d\omega\\

&= \lim_{a\to 0} e^{-\frac{(t-kT)^2}{4a}}
\frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-a\omega^2} d\omega\\

&= \lim_{a\to 0} e^{-\frac{(t-kT)^2}{4a}}
\frac{1}{2\pi} \pi^{\frac{1}{2}} a^{-\frac{1}{2}}\\

&= \lim_{a\to 0} \frac{\pi^{-\frac{1}{2}} a^{-\frac{1}{2}}}{2} e^{-\frac{(t-kT)^2}{4a}} 
\quad 
[\frac{\pi^{-\frac{1}{2}} a^{-\frac{1}{2}}}{2} \int^{+\infty}_{-\infty} e^{-\frac{(t-kT)^2}{4a}} dt
= \frac{\pi^{-\frac{1}{2}} a^{-\frac{1}{2}}}{2} \pi^{\frac{1}{2}} 2 a^{\frac{1}{2}} = 1]\\

&= \delta(t-kT)
\end{aligned}
$$

To sum up, we can choose $\beta$ wisely, to make sure the convergence of  $F_T(s) = \sum_{k=0}^{\infty} f(kT) [e^{-Ts}]^k$, thus
$$
f_T(t) = f^{*}_T(t) = \sum_{k=0}^{\infty} f(kT) \delta(t-kT)\\
F_T(s) = \sum_{k=0}^{\infty} f(kT) [e^{-Ts}]^k
$$

## Keep the signal
$\hat{f}_T(t)=f(kT)$ keep the signal for $t \in [kT, (k+1)T)$

then, we have
$$
\begin{aligned}
\hat{f}_T(t) &\equiv \sum_{k=0}^{\infty} [f(kT) - f((k-1)T)] u(t-kT)\\

\hat{F}_T(s) &\equiv \sum_{k=0}^{\infty} [f(kT) - f((k-1)T)] \int_{0_{-}}^{\infty} u(t-kT) e^{-st} dt\\
&= \sum_{k=0}^{\infty} [f(kT) - f((k-1)T)] \int_{kT}^{\infty}e^{-st} dt\\
&= \sum_{k=0}^{\infty} [f(kT) - f((k-1)T)] \frac{[e^{-Ts}]^k}{s}\\
&= \Big\{ \sum_{k=0}^{\infty} f(kT) [e^{-Ts}]^k \Big\} \frac{[1 - e^{-Ts}]}{s}\\
&= F_T(s) \frac{[1 - e^{-Ts}]}{s}\\

\hat{f}^{*}_T(t) &\equiv \frac{1}{2\pi j} \int_{\beta-j\infty}^{\beta+j\infty} \hat{F}(s) e^{s t} ds\\
&= \sum_{k=0}^{\infty} [f(kT) - f((k-1)T)] \frac{1}{2\pi j} \int_{\beta-j\infty}^{\beta+j\infty} \frac{[e^{(t-kT)}]^s}{s} ds\\
&= \sum_{k=0}^{\infty} e^{(t-kT)\beta} [f(kT) - f((k-1)T)] \{ \frac{1}{2\pi} \int_{-\infty}^{+\infty} \frac{ e^{-jkT\omega} e^{j\omega t} }{\beta + j\omega} d\omega \}\\
&= \sum_{k=0}^{\infty} e^{(t-kT)\beta} [f(kT) - f((k-1)T)] \{ e^{-(t-kT)\beta} u(t-kT)\}\\
&= \sum_{k=0}^{\infty} [f(kT) - f((k-1)T)] u(t-kT) \\
& [u(t)|_{t=0} = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \frac{1}{\beta + j\omega} d\omega = \frac{1}{2\pi j} \lim_{A\to \infty} \ln(\frac{A-j\beta}{-A-j\beta}) = \frac{1}{2}]
\end{aligned}
$$

On the other hand, let's set $t\to 0$, then
$$
\begin{aligned}
f(t) &= \lim_{T\to 0} \hat{f}_T(t)\\
F(s) &= \lim_{T\to 0} \hat{F}_T(s)
= \lim_{T\to 0} F_T(s) \lim_{T\to 0} \frac{[1 - e^{-Ts}]}{s}\\
&= T \lim_{T\to 0} F_T(s)\\
&= T \lim_{T\to 0} \Big\{ \sum_{k=0}^{\infty} f(kT) [e^{-Ts}]^k \Big\}\\
&\equiv \int_{0_{-}}^{\infty} f(t) e^{-st} dt \quad [T=dt, kT=t]
\end{aligned}
$$

## Z transform and Fourier transform 

Think about the flip side, the inverse transform of  Z transform and Fourier transform
$$
\begin{aligned}
x(n) &= \frac{1}{2\pi j} \oint_C X(z) z^{n-1} dz \quad [C \text{ contains poles of } X(z)]\\
X(z) &= \sum^\infty_{n=0} x(n) z^{-n}
\end{aligned}
$$

Here replace $z = e^{sT}$, we have
$$
\begin{aligned}
f(nT) = x(n) &= \frac{1}{2\pi j} \oint_C X(z) e^{s(n-1)T} de^{sT}\\
&= \frac{1}{2\pi j} \int_{\beta-\frac{\pi}{T} j}^{\beta+\frac{\pi}{T} j} T X(z) e^{snT} ds\\

X(z) &= \sum^\infty_{n=0} x(n) z^{-n}\\
&= \sum^\infty_{n=0} f(nT) e^{-snT}\\
\end{aligned}
$$

Think about the following function
$$
\begin{aligned}
f_z(t)|_{t=nT} &= f(nT)\\
F_z(s) &= TX(z) [u(\text{Im}(s)+\frac{\pi}{T}) - u(\text{Im}(s)-\frac{\pi}{T})]\\
&= [\sum^\infty_{n=0} f(nT) e^{-snT}] \cdot T [u(\text{Im}(s)+\frac{\pi}{T}) - u(\text{Im}(s)-\frac{\pi}{T})]\\
&= F_T(s) \cdot F_u(s)
\end{aligned}
$$

If we know $f_T(t) = \mathbf{L^{-1}}[F_T(s)], f_u(t) = \mathbf{L^{-1}}[F_u(s)]$\
Then we have $f_z(t) = f_T(t) * f_u(t)$

$$
\begin{aligned}
f_T(t) &= \sum_{n=0}^{\infty} f(nT) \delta(t-nT)\\
f_u(t) &= \frac{1}{2\pi j} \int_{\beta-\infty}^{\beta+\infty} T[u(\text{Im}(s)+\frac{\pi}{T}) - u(\text{Im}(s)-\frac{\pi}{T})]  e^{st} ds\\
&= \frac{1}{2\pi} e^{\beta t}T \int^{+\frac{\pi}{T}}_{-\frac{\pi}{T}} e^{j\omega t} d\omega\\
&= e^{\beta t} \frac{\sin (\frac{\pi}{T}t)}{(\frac{\pi}{T}t)} \quad [t\in (-\infty, +\infty)]\\

f_z(t) &= f_T(t) * f_u(t) = \sum_{n=0}^{\infty} f(nT) e^{\beta (t-nT)} \frac{\sin (\frac{\pi}{T}(t-nT))}{(\frac{\pi}{T}(t-nT))} \quad [t\in (-\infty, +\infty)]\\

&= e^{\beta t} \sum_{n=0}^{\infty} f(nT) e^{-\beta nT} \frac{\sin (\frac{\pi}{T}(t-nT))}{(\frac{\pi}{T}(t-nT))} \quad [t\in (-\infty, +\infty)]\\

F_z(s) &= \mathbf{L}(f_z(t)) = \mathbf{F}(f_z(t)e^{-\beta t})\\
&= \mathbf{F}[\sum_{n=0}^{\infty} f(nT) e^{-\beta nT} \frac{\sin (\frac{\pi}{T}(t-nT))}{(\frac{\pi}{T}(t-nT))}]\\
&= \sum_{n=0}^{\infty} f(nT) e^{-\beta nT} \mathbf{F}[\frac{\sin (\frac{\pi}{T}(t-nT))}{(\frac{\pi}{T}(t-nT))}]\\
&=[\sum_{n=0}^{\infty} f(nT) e^{-(\beta+j\omega) nT}]
\int^{+\infty}_{-\infty} \frac{\sin (\frac{\pi}{T}(t-nT))}{(\frac{\pi}{T}(t-nT))} e^{-j\omega (t-nT)} d(t-nT)\\
&=[\sum_{n=0}^{\infty} f(nT) e^{-(\beta+j\omega) nT}]
\int^{+\infty}_{-\infty} \frac{\sin (\frac{\pi}{T}x)}{(\frac{\pi}{T}x)} e^{-j\omega x} dx\\
&=[\sum_{n=0}^{\infty} f(nT) e^{-(\beta+j\omega) nT}]
\int^{+\infty}_{-\infty} \frac{\sin (\frac{\pi}{T}x)}{(\frac{\pi}{T}x)} e^{j\omega x} dx\\
&=[\sum_{n=0}^{\infty} f(nT) e^{-(\beta+j\omega) nT}]
\frac{T}{2\pi j}\int^{+\infty}_{-\infty} \frac{e^{j\frac{\pi}{T}x} - e^{-j\frac{\pi}{T}x}}{x} e^{j\omega x} dx\\
&= [\sum_{n=0}^{\infty} f(nT) e^{-(\beta+j\omega) nT}] \cdot
T[u(\omega+\frac{\pi}{T}) - u(\omega-\frac{\pi}{T})]\\
&= [\sum^\infty_{n=0} f(nT) e^{-snT}] \cdot T [u(\text{Im}(s)+\frac{\pi}{T}) - u(\text{Im}(s)-\frac{\pi}{T})]
\end{aligned}\\
[\quad \int^{+\infty}_{-\infty} \frac{e^{j(\omega+a)x} - e^{j(\omega-a)x}}{x} dx = 2\pi j [u(\omega+a)-u(\omega-a)]\quad, a=\frac{\pi}{T} ]
$$

The reason is
$$
\begin{aligned}
\int^{+\infty}_{-\infty} \frac{e^{j(\omega+a)x} - e^{j(\omega-a)x}}{x} dx
&= \lim_{\epsilon \to 0+} [\int^{+\infty}_{+\epsilon} + \int^{+\epsilon}_{-\epsilon} + \int^{-\epsilon}_{-\infty}]\\
&= \lim_{\epsilon \to 0+} [\int^{+\infty}_{+\epsilon} + \int^{-\epsilon}_{-\infty}] + \lim_{\epsilon \to 0+} \int^{+\epsilon}_{-\epsilon} [j2a + o(1)] dx\\
&= \lim_{\epsilon \to 0+} [\int^{+\infty}_{+\epsilon} + \int^{-\epsilon}_{-\infty}] + \lim_{\epsilon \to 0+} j4a\epsilon\\
&= \lim_{\epsilon \to 0+} j2 \int^{+\infty}_{+\epsilon} \frac{\sin((\omega+a)x) - \sin((\omega+a)x)}{x} dx + 0\\
&= j\pi [\text{sgn}(\omega+a) - \text{sgn}(\omega-a)]\\
&= 2\pi j [u(\omega+a)-u(\omega-a)]
\end{aligned}
$$


we will find poles for $F_z(s)$, here
$$
s_k = \beta_k + j \omega_k + j m \frac{2\pi}{T} \quad m \in Z
$$

In the other way
$$
\begin{aligned}
f_z^{*}(t) &= \frac{1}{2\pi j} \int^{\beta + j\infty}_{\beta - j\infty} F_z(s) e^{st} ds\\
&= \frac{1}{2\pi j} \int^{\beta + j\infty}_{\beta - j\infty} 
[\sum^\infty_{n=0} f(nT) e^{-snT}] \cdot T [u(\text{Im}(s)+\frac{\pi}{T}) - u(\text{Im}(s)-\frac{\pi}{T})] e^{st} ds\\
&= \sum^\infty_{n=0} f(nT) [\frac{T}{2\pi j} \int^{\beta + j\frac{\pi}{T}}_{\beta - j\frac{\pi}{T}} e^{s(t-nT)} ds]\\
&= \sum^\infty_{n=0} f(nT) [\frac{T}{2\pi j} e^{\beta(t-nT)} 2j \frac{\sin(\frac{\pi}{T}(t-nT))}{(t-nT)}]\\
&= \sum_{n=0}^{\infty} f(nT) e^{\beta (t-nT)} \frac{\sin (\frac{\pi}{T}(t-nT))}{(\frac{\pi}{T}(t-nT))}\\

f_z^{*}(nT) &= f(nT)
\end{aligned}
$$


## Z transform and Laplace transform

define $x(n), X(z)$, with $e^{sT} = z, \text{Im}(s)\in (-\frac{\pi}{T}, +\frac{\pi}{T}), z\in C$, here we have

$$
x(n) \equiv f_z(t)|_{t=nT} = f(nT)\\
X(z) \equiv \frac{F_z(s)}{T} =[\sum^\infty_{n=0} f(nT) e^{-snT}] = [\sum^\infty_{n=0} f(nT) z^{-n}]
$$

So, inverse Z transformation is derived from inverse Laplace transform
$$
\begin{aligned}
x(n) &\equiv f_z(t)|_{t=nT} = \mathbf{L^{-1}}[F_z(s)]|_{t=nT}\\
&= [\frac{1}{2\pi j} \int^{\beta + j\infty}_{\beta - j\infty} F_z(s) e^{st} ds] |_{t=nT}\\
&= [\frac{1}{2\pi j} \int^{\beta + j\frac{\pi}{T}}_{\beta - j\frac{\pi}{T}} F_z(s) e^{st} ds] |_{t=nT}\\
&= \frac{1}{2\pi j} \oint_{|z| = e^{\beta}} TX(z) z^{n} d\frac{\ln(z)}{T}\\
&= \frac{1}{2\pi j} \oint_{|z| = e^{\beta}} X(z) z^{n-1} dz
\end{aligned}
$$

## Z transform and DTFT
when $n \in (\infty, +\infty), \beta = 0$

$$
\begin{aligned}
f_{DTFT}(t) &= \sum_{n=-\infty}^{\infty} f(nT) \frac{\sin (\frac{\pi}{T}(t-nT))}{(\frac{\pi}{T}(t-nT))}\\

F_{DTFT}(j\omega) &= F_z(s)|_{\text{Re}(s)=0} \\
&= [\sum^\infty_{n=0} f(nT) e^{-snT}] \cdot T [u(\text{Im}(s)+\frac{\pi}{T}) - u(\text{Im}(s)-\frac{\pi}{T})]|_{\text{Re}(s)=0}\\
&= [\sum^\infty_{n=0} f(nT) e^{-j\omega T n}] \cdot T [u(\omega+\frac{\pi}{T}) - u(\omega -\frac{\pi}{T})]\\
&= [\sum^\infty_{n=0} f(nT) e^{-j\Omega n}] \cdot T [u(\Omega+\pi) - u(\Omega -\pi)] \quad [\Omega \equiv \omega T]

\end{aligned}
$$

Here we have $e^{sT} = e^{(\beta + j\omega)T} = e^{B} e^{j\Omega}$
$$
\begin{aligned}
x(n) &\equiv f_{DTFT}(t)|_{t=nT} = f(nT)\\
X(e^{j\Omega}) &\equiv \frac{F_{DTFT}(j\omega)}{T}\\
&=[\sum^\infty_{n=0} f(nT) e^{-j\omega nT}] = [\sum^\infty_{n=0} x(n) e^{-j\Omega n}]\\

x(n) &= [\frac{1}{2\pi j} \int^{ + j\infty}_{ - j\infty} F_{DTFT}(j\omega) e^{j\omega t} dj\omega] |_{t=nT}\\
&= \frac{1}{2\pi} \int^{ + \pi/T}_{ - \pi/T} F_{DTFT}(j\omega) e^{j\omega T n} d\omega\\
&= \frac{1}{2\pi} \int^{ + \pi}_{ - \pi} T X(e^{j\Omega}) e^{j\Omega n} d\frac{\Omega}{T}\\
&= \frac{1}{2\pi} \int^{ + \pi}_{ - \pi} X(e^{j\Omega}) e^{j\Omega n} d\Omega
\end{aligned}
$$


## DTFT


$$
\begin{aligned}
X(f) &= \int_{-\infty}^{\infty} x(t) e^{-j2\pi ft} dt\\
x^*(t) &= \int_{-\infty}^{\infty} X(f) e^{j2\pi ft} df\\
\end{aligned}
$$


When $\hat{x}(t) = x(t) p(t) = x(t) \cdot \sum \delta(t-nT)= \sum x(nT)  \delta(t-nT)$, then we have $\lambda < 1$ that
$$
\begin{aligned}
\hat{X}(f) &= \int_{-\infty}^{\infty} \hat{x}(t) e^{-j2\pi ft} dt = \sum_n x(nT) \int_{-\infty}^{\infty} \delta(t-nT)e^{-j2\pi ft} dt\\
&=\sum_n x(nT) e^{-j2 \pi n (f/f_s)}\\
\hat{x}^*(t) &= \int_{-\infty}^{\infty} \hat{X}(f) e^{j2\pi ft} df\\
x(nT) &=\int_{-\infty}^{\infty} \hat{x}^*(t) [\text{u}(t-(n-\lambda)T)-\text{u}(t-(n+\lambda)T)] dt\\
&= \int_{-\infty}^{\infty}  \int_{-\infty}^{\infty} \hat{X}(f) e^{j2\pi ft} df [\text{u}(t-(n-\lambda)T)-\text{u}(t-(n+\lambda)T)] dt\\
&= \int_{-\infty}^{\infty} \hat{X}(f) df  \int_{-\infty}^{\infty} e^{j2\pi ft} [\text{u}(t-(n-\lambda)T)-\text{u}(t-(n+\lambda)T)] dt\\
&= \int_{-\infty}^{\infty} \hat{X}(f) df  \int_{(n-\lambda)T}^{(n+\lambda)T} e^{j2\pi ft} dt\\
&= \int_{-\infty}^{\infty} \hat{X}(f) df  \int_{(n-\lambda)}^{(n+\lambda)} e^{j2\pi (f/f_s)t'} dt'/f_s  \quad[t' = f_s t]\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) \frac{e^{j2\pi (f/f_s)(n+\lambda)}-e^{j2\pi (f/f_s)(n-\lambda)}}{j2\pi  (f/f_s)}\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) e^{j2\pi (f/f_s)n} \frac{e^{j2\pi (f/f_s)\lambda}-e^{-j2\pi (f/f_s)\lambda}}{j2\pi  (f/f_s)}\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) e^{j2\pi (f/f_s)n} \frac{2\lambda j\sin(2\pi(f/f_s)\lambda)}{j2\pi  (f/f_s)\lambda}\\
&= 2\lambda \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) e^{j2\pi (f/f_s)n} \frac{\sin(2\pi(f/f_s)\lambda)}{2\pi  (f/f_s)\lambda}\\
\end{aligned}
$$

If we replace kernel function: $[\text{u}(t-(n-\lambda)T)-\text{u}(t-(n+\lambda)T)]$ with function
$$
\frac{\sin(\pi f_s(t-nT))}{\pi f_s(t-nT)} = \frac{e^{j2\pi (f_s/2)(t-nT)}-e^{-j2\pi (f_s/2)(t-nT)}}{j2\pi f_s(t-nT)}
$$
We still have:
$$
\int_{-\infty}^{\infty} \hat{x}^*(t) \frac{\sin(\pi f_s(t-nT))}{\pi f_s(t-nT)} dt\\
= \int_{-\infty}^{\infty} \sum_{n'} x(n'T)  \delta(t-n'T) \frac{\sin(\pi f_s(t-nT))}{\pi f_s(t-nT)} dt\\
= \sum_{n'} x(n'T)  \int_{-\infty}^{\infty} \delta(t-n'T) \frac{\sin(\pi f_s(t-nT))}{\pi f_s(t-nT)} dt\\
= \sum_{n'} x(n'T) \frac{\sin(\pi (f_s/f_s)(n'-n))}{\pi (f_s/f_s)(n'-n)}  \int_{-\infty}^{\infty} \delta(t-n'T) dt\\
= \sum_{n'} x(n'T) \delta(n'-n) = x(nT)
$$
So, we have:
$$
\begin{aligned}
x(nT)&=\int_{-\infty}^{\infty} \hat{x}^*(t) \frac{\sin(\pi(t-nT))}{\pi(t-nT)} dt\\
&= \int_{-\infty}^{\infty} \hat{X}(f) df  \int_{-\infty}^{\infty} e^{j2\pi ft}\frac{\sin(2\pi (f_s/2)(t-nT))}{2\pi (f_s/2)(t-nT)}dt\\
&= \int_{-\infty}^{\infty} \hat{X}(f) df  \int_{-\infty}^{\infty} e^{j2\pi ft} \frac{e^{j2\pi (f_s/2)(t-nT)}-e^{-j2\pi (f_s/2)(t-nT)}}{2j2\pi (f_s/2)(t-nT)}dt\\
&= \int_{-\infty}^{\infty} \hat{X}(f) df \cdot [e^{-j2\pi n} \int_{-\infty}^{\infty} e^{j2\pi ft} \frac{e^{j2\pi (f_s/2) t}}{j2\pi f_s(t-nT)}dt - e^{ j2\pi n} \int_{-\infty}^{\infty} e^{j2\pi ft} \frac{e^{-j2\pi (f_s/2) t}}{j2\pi f_s(t-nT)}dt]\\
&= \int_{-\infty}^{\infty} \hat{X}(f) df \cdot [e^{-j2\pi n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s)t'} \frac{e^{j\pi t'}}{j2\pi (t'-n)}dt'/f_s - e^{ j2\pi n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s)t'} \frac{e^{-j\pi  t'}}{j2\pi (t'-n)}dt'/f_s]\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) \cdot [e^{-j2\pi n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s+0.5)t'} \frac{1}{j2\pi (t'-n)}dt' - e^{ j2\pi n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s-0.5)t'} \frac{1}{j2\pi (t'-n)}dt']\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) \cdot [e^{-j2\pi n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s+0.5)(t'+n)} \frac{1}{j2\pi t'}dt' - e^{ j2\pi n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s-0.5)(t'+n)} \frac{1}{j2\pi t'}dt']\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) \cdot [e^{-j2\pi n}e^{j2\pi (f/f_s+0.5)n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s+0.5)t'} \frac{1}{j2\pi t'}dt' - e^{ j2\pi n} e^{j2\pi (f/f_s-0.5)n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s-0.5)t'} \frac{1}{j2\pi t'}dt']\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) [e^{j2\pi (f/f_s)n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s+0.5)t'} \frac{1}{j2\pi t'}dt' - e^{j2\pi (f/f_s)n} \int_{-\infty}^{\infty} e^{j2\pi (f/f_s-0.5)t'} \frac{1}{j2\pi t'}dt' ]\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) e^{j2\pi (f/f_s)n} [\int_{-\infty}^{\infty} e^{j2\pi (f/f_s+0.5)t'} \frac{1}{j2\pi t'}dt' - \int_{-\infty}^{\infty} e^{j2\pi (f/f_s-0.5)t'} \frac{1}{j2\pi t'}dt' ]\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) e^{j2\pi (f/f_s)n} \frac{1}{2}[\text{sgn}(f/f_s+0.5) - \text{sgn}(f/f_s-0.5) ]\\
&= \int_{-\infty}^{\infty} \hat{X}(f) d(f/f_s) e^{j2\pi (f/f_s)n} [\text{u}(f/f_s+0.5) - \text{u}(f/f_s-0.5) ]\\
&= \int_{-0.5}^{0.5} \hat{X}(f) e^{j2\pi (f/f_s)n} d(f/f_s)\\
\end{aligned}
$$


because $\text{sgn}(t) \leftrightarrow \frac{1}{j\pi f}$, then we have $\frac{1}{j\pi t} \leftrightarrow \text{sgn}(-f)=-\text{sgn}(f)$,

Thus means
$$
-\text{sgn}(f) = \int^{\infty}_{-\infty} \frac{1}{j\pi t} e^{-j2\pi ft} dt\\
\text{sgn}(f) =-\text{sgn}(-f) = \int^{\infty}_{-\infty} \frac{1}{j\pi t} e^{j2\pi ft} dt\\
\text{sgn}(f/f_s+0.5)= \int^{\infty}_{-\infty} \frac{1}{j\pi t} e^{j2\pi (f/f_s+0.5)t} dt = 2\text{u}(f/f_s+0.5)-1\\
\text{sgn}(f/f_s-0.5)= \int^{\infty}_{-\infty} \frac{1}{j\pi t} e^{j2\pi (f/f_s-0.5)t} dt = 2\text{u}(f/f_s-0.5)-1\\
$$
To sum up:

for $\hat{x}(t) = x(t) p(t) = x(t) \cdot \sum \delta(t-nT)= \sum x(nT)  \delta(t-nT)$, we have
$$
\begin{aligned}
\hat{X}(f) &= \int_{-\infty}^{\infty} \hat{x}(t) e^{-j2\pi ft} dt\\
&=\sum_n x(nT) e^{-j2 \pi n (f/f_s)}\\
\hat{x}^*(t) &= \int_{-\infty}^{\infty} \hat{X}(f) e^{j2\pi ft} df\\
x(nT) &= \int_{-\infty}^{\infty} \hat{x}^*(t) \frac{\sin(\pi(t-nT))}{\pi(t-nT)} dt\\
&= \int_{-0.5}^{0.5} \hat{X}(f) e^{j2\pi (f/f_s)n} d(f/f_s)\\
\end{aligned}
$$
Now define $\omega = 2\pi f/f_s$, then
$$
X(e^{jw}) \equiv \hat{X}(f) = \sum_n x(nT) [e^{j\omega}]^{-n}\\
x(nT)=  \int_{-0.5}^{0.5} \hat{X}(f) e^{j2\pi (f/f_s)n} d(f/f_s) = \frac{1}{2\pi} \int_{2\pi} X(e^{jw}) [e^{j\omega}]^{n} d\omega
$$

<div STYLE="page-break-after: always;"></div>

## Formula for Comb function and Rectangular signal 

$$
\text{FT}[\delta(t)] = \int\delta(t) e^{-j2\pi ft} dt = \int\delta(t) e^{-j2\pi f0} dt = 1\cdot \int\delta(t) dt=1(f)\\
\text{so, } \delta(t) = \text{FT}^{-1}[1(f)] = \int 1 \cdot e^{j2\pi ft} df
$$

then replace $f\to t, t\to -f$, having
$$
\begin{aligned}
\delta(-f) &= \int1(t) \cdot e^{j2\pi t(-f)} dt = \text{FT}[1(t)]\\
&= \delta(f)
\end{aligned}
$$
Thus Fourier pair $1(t) \leftrightarrow \delta(f)$, now we want to verify:
$$
\begin{aligned}
\sum_n \delta(t-nT) &= \frac{1}{T} \sum_k e^{j2\pi k(\frac{t}{T})}  \quad [\alpha\delta(\alpha t') = \delta(t'), t'=\frac{t}{T}=tf_s]\\  
\sum_n \delta(t'-n) &= \sum_k e^{j2\pi k t'}
\end{aligned}
$$
Here we notice: the Fourier transform (FT) of a rectangular pulse is the sinc function

The Fourier transform (DFT) of a rectangular signal after pulse discrete sampling is the Dirichlet function
$$
\begin{aligned}
\sum_{k=-A}^{A}e^{j2\pi kt'} &= 1+ 2 \sum_{k=1}^A \cos(2\pi t' k)\\
\sin(\pi t' ) \sum_{k=-A}^{A}e^{j2\pi kt'} &= \sin(\pi t' ) + \sum_{k=1}^A[ \sin(2\pi t'(k+0.5)) - \sin(2\pi t'(k-0.5)) ]\\
&= \sin(2\pi t'(A+0.5)) = \sin(\pi t'(2A+1))\\
\sum_{k=-A}^{A}e^{j2\pi kt'} &= \frac{\sin(\pi t'(2A+1))}{\sin(\pi t' )}
\end{aligned}
$$


Moreover, $ \frac{\sin(\pi (t'+\Delta) (2A+1))}{\sin(\pi (t'+\Delta) )}=  \frac{\sin(\pi t'(2A+1))}{\sin(\pi t' )}, \Delta\in Z$, the period is 1:
$$
\int_{-0.5}^{0.5} \frac{\sin(\pi t'(2A+1))}{\sin(\pi t' )} dt' = \sum_{k=-A}^{A}  \int_{-0.5}^{0.5}e^{j2\pi kt'} dt'= \sum_{k=-A}^{A} \delta(k) = 1
$$


So, $\lim_{A\to \infty} \frac{\sin(\pi t'(2A+1))}{\sin(\pi t' )}[\text{u}(t'+0.5)-\text{u}(t'-0.5)] = \delta(t')$, then we have
$$
\begin{aligned}
\lim_{A\to \infty} \sum_{k=-A}^{A}e^{j2\pi kt'} &= \lim_{A\to \infty} \frac{\sin(\pi t'(2A+1))}{\sin(\pi t' )}\\
&= \lim_{A\to \infty} \sum_n \frac{\sin(\pi t'(2A+1))}{\sin(\pi t' )} [\text{u}(t'+0.5-n)-\text{u}(t'-0.5-n)] \\
&= \lim_{A\to \infty} \sum_n \frac{\sin(\pi (t'-n)(2A+1))}{\sin(\pi (t'-n) )} [\text{u}(t'+0.5-n)-\text{u}(t'-0.5-n)] \\
&= \sum_n \lim_{A\to \infty} \frac{\sin(\pi (t'-n)(2A+1))}{\sin(\pi (t'-n) )} [\text{u}(t'+0.5-n)-\text{u}(t'-0.5-n)] \\
&= \sum_n \delta(t'-n) \\
\end{aligned}
$$
Thus,
$$
\sum_n \delta(t'-n) = \sum_k e^{j2\pi k t'} \quad[t=t' T]\\
T\sum_n \delta(t-nT) =  \sum_n \delta(t/T-n) = \sum_k e^{j2\pi k(\frac{t}{T})}
$$

<div STYLE="page-break-after: always;"></div>

## DFT

Sample $\hat{x}(t) = x(t) p(t) = x(t) \cdot \sum \delta(t-nT)= \sum x(nT)  \delta(t-nT)$ in a period 0~NT
$$
\begin{aligned}
\tilde{x}(t) &= \left\{ \hat{x}(t) \left[ \text{u}(t)-\text{u}(t-NT) \right]  \right\} * \sum_{n'} \delta(t-n'NT)\\
&= \left\{  \sum_{n=0}^{N-1} x(nT)  \delta(t-nT) \right\} * \sum_{n'} \delta(t-n'NT)\\
&=  \sum_{n'} \left\{  \sum_{n=0}^{N-1} x(nT)  \delta(t-(n+n'N)T) \right\}  \\
\end{aligned}
$$


For frequency domain:
$$
\begin{aligned}
\tilde{X}(f) &= \int_{-\infty}^{\infty} \tilde{x}(t) e^{-j2\pi ft} dt \\
&=  \sum_{n'} \left\{  \sum_{n=0}^{N-1} x(nT)  [ \int_{-\infty}^{\infty} \delta(t-(n+n'N)T) e^{-j2\pi ft} dt] \right\} \\
&=  \sum_{n'} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (f/f_s)(n+n'N)}  \right\} \\
&=  \sum_{n'} e^{-j2\pi (\frac{f}{f_s/N})n'} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (f/f_s)n}  \right\}  \quad[\sum_n \delta(t'-n) = \sum_k e^{j2\pi k t'}] \\
&=  \sum_{k} \delta(\frac{f}{f_s/N}-k) \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (f/f_s)n}  \right\}\\
&=  \frac{f_s}{N} \sum_{k} \delta(f-k\frac{f_s}{N}) \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (f/f_s)n}  \right\}\\
&=  \frac{f_s}{N} \sum_{k} \delta(f-k\frac{f_s}{N}) \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (k/N)n}  \right\}\\
&= \sum_{k} \delta(f-k\frac{f_s}{N}) \Bigg[\frac{f_s}{N} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (k/N)n}  \right\} \Bigg]
\end{aligned}
$$
Reconstruction:
$$
\begin{aligned}
\tilde{x}^*(t) &= \int_{-\infty}^{\infty} \tilde{X}(f) e^{j2\pi ft} df\\
&=\int_{-\infty}^{\infty} e^{j2\pi ft} df \sum_{k} \delta(f-k\frac{f_s}{N}) \Bigg[\frac{f_s}{N} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (k/N)n}  \right\} \Bigg] \\
&= \sum_{k} \Bigg[\frac{f_s}{N} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (k/N)n}  \right\} \Bigg]  \int_{-\infty}^{\infty} e^{j2\pi ft} \delta(f-k\frac{f_s}{N}) df \\
&= \sum_{k} \Bigg[\frac{f_s}{N} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (k/N)n}  \right\} \Bigg]  e^{j2\pi (k/N)f_st} \\
x(nT) &= \int_{-\infty}^{\infty} \tilde{x}^*(t) \frac{\sin(\pi(t-nT))}{\pi(t-nT)} dt\\
&= \int_{-0.5}^{0.5} \tilde{X}(f) e^{j2\pi (f/f_s)n} d(f/f_s) = \int_{0}^{1} \tilde{X}(f) e^{j2\pi (f/f_s)n} d(f/f_s)\\
&=  \int_{0}^{1} e^{j2\pi (f/f_s)n} d(f/f_s)  \sum_{k} \delta(f-k\frac{f_s}{N}) \Bigg[\frac{f_s}{N} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (k/N)n}  \right\} \Bigg]\\  
&= \sum_{k} \int_{0}^{1} e^{j2\pi (\frac{f}{f_s})n} \delta(\frac{f}{f_s}-\frac{k}{N})  d(\frac{f}{f_s})
\Bigg[\frac{1}{N} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (k/N)n}  \right\} \Bigg]\\  
&= \sum_{k} \int_{0}^{1} e^{j2\pi (\frac{k}{N})n} \delta(\frac{f}{f_s}-\frac{k}{N})  d(\frac{f}{f_s})
\Bigg[\frac{1}{N} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (k/N)n}  \right\} \Bigg]\\
&= \sum_{k=0}^{N-1} e^{j2\pi (\frac{k}{N})n} \Bigg[\frac{1}{N} \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (k/N)n}  \right\} \Bigg]\\
&= \frac{1}{N} \sum_{k=0}^{N-1}  \left\{  \sum_{n=0}^{N-1} x(nT)  e^{-j2\pi (\frac{k}{N}) n}  \right\} e^{j2\pi (\frac{k}{N})n}
\end{aligned}
$$
To sum up, the Fourier transform (FT) of a rectangular pulse is the sinc function. The Fourier transform (FT) of a rectangular signal after pulse discrete sampling is the Dirichlet function. That is,  DTFT is equivalent to FT first, then convolve with the sinc function; DFT is equivalent to FT first, then convolve with the Dirichlet function.

title: Parity Distribution of Divisors of Integers
date: 2013-11-27
tags: undergrad, analysis, number theory
category: math

This paper studies parity distribution of divisors of all integers up to $n$, by dealing with a variant of the alternating harmonic series, namely

$$\lim_{n \to \infty} \left( \frac{1}{n} \sum_{\nu=1}^n (-1)^{\nu-1} \left[\frac{n}{\nu}\right] \right)$$

where $\left[x\right]$ is the floor function, In particular, it will be shown that this series converges to $\log 2$, by comparing it with the standard alternating harmonic series. This implies that of all integers up to $n$, both the numbers of odd and even divisors are of $O(n \log n)$, with odd ones slightly more than even ones by $2n \log 2$. This estimation is accurate to $n^{2/3}$. In a more general form, define $d_{m,k}(n)$ to be the number of divisors of $n$ that is congruent to $k$ modulo $m$, and $D_{m,k}(n) =
    \sum_{\nu=1}^n d_{m,k}(\nu)$, it is shown that $D_{m,k}(n)$ are asymptotically equivalent, with $D_{m,k}(n)$ slightly larger when $0 \le k < m$ smaller.

### Sum of the Series ###

Consider $n$ times the partial sum

$$L(n) = \sum_{\nu=1}^{n}{ (-1)^{\nu-1} \left[\frac{n}{\nu}\right] }.$$

We may divide the sum into two parts,

$$\Biggl( \sum_{1 \le \nu < m} + \sum_{m \le \nu \le n} \Biggr) (-1)^{\nu-1} \left[\frac{n}{\nu}\right]$$

where $m = n^{2/3}$. The estimation of the latter term is based on the observation that $\left[\frac{n}{\nu}\right]$ can take only $\frac{n}{m} = n^{1/3}$ values in the range $m \le \nu \le n$.

For a given integer $1 \le l \le n^{1/3}$, $\left[\frac{n}{\nu}\right] = l$ for  $\frac{n}{l+1} < \nu \le \frac{n}{l}$. Thanks to the alternating nature of the series, most summands in the sum of $(-1)^{\nu-1} \left[\frac{n}{\nu}\right]$ for $\nu$ in this range cancel, leaving at most one summand. Therefore the sum is $\pm l$ or $0$. In any case,

$$\left| \sum_{\frac{n}{l+1} < \nu \le \frac{n}{l}} (-1)^{\nu-1} \left[\frac{n}{\nu}\right] \right| \le l.$$

Now summing for $l$ over $1 \le l \le n^{1/3}$ (this covers $m \le \nu \le n$) we obtain

$$\begin{align}
    & \left| \sum_{m \le \nu \le n} (-1)^{\nu-1} \left[\frac{n}{\nu}\right] \right| \nonumber \\
    =& \sum_{1 \le l \le n^{1/3}}
    \sum_{\frac{n}{l+1} < \nu \le \frac{n}{l}} (-1)^{\nu-1} \left[\frac{n}{\nu}\right] \nonumber \\
    \le& 1 + 2 + \ldots + \left[n^{1/3}\right] = O(n^{2/3}) \label{part1}
\end{align}$$

as $n \to \infty$.

The estimation of the first term is done by comparing it with the standard alternating harmonic series. As there are no more than $n^{2/3}$ summands, the error will be small. $0 \le \frac{n}{\nu} - \left[\frac{n}{\nu}\right] < 1$, hence

$$\left| \sum_{\nu=1}^m {(-1)^{\nu-1} \biggl(\left[\frac{n}{\nu}\right] - \frac{n}{\nu} \biggr)}
    \right| \le n^{2/3}$$

Let $n \to \infty$, and note the fact that

$$\sum_{\nu=1}^\infty {\frac{(-1)^{\nu-1}}{\nu}} = \log 2,$$

the inequality above leads to

$$\label{part2} \frac{1}{n} \sum_{1 \le \nu < m}^{n} (-1)^{\nu-1} \left[\frac{n}{\nu}\right] = \log 2 + O(n^{-1/3})$$

as $n \to \infty$.

Putting and together, we obtain the desired result

$$\frac{1}{n} \sum_{\nu=1}^n (-1)^{\nu-1} \left[\frac{n}{\nu}\right] = \log 2 + O(n^{-1/3})$$

as $n \to \infty$.

### Implications in Number Theory ###

The relation between the series and number theory begins with the following observation:

$$\left[\frac{n}{m}\right] - \left[\frac{n-1}{m}\right] =
    \begin{cases}
        1 & \text{if } m \mid n \\
        0 & \text{if } m \nmid n \\
    \end{cases}$$

Now let $d(n)$ denote the number of divisors of $n$, and $d_0(n)$, $d_1(n)$ denote the number of even and odd divisors, respectively, of $n$. Then,

$$\begin{align}
    L(n) - L(n-1) &= \sum_{\nu=1}^n { (-1)^{\nu-1}
    \left(\left[\frac{n}{\nu}\right] - \left[\frac{n-1}{\nu}\right]\right) } \\
    &= \sum_{d \mid n} { (-1)^{d-1} } = d_1(n) - d_0(n).
\end{align}$$

Therefore, $L(n) - L(n-1)$ is the difference between the number of odd divisors and even divisors of $n$. Let $D_i(n) = \sum_{\nu=1}^n d_i(\nu)$, $i=1$, $2$, we have

$$\begin{align}
    L(n) &= \sum_{\nu=1}^n \left(L(\nu) - L(\nu-1)\right) \\
    &= \sum_{\nu=1}^n \left(d_1(\nu) - d_0(\nu)\right) = D_1(n) - D_0(n).
\end{align}$$

where $L(0) = d_0(0) = d_1(0) = 0$ for convenience. On the other hand, $D_1(n) + D_0(n) = D(n)$ is known to have the expansion:

$$D(n) = n \log n + (2\gamma - 1) n + O(\sqrt n).$$

Putting these together we obtain an interesting result, namely

$$\begin{align}
    D_1(n) &= \frac{1}{2}\big(n \log n + (2\gamma - 1 + \log2) n\big) +
    O(n^{2/3}) \\
    D_0(n) &= \frac{1}{2}\big(n \log n + (2\gamma - 1 - \log2) n\big) +
    O(n^{2/3})
\end{align}$$

This shows that, in fact,

$$\lim_{n \to \infty} \frac{D_1(n)}{D_0(n)} = 1$$

despite the irregularities in $d_1(n)$, $d_0(n)$, e.g. for odd $n$, $d_1(n) = d(n)$ while $d_0(n) = 0$; but for even $n = 2^r \cdot m$, $m$ odd, $d_1(n) = d(m)$ and $d_0 = r \cdot d(m)$. Actually, these fluctuations eliminate accurately that $D_0$ and $D_1$ are asymptoticly equivalent.

### Generalizations ###

This result describes the distribution of the parity of divisors. Namely, the total number of odd and even divisors of all integers up to $n$ differs only by a quantity of lower order, $2n\log2$. Also note that the convergence alone (not regarding what limit it converges to) implies the asymptotic equivalence between $D_0$ and $D_1$, and the key in the above argument is the cancellation process demonstrated in . Thus some generalizations are possible.

Let $d_{m,k}(n)$ denote the number of divisors of $n$ that is congruent to $k$ modulo $m$, i.e., $\#\{d \mid n : d \equiv k \pmod m\}$, and $D_{m,k}$ the respective sum. It is desirable to show that for given $m$ and all $k_1$, $k_2$, $D_{m,k_1}(n) \sim D_{m,k_2}(n)$. This follows from the argument presented above almost unaltered. Actually, let

$$s(n) = \begin{cases}
        1 & \text{if } n \equiv k_1 \pmod m \\
        -1 & \text{if } n \equiv k_2 \pmod m \\
        0 & \text{otherwise},
      \end{cases}$$

we still have

$$\left| \sum_{\frac{n}{l+1}<\nu\le\frac{n}{l}} s(\nu)\left[\frac{n}{\nu}\right] \right|\le l.$$

So what remains is to show that $\sum_{\nu=1}^\infty {\frac{s(\nu)}{\nu}}$ converges, which follows from Leibniz’s test. The test also shows that the sum is positive whenever $k_1 < k_2$. Therefore, the fact that $D_{2,1}$ is slightly more than $D_{2,0}$ finds its analog for larger $m$, that is, $D_{m,k}(n)$ is larger by a quantity of $O(n)$ when $k$ is smaller.

Other generalizations can be suggested as well, such as adapting the argument above to study the series $\frac{1}{n}\sum_{\nu=1}^\infty \left[\frac{n}{\nu}\right]$, which might lead to new insight into the relation between harmonic series and $d_{m,k}$ functions.

title: ENS Entrance Math 1995
date: 2015-02-12
tags: grad school, problem set, exam
category: math

This is the ENS Entrance Exam 1995 Mathematics Written Part.  Translated by Tony Beta Lambda.

[TOC]

## Written Test of Mathematics ##
Duration: 4 hours

### Introduction ###

In an informal way, an elementary function is a function defined on an open set of ${\mathbb R}$ or ${\mathbb C}$ and that can be “expressed as compositions” with the help of the exponential function ($e^z = \sum_{n \ge 0} \frac{z^n}{n}$), the logarithm function ($\log(1+z) = \sum_{n \ge 1} \frac{(-1)^{n-1}z^n}{n}$), the rational operations (sum, product, quotient) and algebraic operations (taking the $n$-th roots). For example, the functions

$$\cos(z) = \frac{e^{iz}+e^{-iz}}{2}, \sin(z) = \frac{e^{iz}-e^{-iz}}{2i},$$

$$\frac{z^{1995 \sqrt[3]{\sin \frac{z^2}{1+z}}}}{e^{\sqrt{\log z}}},
\arctan z = \frac{\log(1+iz)-\log(1-iz)}{2i}$$

are elementary functions. It is plausible, after this vague definition, that the derivative of an elementary function is again elementary and it is well known that a rational fraction with real or complex coefficients admits an elementary function as the primitive. On the contrary, there exist very simple elementary functions that do not have an elementary primitive function: it is the case for example for the function $z \mapsto e^{z^2}$; it is therefore impossible to calculate “the” primitive for such a function, at least with the usual set of rules.

The aim of this test consists of one part formalizing the concept of elementary functions and the other part proving a criterion that originate from Liouville and improved by Ostrowski permitting to test if certain functions admit an elementary function as a primitive. The framework in this study is purely algebraic, the notion of a primitive being considered as the inverse of the derivative: one starts with a base field $K$ (think of the field of rational fractions over ${\mathbb R}$ or ${\mathbb C}$), an extension field $E$ of $K$ (one admits here that the set of functions that is can be expanded in power series on a connected open set of ${\mathbb R}$ or ${\mathbb C}$ is a integral ring, of which one can consider the field of fractions) and an operation of derivation $D \colon E \to E$ satisfying the usual properties (see below). It is then possible to define it in a rigorous manner that says “$f \in E$ is elementary over $K$” and to give in certain cases a criterion permitting the affirmative that $f \in E$ admits a primitive $g \in E$, i.e., $D(g) = f$, elementary over $K$.

### Preliminaries ###

We suppose that all fields considered in the problem is commutative and contains ${\mathbb Q}$; in particular, if $x$ is an element in such fields and $n \in {\mathbb Z}\setminus \{0\}$, then $nx = 0$ implies $x = 0$. One recalls that if $K$ is a field (commutative), the ring of polynomials $K[X]$ is an principle ideal ring.

-   Let $E$ be an extension field of the field $K$, this is to say a field containing $K$; an element $x \in E$ is *algebraic* over $K$ if there exists $P \in K[X] \setminus \{0\}$ such that $P(x) = 0$; it is call transcendental over $K$ otherwise. For $x \in E$, one writes $K(x)$ for the smallest subfield of $E$ containing $K$ and $x$.

1.  If $x \in E$ is algebraic over $K$, show the existence and uniqueness of a *monic* polynomial $P_x \in K[X]$ such that, for $Q \in K[X]$, one has the equivalence $Q(x) = 0 {\Leftrightarrow}P_x \mid Q$; show then that $K(x) = \bigoplus_{i=0}^{n-1} Kx^i$ where $n = \deg P_x$; in particular $\dim_K K(x) = n$.

    Conversely, if $K(x)$ is of finite dimension over $K$, show that $x$ is algebraic over $K$ (consider the powers of $x$ in the $K$-vector space $K(x)$).

    The polynomial $P_x$ is called the *minimal polynomial* of $x$ over $K$.

2.  If $x \in E$ is transcendental over $K$, show that the mapping $K(X) \to E, R \mapsto R(x)$ induces an isomorphism from the field of rational fractions $K(X)$ onto the field $K(x)$.

### The Derivations and their elementary properties ###

-   A *derivation* on the field $K$ is a mapping $D \colon K \to
        K$ satisfying:

$$D(u+v) = D(v)+D(v), D(uv) = D(u)v+D(v)u, u,v \in K.$$

-   A *differential field* $K$ is a field equipped with a derivation  $D$; one writes $K_{cst} = \{u \in K \mid D(u) = 0\}$ that is called the *subfield of constants*.

1.  What is $D(1)$? For $(u, v) \in K \times K^*$, express $D(u/v)$ in a function of $u$, $v$, $D(u)$, $D(v)$. An analog question for $D(u^n)$ with $(u, n) \in K \times {\mathbb N}$ or $(u, n) \in K^* \times {\mathbb Z}$.

    Verify that $K_{cst}$ is indeed a subfield of $K$. What properties does the “logarithmic derivative” $K^* \to K$ that associates $D(u)/u$ to $u$ possess? On what condition does one have $D(u)/u = D(v)/v$?

2.  If $P =\sum_i a_iX^i \in K[X]$, one writes $P^D$ for the polynomial $\sum_i D(a_i)X^i$ and $P'$ for the derivative polynomial in the usual sense, i.e., $\sum_i ia_iX^i$. For $u \in K$, verify that $D(P(u)) = P'(u)D(u) + P^D(u)$.

3.  One recalls that a polynomial with coefficients in $K$ is square-free if it is a product of distinct irreducible polynomials, this is to say, if the exponentials involved in the decomposition into prime factor are all equal to $1$. Let $D$ be a derivation on the field of rational fractions $K(X)$ verifying $D(K[X]) \subseteq K[X]$. One considers a *finite* family $(Q_j)_{j \in J}$ of nonzero square-free polynomials in $K[X]$, pairwise prime, and an identity:

$$\sum_{j \in J}\frac{P_j}{Q_j} = D\left( \frac{P}{Q} \right), P_j, P \in K[X], Q \in K[X] \setminus \{0\}, \gcd(P, Q) = 1.$$

Show that $Q$ divides $D(Q)$. Then show that if $j \in J$ is such that $\gcd(Q_j, Q) = 1$, then $Q_j \mid P_j$.

### Derivation on $K(X)$ of logarithmic type ###

-   A *differential extension field* $E$ of a field $K$ is an extension field of $K$ equipped with a derivation $D$ verifying $D(K) \subseteq K$ and having *the same subfield of constants* as $K$ (i.e., if $v \in E$ verifies $D(v) = 0$ then $v \in K$).

One considers in this part a derivation $D$ on the field of rational fractions $K(X)$ such that $K(X)$ is a differential extension field of $K$ and $D(X) \in K$.

1.  Let $P = \sum_i a_iX^i \in K[X]$; with the help of the expression of $D(P)$ as a function of $D(X)$, $P^D = \sum_i D(a_i)X^i$ and $P'$ (cf. question **I.2**), show that $D(P) \in K[X]$ and compare its degree with that of $P$. On what condition does one have $\deg D(P) < \deg P$?

2.  What are the *monic* polynomials $Q \in K[X]$ such that $Q$ divides $D(Q)$? the polynomials $P \in K[X]$ such that $D(P) \in K$?

3.  Let $R$ be a rational fraction in $K(X)$ such that $D(R) \in K$; show $R = cX + g$ with $c \in K_{cst}$ and $g \in K$.

In a differential field $K$, one calls *Liouville sum* in  $K$ all elements in $K$ of the form:

$$D(g) + \sum_{i=1}^n c_i\frac{D(f_i)}{f_i}, g \in K, c_i \in K_{cst}, f_i \in K \setminus \{0\}.$$

4.  Let $f \in K$; one suppose that $f$ is a Liouville sum *in* $K(X)$. Show that there exists $c \in K_{cst}$ such that $f - cD(X)$ is a Liouville sum in $K$. For this, one shows, starting from the definition of a Liouville sum in $K(X)$, that one can write $f$ under the form:

$$f = D(R) + \sum_{i \in I} c_i\frac{D(f_i)}{f_i} + \sum_{j \in J} d_j\frac{D(Q_j)}{Q_j},$$

$\text{with } R \in K(X), f_i \in K \setminus \{0\}, Q_j \in K[X] \setminus \{0\}, c_i, d_j \in K_{cst},$

the $Q_j$ being *distinct* polynomials in $K[X]$ of nonzero degree, irreducible and monic and then one utilizes the question **I.3**.

-   In a differential field $K$, one says that $v \in K$ is a *logarithm* of $u \in K \setminus \{0\}$ if $D(v) = D(u)/u$ (think of the formula $(\log u)' = u'/u$).

-   A differential extension field $E$ of $K$ is said to be *logarithmic* if it is of the form $E = K(v)$ where $v \in E$ is a logarithm of a function $u \in K \setminus \{0\}$.

5.  Let $E = K(v)$ be a logarithmic differential extension field, $v$ being supposed to be transcendental over $K$. Show the reduction theorem of Liouville: if $f \in K$ is a Liouville sum *in* $E$, then $f$ is a Liouville sum *in* $K$. For this, one transfers the derivation of $E$ to a derivation of $K(X)$ with the help of the isomorphism of fields $K(X) {\leftrightarrow}E$ (cf. the question **0.2**) and one applies the previous question.

### Derivation on $K(X)$ of exponential type ###

One considers in this part a derivation $D$ on the fields of rational fractions $K(X)$ such that:

$K(X)\text{ is a differential extension field of }K, \frac{D(X)}{X} \in K.$

The first assertion therefore signifies that $D(K) \subseteq K$ and $K(X)_{cst} = K_{cst}$ (in particular $D(X) \ne 0$).

1.  Let $P \in K[X]$; Show that $D(P) \in K[X]$ and compare its degree with that of $P$.

2.  Let $P \in K[X]$; show that $P$ divides $D(P)$ if and only if $P$ is of the form $aX^n$, with $a \in K$.

3.  Let $R \in K(X)$ be a rational fraction; show the if $D(R) \in K[X]$, then either $R \in K_{cst}$ or $R$ is a polynomial, of the same degree as $D(R)$ (in particular, if $D(R) \in K$ then $R \in K$).

4.  Let $f \in K$; one supposes that $f$ is a Liouville sum *in* $K(X)$. Show that there exists $c \in K_{cst}$ such that $f - cD(X)/X$ is a Liouville sum *in* $K$. For this, one reasons as in the question **II.4**.

    1.  In a differential field $K$, one says that $v \in K \setminus \{0\}$ is an *exponential* of $u \in K$ if $D(v)/v = D(u)$ (think of the formula $(e^u)' = u'e^u$).

    2.  A differential extension field $E$ of $K$ is said to be *exponential* if it is of the form $E = K(v)$ where $v$  is an exponential of an element $u \in K$.

5.  Let $E = K(v)$ be a differential extension field, $v$ being supposed to be transcendental over $K$. State and prove a reduction theorem of Liouville analogous to that of the question **II.5**.

### Norm, trace and reduction in an extension field of finite dimension ###

In this part, $K$ denotes a field (recall: $K$ is commutative and contains ${\mathbb Q}$, in particular it is infinite); if $u$ is an endomorphism of a $K$-vector space $E$ of dimension $n$, one writes $\chi_u(T) = \det(TI_E - u) \in K[T]$ the characteristic polynomial of $u$, $\Omega_u(T) \in K[T]$ the polynomial $\frac{\chi_u(T)-\chi_u(0)}{T}$ and $u^\#$ the endomorphism $(-1)^{n-1} \Omega_u(u)$.

1.  Let $A$ be the matrix of $u$ in a basis of $E$; show that the matrix  $A^\#$ of $u^\#$ in this basis is the transpose of the matrix of cofactors of $A$ (consider first the case where $u$ is invertible; consider then the endomorphisms $u - \lambda I_E$ for $\lambda \in K$).

2.  Let $E$ be an extension field of $K$ of finite dimension as a $K$-vector space; one defines two mappings $\operatorname{tr}\colon E \to K$ (the trace) and $N \colon E \to K$ (the norm) by:

$$\operatorname{tr}(x) = \operatorname{tr}(m_x), N(x) = \det(m_x) (m_x = y \mapsto xy\text{ is the multiplication by $x$ in $E$)}.$$

Verify that the trace is $K$-linear; what is $\operatorname{tr}(\lambda)$ for $\lambda \in K$? Verify that $N(xy) = N(x)N(y)$ for $x$, $y \in E$; what is $N(\lambda)$ for $\lambda \in K$?

Let $x \in E$; show that there exists a unique $x^\# \in E$ such that $(m_x)^\# = m_{x^\#}$. Verify that $x^\#x = xx^\# = N(x)$.

3.  Let $D$ be a derivation on $K$; for $A = (a_{i,j}) \in M_n(K)$, one write $D(A)$ for the matrix $(D(a_{i,j}))$. Show that $D(\det A) = \operatorname{tr}(A^\# D(A))$.

4.  Let $D$ be a derivation on $K$ verifying $D(K) \subseteq K$. Show that $\operatorname{tr}(D(x)) = D(\operatorname{tr}(x))$ for $x \in E$. For this, one fixes a basis $\mathcal B = \{e_1, e_2, \ldots, e_n\}$ of $E$ over $K$ ($n = \dim_K E$) and one write $\Delta \colon E \to E$ the unique $K$-linear mapping defined by $\Delta(e_i) = D(e_i)$ (attention, $D$ is not $K$- linear); let $(a_{i,j})$ be the matrix of $m_x$ in $\mathcal B$ and $m_x^D \colon E \to E$ the $K$-linear mapping of the matrix $(D(a_{i,j}))$. Verify that:

$$m_x \circ \Delta + m_{D(x)} = \Delta \circ m_x + m_x^D \tag{*}$$

and then conclude.

5.  Show that $\operatorname{tr}(x^\#D(x)) = D(N(x))$ (one can eventually utilize a basis $\mathcal B = \{e_1, e_2, \ldots, e_n\}$ of $E$ and the relation $(*)$ of the previous question. Deduce that for $x \in E \setminus \{0\}$:

$$\frac{D(N(x))}{N(x)} = \operatorname{tr}\left(\frac{D(x)}{x}\right).$$

6.  State a reduction theorem for a differential extension field $E$ of $K$ of finite dimension.

### The theorem of Liouville-Ostrowski ###

1.  Let $E$ be a differential extension field of $K$; if $x \in E$ is algebraic over $K$, show that $D(K(x)) \subseteq K(x)$.

    -   A differential extension field $E$ of $K$ is said to be elementary over $K$ if there exists a sequence $(K_i)_{0 \le i \le m}$ of subfields of $E$ such that:

$$K = K_0 \subseteq K_1 \subseteq K_2 \subseteq \ldots \subseteq K_{m-1} \subseteq K_m = E$$

where $K_{i+1}$ is either of finite dimension over $K_i$ or of the form $K_i(v_{i+1})$, $v_{i+1} \in K_{i+1}$ being either a logarithm or an exponential of an element of $K_i$. One recalls that $E$ and $K$ have the same subfield of constants.

2.  Let $f$ belong to a differential field $K$; one supposes that $f$ admits a primitive *in* an differential extension field $E$ *elementary* over $K$: i.e., there exists $g \in E$ such that $D(g) = f$. Show that $f$ is a Liouville sum *in* $K$: this is the [Liouville-Ostrowski theorem](https://en.wikipedia.org/wiki/Liouville%27s_theorem_%28differential_algebra%29) (it brings a property taking place in  $E$ back to a property taking place in $K$).

### $\int e^{t^2} \mathrm d\,t$ is not an elementary function ###

Let $K$ be a differential field and $u \in K$; to simplify notations, one write (in an abusive way) $e^u$ for all element belonging to a differential extension field of $K$ which is an exponential of $u$. Same for the logarithms with the notation $\log(u)$.

1.  One takes back the hypotheses appeared at the beginning of part **III**. Let $f \in K$; show that $Xf$ is a Liouville sum in $K(X)$ if and only if there exists $g \in K$ such that $f = D(g) + gD(X)/X$. If in addition, $K$ is equal to a field of rational fractions $k(T)$ (with coefficients in a field $k$) equipped with the usual derivation, show that if $f$ and $D(X)/X$ belong to $k[T]$, then $g \in k[T]$ (i.e., if $f$ and $D(X)/X$ are *polynomials* in $T$, then $g$ is a polynomial in $T$).

2.  Let $E$ be a differential extension field of $K$; one considers an element $v \in E$ such that $D(v) \in K$ (this is the case for example when $v = \log(u)$ for $u \in K \setminus \{0\}$); show that if $v \notin K$, then $v$ is transcendental over $K$. In an analogous way, for $u \in K$, show that $e^u$ is transcendental over $K$ except in the case where there exists an integer $n > 0$ such that $nu$ is a logarithm of an element in $K$ (for these two cases, one can reason by contradiction and consider the minimal polynomial of $v$ over $K$).

3.  One considers the “usual” differential field $K = {\mathbb C}(T)$; show that a non-constant rational fraction of ${\mathbb C}(T)$ does not admit a logarithm in ${\mathbb C}(T)$. Deduce that if $u \in {\mathbb C}(T)$ is not a constant, then $e^u$ is transcendental over ${\mathbb C}(T)$.

4.  Deduce the Liouville criterion: let $f \in {\mathbb C}(T)$, $u \in {\mathbb C}(T) \setminus {\mathbb C}$; then $fe^u$ admits a primitive in a elementary differential extension field over ${\mathbb C}(T)$ if and only if there exists $g \in {\mathbb C}(T)$ such that $f = g' + gu'$. In addition, if $f$, $u$ are polynomials, then $g$ is a polynomial and $\deg u \le 1 + \deg f$.

5.  Deduce that $\int e^{t^2} \mathrm d\,t$ is not an elementary function, i.e., does not belong to any elementary differential extension field of ${\mathbb C}(T)$.


## Solution ##

Done by me.

### Preliminaries ###

All too trivial. This part will be omitted.

### The derivations and their elementary properties ###

1.  $D(u/v) = (u/v)^{-1} (D(u)/u-D(v)/v)$. $D(u^n) = nu^{n-1} D(u)$. $D(u)/u$ is a homomorphism from $(K^*, \cdot)$ to $(K, +)$. (this explains the name *logarithmic derivative*).

2.  Verify for monomials $P = a_iu^i$.

3.  Let $G = \prod_{j \in J} Q_j$. Multiplying both sides by $Q^2G$ and expanding, one can see in $K[X]$:

$$Q^2 \cdot \text{some polynomial} = G(QD(P)-PD(Q)).$$

By assumption, $G$ is square-free. Hence even though $Q$ might divide $G$, $Q^2$ cannot. Thus $Q \mid QD(P)-PD(Q)$, and $Q \mid D(Q)$.

Assume that $Q_i$ is prime to $Q$. Let $S \mid Q_i$ be an irreducible factor. Multiplying both sides by $Q_i$

$$Q^2(P_i + Q_i \sum_{j \ne i} \frac{P_j}{Q_j}) = Q_i(QD(P)-PD(Q)).$$

Taking quotient modulo $S$, noting that all $Q_j$ except $Q_i$ is prime to $S$, hence invertible modulo $S$:

$$Q^2P_i = 0$$

in $K[X]/(S)$. By assumption $Q \ne 0$, therefore $P_i = 0$. So for each irreducible $S \mid Q_i$, $S \mid P_i$. Note that $Q_i$ is square-free, this implies $Q_i \mid P_i$.

### Derivation on $K(X)$ of logarithmic type ###

1.  $D(P) = P'D(X) + P^D \in K[X]$. If the coefficient of the highest-order term in $P$ is in $K_{cst}$.

2.  $Q=1$. $P = cX+g$ with $c \in K_{cst}$.

3.  Let $R=A+P/Q$, with $A$, $P$, $Q \in K[X]$, $\deg P < \deg Q$. $D(A) \in K[X]$, $D(R) \in K \subset K[X]$, so $D(P/Q) \in
            K[X]$. But $D(P/Q) = (QD(P)-PD(Q))/Q^2$, and $\deg P < \deg Q$ implies that $D(P/Q) = 0$. The problem is reduced to the previous one.

4.  By definition of Liouville sums, one may write

$$f = D(R) + \sum_{i \in I} c_i \frac{D(P_i)}{P_i},$$

Write

$$P_i = f_i \prod_{j \in J_i} Q_j^{n_j},$$

with each $f_i \in K$, $Q_j$ monic irreducible. Note that $u \mapsto D(u)/u$ is a homomorphism,

$$f = D(R) + \sum_{i \in I} c_i \frac{D(f_i)}{f_i} + \sum_{i \in I} \sum_{j \in J_i} n_jc_i \frac{D(P_j)}{P_j}.$$

The said form can be obtained by combining terms with the same $P_j$’s.

Now let $R = P/Q$ with $Q$ monic irreducible, then

$$D(P/Q) = \sum_{j \in J}\frac{-d_jD(Q_j)}{Q_j} + (f - \frac{\sum_{i \in I}c_iD(f_i)/f_i}{1}$$

has the form of the proposition above, where the last term is in $K$ by assumption. So $Q \mid D(Q)$, and $Q = 1$, which is prime to every $Q_j$, so $Q_j \mid D(Q_j)$, $Q_j = 1$. Thus

$$f = D(P^*) + \sum_{i \in I} c_i \frac{D(f_i)}{f_i} \in K,$$

with $P^* \in K[X]$. But the latter term is in $K$, hence $P^* = cX+g$, with $c \in K_{cst}$. The rest is obvious.

5.  Direct verification. Note this problem demonstrates the motivation behind the definition of a Liouville sum.

### Derivation on $K(X)$ of exponential type ###

1.  Let $D(X) = fX$, $f \in K$. Then $D(P) = fXP' + P^D \in K[X]$. $\deg D(P) \le \deg P$.

2.  If $P \mid D(P)$, then $D(P) = kP$ for some $k \in K^*$. Let

$$P = \sum_{i \in I} a_iX^i,$$

where $I \subseteq \{0, 1, \ldots, n\}$ and each $a_i \ne 0$. Then

$$D(P) = \sum_{i \in I} (f \cdot ia_i+D(a_i))X^i.$$

So one has for each $i \in I$,

$$f \cdot ia_i + D(a_i) = ka_i.$$

This is equivalent to

$$\frac{D(a_i)}{a_i} = k - if.$$

Let $i$, $j \in I$, by the property of logarithmic derivatives,

$$\frac{D(a_i/a_j)}{a_i/a_j} = (j-i)f = \frac{D(X^{j-i})}{X^{j-i}}.$$

So again by the said property, $\frac{a_i/a_j}{X^{i-j}}$ has logarithmic derivative $0$, and so $a_i/a_j = gX^{i-j}$ with $g \in K(X)_{cst}^* \subseteq K^*$. But $a_i$, $a_j \in K^*$, and this is not possible unless $i = j$. Therefore $I$ is a singleton.

3.  Let $R = P/Q$ with $\gcd(P,Q) = 1$ and $Q$ monic. $D(R) =
            (QD(P)-PD(Q))/Q^2 \in K[X]$, thus $Q \mid D(Q)$, and $Q = X^n$. Then $R$ is a Laurent polynomial, i.e., $R = \sum_{i \in {\mathbb Z}}
            a_iX^i$. Note that $D(a_iX_i) \ne 0$ (because $K(X)_{cst} =
            K_{cst}$) and has degree $i$, one sees that $R \in K[X]$ and that $\deg R = \deg D(R)$.

4.  If $f \in K$ is a Liouville sum in $E$, then $f$ is a Liouvile sum in $K$. Indeed, by the proof of the problem in the previous section, one has

$$f = D(P/Q) + \sum_{i \in I} c_i\frac{D(f_i)}{f_i} + \sum_{j \in J} d_j \frac{D(Q_j)}{Q_j}$$

with $Q$, $Q_j$ irreducible and $Q \mid D(Q)$, hence $Q = X$ or $Q = 1$. If $Q = 1$, every $Q_j$ is prime to $Q$, so $Q_j \mid
            D(Q_j)$. If on the other hand $Q = X$ and $Q_j$ is not prime to $Q$, then $Q_j = X$. Either way, the sum actually consists of only one term, $d\frac{D(X)}{X} \in K$. Therefore $D(R) \in
            K$, and $R = g \in K$. It follows that

$$f - d\frac{D(X)}{X} = D(g) + \sum_{i \in I} c_i\frac{D(f_i)}{f_i}$$

is a Liouville sum in $K$.

### Norm, trace and reduction in extension fields of finite dimension ###

1.  $uu^\# = (-1)^{n-1} (\chi_u(u)-\chi_u(0))$. By [Cayley-Hamilton theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem), $\chi_u(u) = 0$. $\chi_u(0) = (-1)^{n-1} \det u$, so $uu^\# = \det u$, and $A^\#$ is the transpose of cofactor matrix of $A$ if $u$ is invertible. This is an algebraic identity that holds on the Zariski open set of all invertible matrices, and hence on the space of all matrices.

2.  $\operatorname{tr}(\lambda) = n\lambda$, $N(\lambda) = \lambda^n$ when $\lambda
            \in K$. Consider the case $x \ne 0$. Let $x^\# = N(x)/x$. For all $y \in E$, $(m_x)^\#(y) = \det m_x \cdot (m_x)^{-1}(y) =
            x^\#y$ as shown above. The uniqueness is direct.

3.  Let $A^{ij}$ denote the cofactor matrix of $(i,j)$-entry in $A$. For each $\sigma \in S_n$ with $\sigma(i) = j$, one can assign a $\sigma' \in S_{n-1}$, removing $\binom{i}{j}$ in the permutation, and one easily verify that $\operatorname{sgn}\sigma =
            (-1)^{i+j} \operatorname{sgn}\sigma'$. Also it is well-known that $\operatorname{tr}(A^TB) = \sum_{i,j} a_{ij}b_{ij}$. One now has

$$\begin{align}
            D(\det A) &= D\left(\sum_{\sigma \in S_n} (-1)^{\operatorname{sgn}\sigma}
            \prod_{i=1}^n a_{i\sigma(i)}\right) \\
            &= \sum_\sigma (-1)^{\operatorname{sgn}\sigma} \sum_i D(a_{i\sigma(i)})
            \prod_{k \ne i} a_{k\sigma(k)} \\
            &= \sum_{i,j} D(a_{ij}) \sum_{\substack{\sigma \in S_n \\
            \sigma(i)=j}} (-1)^{\operatorname{sgn}\sigma}
            \prod_{k \ne i} a_{k\sigma(k)} \\
            &= \sum_{i,j} D(a_{ij}) (-1)^{i+j} \sum_{\sigma' \in S_{n-1}}
            (-1)^{\operatorname{sgn}\sigma'} \prod_{k=1}^{n-1} (A^{ij})_{k\sigma'(k)} \\
            &= \sum_{i,j} D(a_{ij}) (-1)^{i+j} \det A_{ij} \\
            &= \operatorname{tr}(A^\#D(A)).
\end{align}$$

Sorry about the mess, but I did not find a more clear proof.

4.  To show that Eq. (\*) holds, one observes that all terms involved are linear, and verifies that

$$\begin{align}
            (\Delta \circ m_x + m_x^D)(e_j) &=
            \Delta\left(\sum_i a_{ij}e_i\right) + \sum_i D(a_{ij})e_i \\
            &= \sum_i a_{ij}D(e_i) + \sum_i D(a_{ij}e_i) \\
            &= D\left(\sum_i a_{ij}e_i\right) \\
            &= D(m_x(e_j)) = D(xe_j) \\
            &= xD(e_j) + D(x)e_j = (m_x \circ \Delta + m_{D(x)})(e_j).
\end{align}$$

Taking traces of both sides and note that $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ yields the desired relation.

5.  By above propositions,

$$\begin{align}
            D(N(x)) &= D(\det m_x) = \operatorname{tr}(m_x^\# m_x^D) \\
            &= \operatorname{tr}(m_{x^\#} (m_x\circ\Delta-\Delta\circ m_x+m_{D(x)})) \\
            &= \operatorname{tr}(m_x \circ m_{x^\#} \circ \Delta) - \operatorname{tr}(m_{x^\#} \circ
            \Delta \circ m_x) + \operatorname{tr}(m_{x^\#} \circ m_{D(x)}) \\
            &= \operatorname{tr}(m_{x^\#}m_{D(x)}) = \operatorname{tr}(x^\#D(x)).
\end{align}$$

Note the commutativity between $m_x$ and $m_{x^\#}$ is neccessary: $\operatorname{tr}(ABC) = \operatorname{tr}(ACB)$ is not true in general.

To obtain the desired conclusion, note that $N(x) \in K$, $\operatorname{tr}$ is $K$-linear and substitute $x^\# = \frac{N(x)}{x}$.

6.  Let $E$ be a finite extension field of $K$. If $f \in K$ is a Liouville sum in $E$, then $f$ is a Liouvile sum in $K$. Indeed, let $\dim_K(E) = n$, write

$$f = D(g) + \sum_i \frac{c_i}{D(h_i)}h_i,$$

with $g$, $h_i \in E$. Taking traces,

$$nf = D(\operatorname{tr}(g)) + \sum_i \frac{D(N(h_i))}{N(h_i)}$$

is a Liouville sum in $K$, as $\operatorname{tr}(g)$, $N(h_i) \in K$, and $n$ is a constant. Here ${\mathbb Q}\subseteq K$ is used.

### Liouville-Ostrowski Theorem ###

1.  Let $f \in K[X]$ be the minimal polynomial of $x$ over $K$. Then $f(x) = 0$, $f'(x) \ne 0$ (this uses ${\mathbb Q}\subseteq K$). Taking derivative, $f'(x)D(x) + f^D(x) = 0$, so $D(x) =
            -f^D(x)/f'(x) \in K(x)$, and it is easy to see that $D(K(x))
            \subseteq K(D(x))$.

2.  $f = D(g)$ is trivially a Liouville sum in $E$. Descend along the tower of field extensions.

### $\int\!e^{t^2} \mathrm d\,t$ is not an elementary function ###

1.  One may write, like above,

$$D(P/Q) = Xf - \sum_{i \in I} c_i\frac{D(f_i)}{f_i},$$

and conclude that $Q = 1$, $\vert I \vert = 1$ and $f_i = X$. So

$$D(P) = Xf - cD(X)/X.$$

By assumption, $cD(X)/X \in K$, and the right hand side has degree $1$. Hence $\deg P = 1$. Let $P = Xg + h$, $g$, $h \in K$. Comparing $D(P)$ with $Xf - cD(X)/X$ as polynomials shows that $D(Xg) = Xf$, $D(h) = cD(X)/X$. And

$$f = \frac{D(X)g + XD(g)}{X} = D(g) + gD(X)/X.$$

Let $g = p/q$, $p$, $q \in k[T]$, then

$$q^2f = qD(p) - pD(q) + pq\frac{D(X)}{X}.$$

Hence, $q \mid D(q)$. This implies $q = 1$ under the usual derivative operation.

2.  Let $P \in K[X]$ be the minimal (monic) polynomial of $v$ over  $K$. $P(v) = 0$, so $P'(v)D(v) + P^D(v) = 0$. As $D(v) \in
            K$, $D(v)P' + P^D$ is a polynomial in $K[X]$, and because $P$ is monic, it has degree lower than $P$, which is impossible.

    Let $P = \sum_{i \in I} a_iX^i \in K[X]$ be the minimal polynomial of $e^u$ over $K$. Then $e^u$ satisfies $D(u)XP' +
            P^D = 0$, which leads to $D(u)ia_i + D(a_i) = D(u)a_i$. Analogous to the equivalence of $P \mid D(P)$ and $P = aX^n$, one obtains that $e^{(i-j)u} \in K^*$ for all $i$, $j \in I$. Thus either $I$ is a singleton $\{n\}$ and $e^{nu} = 0$, which is impossible, or $v = e^{nu} \in K^*$ for some $n \in {\mathbb N}^*$, and it is easy to verify that $nu = \log v$.

3.  If $\log(f/g) = P/Q$, namely $D(P/Q) = D(f)/f - D(g)/g$, then $Q \mid D(Q)$ and $Q = 1$, hence $f \mid D(f)$, $g \mid D(g)$, and $f = g = 1$. Then $D(P/Q) = 0$.

4.  $e^u$ is transcendental, so $e^u \mapsto X$ is an isomorphism onto $K(X)$. As shown above, the assumption implies that $Xf$ is a Liouville sum in ${\mathbb C}(T)$, and hence $\exists g \in
            {\mathbb C}(T)$ such that $f = g' + gD(X)/X = g' + gu'$. It is also shown above that if $f$, $u$ are polynomials, then $g$ is a polynomial. Now $u' = (f-g')/g \in {\mathbb C}[T]$, and $\deg g' <
            \deg g$, so it must be that $\deg u' = \deg f - \deg g \le
            \deg f$, and $\deg u \le \deg f + 1$.

5.  Take $f = 1$, $u = t^2$, then $\deg u > 1 + \deg f$.

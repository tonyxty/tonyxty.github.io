title: \( n \sin n \) 是无穷大量吗？
date: 2011-11-01
tags: undergrad, analysis, number theory
category: math
lang: zh

某次数学分析习题课上，助教提出一个问题：$\lbrace n \sin n \mid n \in \mathbb N \rbrace$ 是无穷大量吗？

第一眼看去，我就觉得这是一个披着分析外衣的数论题.  更具体地说，这与逼近理论有关系.  事实上，因为 $\pi$ 是一个无理数，由连分数理论我们知道：存在无穷多对自然数 $p < q$, 满足 $\vert\pi - p/q\vert < 1/q^2 < 1$, 于是有 $\vert q\pi - p\vert < 1/q$.  由此我们知道

$$
\vert\sin p\vert = \sin \vert p\vert = \sin \vert q\pi - p\vert <
\vert q\pi - p\vert < 1/q.
$$

另一方面，$p/q < \pi + 1 < 5$, 故 $\vert p \sin p\vert < \vert 5q \sin p\vert < 5$.  因此 $\lbrace n \sin n \rbrace$ 有一个子列以 $5$ 为界，自然不会是无穷大量.

但我们的问题尚没有结束.  一方面，尚有许多问题可以建议.  在这个证明中只用到了 $\pi$ 的无理性，还有许多深刻的结果没有用到.  我们可以问: $\lbrace n \sin n \rbrace$ 有哪些聚点？是否存在 $a, b$ 使得 $\lbrace n^a \sin(bn) \rbrace$ 成为无穷大量？这些都不像是简单的问题.  另一方面，许多数论问题都可以借助分析方法获得解答，而此题以分析的形式出现，是否有分析的解答方法呢？

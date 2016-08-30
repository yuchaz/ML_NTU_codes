# 1.

$P(y|x) = \lambda$ if $y=f(x)$; $P(y|x)=1-\lambda$ if $y \neq f(x)$

We can thus infer that the flipping rate is $\lambda$

Error = Wrong and not flip + right but flipped

$$E_{out} = \mu\times\lambda + (1-\mu)(1-\lambda) = 1 - \mu - \lambda + 2\mu\lambda$$


#2.
$$
E_{out} = 1-\lambda + (2\lambda-1)\mu
$$

To make $E_{out}$ independent of $\mu$, we have to make $2\lambda -1 = 0$

Therefore, $E_{out}$ is independent of $\mu$ when $\lambda = 0.5$

#3.
The **generalization error** is the difference between the expected and the empirical error.
$$
G = |E_{in}(h) - E_{out}(h)|
$$

We need $\mathbb{P}[G<0.05] = 95\%$, Therefore from VC bound:
$$
\mathbb{P}[G>0.05] = 5\% \leq 4\cdot m_H(2N)\cdot \exp(-{1\over8}\cdot \epsilon^2 N)
$$

Where $\epsilon = 0.05$, and $m_H(2N) = (2N)^{d_{VC}} = 1024\cdot N^{10}$

Therefore we can get $N \approx 452,957 \sim 453,000$

[Wolfram Link](https://www.wolframalpha.com/input/?i=0.05+%3D+4*(2*x)%5E10*exp(-1%2F8*0.05%5E2*x))

#4. & 5.

|                            | Q4       |  Q5       |
|----------------------------|----------|-----------|
| Original VC bound          | 0.304638 | 13.828161 |
| Variant VC bound           | 0.416914 | 16.264111 |
| Rademacher Penalty Bound   | 0.160030 | 7.151976  |
| Parrondo and Van den Broek | 0.107764 | **5.10136**   |
| Devroye                    | **0.10425**  | 5.59313   |

####Formulas for Wolfram

>*Parrondo and Van den Broek, $N = 50,000$*
>
>x = sqrt(1/50000*(2x+ln((2*50000)^50*6/0.05)))
>
>*Parrondo and Van den Broek, $N = 5$*
>
>x = sqrt(1/5*(2x+ln((2*5)^50*6/0.05)))
>
>*Devroye, $N = 50,000$*
>
>x = sqrt(1/(2*50000)*(4x*(1+x)+ln(4*50000^100/0.05)))
>
>*Devroye, $N = 5$*
>
>x = sqrt(1/(2*5)*(4x*(1+x)+ln(4*5^100/0.05)))


# Question #16
Just like question #1, if we set the flipping rate to be $\mu=20\%$, then we know that

for $s>0$
$$
E_{out} = \mu - \left|\theta\right|\mu+\frac{\left|\theta\right|}{2}
$$
for $s<0$
$$
E_{out} = 1- \mu + \left|\theta\right|\mu-\frac{\left|\theta\right|}{2}
$$

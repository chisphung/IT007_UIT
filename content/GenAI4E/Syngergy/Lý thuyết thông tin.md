# Entropy - Đo độ không chắc chắn 

## 1. Tại sao cần entropy 

Trong xác suất, ta thường hỏi

$$
P(X=x)
$$

Có thể hiểu là: Khả năng xảy ra của kết quả \(x\) là gì?

Nhưng trong lý thuyết thông tin, ta đặt một câu hỏi khác:

> Sự không chắc chắn trước khi quan sát sự kiện \(X\) là bao nhiêu?

Entropy là một phương pháp toán học, giúp định lượng độ không chắc chắn

Cho một biến ngẫu nhiên X, entropy cho biết:

> Một cách trung bình, độ ngạc nhiên sau khi quan sát sự kiện X là bao nhiêu?

---

## 2. From probability to surprise

If an event is very likely, it is not surprising.

Example:

$$
P(X=x)=0.99
$$

Seeing \(x\) gives very little new information.

If an event is rare, it is surprising.

Example:

$$
P(X=x)=0.01
$$

Seeing \(x\) gives a lot of information.

Information theory defines the surprise of an event as:

$$
-\log P(X=x)
$$

Usually we use log base 2:

$$
-\log_2 P(X=x)
$$

Then the unit is **bits**.

---

## 3. Entropy is expected surprise

Entropy is the average surprise over all possible outcomes:

$$
H(X) = - \sum_x P(x)\log_2 P(x)
$$

Equivalent form:

$$
H(X) = \sum_x P(x) \left[-\log_2 P(x)\right]
$$

So entropy is just:

> probability-weighted average surprise.

---

## 4. Simple examples

### Case 1: deterministic variable

Suppose:

$$
P(X=0)=1
$$

Then there is no uncertainty.

Before observing \(X\), we already know the answer.

So:

$$
H(X)=0
$$

Interpretation:

> No uncertainty, no surprise, no information gained.

---

### Case 2: fair coin

Suppose:

$$
P(H)=0.5,\quad P(T)=0.5
$$

Then:

$$
H(X)
= -0.5\log_2 0.5 - 0.5\log_2 0.5
$$

Since:

$$
\log_2 0.5 = -1
$$

we get:

$$
H(X)=1
$$

Interpretation:

> A fair coin has 1 bit of uncertainty.

---

### Case 3: biased coin

Suppose:

$$
P(H)=0.9,\quad P(T)=0.1
$$

Then the outcome is less uncertain than a fair coin.

So:

$$
H(X) < 1
$$

Interpretation:

> The more predictable the distribution, the lower the entropy.

---

## 5. Binary entropy curve

For a binary variable:

$$
X \in \{0,1\}
$$

let:

$$
P(X=1)=p
$$

Then:

$$
P(X=0)=1-p
$$

The entropy is:

$$
H(X) = -p\log_2 p - (1-p)\log_2(1-p)
$$

Important cases:

| \(p\) | Meaning | Entropy |
|---|---|---|
| \(0\) | always 0 | 0 |
| \(0.5\) | maximally uncertain | 1 bit |
| \(1\) | always 1 | 0 |

![[Pasted image 20260703094351.png]]

	Entropy Η(_X_) (i.e. the expected,surprisal of a coin flip, measured in bits, graphed versus the bias of the coin Pr(X = 1), where X = 1 represents a result of heads.  Here, the entropy is at most 1 bit, and to communicate the outcome of a coin flip (2 possible values) will require an average of at most 1 bit (exactly 1 bit for a fair coin). The result of a fair die (6 possible values) would have entropy log26 bits.

## 6. Entropy is not the same as variance

Variance measures spread in numerical values.

Entropy measures uncertainty in probability mass.

For example:

| Distribution | Entropy intuition |
|---|---|
| \(P(A)=1\) | no uncertainty |
| \(P(A)=0.5, P(B)=0.5\) | high uncertainty |
| \(P(A)=P(B)=P(C)=P(D)=0.25\) | even higher uncertainty |

Entropy does not care about the numerical distance between labels unless the probability distribution changes.

For categorical variables like class labels, words, image IDs, or target labels, entropy is often more natural than variance.

---

## 7. Maximum entropy

For a variable with \(n\) equally likely outcomes:

$$
P(x)=\frac{1}{n}
$$

the entropy is:

$$
H(X)=\log_2 n
$$

Examples:

| Number of equally likely outcomes | Entropy |
|---|---|
| 2 | \(1\) bit |
| 4 | \(2\) bits |
| 8 | \(3\) bits |
| 16 | \(4\) bits |

Interpretation:

> Entropy measures how many binary yes/no questions are needed on average to identify the outcome.

---

## 8. Joint entropy

Now suppose we have two variables:

$$
X, Y
$$

Their joint entropy is:

$$
H(X,Y)
=
-\sum_x\sum_y P(x,y)\log_2 P(x,y)
$$

This measures:

> How uncertain we are about the pair \((X,Y)\).

In multimodal learning, we might think:

$$
X = \text{image}
$$

$$
Y = \text{text}
$$

Then:

$$
H(X,Y)
$$

measures the uncertainty of the image-text pair.

---

## 9. Conditional entropy

Conditional entropy means:

> How uncertain is \(Y\) after knowing \(X\)?

It is written as:

$$
H(Y|X)
$$

Formula:

$$
H(Y|X)
=
-\sum_x \sum_y P(x,y)\log_2 P(y|x)
$$

Interpretation:

| Quantity | Meaning |
|---|---|
| \(H(Y)\) | uncertainty about \(Y\) before seeing \(X\) |
| \(H(Y|X)\) | uncertainty about \(Y\) after seeing \(X\) |

If knowing \(X\) helps predict \(Y\), then:

$$
H(Y|X) < H(Y)
$$

If \(X\) tells us nothing about \(Y\), then:

$$
H(Y|X)=H(Y)
$$

---

## 10. Chain rule of entropy

Joint entropy can be decomposed as:

$$
H(X,Y)=H(X)+H(Y|X)
$$

or symmetrically:

$$
H(X,Y)=H(Y)+H(X|Y)
$$

Interpretation:

> To describe both \(X\) and \(Y\), first describe \(X\), then describe the remaining uncertainty of \(Y\) after \(X\) is known.

---

## 11. From entropy to mutual information

Mutual information measures uncertainty reduction.

$$
I(X;Y)=H(Y)-H(Y|X)
$$

Meaning:

> How much does knowing \(X\) reduce uncertainty about \(Y\)?

Equivalent form:

$$
I(X;Y)=H(X)+H(Y)-H(X,Y)
$$

Interpretation:

| Situation | Mutual information |
|---|---|
| \(X\) and \(Y\) independent | \(I(X;Y)=0\) |
| \(X\) perfectly predicts \(Y\) | high MI |
| \(X\) partially predicts \(Y\) | intermediate MI |

![[Pasted image 20260703094703.png]]

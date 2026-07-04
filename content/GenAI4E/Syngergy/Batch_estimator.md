# 15. BATCH Estimator Foundation

## 15.1 Why do we need BATCH?

The original PID definition requires optimizing over a full joint distribution:

$$
q(x_1, x_2, y)
$$

For small discrete variables, this is possible.

For example, if:

$$
|X_1|=10,\quad |X_2|=10,\quad |Y|=5
$$

then the joint table has:

$$
10 \times 10 \times 5 = 500
$$

entries.

This is manageable.

But in real multimodal learning:

$$
X_1 = \text{image feature}
$$

$$
X_2 = \text{text / audio / video feature}
$$

These features may be continuous and high-dimensional.

For example:

$$
X_1 \in \mathbb{R}^{768}
$$

$$
X_2 \in \mathbb{R}^{768}
$$

Then we cannot explicitly build a full probability table:

$$
q(x_1,x_2,y)
$$

because almost every sample has a unique feature value.

So BATCH is introduced to approximate PID without explicitly storing the full joint distribution.

The paper describes BATCH as an estimator for large datasets where \(X_i\) is high-dimensional or continuous, while \(Y\) remains finite. It parameterizes marginal-matching joint distributions with neural networks and optimizes them using minibatches. 

The paper’s own Section 3.2 says BATCH is for high-dimensional/continuous (X_i), and it learns an approximate marginal-matching distribution (\tilde{q}\in\Delta_p) using neural networks rather than exact optimization.

---

## 15.2 What CVX does vs. what BATCH does

CVX tries to solve the PID optimization directly.

It explicitly creates a tensor:

$$
Q[i,j,k] = q(X_1=i, X_2=j, Y=k)
$$

Then it optimizes this tensor under marginal constraints:

$$
q(x_1,y)=p(x_1,y)
$$

$$
q(x_2,y)=p(x_2,y)
$$

This is exact but only feasible when the supports of \(X_1\), \(X_2\), and \(Y\) are small.

BATCH does something different.

Instead of optimizing the full tensor over the whole dataset, it samples a mini-batch:

$$
\{(x_1^{(i)}, x_2^{(i)}, y^{(i)})\}_{i=1}^{m}
$$

Then it constructs a small batch-level joint distribution:

$$
A \in \mathbb{R}^{m \times m \times |Y|}
$$

where:

$$
A[i,j,y] \approx \tilde{q}(x_1^{(i)}, x_2^{(j)}, y)
$$

Important:

- index \(i\) chooses an \(X_1\) sample from the batch;
- index \(j\) chooses an \(X_2\) sample from the batch;
- index \(y\) chooses a label class.

So instead of considering all possible dataset pairs, BATCH only considers pairings inside the current mini-batch.

---

## 15.3 The key idea

BATCH asks:

> Can we learn a neural network that produces a good fake distribution \(\tilde{q}\) for each mini-batch?

This fake distribution should satisfy the same BROJA/PID idea:

$$
\tilde{q}(x_1,y) \approx p(x_1,y)
$$

$$
\tilde{q}(x_2,y) \approx p(x_2,y)
$$

but it is allowed to change the coupling between \(X_1\) and \(X_2\).

So BATCH still follows the same conceptual goal as CVX:

> Preserve unimodal relationships, but modify the joint coupling to estimate redundancy, uniqueness, and synergy.

The difference is computational:

| Estimator | What it optimizes |
|---|---|
| CVX | explicit full distribution tensor |
| BATCH | neural network that outputs batch-level fake distributions |

---

## 15.4 Illustration

```mermaid
flowchart TD
    D["Large multimodal dataset D<br/><br/>(x1, x2, y) samples<br/>high-dimensional / continuous features"]

    B["Sample a mini-batch<br/><br/>m examples from D"]

    E1["Encoder for X1<br/><br/>f₁(x1, y)"]
    E2["Encoder for X2<br/><br/>f₂(x2, y)"]

    A["Build score tensor A<br/><br/>A[i,j,y] ≈ q̃(x1ᵢ, x2ⱼ, y)<br/><br/>shape: m × m × |Y|"]

    S["Sinkhorn normalization<br/><br/>force batch-level marginal constraints:<br/>q̃(x1,y) ≈ p(x1,y)<br/>q̃(x2,y) ≈ p(x2,y)"]

    Q["Normalized fake distribution q̃<br/><br/>same unimodal information<br/>altered X1-X2 coupling"]

    O["Optimize information objective<br/><br/>maximize co-information / compute PID terms"]

    PID["Approximate PID values<br/><br/>R, U1, U2, S"]

    D --> B
    B --> E1
    B --> E2
    E1 --> A
    E2 --> A
    A --> S
    S --> Q
    Q --> O
    O --> PID
````

---

## 15.5 What does the matrix/tensor (A) mean?

The paper parameterizes (\tilde{q}) using a neural network.

For each label (y), it builds a matrix:

$$  
A_y \in \mathbb{R}^{m \times m}  
$$

where each entry represents a possible pairing between one (X_1) sample and one (X_2) sample.

The paper describes this as:

$$  
A[i][j][y] = \tilde{q}(X_1[i], X_2[j], y)  
$$

In practice, it uses two encoders and an outer-product-like operation:

$$  
A_y =  
\exp \left(  
f_\phi^{(1)}(X_1,y)  
f_\phi^{(2)}(X_2,y)^\top  
\right)  
$$

Interpretation:

> The network assigns a score to every possible (X_1)-(X_2)-label combination inside the batch.

High value:

$$  
A[i,j,y] \text{ is large}  
$$

means:

> Under the fake distribution (\tilde{q}), (x_1^{(i)}), (x_2^{(j)}), and label (y) are strongly coupled.

Low value means the pairing is unlikely.

The paper states that BATCH returns a matrix/tensor (A \in \mathbb{R}^{n \times n \times |Y|}) for a batch, where (A[i][j][y]) represents the unnormalized joint distribution (\tilde{q}(X_1[i], X_2[j], y)).

---

## 15.6 Why Sinkhorn is needed

The network can output any score tensor (A).

But BROJA/PID requires marginal constraints:

$$  
\tilde{q}(x_1,y)=p(x_1,y)  
$$

$$  
\tilde{q}(x_2,y)=p(x_2,y)  
$$

So BATCH must force the neural fake distribution (\tilde{q}) to preserve the unimodal relationships.

This is where Sinkhorn is used.

Sinkhorn repeatedly normalizes rows and columns so the distribution has the desired marginals.

In simple terms:

```text
Raw neural scores A
        ↓
Sinkhorn normalization
        ↓
A valid fake distribution q̃ that preserves unimodal marginals
```

For BATCH:

- row constraints correspond roughly to preserving (X_1)-to-(Y) information;
    
- column constraints correspond roughly to preserving (X_2)-to-(Y) information.
    

Because exact (p(x_i,y)) is hard to estimate for continuous (x_i), the paper approximates it using:

$$  
p(x_i,y)=p(y|x_i)p(x_i)  
$$

The samples already approximate (p(x_i)), so BATCH trains unimodal classifiers:

$$  
\hat{p}(y|x_1)  
$$

$$  
\hat{p}(y|x_2)  
$$

Then Sinkhorn normalizes the rows and columns of (A) to match these estimated unimodal label distributions.

The paper specifically says it uses an unrolled Sinkhorn algorithm to project (A) onto (\Delta_p), and because estimating (p(x_i,y)) is hard, it approximates (p(y|x_i)) with separately trained unimodal classifiers.

---

## 15.7 What is being optimized?

After Sinkhorn, we get a normalized fake distribution:

$$  
\tilde{q}  
$$

Then BATCH optimizes an information-theoretic objective under (\tilde{q}).

The paper uses:

$$  
I_{\tilde{q}}(X_1;X_2;Y)  
$$

where:
$$  
I_{\tilde{q}}(X_1;X_2;Y)

= I_{\tilde{q}}(X_1;X_2) -

I_{\tilde{q}}(X_1;X_2|Y)  
$$

This objective is optimized with gradient descent through the neural parameters (\phi).

Because Sinkhorn is differentiable, gradients can pass through:

```text
information objective
        ↓
normalized q̃
        ↓
Sinkhorn
        ↓
raw neural score tensor A
        ↓
encoders fϕ
```

So the whole estimator can be trained end-to-end.

The paper notes that each gradient step computes (\tilde{q}=\text{Sinkhorn}_{\hat{p}}(A)), then updates (\phi), and because Sinkhorn is differentiable, gradients are backpropagated end-to-end.

---

## 15.8 Why is it called BATCH?

Because it never needs to build the full distribution over all (n) data points.

Instead, at each training step, it samples a mini-batch of size:

$$  
m \ll n  
$$

and builds:

$$  
A \in \mathbb{R}^{m \times m \times |Y|}  
$$

instead of:

$$  
A \in \mathbb{R}^{n \times n \times |Y|}  
$$

This makes the method scalable.

The learned neural parameters (\phi) are shared across batches, so the model gradually learns how to construct good approximate (\tilde{q}) distributions.

This is why the paper calls it **batch-level amortization**.

Amortization means:

> Instead of solving a new expensive optimization problem from scratch for every dataset or batch, learn a neural function that produces approximate solutions.

The paper describes this as using small subsampled batches (m \ll n), performing Sinkhorn and gradient updates as if the batch were the full dataset, and informally viewing this as amortized optimization.

---

## 15.9 Simple intuition

Think of CVX as:

```text
Build the whole probability table.
Solve the optimization exactly.
Get PID.
```

Think of BATCH as:

```text
Sample a mini-batch.
Let a neural network guess a fake joint distribution.
Use Sinkhorn to fix its marginals.
Optimize the information objective.
Repeat over many batches.
Get approximate PID.
```

So BATCH is not changing the theory of PID.

It is changing how the required fake distribution (q^*) is approximated in high-dimensional settings.

---

## 15.10 Important limitation

BATCH is an approximation.

It depends on:

1. the quality of the neural parameterization;
    
2. the quality of the unimodal classifiers (\hat{p}(y|x_i));
    
3. the batch size (m);
    
4. the stability of Sinkhorn normalization;
    
5. the optimization process.
    

So BATCH should be understood as:

> a scalable estimator of PID statistics,

not as exact PID computation.

This is why CVX is better for toy discrete variables, while BATCH is more practical for real multimodal datasets.

---

## 15.11 One-sentence summary

BATCH approximates the BROJA/PID optimization by learning a neural network that constructs batch-level fake joint distributions (\tilde{q}(x_1,x_2,y)), uses Sinkhorn to enforce unimodal marginal constraints, and optimizes an information objective over many mini-batches to estimate redundancy, uniqueness, and synergy.
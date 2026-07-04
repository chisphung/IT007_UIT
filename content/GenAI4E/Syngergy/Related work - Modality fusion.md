---
share_link: https://share.note.sx/orbo0jfb#G6wO31QEeGIDjUDKza0zwT7PlZqu4Q23B4nVUjnsygg
share_updated: 2026-07-03T18:03:05+07:00
---
1. Information-theoretic multimodal interaction
   - TCMax
   - DMIL
   - SynIB
   - LVLM PID analysis

2. Synergy-oriented training and curricula
   - SynIB
   - MCR
   - SPICE
   - TCMax

3. Higher-order retrieval and interaction-aware architectures
   - ConFu
   - MMoE
   - I2MoE
   - MERGE

4. Gap and our position
   - Existing works mostly optimize or analyze classification/VQA/temporal tasks.
   - CIR is retrieval with a composed query.
   - We study whether target retrieval truly requires both modalities.
---

# Multimodal Classification via Total Correlation Maximization

## Problem

![[Pasted image 20260703153006.png]]

Standard multimodal joint learning can suffer from **modality competition**.

When one modality learns faster or is more predictive, the joint model may rely on that dominant modality and neglect the weaker one. This can make the multimodal model perform worse than a strong unimodal model.

The paper analyzes this phenomenon from an information-theoretic view:

- **Joint learning** maximizes information between the fused multimodal feature and the label.
- **Unimodal learning** maximizes information between each modality and the label separately.
- But neither fully captures the relationship among all modalities and the label.

The authors propose that multimodal learning should maximize dependency among:

$$
Z_1, Z_2, \ldots, Z_M, Y
$$

where \(Z_m\) is the feature of modality \(m\), and \(Y\) is the class label.

---

## Core concept: Total Correlation

For multiple variables, **total correlation** extends mutual information.

For modalities and label:

$$
TC(Z_1, Z_2, \ldots, Z_M, Y)
$$

measures how dependent all variables are as a group.

For two modalities, total correlation can be interpreted as combining:

1. modality-label dependency;
2. unimodal label dependency;
3. modality-modality alignment.

So maximizing total correlation is intended to combine the benefits of:

```text
joint learning
+ unimodal learning
+ cross-modal alignment
```

![[Pasted image 20260703152555.png]]

## Method: TCNE and TCMax

The method has two steps:

$$
\text{TCMax} = \text{TCNE} + \text{TCMax loss}  
$$


### 1. TCNE — Total Correlation Neural Estimation

The paper extends **MINE** from mutual information estimation to total correlation estimation.

MINE estimates a lower bound of mutual information using a neural critic.

TCNE similarly estimates a lower bound of total correlation among multiple variables.

Core idea:

> Use a neural estimator to make total correlation optimizable by gradient descent.

---

### 2. TCMax loss

Using the TCNE bound, the authors derive a training objective that maximizes total correlation between multimodal features and labels.

The important claim is that TCMax does not require:

```text
extra unimodal losses
extra contrastive alignment losses
manual loss weights
architectural modifications
```

Instead, simply replacing the standard training loss with TCMax is supposed to encourage:

- stronger multimodal classification;
    
- better use of weaker modalities;
    
- better inter-modal alignment.
    

The paper describes TCMax as **hyperparameter-free** because it avoids manually balancing joint, unimodal, and alignment losses.

---

## Experimental setup

The paper evaluates TCMax mainly on multimodal classification benchmarks:

- CREMA-D
    
- Kinetics-Sounds
    
- AVE
    
- VGGSound
    
- UCF101
    
- MVSA
    

For audio-visual datasets, they use ResNet-18 encoders for audio and visual modalities. For UCF101, they use RGB and optical-flow modalities.

![[Pasted image 20260703152720.png]]

---

## Main results

The authors report that TCMax improves multimodal classification compared with:

- concatenation;
    
- shared-head joint learning;
    
- unimodal ensemble;
    
- FiLM;
    
- BiGated;
    
- OGM-GE;
    
- AGM;
    
- QMF;
    
- OPM;
    
- MLA;
    
- MMPareto.
    

They also evaluate Jensen–Shannon divergence between predictions of two modalities. Lower JS divergence means the modality-specific predictions are more aligned. TCMax obtains lower JS divergence across datasets, suggesting that it improves cross-modal consistency.

![[Pasted image 20260703152844.png]]

---

## Why this paper matters

This paper is useful because it frames **modality competition** as an information-theoretic problem.

It argues that improving multimodal learning is not only about adding fusion layers or balancing gradients. Instead, the objective should encourage dependency among:

$$
\text{modality 1 feature},\quad \text{modality 2 feature},\quad \text{label}  
$$

This makes it relevant to the broader line of work that treats multimodal interaction as an information structure.

---

## Relation to synergy

TCMax does not explicitly decompose information into:

$$
R,\quad U_1,\quad U_2,\quad S  $$

Unlike PID-based works, it does not separately measure redundancy, uniqueness, and synergy.

Instead, it maximizes **total correlation**, which captures overall multivariate dependency.

So TCMax is related to synergy, but indirectly:

```text
PID:
  separates redundancy / uniqueness / synergy

TCMax:
  increases overall dependency among modalities and label
```

A useful way to position it:

> TCMax encourages multimodal interaction globally, but it does not tell us whether the useful information is redundant, unique, or synergistic.

---

## Relation to my proposal

TCMax asks:

> How can we train a multimodal classifier to better use all modalities?

My proposal asks:

> In composed image retrieval, which samples genuinely require both reference image and modification text?

So TCMax is useful as background for **information-theoretic multimodal training**, but it is not a direct solution for CIR synergy measurement.

Key differences:

|TCMax|My proposal|
|---|---|
|classification|retrieval|
|label (Y) is a class|target is an image in a gallery|
|optimizes total correlation|measures retrieval-level synergy|
|model-training method|measurement/evaluation study|
|no explicit R/U/S decomposition|PID-inspired redundancy/uniqueness/synergy framing|

---

## Critical note

TCMax’s total correlation objective is broader than synergy.

High total correlation may come from:

- redundancy;
    
- strong unimodal label information;
    
- cross-modal alignment;
    
- genuine synergy.
    

Therefore, TCMax cannot directly answer:

```text
Does the prediction require both modalities?
```

For CIR, this distinction is important because a sample may have high text-label dependency but low true composition requirement.

---

# Kontras et al. 2026 — SynIB

---

## Problem

Many multimodal models can achieve strong performance by relying on:

- one dominant modality;
- redundant cues shared across modalities;
- dataset shortcuts.

However, true multimodal synergy means:

$$
\text{useful task information appears only from the joint use of modalities}
$$

and is not available from any single modality alone.

The paper argues that standard training often fails on synergy-dependent samples because the model is not explicitly discouraged from using unimodal shortcuts.

---

## Core idea

SynIB changes the **training objective**, not necessarily the architecture.

The model is trained with:

1. a normal multimodal task loss;
2. additional masked-modality forward passes;
3. a penalty if the model remains confident when one modality is missing.

Intuition:

If the model can still confidently predict after removing one modality,
then it may be relying on unimodal or redundant information.

If the task truly requires synergy,
the model should become less confident when a modality is withheld.

![[Pasted image 20260703153603.png]]

---

## Method: Synergistic Information Bottleneck

The objective encourages:
$$
p(y \mid x_1, x_2)  
$$

to be accurate, while discouraging confident prediction from:

$$
p(y \mid x_1, \varnothing)  
$$

or

$$
p(y \mid \varnothing, x_2)  
$$

where (\varnothing) means a masked or withheld modality.

So the model learns:

```text
Use both modalities together.
Do not solve synergy-dependent examples from one modality alone.
```

This makes SynIB a **training-time synergy regularizer**.

![[Pasted image 20260703153659.png]]
    

---

## Why this is an information bottleneck

Traditional information bottleneck asks the representation to preserve task-relevant information while discarding irrelevant information.

SynIB adapts this idea to synergy:

```text
Preserve task-relevant information in the full multimodal representation.
Suppress task-relevant confidence in unimodal/masked representations.
```

So the bottleneck is not merely about compression. It is about forcing the useful predictive information to live in the **joint multimodal pathway** rather than in any single modality.

---

## Experiments

The paper validates SynIB in two regimes.

### 1. Synthetic XOR

XOR is the cleanest example of synergy:

$$
x_1 \text{ alone is insufficient}  
$$

$$
x_2 \text{ alone is insufficient}  
$$

$$
(x_1, x_2) \text{ determines } y  
$$

Standard training struggles to recover this synergy, while SynIB is designed to recover it.

---

### 2. Real-world multimodal benchmarks

The paper evaluates on five real-world benchmarks, including:

- MultiBench affective tasks;
    
- Hateful Memes with CLIP-ViT and DeBERTa backbones;
    
- a controllable irony extension of CREMA-D introduced by the authors.
    

The reported gains are larger on synergy-dependent examples than on the overall test set, which supports the claim that SynIB specifically helps examples requiring cross-modal reasoning.

![[Pasted image 20260703153914.png]]

---

## Why this paper matters

SynIB is important because it directly targets **synergy**, rather than only improving generic fusion.

Most multimodal methods say:

```text
combine modalities better
```

SynIB says:

```text
force the model to need the joint modality combination
```

This makes it highly relevant to a proposal about measuring whether CIR samples genuinely require both reference image and modification text.

---

## Critical note

SynIB assumes that reducing confidence under modality masking is desirable.

This is reasonable for synergy-dependent examples, but it may be harmful for samples where one modality genuinely contains enough task-relevant information.

For example:

```text
If text alone is sufficient,
penalizing text-only confidence may suppress useful unique information.
```

Therefore, SynIB is most appropriate when the goal is to emphasize synergy, not when the dataset contains a mixture of redundant, unique, and synergistic samples.

This is exactly why my proposal should first **measure** sample types before designing a synergy-maximizing loss.

---
# Yang et al. 2026 — Information-Theoretic Decomposition for Multimodal Interaction Learning

## Problem

Multimodal data does not always require the same kind of fusion.

For some samples:

- one modality is enough;
- both modalities provide redundant evidence;
- each modality contributes unique information;
- the answer only emerges from their joint interaction.

The paper argues that conventional multimodal learning paradigms handle these interactions only implicitly.

Two common paradigms have opposite weaknesses:

| Paradigm | Strength | Weakness |
|---|---|---|
| **Joint learning** | can capture cross-modal synergy | may suffer from modality competition and underuse redundancy |
| **Modality ensemble** | preserves unimodal information | struggles with synergy because modalities are processed separately |

So the main question is:

> How can a model learn from different interaction types on a per-sample basis?

---

## Information-theoretic framing

The paper starts from the standard decomposition:

$$
I(X^{(1)}, X^{(2)}; Y)
=
R + U^{(1)} + U^{(2)} + S
$$

where:

| Term        | Meaning                                                                      |
| ----------- | ---------------------------------------------------------------------------- |
| \(R\)       | redundant information shared by both modalities                              |
| \(U^{(1)}\) | information unique to modality 1                                             |
| \(U^{(2)}\) | information unique to modality 2                                             |
| \(S\)       | synergistic information only available from the joint use of both modalities |

Important point:

> The paper emphasizes that these interactions are **sample-specific**, not just dataset-level averages.

They introduce an interaction composition variable:

$$
C
$$

which represents the mixture of redundancy, uniqueness, and synergy required by each sample.

![[Pasted image 20260703154844.png]]

---

## Method: DMIL

![[Pasted image 20260703154913.png]]

The proposed method is:

$$
\text{DMIL} = \text{decomposition} + \text{targeted interaction learning}
$$

DMIL explicitly decomposes multimodal representations into interaction components and then combines them for prediction.

The overall pipeline is:

```text
modality representations
→ intra-modality decomposition
→ consistency decomposition
→ R / U1 / U2 / S components
→ component-wise prediction
→ gated aggregation
````

---

## Step 1: Intra-modality decomposition

For each modality representation (Z^{(m)}), DMIL separates it into two parts:

$$
M^{(m)}  
$$

and
$$
N^{(m)}  
$$

where:

|Component|Meaning|
|---|---|
|(M^{(m)})|information directly accessible from modality (m)|
|(N^{(m)})|residual information that is not useful alone but may support cross-modal emergence|

Intuition:

```text
M = what this modality can predict by itself
N = what may become useful only when paired with the other modality
```

This is important because the synergy component is later constructed from the residual parts:

$$
N^{(1)}, N^{(2)}  
$$


![[Pasted image 20260703155047.png]]

---

## Step 2: Consistency decomposition

After obtaining directly predictive components (M^{(1)}) and (M^{(2)}), DMIL further separates them into:

$$
R,\quad U^{(1)},\quad U^{(2)}  
$$

where:

- (R) captures information consistent across both modalities;
    
- (U^{(1)}) captures modality-1-specific information;
    
- (U^{(2)}) captures modality-2-specific information.
    

The goal is to prevent all predictive information from collapsing into one fused representation.

---

## Step 3: Synergy construction

The synergy component is built from the residual components:

$$
S = f(N^{(1)}, N^{(2)})  
$$

The intuition is close to XOR:

```text
N1 alone is insufficient.
N2 alone is insufficient.
N1 + N2 can become predictive.
```

This makes DMIL explicitly model information that emerges only through multimodal interaction.

---

## Step 4: Gated prediction aggregation

Each component makes its own prediction:

$$
\hat{y}_R,\quad \hat{y}_{U^{(1)}},\quad \hat{y}_{U^{(2)}},\quad \hat{y}_S  
$$

A gating module then combines them:

$$  
\hat{y}
=
g_R\hat{y}_R  
+  
g_{U^{(1)}}\hat{y}_{U^{(1)}}  
+  
g_{U^{(2)}}\hat{y}_{U^{(2)}}  
+  
g_S\hat{y}_S  
$$

So the model can adaptively decide which interaction type matters more for each sample.

![[Pasted image 20260703155433.png]]

## Training strategy

DMIL uses a staged training process:

1. **Learn intra-modality decomposition**  
    Separate each modality into directly predictive and residual components.
    
2. **Learn interaction components**  
    Extract redundancy and uniqueness from directly predictive parts, and construct synergy from residual parts.
    
3. **Fine-tune with gated aggregation**  
    Combine all components for final prediction.
    

The losses include:

- task prediction loss;
    
- variational decomposition loss;
    
- alignment loss for redundant information;
    
- component-specific learning objectives.
    

---

## Experiments

The paper evaluates on several multimodal classification-style benchmarks, including:

- CREMA-D
    
- Kinetic-Sounds
    
- UCF101
    
- CMU-MOSEI
    
- VQAv2
    
- CLEVR
    

The main empirical claim is that DMIL outperforms conventional joint learning, modality ensemble, and several multimodal fusion/balancing baselines by explicitly adapting to heterogeneous interaction types.

![[Pasted image 20260703155450.png]]

---

## Synergy evaluation

The paper uses an operational synergy-style metric on VQA-type tasks:

$$
\text{multimodal correct}  
\land  
\text{modality 1 wrong}  
\land  
\text{modality 2 wrong}  
$$

This is very important for my proposal because it is the classification analogue of retrieval-level synergy.

## Critical note

DMIL’s components are **learned latent factors**, not exact PID quantities.

Although the paper is motivated by information decomposition, its (R, U, S) components are produced by architectural constraints and training losses.

Therefore, DMIL should be cited as:

```text
interaction-aware multimodal learning
```

not as:

```text
exact PID estimation
```

---
# Yu et al. 2024 — MMoE: Enhancing Multimodal Models with Mixtures of Multimodal Interaction Experts

## Problem

Most multimodal models focus on generic fusion or pairwise correspondence, such as image-text alignment.

However, real multimodal tasks may involve different interaction types:

- **redundancy**: both modalities contain similar task-relevant information;
- **uniqueness**: one modality contributes information not present in the other;
- **synergy**: the task-relevant signal only emerges when modalities are combined.

The paper argues that a single shared fusion model may not handle all interaction types well.

So the main question is:

> Can we improve multimodal models by assigning different experts to different interaction types?

![[Pasted image 20260703160026.png]]

---

## Method: MMoE

The proposed method is:

$$
\text{MMoE} = \text{mixture of multimodal interaction experts}
$$

Each expert is designed to specialize in a certain interaction type:

| Expert type | Role |
|---|---|
| Redundancy expert | captures information shared across modalities |
| Uniqueness expert | captures modality-specific information |
| Synergy expert | captures information emerging from modality fusion |

The model combines expert outputs through a mixture mechanism.

Intuition:

```text
Different samples may require different interaction experts.
Instead of one fusion strategy, use multiple specialized experts.
````

![[Pasted image 20260703160143.png]]

---

## Experiments

The paper evaluates MMoE mainly on multimodal language/audio/vision tasks such as:

- sarcasm detection;
    
- humor detection.
    

The key empirical claim is that modeling interaction types explicitly improves over generic multimodal fusion.

![[Pasted image 20260703160223.png]]

## Critical note

MMoE uses predefined expert roles for interaction types.

This makes the architecture interpretable, but the expert outputs are not exact PID quantities.

Therefore, cite MMoE as:

```text
interaction-aware expert modeling
```

not as:

```text
exact information decomposition
```

---
# Xin et al. 2025 — I2MoE: Interpretable Multimodal Interaction-aware Mixture-of-Experts

## Problem

Vanilla multimodal fusion methods usually combine modalities without explaining what kind of interaction is being used.

This creates two limitations:

- they may not capture heterogeneous interactions between modalities;
- they provide limited interpretability about why a multimodal prediction is made.

The paper asks:

> Can a multimodal model learn different interaction types while also explaining which interactions matter?

![[Pasted image 20260703160332.png]]

---

## Method: I2MoE

The proposed method is:

$$
\text{I2MoE} = \text{interaction experts} + \text{reweighting model}
$$

The model contains multiple interaction experts. Each expert is encouraged to capture a different type of multimodal interaction.

Then a reweighting model assigns importance scores to expert outputs.

```text
input modalities
→ interaction experts
→ expert outputs
→ reweighting model
→ final prediction
````

The reweighting scores provide:

- **local interpretation**: which interaction matters for this sample;
    
- **global interpretation**: which interaction types matter across the dataset.
    

![[Pasted image 20260703160348.png]]

---

## Interaction experts

I2MoE uses weakly supervised interaction losses to encourage experts to learn different interaction patterns.

The key idea is:

```text
Do not force all modalities through one fusion path.
Let different experts specialize in different interaction structures.
```

This extends the MMoE idea by making interaction modeling more data-driven and interpretable.

---

## Experiments

The paper evaluates I2MoE on medical and general multimodal datasets.

The main empirical claims are:

- I2MoE improves task performance;
    
- it can be combined with different fusion backbones;
    
- its reweighting scores provide sample-level and dataset-level interpretability.
    
![[Pasted image 20260703160431.png]]

---
## Critical note

I2MoE gives interpretable expert weights, but these weights are still model-dependent.

A high synergy-expert weight does not necessarily prove exact information-theoretic synergy.

Therefore, cite I2MoE as:

```text
interpretable interaction-aware MoE
```

not as:

```text
ground-truth synergy measurement
```

---
# Han et al. 2026 — MERGE: Massively Multimodal Foundation Models with Specialized MoE

## Problem

Real-world multimodal systems may contain many heterogeneous input streams, such as clinical sensors, wearable signals, images, text, and audio.

Standard MoE models usually route tokens based on feature similarity.

The paper argues that this is insufficient because multimodal interactions can be:

- redundant;
- unique;
- synergistic;
- temporally delayed.

So the main question is:

> Can redundancy, uniqueness, and synergy guide expert routing in massively multimodal models?

---

## Core idea: Temporal RUS

MERGE estimates temporal interaction patterns:

$$
R(\tau),\quad U(\tau),\quad S(\tau)
$$

where \(\tau\) is a time lag.

This means the model does not only ask:

```text
Do these modalities interact?
````

It asks:

```text
When do these modalities interact?
At what temporal delay?
Through redundancy, uniqueness, or synergy?
```

![[Pasted image 20260703160529.png]]

---

## Multi-scale BATCH estimator

MERGE extends the BATCH estimator to temporal data.

Instead of estimating one static:

$$  
R,\quad U,\quad S  
$$

it estimates a sequence across time lags:

$$  
R(0), R(1), \ldots  
$$

$$  
U(0), U(1), \ldots  
$$

$$  
S(0), S(1), \ldots  
$$

It uses lag-conditioned discriminators and learnable temporal embeddings to estimate interaction at multiple lags efficiently.

```text
temporal modality features
→ lag embedding
→ lag-conditioned discriminators
→ alignment tensor
→ Sinkhorn normalization
→ temporal R/U/S
```

![[Pasted image 20260703160554.png]]

---

## Method: RUS-aware MoE routing

MERGE uses estimated temporal RUS values to guide expert routing.

|High interaction type|Routing strategy|Intuition|
|---|---|---|
|High redundancy|route tokens together|shared information can use shared experts|
|High uniqueness|diversify routing|modality-specific information should be preserved|
|High synergy|route to cross-modal experts|joint interaction needs explicit fusion|

So the model becomes:

$$  
\text{MERGE} = \text{temporal RUS estimation} + \text{RUS-aware routing}  
$$

![[Pasted image 20260703160746.png]]


---

## Auxiliary losses

MERGE adds losses to make routing follow the intended interaction behavior:

- redundancy loss encourages similar routing;
    
- uniqueness loss encourages diverse routing;
    
- synergy loss encourages routing to cross-modal experts.
    

This turns R/U/S from an analysis tool into a training signal.

---

## Experiments

MERGE is evaluated on multimodal temporal tasks such as:

- healthcare prediction;
    
- activity recognition;
    
- affective computing.
    

The key claim is that RUS-aware routing improves performance and produces more interpretable expert specialization.

![[Pasted image 20260703160851.png]]

---

## Critical note

MERGE is powerful but much more complex than what CIRR needs.

CIRR is not temporal, and the main output is a ranked image gallery rather than a time-indexed prediction.

Therefore, MERGE should be cited as:

```text
R/U/S-guided expert routing
```

not as:

```text
a direct method for CIR synergy measurement
```

---

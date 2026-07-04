---
share_link: https://share.note.sx/p8mn2jg6#0bTw7e2+B75DR2mdxE83GH7p1YZjrPAd4O6tlM7/sp0
share_updated: 2026-07-03T14:52:12+07:00
---
# RDE

## Problem

Text-to-image person re-identification retrieves a person image from a gallery using a natural-language description.

Most prior methods assume every training pair is correctly aligned:

$$
(I_i, T_i) \text{ is a positive pair}
$$

However, real datasets may contain **false positive pairs**: the image and text are not semantically matched, but are still used as positive supervision.

This is called **Noisy Correspondence (NC)**.

> Key distinction: NC is not class-label noise. It is pair-level correspondence noise.

![[Pasted image 20260703142153.png]]

---

## Method: RDE

The proposed method is **RDE: Robust Dual Embedding**.

$$
\text{RDE} = \text{CCD} + \text{TAL}
$$

It has two main parts:

### 1. CCD — Confident Consensus Division

CCD divides training pairs into:

- clean pairs;
- noisy pairs;
- uncertain pairs.

It uses two embedding branches:

| Branch | Role |
|---|---|
| BGE — Basic Global Embedding | coarse global image-text matching |
| TSE — Token Selection Embedding | finer token-level matching |

Each branch estimates whether a sample is clean/noisy. Only samples consistently judged clean by both branches are trusted as clean supervision.

Intuition:

> A sample is reliable only if both coarse and fine-grained views agree.


![[Pasted image 20260703142312.png]]

---

### 2. TAL — Triplet Alignment Loss

Standard triplet ranking loss focuses heavily on the hardest negative.

Under noisy correspondence, the hardest negative may be unreliable, so hard-negative mining can collapse.

TAL replaces hard-negative-only optimization with a smoother log-sum-exp upper bound over all negatives.

Intuition:

> Still emphasize hard negatives, but do not let one possibly noisy negative dominate training.


# TME 

## Problem

Composed Image Retrieval uses a triplet:

$$
(I_r, m, I_t)
$$

where the model should retrieve target image \(I_t\) from a composed query \((I_r, m)\).

Most supervised CIR methods assume this triplet is correctly matched. TME argues this assumption is often violated because modification text can be incomplete, subjective, or incorrectly aligned with the reference-target pair.

They define this as **Noisy Triplet Correspondence (NTC)**.

NTC has two forms:

1. **Partial matching**  
   The modification text only partially describes the real visual change from reference to target.

2. **Incorrect matching**  
   The modification text describes changes that are not reflected in the target image.

![[Pasted image 20260703143905.png]]

---

## Method: TME

The proposed framework is:

$$
\text{TME} = \text{RFQ} + \text{PTE} + \text{TOP}
$$

with total loss:

$$
\mathcal{L}
=
\mathcal{L}_{rm}
+
\alpha\mathcal{L}_{sa}
+
\beta\mathcal{L}_{rd}
+
\gamma\mathcal{L}_{pm}
$$

---

## Module 1: RFQ — Robust Fusion Query

RFQ performs sample selection to separate training triplets into clean and noisy sets.

It uses a GMM-style clean/noisy partition based on training loss. Clean samples are used for reliable query-target alignment.

Core role:

> Reduce the negative effect of noisy triplets during the normal composed retrieval loss.

In code, this corresponds to the main composed query branch:

$$
(I_r, m) \rightarrow I_t
$$

trained with:

$$
\mathcal{L}_{rm}
$$

![[Pasted image 20260703143951.png]]
---

## Module 2: PTE — Pseudo Text Enhancement

PTE tries to reuse noisy triplets instead of discarding them.

It computes the visual difference between target and reference:

$$
I_t - I_r
$$

then projects this difference into pseudo-text / adapter tokens. These pseudo tokens are used to model the actual visual modification even when the human text is noisy.

Core role:

> Replace unreliable modification text with visual-difference-based pseudo modification supervision.

This introduces:
$$
\mathcal{L}_{sa}
$$

for semantic alignment, and:

$$
\mathcal{L}_{rd}
$$

for retrieval using the reference-difference branch.

---

## Module 3: TOP — Task-Oriented Prompt

TOP replaces the reference image with a learnable prompt and trains a reference-independent query:
$$
(p, m) \rightarrow I_t
$$

The goal is to learn modification-target alignment, especially when the reference image is irrelevant or misleading.

Core role:

> Make the model learn from modification-target pairs even when the reference image is noisy or partially mismatched.

This introduces:

$$
\mathcal{L}_{pm}
$$

### Critical note

For my synergy proposal, TOP is risky because it encourages text-target alignment without relying on the reference image.

---

## Experimental setup

They evaluate on:

- CIRR
- FashionIQ

They simulate noisy triplets by selecting a noise ratio \(\sigma\), then shuffling one component of selected training triplets:

```text
shuffle reference image  → partial matching
shuffle modification text → incorrect matching
shuffle target image      → incorrect matching
```
Noise ratios include:
$$
σ∈{0,0.2,0.5,0.8}
$$
## Important ablation

The ablation table shows that the base model without RFQ / PTE / TOP is already strong.

For example, on CIRR validation with σ=0.2

```
TME-Base:  R@1 = 50.92  Avg = 78.75 Full TME:  R@1 = 53.84  Avg = 81.60
```

This means most basic CIR ability comes from the base composed-query model, while TME modules mainly improve robustness to noisy triplets.

![[Pasted image 20260703144225.png]]

## Five 2026 CIR papers

Năm papers này về cơ bản đến từ **cùng một nhóm (lab của Yupeng Hu, Shandong University)** và chia sẻ một "khuôn mẫu" (template) nghiên cứu rất nhất quán. Dưới đây là phân tích các pattern chung, kèm mức độ tin cậy cho mỗi nhận định.

## 1. Bảng phân rã theo "khuôn mẫu" chung

|Slot|HINT|MELT|HABIT|INTENT|Air-Know|
|---|---|---|---|---|---|
|Venue|ICASSP-style (4tr)|ICASSP-style|AAAI'26|AAAI'26|(8tr, CVPR-style)|
|"Limitation → đúng 2 challenges"|implicit deps + thiếu discrepancy amplification|rare semantic localization + robust sim dưới hard-neg|composed semantic discrepancy + progressive adaptation|neglected inherent noise + hard decision boundary|small-loss hypothesis sụp đổ → self-dependent vicious cycle|
|Backbone|BLIP-2 / Q-Former|BLIP-2 / Q-Former|BLIP-2 / Q-Former|BLIP-2 / Q-Former|BLIP-2 / Q-Former|
|Số module|3 (DCE, QCR, DPCC)|2 (RATR, DSD)|2 (MKE, DPL)|2 (VIC, BiODL)|3 (EPA, EKI, DSR)|
|Hàm loss|$L=L_{rank}+\lambda L_{context}$|$L=L_{bbc}+\kappa L_{KD}+\lambda L_{diff}$|$L=L_{rank}+\kappa L_{KL}+\gamma L_{soft}$|$L=L_{robust}+\mu L_{sod}+\alpha L_{caco}$|$L=L_{Align}+\lambda L_{Recon}$|
|Datasets|FashionIQ + CIRR|FashionIQ + CIRR|FashionIQ + CIRR|FashionIQ + CIRR|FashionIQ + CIRR|
|Vấn đề trung tâm|performance (no-noise)|performance (no-noise)|robustness (NTC)|robustness (NTC)|robustness (NTC)|

## 2. Các pattern chung (theo nhóm)

**A. Provenance — cùng lab, trích dẫn vòng tròn** _(tin cậy: Cao)_ Yupeng Hu là corresponding author của cả 5; các tác giả Zhiwei Chen / Zixu Li / Zhiheng Fu / Qinlei Huang xuất hiện lặp lại. HINT cite MELT và ngược lại; Air-Know benchmark trực tiếp với HABIT và INTENT. Đây là một cụm tự-trích-dẫn chặt.

**B. Khuôn mẫu tu từ (rhetorical template)** _(tin cậy: Cao)_ Mọi paper đi theo đúng kịch bản: _"key limitation của existing methods" → bẻ thành **đúng hai** challenges → đặt tên network theo backronym → 2–3 module, mỗi module trị một challenge → tổ hợp loss có hệ số $\lambda$ → SOTA trên "most/all metrics"_. Mẫu "exactly two challenges" gần như là chữ ký.

**C. Naming convention — backronym viết hoa rải chữ** _(tin cậy: Cao)_ dual-pat**H** compos**I**tional co**N**textualized ne**T**work (HINT); Modification fr**E**quentation-rarity ba**L**ance ne**T**work (MELT); c**H**rono-synergi**A** ro**B**ust progress**I**ve ... re**T**rieval (HABIT); v.v.

**D. Khuôn mẫu phương pháp** _(tin cậy: Cao)_ Frozen BLIP-2 backbone → composed feature $F_c$ và target $F_t \in \mathbb{R}^{Q\times D}$ ($Q=32, D=256$) → cosine similarity → **một** robust/rank/contrastive loss (hầu hết kế thừa từ RCL, Hu et al. TPAMI'23, hoặc BBC/InfoNCE) **cộng** một auxiliary loss "mới", cân bằng bằng hệ số Hy Lạp.

**E. Khuôn mẫu thực nghiệm** _(tin cậy: Cao)_ Cùng baseline set (SSN, CALA, SPRC, + robust: RCL, RDE, TME), **dùng lại y nguyên các con số baseline** (ví dụ SPRC FashionIQ Dresses R@10 = 49.18 xuất hiện identical ở cả 5 papers); ablation kiểu "w/o module"; case study top-5 (1 CIRR + 1 FashionIQ, target tô màu); efficiency table (FLOPs/params ~915M/GPU mem/test+train time so với SPRC & TME).

## 3. Local genealogy: NTC

Ba paper HABIT / INTENT / Air-Know tạo thành một dòng tiến hóa rõ rệt, tất cả đều xây trên **TME (Li et al., CVPR'25)** và đánh giá tại noise ratio
$$\sigma \in {0, 20, 50, 80}\%$$

- **TME** mở ra bài toán NTC (small-loss hypothesis + GMM).
- **HABIT / INTENT** (AAAI'26) mở rộng TME theo hai hướng khác nhau (mutual-knowledge transition rate; causal intervention + scalable decision boundary).
- **Air-Know** là mới nhất, **phê phán thẳng giả định small-loss** mà chính HABIT/INTENT/TME dựa vào, rồi nâng cấp machinery (MLLM GPT-4o làm offline arbiter + Bayesian VI). Đây là pattern "mỗi paper sau critique giả định của paper trước". _(tin cậy: Cao)_

## 4. Two important caveats

**Về "honest baselines" và độ lớn cải tiến** _(tin cậy: Trung bình–Cao)_: Vì baseline numbers được tái sử dụng và template rất cố định, nhiều delta thực ra khá nhỏ trên CIRR (ví dụ HINT R@1 = 52.34 vs QuRe 52.22, ~0.12 điểm). Cải tiến tập trung mạnh hơn ở FashionIQ. 

**Disambiguation "synergy"** _(tin cậy: Cao)_: HABIT có chữ "Chrono-**Synergia**", nhưng đây là synergy ẩn dụ (collaboration giữa historical & current model), **không phải** synergy theo nghĩa information-theoretic / PID. Tương tự, không paper nào trong nhóm này dùng PID hay đo synergistic information — chúng thuần về CIR + robust learning. 

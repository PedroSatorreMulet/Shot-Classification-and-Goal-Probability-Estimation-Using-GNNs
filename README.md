# **Shot Classification & Goal Probability Estimation Using GNNs**

Repository of my **MSc. Data Science master's thesis**

**Supervisor: Dr. Gabriel Anzer  (Head of Soccer Data Analytics @ RB Leipzig)**

**Grade:** 1.1 (German Scoring System)  ≡  98%


## **Abstract**

This thesis investigates the efficacy of Heterogeneous Graph Transformers (HGTs) in soccer analytics, focusing on shot classification and goal probability estimation. Central to this research were 3 questions: the capability of HGTs in classifying soccer shots as goals or non-goals, their proficiency in calibrating shot classification probabilities, and their comparative performance against a traditional Expected Goals (xG) model using the ROC AUC-score and Brier-score metrics. The findings, derived from implementing and comparing a HGT model, by injecting into it simpler or more complex graphs, and a (regularized logistic regression) xG model, revealed that the HGT model dealing with complex graphs significantly outperformed the others in both ROC AUC-score and Brier-score, with mean values $`\overline{\text{AUC}}_{\text{HGT}_{\text{complex}}} = 0.679 \pm 1.50 \times10^{-3}`$ and $`\overline{\text{Brier}}_{\text{HGT}_{\text{complex}}} = 0.155 \pm 6.41\times10^{-3}`$. The worst-performing model was the xG model with mean values $`\overline{\text{AUC}}_{\text{xG}} = 0.613 \pm 1.95 \times10^{-6}`$ and $`\overline{\text{Brier}}_{\text{xG}} = 0.246 \pm 2.41\times10^{-4}`$. This suggests that the sophisticated architecture of HGTs, proficient at capturing complex relationships within graph-structured data, offers improvements in predicting soccer shot outcomes. The study highlights the necessity for more precise event data, and suggests future exploration in enhanced HGT architectures and usage of GPUs. This thesis contributes to soccer analytics by being, to the best of my knowledge, the first to apply Graph Neural Networks (GNNs), particularly HGTs, in shot classification and goal probability calibration, and comparing the performance of these with traditional xG models. The findings support the hypothesis that utilizing HGTs can enhance shot classification and goal probability calibration in comparison with the traditional xG model, offering a novel perspective in a field that is rapidly evolving.

**Keywords:** Heterogeneous Graph Transformers (HGTs) · Shot Classification · Goal Probability Estimation · Expected Goals (xG)

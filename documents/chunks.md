=== CHUNK 0 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 0, 'page_label': '1', 'start_index': 0}
Length: 788 characters
End of Chunk 0 sentences... :
Journal of Machine Learning Research 26 (2025) 1-40 Submitted 10/23; Revised 11/24; Published 1/25
Locally Private Causal Inference for Randomized Experiments
Yuki Ohnishi yuki.ohnishi@yale.edu
Department of Biostatistics
Yale School of Public Health
New Haven, CT 06510, USA
Jordan Awan ja w an@purdue.edu
Department of Statistics
Purdue University
West Lafayette, IN 47907, USA
Editor: Elias Bareinboim
Abstract
Local diﬀerential privacy is a diﬀerential privacy paradigm in which individuals ﬁrst apply a
privacy mechanism to their data (often by adding noise) before transmitting the result to a
curator. The noise for privacy results in additional bias and variance in their analyses. Thus
it is of great importance for analysts to incorporate the privacy noise into valid inference.



=== CHUNK 1 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 0, 'page_label': '1', 'start_index': 695}
Length: 798 characters
End of Chunk 1 sentences... :
it is of great importance for analysts to incorporate the privacy noise into valid inference.
In this article, we develop methodologies to infer causal eﬀects from locally privatized
data under randomized experiments. First, we present frequentist estimators under various
privacy scenarios with their variance estimators and plug-in conﬁdence intervals. We show a
naïve debiased estimator results in inferior mean-squared error (MSE) compared to minimax
lower bounds. In contrast, we show that using a customized privacy mechanism, we can
match the lower bound, giving minimax optimal inference. We also develop a Bayesian
nonparametric methodology along with a blocked Gibbs sampling algorithm, which can be
applied to any of our proposed privacy mechanisms, and which performs especially well in



=== CHUNK 2 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 0, 'page_label': '1', 'start_index': 1405}
Length: 799 characters
End of Chunk 2 sentences... :
applied to any of our proposed privacy mechanisms, and which performs especially well in
terms of MSE for tight privacy budgets. Finally, we present simulation studies to evaluate
the performance of our proposed frequentist and Bayesian methodologies for various privacy
budgets, resulting in useful suggestions for performing causal inference for privatized data.
Keywords: Rubin Causal Model, Local Diﬀerential Privacy, Minimax Optimal Estimation,
Debiased Estimators, Dirichlet Process Mixture, Data Augmentation
1. Introduction
Causal inference is a fundamental consideration across a wide range of domains in science,
technology, engineering, and medicine. Researchers study experimental or observational
data to unveil the causal eﬀects of treatment assignment in an unbiased manner with valid



=== CHUNK 3 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 0, 'page_label': '1', 'start_index': 2115}
Length: 717 characters
End of Chunk 3 sentences... :
data to unveil the causal eﬀects of treatment assignment in an unbiased manner with valid
uncertainty quantiﬁcation. A traditional gold standard for performing causal inference is
the classical randomized experiment (Imbens and Rubin, 2015). In this type of experiment,
a great deal of control and precautions can be taken so as to eliminate events that would
introduce instabilities and biases in causal inferences.
On the other hand, diﬀerential privacy (DP), introduced by Dwork et al. (2006), is another
growing domain in science and business, as privacy protection has become a core concern
for many organizations in the modern data-rich world. DP is a mathematical framework
c©2025 Yuki Ohnishi and Jordan Awan.



=== CHUNK 4 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 0, 'page_label': '1', 'start_index': 2711}
Length: 273 characters
End of Chunk 4 sentences... :
for many organizations in the modern data-rich world. DP is a mathematical framework
c©2025 Yuki Ohnishi and Jordan Awan.
License: CC-BY 4.0, see https://creativecommons.org/licenses/by/4.0/. Attribution requirements are provided
at http://jmlr.org/papers/v26/23-1401.html.



=== CHUNK 5 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 1, 'page_label': '2', 'start_index': 0}
Length: 752 characters
End of Chunk 5 sentences... :
Yuki Ohnishi and Jordan A w an
that provides a probabilistic guarantee that protects private information about individuals
when publishing statistics about a dataset. This probabilistic guarantee is often achieved by
adding random noise to the data. One DP model is thecentral diﬀerential privacy model,
in which the data curators have access to the sensitive data and apply a DP mechanism
to the data to produce the published outputs. A weakness of this model is that users are
required to trust the data curators with their sensitive data. Another DP model islocal
diﬀerential privacy (LDP). In this model, the users do not directly provide their data to the
data curator; instead, users apply the DP mechanism to their data locally before sending it



=== CHUNK 6 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 1, 'page_label': '2', 'start_index': 661}
Length: 775 characters
End of Chunk 6 sentences... :
data curator; instead, users apply the DP mechanism to their data locally before sending it
to the curator. LDP is a preferable model if the data curators are not trusted by users. The
LDP model has been adopted by various organizations, e.g., Google (Erlingsson et al., 2014)
and Apple (Apple, 2017), for more stringent privacy protection.
Drawing causal conclusions from privatized data can be challenging. While the added
random noise helps in safeguarding individuals’ privacy, it distorts the patterns in the
data. This distortion can lead to biased conclusions even in randomized experiments.
This issue becomes even more pronounced in the LDP setting, where each data point is
individually altered before it is compiled. Therefore, when trying to understand cause-and-



=== CHUNK 7 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 1, 'page_label': '2', 'start_index': 1345}
Length: 791 characters
End of Chunk 7 sentences... :
individually altered before it is compiled. Therefore, when trying to understand cause-and-
eﬀect relationships using this protected data, researchers must exercise extra caution to
ensure their interpretations remain accurate and unbiased.
In this article, we propose statistically valid causal inferential methodologies under three
distinct local privacy scenarios. The ﬁrst scenario, which we refer to as a “joint scenario,”
assumes that all accessible variables are separately privatized. In the second and third
scenarios, which we term as “custom scenarios,” we are allowed to select the variables we
privatize with known and unknown treatment assignment probabilities. We then oﬀer causal
inference methodologies to analyze such privatized data. Our main contributions are as
follows:



=== CHUNK 8 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 1, 'page_label': '2', 'start_index': 2041}
Length: 723 characters
End of Chunk 8 sentences... :
inference methodologies to analyze such privatized data. Our main contributions are as
follows:
• We propose a “naïve” inverse probability weighting (IPW) estimator for the joint
scenario. The bias of this IPW estimator is computed, and we introduce a technique
to debias it. Furthermore, we present eﬃcient frequentist estimators that achieve
the minimax optimal rate for custom scenarios. The asymptotic variance of each of
our estimators is calculated, and we construct asymptotic plugin nominal conﬁdence
intervals for these frequentist estimators.
• We develop a ﬂexible and eﬃcient Bayesian nonparametric methodology. Additionally,
we introduce a novel data augmentation Gibbs sampler, tailored for locally privatized



=== CHUNK 9 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 1, 'page_label': '2', 'start_index': 2679}
Length: 792 characters
End of Chunk 9 sentences... :
we introduce a novel data augmentation Gibbs sampler, tailored for locally privatized
observations under the potential outcome framework. This methodology is general and
can be applied to all scenarios considered in the frequentist analyses. Our simulation
studies show that our Bayesian approach performs well in terms of MSE, especially for
tight privacy budgets.
• We present simulation studies to evaluate the frequentist and Bayesian methodologies at
various privacy budgets, resulting in useful suggestions for performing causal inference
for privatized data. We then apply our methodologies to the real-life data from
the evaluation of a cash transfer program conducted in Colombia. We show our
methodologies successfully recover the non-private estimates for moderate privacy
budgets.



=== CHUNK 10 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 1, 'page_label': '2', 'start_index': 3381}
Length: 273 characters
End of Chunk 10 sentences... :
methodologies successfully recover the non-private estimates for moderate privacy
budgets.
The rest of the paper is organized as follows. Section 2 presents the preliminaries for the
Rubin Causal Model and LDP. In Section 3, we develop frequentist approaches to inferring
2



=== CHUNK 11 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 2, 'page_label': '3', 'start_index': 0}
Length: 794 characters
End of Chunk 11 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
the causal eﬀects of interest. Section 4 presents a Bayesian methodology for performing valid
causal inference with the privatized data. Section 5 provides simulation studies for validating
our methodologies developed in the previous sections, and Section 6 provides an application
of our methodologies to real-world data of a cash transfer program conducted in Colombia.
Section 7 concludes with some ﬁnal discussion. The Appendix contains proofs, technical
details, and additional numerical results. We also propose a regression adjustment technique
under the joint scenario, which incorporates covariate information, but since it does not oﬀer
substantial gains over our other methods we leave it in the Appendix.
1.1 Related Work



=== CHUNK 12 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 2, 'page_label': '3', 'start_index': 708}
Length: 774 characters
End of Chunk 12 sentences... :
substantial gains over our other methods we leave it in the Appendix.
1.1 Related Work
In non-causal domains, Evans and King (2022) oﬀered statistically valid linear regression
estimates and descriptive statistics for locally private data that can be interpreted as ordinary
analyses of non-conﬁdential data but with appropriately larger standard errors. Schein et al.
(2019) presented an MCMC algorithm that approximates the posterior distribution over
the latent variables conditioned on data that has been locally privatized by the geometric
mechanism. Ju et al. (2022) proposed a general privacy-aware data augmentation MCMC
framework to perform Bayesian inference from privatized data.
Some researchers have developed causal inference methodologies under the central DP



=== CHUNK 13 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 2, 'page_label': '3', 'start_index': 1337}
Length: 788 characters
End of Chunk 13 sentences... :
framework to perform Bayesian inference from privatized data.
Some researchers have developed causal inference methodologies under the central DP
model. D’Orazio et al. (2015) introduced the construction of central diﬀerential privacy
mechanisms for summary statistics in causal inference. They then presented new algorithms
for releasing diﬀerentially private estimates of causal eﬀects and the generation of diﬀerentially
private covariance matrices from which any least squares regression may be estimated. Lee
et al. (2019) proposed a privacy-preserving inverse propensity score estimator for estimating
the average treatment eﬀect (ATE). Komarova and Nekipelov (2020) studied the impact of
diﬀerential privacy on the identiﬁcation of statistical models and demonstrated identiﬁcation



=== CHUNK 14 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 2, 'page_label': '3', 'start_index': 2032}
Length: 757 characters
End of Chunk 14 sentences... :
diﬀerential privacy on the identiﬁcation of statistical models and demonstrated identiﬁcation
of causal parameters failed in regression discontinuity design under the central diﬀerential
privacy. Niu et al. (2022) introduced a general meta-algorithm for privately estimating
conditional average treatment eﬀects. Kusner et al. (2016) tackles causal inference using a
framework called the additive noise model (ANM), a more restrictive causal model than the
Rubin Causal Model.
While all of the above works predominantly focus on the central diﬀerential privacy model,
our research emphasizes the application of local diﬀerential privacy (LDP) for causal inference.
This shift is crucial as LDP ensures robust privacy protection by adding noise to individual



=== CHUNK 15 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 2, 'page_label': '3', 'start_index': 2697}
Length: 794 characters
End of Chunk 15 sentences... :
This shift is crucial as LDP ensures robust privacy protection by adding noise to individual
data points before they are shared, eliminating the need for a trusted central authority.
Given the increasing concerns about data privacy and the potential risks of centralized data
breaches, LDP is now widely adopted in many organizations. It allows for stronger privacy
guarantees without compromising the integrity of individual data contributions. Our work
demonstrates how to perform causal inference under LDP model, maintaining the accuracy
and reliability of results while providing enhanced privacy protection.
While LDP is a rapidly growing technique, the literature on causal inference methodologies
under LDP remains sparse. Agarwal and Singh (2021) introduced an end-to-end procedure for



=== CHUNK 16 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 2, 'page_label': '3', 'start_index': 3402}
Length: 372 characters
End of Chunk 16 sentences... :
under LDP remains sparse. Agarwal and Singh (2021) introduced an end-to-end procedure for
covariates cleaning, estimation, and inference, oﬀering covariates cleaning-adjusted conﬁdence
intervals under the local diﬀerential privacy mechanism. This work targets situations where
only the covariates are privatized. In contrast, our methods consider the joint privatization
3



=== CHUNK 17 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 3, 'page_label': '4', 'start_index': 0}
Length: 757 characters
End of Chunk 17 sentences... :
Yuki Ohnishi and Jordan A w an
of all variables, including treatment, outcomes, and covariates. Additionally, we emphasize
the context of randomized experiments, which remains the benchmark for credible causal
inference. Other key contributions of our work are the minimax optimal rates for our
estimates and the introduction of Bayesian methodologies, which are optimized for tight
privacy budgets and have not been proposed in previous literature.
2. Preliminaries
2.1 Rubin Causal Model
Causal inference is of fundamental importance across many scientiﬁc and engineering domains
that require informed decision-making based on experiments. Throughout this manuscript,
we adopt the Rubin Causal Model (RCM) as our causal paradigm. In the RCM it is critical



=== CHUNK 18 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 3, 'page_label': '4', 'start_index': 670}
Length: 793 characters
End of Chunk 18 sentences... :
we adopt the Rubin Causal Model (RCM) as our causal paradigm. In the RCM it is critical
to ﬁrst carefully deﬁne the Science of a particular problem, i.e., to deﬁne the experimental
units, covariates, treatments, and potential outcomes (Imbens and Rubin, 2015). We consider
N experimental units, indexed byi = 1,...,N , that correspond to physical objects at a
particular point in time. Each uniti has an observed outcomeYi and treatment assignment
Wi respectively. We consider a binary treatment Wi ∈ {0, 1} with a ﬁxed assignment
probability,p = P (Wi = 1), which is usually assumed to be known by the experimental
design, and letYi(w) denote a potential outcome forw∈{ 0, 1}. In this article, we consider
the N units as a random sample from a large super-population, and we are interested in



=== CHUNK 19 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 3, 'page_label': '4', 'start_index': 1377}
Length: 775 characters
End of Chunk 19 sentences... :
the N units as a random sample from a large super-population, and we are interested in
inferring the Population Average Treatment Eﬀect (PATE):τ = E[Yi(1)−Yi(0)]. We invoke
the common set of assumptions, which enable us to identify the PATE by the estimators
derived in this manuscript (Imbens and Rubin, 2015).
Assumption 1 1. (Positivity) The probability of treatment assignment given the covari-
ates is bounded away from zero and one:0<P (Wi = 1)< 1.
2. (Random Assignment) The potential outcomes are independent of treatment assignment:
{Yi(0),Yi(1)}⊥ ⊥Wi.
3. (Stable Unit Treatment Value Assumption [SUTVA]) There is neither interference
nor hidden versions of treatment. The observed outcome is formally expressed as:
Yi =WiYi(1) + (1−Wi)Yi(0).
2.2 Diﬀerential Privacy



=== CHUNK 20 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 3, 'page_label': '4', 'start_index': 2021}
Length: 759 characters
End of Chunk 20 sentences... :
nor hidden versions of treatment. The observed outcome is formally expressed as:
Yi =WiYi(1) + (1−Wi)Yi(0).
2.2 Diﬀerential Privacy
In this article, we use the local diﬀerential privacy (LDP) model. LetD be the set of
possible contributions from one individual in databaseD. In this paper, we only consider
non-interactive local DP mechanisms. LDP is formally deﬁned for anyD as follows.
Deﬁnition 1 (Local Diﬀerential Privacy)An algorithmM is said to beϵ-locally diﬀer-
entially private (ϵ-LDP) if for any two data pointsx,x′∈D , and anyS⊆ Range(M),
P (M(x)∈S)
P (M(x′)∈S)≤ exp(ϵ).
The deﬁnition states that if an individual changes their value fromx to x′, the output
distribution ofM remains similar, making it diﬃcult for an adversary to determine whether



=== CHUNK 21 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 3, 'page_label': '4', 'start_index': 2691}
Length: 185 characters
End of Chunk 21 sentences... :
distribution ofM remains similar, making it diﬃcult for an adversary to determine whether
the true value wasx or x′. Intuitively, the probability ratio on the left-hand side quantiﬁes
4



=== CHUNK 22 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 4, 'page_label': '5', 'start_index': 0}
Length: 712 characters
End of Chunk 22 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
the “similarity” of the algorithm’s output for diﬀerent inputsx and x′. The valueϵ on the
right-hand side is called theprivacy budget. Lower values ofϵ, which indicate tighter upper
bounds on the probability ratio, correspond to stronger privacy guarantees. This is because
a tightly bounded ratio implies that the random output provides little information about
whether the input wasx or x′.
Two important properties of diﬀerential privacy arecomposition and invariance to post-
processing. Composition allows one to derive the cumulative privacy cost when releasing
the results of multiple privacy mechanisms: ifM1 is ϵ1-LDP andM2 is ϵ2-DP, then the



=== CHUNK 23 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 4, 'page_label': '5', 'start_index': 629}
Length: 766 characters
End of Chunk 23 sentences... :
the results of multiple privacy mechanisms: ifM1 is ϵ1-LDP andM2 is ϵ2-DP, then the
joint release (M1(x),M2(x)) satisﬁes (ϵ1 +ϵ2)-LDP. Invariance to post-processing ensures
that applying a data-independent procedure to the output of a DP mechanism does not
compromise the privacy guarantee: ifM is ϵ-LDP with rangeY, and f :Y →Z is a
(potentially randomized) function, thenf◦M is alsoϵ-LDP. Invariance to post-processing is
especially important in this paper, as all of our inference procedures (i.e., frequentist and
Bayesian) can be expressed as post-processing of more basic DP quantities.
One of the most commonly used DP mechanisms is the Laplace mechanism, which adds
noise to a function of interest. Importantly, the noise must be scaled proportionally to the



=== CHUNK 24 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 4, 'page_label': '5', 'start_index': 1303}
Length: 789 characters
End of Chunk 24 sentences... :
noise to a function of interest. Importantly, the noise must be scaled proportionally to the
sensitivity of the function, which measures the worst-case magnitude by which the function’s
value may change between two individuals. Formally, the𝓁1-sensitivity of a functionf:
D→ Rk is ∆f = supx,y∈D||f(x)−f(y)||1.
Proposition 2 (Laplace Mechanism)Let f : D → Rk. The Laplace mechanism is
deﬁned asM(x) =f(x)+(ν1,...,ν k)⊤, where theνi are independent Laplace random variables,
νi ∼ Lap(0, ∆f/ϵ), where the density of the Laplace distribution,Lap(µ,b ), is given by
f(ν|µ,b ) = 12b exp(−|ν−µ|b ). ThenM satisﬁes ϵ-LDP.
For a binary variable (e.g., treatment assignment), a common mechanism is the randomized
response.
Proposition 3 (Randomized Response Mechanism)LetZi∈{ 0, 1} be a binary vari-



=== CHUNK 25 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 4, 'page_label': '5', 'start_index': 2006}
Length: 733 characters
End of Chunk 25 sentences... :
response.
Proposition 3 (Randomized Response Mechanism)LetZi∈{ 0, 1} be a binary vari-
able. The randomized response mechanism is deﬁned as
M(Zi) =
{
Zi w.p. exp(ϵ)1+exp(ϵ)
1−Zi w.p. 11+exp(ϵ),
which satisﬁesϵ-LDP.
3. Frequentist Approach
3.1 Minimax Risk Lower Bound for PATE Estimation
In this section, we discuss frequentist estimators forτ under several privacy scenarios where
variables are privatized in diﬀerent manners. According to Duchi et al. (2018), the minimax
lower bound of the mean-squared error (MSE) for one-dimensional mean estimation is
O((Nϵ 2)−1). In Lemma 4, we show that this same lower bound applies to the MSE for PATE
estimation as well. We letMϵ denote the set of all privacy mechanisms that satisfyϵ-LDP.



=== CHUNK 26 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 4, 'page_label': '5', 'start_index': 2651}
Length: 268 characters
End of Chunk 26 sentences... :
estimation as well. We letMϵ denote the set of all privacy mechanisms that satisfyϵ-LDP.
To ensure bounded𝓁1-sensitivity, we assumeYi(w)∈ [0, 1] for i = 1,...,N , and{Yi(w)}Ni=1
are drawn according to some distributionPw∈P w, wherePw denotes a class of distributions
5



=== CHUNK 27 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 5, 'page_label': '6', 'start_index': 0}
Length: 767 characters
End of Chunk 27 sentences... :
Yuki Ohnishi and Jordan A w an
on the sample space of potential outcomes. Our restriction toYi(w)∈ [0, 1] is for simplicity
and clarity. This follows standard practice (e.g., Lei et al. (2017), Ferrando et al. (2022) to
name a few), and our discussions can be easily generalized to bounded outcomesYi(w)∈ [a,b ]
with−∞<a<b< ∞ using shifting and scaling factors. In Section 7 we discuss a potential
extension to unbounded outcomes. We deﬁne an estimatorˆτ as a measurable function that
maps privatized inputs to a real value, that is,ˆτ :XN→ R, whereX generally denotes the
space of privatized inputs under various privacy scenarios.
Lemma 4 Forϵ∈ [0, 1], there exists a constantc such that
c min(1, (Nϵ 2)−1)≤ inf
Mϵ∈Mϵ
inf
ˆτ
sup
P0∈P0,
P1∈P1,
p∈[0,1]
E[(ˆτ−τ)2] (1)



=== CHUNK 28 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 5, 'page_label': '6', 'start_index': 633}
Length: 773 characters
End of Chunk 28 sentences... :
Lemma 4 Forϵ∈ [0, 1], there exists a constantc such that
c min(1, (Nϵ 2)−1)≤ inf
Mϵ∈Mϵ
inf
ˆτ
sup
P0∈P0,
P1∈P1,
p∈[0,1]
E[(ˆτ−τ)2] (1)
Lemma 4 states that the optimal estimator of the PATE estimation problem also has the
minimax lower boundO((Nϵ 2)−1), implying that if an LDP ATE estimation procedure
achieves the minimax lower bound, then it is minimax optimal amongall ϵ-LDP procedures.
3.2 Joint Scenario with Knownp
We ﬁrst consider a scenario where all variables are jointly and separately privatized. The
observed outcomes are privatized by the Laplace mechanism. The privatized outcomes are
˜Yi = Yi +νYi , whereνYi ∼ Lap(1/ϵy). We chose the Laplace mechanism as our privacy
mechanism because of its versatility in that it can be used for both continuous and binary



=== CHUNK 29 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 5, 'page_label': '6', 'start_index': 1316}
Length: 788 characters
End of Chunk 29 sentences... :
mechanism because of its versatility in that it can be used for both continuous and binary
outcomes, oﬀering a more general solution for our analysis. If the outcome is binary, the
randomized response mechanism can also be used for privatizingYi. Appendix C provides
detailed discussions of this special case. The binary treatment variableWi is privatized by
the random response mechanism.
˜Wi =
{
Wi w.p. qϵw = exp(ϵw)1+exp(ϵw)
1−Wi w.p. 1−qϵw = 11+exp(ϵw).
By composition, the joint release of( ˜Yi, ˜Wi)Ni=1 satisﬁes (ϵy +ϵw)-LDP. ˜Yi is observed after
adding noise toYi, which is eitherYi(0) or Yi(1), but we cannot identify which it is through
the observed variables becauseWi is also unobserved.
First, we propose estimators by plugging in the privatized observations into classical



=== CHUNK 30 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 5, 'page_label': '6', 'start_index': 1965}
Length: 718 characters
End of Chunk 30 sentences... :
the observed variables becauseWi is also unobserved.
First, we propose estimators by plugging in the privatized observations into classical
formulas, then derive bias correction results of the plug-in estimators. We also provide
variance estimators, enabling asymptotically accurate plug-in conﬁdence intervals.
We consider the following naïve inverse probability weighting (IPW) estimator˜τnaive.
This naïve IPW estimator is deﬁned by plugging in privatized observations for the usual
IPW estimator.
˜τnaive = 1N N∑i=1{ ˜Wi ˜Yiρ1 − (1− ˜Wi) ˜Yiρ0 }, (2)
whereρw =P ( ˜Wi =w) forw = 0, 1. Note thatρw is a known marginal probability expressed
byp and qϵw. The following lemma quantiﬁes the bias of the estimator (2).
6



=== CHUNK 31 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 6, 'page_label': '7', 'start_index': 0}
Length: 796 characters
End of Chunk 31 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
Lemma 5 Under Assumption 1, the estimator(2) is biased forτ. The bias is
Bias(˜τnaive) =
( 1
Cp,ϵw
− 1
)
τ,
whereCp,ϵw = ρ0ρ1p(1−p)(2qϵw−1) with qϵw = exp(ϵw)/(1 + exp(ϵw)).
Let ˆEw = 1˜Nw∑i: ˜Wi=w ˜Yi and ˆVw = 1˜Nw−1∑i: ˜Wi=w( ˜Yi− ˆEw)2, where ˜Nw =∑Ni=1 1 ( ˜Wi =
w) forw = 0, 1. In Theorem 6, we show that the estimatorCp,ϵw·˜τnaive is unbiased, consistent,
and that we can construct asymptotically valid conﬁdence intervals for PATE based on this
estimator.
Theorem 6 1. (Unbiasedness & Consistency)Cp,ϵw· ˜τnaive is unbiased and consistent
for τ.
2. (CLT)
√
N(Cp,ϵw· ˜τnaive−τ) converges in distribution to a mean-zero normal distribu-
tion.
3. (Conﬁdence Interval) The following interval is the nominal central conﬁdence at the



=== CHUNK 32 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 6, 'page_label': '7', 'start_index': 704}
Length: 767 characters
End of Chunk 32 sentences... :
tion.
3. (Conﬁdence Interval) The following interval is the nominal central conﬁdence at the
signiﬁcance levelα:

Cp,ϵw· ˜τnaive−zα2
√
ˆΣnaive
N ,Cp,ϵw· ˜τnaive +zα2
√
ˆΣnaive
N

,
where ˆΣnaive =C2p,ϵw( 1ρ1 ˆV1 + 1ρ0 ˆV0 + ρ0ρ1 ˆE21 + ρ1ρ0 ˆE20 + 2 ˆE0 ˆE1).
4. (Convergence rate) The MSE ofCp,ϵw· ˜τnaive is O((Nϵ 2yϵ2w)−1).
The details of the asymptotic normality and the conﬁdence interval construction are in
Appendix A.4. Settingϵy =ϵw =ϵ/2 gives MSE ofO((Nϵ 4)−1), which matches the minimax
rate (1) in terms ofN, but not in terms ofϵ. In the following sections, we see that when
we use a customized privacy mechanism, rather than a naïve joint privatization, we can
match the minimax lower bound. In the Appendix, we introduce another class of frequentist



=== CHUNK 33 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 6, 'page_label': '7', 'start_index': 1382}
Length: 762 characters
End of Chunk 33 sentences... :
match the minimax lower bound. In the Appendix, we introduce another class of frequentist
estimators: the OLS estimator, speciﬁcally under the joint scenario. We explore both the
advantages and limitations of the OLS estimator in comparison to the IPW estimator within
this context.
3.3 Custom Scenario with Knownp
In this section, we will tailor the privacy mechanism to the PATE estimation problem,
assuming that the value p is known (such as in most designed experiments). Speciﬁ-
cally, for unit i = 1,...,N , we privatize the following variable by the Laplace mech-
anism: Ai = WiYip − (1−Wi)Yi1−p . The sensitivity of A is ∆A = maxAi,A′i|Ai− A′i| =
maxWi,Yi,W′i,Y′i
⏐⏐⏐WiYip − (1−Wi)Yi1−p − W′iY′ip + (1−W′i )Y′i1−p ⏐⏐⏐ ≤ 1p + 11−p. The privatized value of



=== CHUNK 34 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 6, 'page_label': '7', 'start_index': 2037}
Length: 275 characters
End of Chunk 34 sentences... :
maxWi,Yi,W′i,Y′i
⏐⏐⏐WiYip − (1−Wi)Yi1−p − W′iY′ip + (1−W′i )Y′i1−p ⏐⏐⏐ ≤ 1p + 11−p. The privatized value of
A is ˜Ai =Ai +νAi , whereνAi ∼ Lap(∆A/ϵa). Then, it is straightforward to show that the
following IPW estimator is unbiased and consistent.
˜τIPW = 1N N∑i=1 ˜Ai. (3)
7



=== CHUNK 35 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 7, 'page_label': '8', 'start_index': 0}
Length: 738 characters
End of Chunk 35 sentences... :
Yuki Ohnishi and Jordan A w an
Theorem 7 1. (Unbiasedness & Consistency)˜τIPW is unbiased and consistent forτ.
2. (CLT)
√
N(˜τIPW −τ) converges in distribution to a mean-zero normal distribution.
3. (Conﬁdence Interval) The following interval is the nominal central conﬁdence at the
signiﬁcance levelα:

˜τIPW −zα2
√
ˆΣIPW
N , ˜τIPW +zα2
√
ˆΣIPW
N

,
where ˆΣIPW = 1N−1∑Ni=1( ˜Ai− ˆEA)2 with ˆEA = 1N∑Ni=1 ˜Ai.
4. (Convergence rate) The MSE of˜τIPW is O((Nϵ 2a)−1).
The details of the asymptotic normal distribution and the conﬁdence interval construction are
provided in Appendix A.5. We see in Theorem 7 that the lower bound of the IPW estimator
under the custom scenario matches the minimax lower bound for the locally private PATE



=== CHUNK 36 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 7, 'page_label': '8', 'start_index': 652}
Length: 761 characters
End of Chunk 36 sentences... :
under the custom scenario matches the minimax lower bound for the locally private PATE
estimation (1), improving over the naïve estimator from Section 3.2.
3.4 Custom Scenario with Unknownp
The estimator (3) is appealing in the sense of optimality whenp is known, such as in
randomized experiments, however, their application is restricted whenp is unknown. In
this regard, we proceed a step further to address situations in whichp is inaccessible, while
Assumption 1 remains valid. Examples of this setting include A/B testing and clinical trials,
where marketers or doctors assign treatments with an undisclosed probability (that does not
depend on the covariate information).
We consider releasing the following quantities:˜Bi = ( ˜Bi,1, ˜Bi,2, ˜Bi,3), where



=== CHUNK 37 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 7, 'page_label': '8', 'start_index': 1293}
Length: 759 characters
End of Chunk 37 sentences... :
depend on the covariate information).
We consider releasing the following quantities:˜Bi = ( ˜Bi,1, ˜Bi,2, ˜Bi,3), where
˜Bi,1 =WiYi +νB1i , ˜Bi,2 = (1−Wi)Yi +νB2i , and ˜Bi,3 =Wi +νB3i ,
whereνBji ∼ Lap(1/ϵbj) forj = 1, 2, 3. We also let˜Bi,4 = 1− ˜Bi,3. By composition, the joint
release of ( ˜Bi,1, ˜Bi,2, ˜Bi,3)Ni=1 satisﬁes (ϵb1 +ϵb2 +ϵb3)-LDP.
Given these privatized quantities, we construct our diﬀerence-in-means (DM) estimator
as follows.
˜τDM =
∑N
i=1 ˜Bi,1∑N
i=1 ˜Bi,3
−
∑N
i=1 ˜Bi,2∑N
i=1 ˜Bi,4
. (4)
Let ˆEBj = 1N∑Ni=1 ˜Bi,j, ˆVBj = 1N−1∑Ni=1( ˜Bi,j− ˆEBj)2 for j = 1, 2, 3, 4 and ˆCovj,k =
1
N−1
∑N
i=1( ˜Bi,j− ˆEBj)( ˜Bi,k− ˆEBk) for j⁄=k. We have the following properties for˜τDM:
Theorem 8 1. (Consistency) ˜τDM is consistent forτ.
2. (CLT)
√



=== CHUNK 38 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 7, 'page_label': '8', 'start_index': 1903}
Length: 377 characters
End of Chunk 38 sentences... :
∑N
i=1( ˜Bi,j− ˆEBj)( ˜Bi,k− ˆEBk) for j⁄=k. We have the following properties for˜τDM:
Theorem 8 1. (Consistency) ˜τDM is consistent forτ.
2. (CLT)
√
N(˜τDM−τ) converges in distribution to a mean-zero normal distribution.
3. (Conﬁdence Interval) The following interval is the nominal central conﬁdence at the
signiﬁcance levelα:

˜τDM−zα2
√
ˆΣDM
N , ˜τDM +zα2
√
ˆΣDM
N

,
8



=== CHUNK 39 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 8, 'page_label': '9', 'start_index': 0}
Length: 748 characters
End of Chunk 39 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
where ˆΣDM = ˆe′ˆSˆe, with ˆe = (1/ ˆEB3,−1/(1− ˆEB3),− ˆEB1/ ˆE2B3, ˆEB2/(1− ˆEB3)2)′ and
ˆS =


ˆVB1 ˆCov1,2 ˆCov1,3 ˆCov1,4
ˆCov2,1 ˆVB2 ˆCov2,3 ˆCov2,4
ˆCov3,1 ˆCov3,2 ˆVB3 ˆCov3,4
ˆCov4,1 ˆCov4,2 ˆCov4,3 ˆVB4

.
4. (Convergence rate) The MSE of˜τDM is O((N(ϵ2b1 +ϵ2b2 +ϵ2b3))−1).
The details of the asymptotic normal distribution and the conﬁdence interval construction
are provided in Appendix A.6. Settingϵb1 =ϵb2 =ϵb3 =ϵ/3 givesO((Nϵ 2)−1), which also
matches the minimax lower bound of (1), indicating the optimality of the estimator.
3.5 Discussion on Frequentist Estimators
The three scenarios serve diﬀerent purposes. While the joint scenario permits the release of



=== CHUNK 40 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 8, 'page_label': '9', 'start_index': 615}
Length: 780 characters
End of Chunk 40 sentences... :
3.5 Discussion on Frequentist Estimators
The three scenarios serve diﬀerent purposes. While the joint scenario permits the release of
the entire synthetic dataset to analysts, it suﬀers from the privatization of multiple variables,
thereby compromising its optimality. As discussed in the Appendix, the OLS estimator helps
improve the eﬃciency under the joint scenario, however, the gain is limited since we must pay
additional privacy budgets for covariates. In the custom scenarios, access to the complete
dataset is unavailable, but the estimators attain the optimal rate of the locally private PATE
estimation. While both custom estimators achieve the minimax rate, the estimator with
knownp is able to focus its privacy budget on a single quantity, which gives improved ﬁnite



=== CHUNK 41 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 8, 'page_label': '9', 'start_index': 1304}
Length: 796 characters
End of Chunk 41 sentences... :
knownp is able to focus its privacy budget on a single quantity, which gives improved ﬁnite
sample performance; see Section 5. We emphasize that despite the simplicity of the Laplace
and randomized response mechanisms we employ, our customized estimators attain the
minimax lower bound, thereby ensuring rate optimality across any privacy mechanisms.
When the sample size is small, or when privacy budgets are too tight, it is possible
that the point estimators and interval estimators are out of support of the estimand, as the
estimand is assumed to be bounded, but the observed private data are usually unbounded.
Therefore, we apply additional post-processing to clamp estimators to the closest end of
the support when they are out of bounds. For example, if the initial estimator isˆτ = 1.8,



=== CHUNK 42 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 8, 'page_label': '9', 'start_index': 2010}
Length: 724 characters
End of Chunk 42 sentences... :
the support when they are out of bounds. For example, if the initial estimator isˆτ = 1.8,
then we instead setˆτ = 1.0. However, suppose the lower and upper bounds of the estimated
conﬁdence interval are both clamped to the bounds of the support: in this case, the estimated
conﬁdence interval is not useful at all. Note that this clamping processing does not aﬀect
the asymptotic statistical properties derived in the paper. It only serves to reduce the
MSE of the estimator by projecting the out-of-bound estimator to the bound. Although its
asymptotic properties are not harmed, the clamping process introduces bias in ﬁnite samples
and is a drawback of many of the frequentist estimators including those proposed in this



=== CHUNK 43 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 8, 'page_label': '9', 'start_index': 2646}
Length: 511 characters
End of Chunk 43 sentences... :
and is a drawback of many of the frequentist estimators including those proposed in this
paper. In the Appendix, we provide an analysis of the bias introduced by the clamping
in ﬁnite samples. Speciﬁcally, in the construction of our frequentist estimators, we do
incorporate the boundedness of the outcomes, which calls for the heuristic clamping step.
The subsequent section about the Bayesian approach results in a Bayesian estimator that
naturally incorporates the boundedness assumption into the modeling.
9



=== CHUNK 44 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 9, 'page_label': '10', 'start_index': 0}
Length: 731 characters
End of Chunk 44 sentences... :
Yuki Ohnishi and Jordan A w an
4. Bayesian Approach
4.1 Overview of the Bayesian Methodology
In this section, we propose a principled Bayesian methodology that operates under any LDP
scenario. We consider the Bayesian formulations for a few key reasons that we clarify here:
First, we can incorporate our speciﬁc prior knowledge as well as information about the DP
mechanism into our inference. For example, the diﬀerential privacy framework typically allows
the release of information about the mechanisms the data curator uses to privatize the data,
and major mechanisms (e.g., Laplace and randomized response mechanisms) have a known
likelihood. Therefore, using this knowledge in the form of the joint distribution (as shown in



=== CHUNK 45 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 9, 'page_label': '10', 'start_index': 637}
Length: 757 characters
End of Chunk 45 sentences... :
likelihood. Therefore, using this knowledge in the form of the joint distribution (as shown in
Equation (5) in the manuscript) enables more eﬃcient inference. We can also incorporate
our knowledge about the boundedness of variables into the modeling process, which also
contributes to more eﬃcient inference. Bayesian methodology allows us to combine all sources
of information and summarize the information aboutτ into the posterior distribution. This
allows us to incorporate statistical information in ways that may not be obvious, which is
expected to improve performance.
More generally, in the context of statistical estimation, Bayesian estimators with proper
priors are justiﬁed in terms of admissibility, whereas frequentist estimators have no such



=== CHUNK 46 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 9, 'page_label': '10', 'start_index': 1304}
Length: 785 characters
End of Chunk 46 sentences... :
priors are justiﬁed in terms of admissibility, whereas frequentist estimators have no such
guarantee. Furthermore, with our current assumption of bounded outcomes, we have a
compact parameter space. In this case, the complete class theorem (Chernoﬀ and Moses,
1959; Ferguson, 1967) implies that all admissible procedures are in fact Bayes estimators. By
incorporating prior information and optimizing posterior expected loss, Bayesian estimators
are not only ﬂexible and robust but also theoretically grounded as the optimal choice within
the class of admissible rules. This strong theoretical support, coupled with their practical
advantages, makes Bayesian estimators well-motivated for our problem.
Following the Bayesian paradigm of Rubin (1978), we consider deriving the posterior



=== CHUNK 47 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 9, 'page_label': '10', 'start_index': 2006}
Length: 794 characters
End of Chunk 47 sentences... :
Following the Bayesian paradigm of Rubin (1978), we consider deriving the posterior
distributions of the causal estimands (Forastiere et al., 2016; Ohnishi and Sabbaghi, 2022a)
given all observed variables. The key idea is the data augmentation (Tanner and Wong,
1987) to obtain the posterior distribution of the causal estimands by imputing in turn the
missing variables. The idea for estimating causal eﬀects in the Bayesian paradigm is outlined
in Rubin (1978); Imbens and Rubin (2015), but our unique challenges lie in the fact that
neither treatment variableW nor either potential outcomeY (0),Y (1) is observed.
For Bayesian inference in our framework, consider the following joint distribution of all
observed variables ˜O and missing variablesY(0), Y(1), W: P (Y(0), Y(1), W, ˜O), where



=== CHUNK 48 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 9, 'page_label': '10', 'start_index': 2714}
Length: 774 characters
End of Chunk 48 sentences... :
observed variables ˜O and missing variablesY(0), Y(1), W: P (Y(0), Y(1), W, ˜O), where
˜O = ( ˜Y, ˜W) for the joint scenario and˜O = ˜A or ˜B for the custom scenarios. As discussed
in Section F, since causal eﬀects are identiﬁable under randomization without covariate
adjustment and incorporating covariates requires additional privacy costs for their release,
we do not include covariates in our Bayesian methodologies, but the extension should be
straightforward (e.g., Maceachern (1999)). In what follows, we focus on the joint scenario
discussed in Section 3.2 to show the outline of our algorithm, but it can easily be extended
to the custom scenarios, as explained in Appendix.
Under the super-population perspective, the observed and missing variables are considered



=== CHUNK 49 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 9, 'page_label': '10', 'start_index': 3348}
Length: 414 characters
End of Chunk 49 sentences... :
to the custom scenarios, as explained in Appendix.
Under the super-population perspective, the observed and missing variables are considered
as a joint draw from the population distribution. Bayesian inference considers the observed
values of these quantities to be realizations of random variables and the missing values to
be unobserved random variables. We also assume these quantities are unit exchangeable,
10



=== CHUNK 50 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 10, 'page_label': '11', 'start_index': 0}
Length: 770 characters
End of Chunk 50 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
then de Finetti’s theorem implies that there exists a vector of parameters,θ, with the prior
distribution P (θ) such that
P (Y(0), Y(1), W, ˜Y, ˜W) =
∫
P (θ)
∏
i
P (Yi(0),Yi(1),Wi, ˜Yi, ˜Wi| θ)dθ
=
∫
P (θ)
∏
i
P (Wi)P ( ˜Wi|Wi)P (Yi(0),Yi(1)| θ)P ( ˜Yi|Yi(0),Yi(1),Wi)dθ,
(5)
which follows from the conditional independence of potential outcomes and˜Wi given Wi
(Lemma 9 in the Appendix) and the random assignment assumption. The distribution of˜Yi
depends not only onYi(0) andYi(1) but also onWi because the DP mechanism is applied to
the observed outcomeYi =WiYi(1) + (1−Wi)Yi(0). Note that we know the DP mechanisms
for W and Y, that is,P ( ˜Yi|Yi(0),Yi(1),Wi) and P ( ˜Wi|Wi) have a known functional form.



=== CHUNK 51 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 10, 'page_label': '11', 'start_index': 680}
Length: 798 characters
End of Chunk 51 sentences... :
for W and Y, that is,P ( ˜Yi|Yi(0),Yi(1),Wi) and P ( ˜Wi|Wi) have a known functional form.
Therefore, the modeling eﬀort is only required forP (Yi(0),Yi(1)| θ). Under this modeling
strategy, our Bayesian approach is a valid inference for PATE. Note that PATE is a function
of the parametersθ, which governs the potential outcomes. Thus, it suﬃces to obtain the
posterior draws of the posterior of theθ for the posterior draws of PATE.
A signiﬁcant insight from(5) is that the treatment assignment mechanism isnot ignorable.
In conventional non-private settings, the treatment assignment model, represented asP (Wi),
is ignorable and falls out of the likelihood in Bayesian causal inference under randomization
or unconfoundedness assumptions (Li et al., 2023). Yet, in a DP context, these treatment



=== CHUNK 52 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 10, 'page_label': '11', 'start_index': 1390}
Length: 722 characters
End of Chunk 52 sentences... :
or unconfoundedness assumptions (Li et al., 2023). Yet, in a DP context, these treatment
assignment variables are not directly observed. This necessitates the integration of both the
treatment assignment models and their respective privacy mechanisms into our inferences.
Additionally, a nuanced but crucial point is the necessity to model bothYi(0) and Yi(1).
Typically, Bayesian causal inference for PATE estimation is performed via observable data
(e.g., Zigler (2016); Stephens et al. (2023)). This is because the missing potential outcome
eventually gets marginalized out from(5) under the assumption of prior parameter indepen-
dence and unconfounded assignment, thus it does not inﬂuence parameter inference. In our



=== CHUNK 53 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 10, 'page_label': '11', 'start_index': 2024}
Length: 751 characters
End of Chunk 53 sentences... :
dence and unconfounded assignment, thus it does not inﬂuence parameter inference. In our
scenario, however, it is uncertain whetherYi(0) orYi(1) has been privatized to yield˜Yi. This
uncertainty calls for a data augmentation strategy for both potential outcomes.
We adopt the Dirichlet Process Mixture (DPM) to modelP (Yi(0),Yi(1)|Wi, θ) for its
ﬂexibility. The DPM is a natural Bayesian choice for density estimation problems, which
ﬁts our needs that requireP (Yi(0),Yi(1)|Wi, θ) to be estimated without assuming strong
parametric forms. The following section and Appendix D provide technical details of the
DPM and the Gibbs sampler.
4.2 Algorithm Outlines
Equation (5) motivates the Gibbs sampling procedures to obtain the draws from the posterior



=== CHUNK 54 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 10, 'page_label': '11', 'start_index': 2634}
Length: 760 characters
End of Chunk 54 sentences... :
DPM and the Gibbs sampler.
4.2 Algorithm Outlines
Equation (5) motivates the Gibbs sampling procedures to obtain the draws from the posterior
distribution of θ. This section describes the key steps of the Gibbs sampler. Each step
is derived from the corresponding components of(5). For inference of DPM parameters,
denoted by θ = (µ, Σ, u), we adopt an approximated blocked Gibbs sampler based on the
truncation of the stick-breaking representation (Ishwaran and Zarepour, 2000), due to its
simplicity. In this algorithm, we set a conservatively large upper bound,K≤∞ , on the
number of components that units potentially belong to. LetCi∈{ 1,...,K} denote the latent
class indicators with a multinomial distribution,Ci∼ Multinomial(u) where u = (u1,...,u K)
11



=== CHUNK 55 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 11, 'page_label': '12', 'start_index': 0}
Length: 742 characters
End of Chunk 55 sentences... :
Yuki Ohnishi and Jordan A w an
denote the weights of all components of the DPM. More speciﬁc details about the DPM are
provided in the Appendix. The algorithm proceeds as follows.
1. Given Yi(0),Yi(1), draw eachWi from P (Wi = 1|−) = r1r0+r1, where rw = P ( ˜Yi|
Yi(w))P ( ˜Wi|Wi =w)P (Wi =w) for w = 0, 1.
2. Given µ, Σ, u, Ci and Wi, draw eachYi(0) and Yi(1) according to:
P (Yi(Wi)|−)∝P (Yi(Wi)|µCiWi, ΣCiWi)P ( ˜Yi|Yi(Wi))
P (Yi(1−Wi)|−)∝P (Yi(1−Wi)|µCi1−Wi, ΣCi1−Wi).
3. Update model parameters via the blocked Gibbs sampler and calculate the estimands.
The key steps of this algorithm are 1 and 2, which correspond to the data augmentation steps,
imputing the latent variablesYi(0),Yi(1) and Wi. In Step 1, the probabilityP ( ˜Yi|Yi(w))



=== CHUNK 56 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 11, 'page_label': '12', 'start_index': 653}
Length: 751 characters
End of Chunk 56 sentences... :
imputing the latent variablesYi(0),Yi(1) and Wi. In Step 1, the probabilityP ( ˜Yi|Yi(w))
for w = 0, 1 indicates that ˜Yi is observed via privatizing the potential outcomeYi(w), which
would have been observed if we observedWi =w.
In step 2, givenWi, the corresponding potential outcomeYi(Wi) is considered to be
privatized, but the other missing potential outcomeYi(1−Wi) should not be associated with
the observed ˜Yi within the iteration. Therefore, the posterior distribution ofYi(Wi) cannot
be obtained in a closed form as it is weighted by the privacy mechanismP ( ˜Yi| Yi(Wi)),
whereas the missing potential outcomesYi(1−Wi) are just generated from the outcome
model P (Yi(1−Wi)| θ). We adopt the Metropolis-within-Gibbs algorithm for this step.



=== CHUNK 57 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 11, 'page_label': '12', 'start_index': 1320}
Length: 744 characters
End of Chunk 57 sentences... :
model P (Yi(1−Wi)| θ). We adopt the Metropolis-within-Gibbs algorithm for this step.
Speciﬁcally, we use the outcome model to sample a proposal value fromP (Yi(Wi)|θ) at
the current value ofθ, rather than specifying a custom proposal distribution and step
size for the Metropolis-Hastings step. Ju et al. (2022) provided theoretical guarantees on
mixing performance for the this data augmentation algorithm, indicating that the acceptance
probability is lower bounded byexp(−ϵy).
Finally, Step 3 updates all the parameters of the DPM that govern the potential outcomes,
using standard Gibbs sampling techniques; see Section D of the Appendix for details of
the DPM, full details of the algorithm and the extension of the algorithm to the custom



=== CHUNK 58 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 11, 'page_label': '12', 'start_index': 1977}
Length: 784 characters
End of Chunk 58 sentences... :
the DPM, full details of the algorithm and the extension of the algorithm to the custom
scenarios, which requires slight modiﬁcations to Steps 1 and 2.
5. Simulation Studies
We evaluate the frequentist properties of our methodologies for various privacy budgets.
The evaluation metrics that we consider are bias and mean square error (MSE) in esti-
mating a causal estimand, coverage of an interval estimator for a causal estimand, and
the interval length. Bias, MSE and coverage are generally deﬁned as∑Mm=1 (τ− ˆτm)/M,∑M
m=1 (τ− ˆτm)2/M and∑Mm=1 1 (ˆτlm≤τ≤ ˆτum)/M respectively, whereM denotes the num-
ber of simulated datasets,τ denotes the true causal estimand,ˆτm, ˆτlm and ˆτum denote the
estimate of the causal estimand,95% lower and upper end of the interval estimator of the



=== CHUNK 59 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 11, 'page_label': '12', 'start_index': 2673}
Length: 600 characters
End of Chunk 59 sentences... :
estimate of the causal estimand,95% lower and upper end of the interval estimator of the
causal estimand using datasetm = 1,...,M . Our summary of the interval length is the
mean of the lengths of the intervals computed fromM simulated datasets. For our Bayesian
method, the point estimator is the mean of the posterior distribution of a causal estimand,
and the interval estimator is the95% central credible interval. We ran the MCMC algorithm
for 100, 000 iterations using a burn-in of50, 000. The iteration numbers were chosen after
experimentation to deliver stable results over multiple runs.
12



=== CHUNK 60 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 12, 'page_label': '13', 'start_index': 0}
Length: 747 characters
End of Chunk 60 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
5.1 Data-generating Mechanisms
For our simulations, we consider a Bernoulli randomized experiment with treatment assign-
ment and covariates for uniti generated according to:
Wi∼ Bernoulli(0.5),Xi,1∼ Uniform(0, 1),Xi,2∼ Beta(2, 5),Xi,3∼ Bernoulli(0.7).
To generate potential outcomes, we adopt the Beta regression (Ferrari and Cribari-Neto,
2004): Yi(w)∼ Beta(µi(w)φ, (1−µi(w))φ), whereµi(w) and φ are a location parameter
and scale parameter respectively withµi(w) = expit(1.0− 0.8X1 + 0.5X2− 2.0X3 + 0.5w)
and φ = 50. We considerXi,d to generateYi but do not release the privatized˜Xi,d. This
model is beneﬁcial for our simulations because the generated data automatically satisfy the



=== CHUNK 61 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 12, 'page_label': '13', 'start_index': 656}
Length: 746 characters
End of Chunk 61 sentences... :
model is beneﬁcial for our simulations because the generated data automatically satisfy the
following sensitivity: ∆Y = 1. Then, we obtain the private data˜Yi, ˜Wi, ˜Ai, ˜Bi by applying
the corresponding privacy mechanisms. The actual value of PATE can be obtained in a closed
form, which is necessary to calculate bias, MSE, and coverage. The details are provided in
the Appendix.
5.2 Results
Table 1 presents the performance evaluation of our estimators under diﬀerent scenarios for
N = 10, 000 with various privacy budgets forϵtot. We letϵtot =ϵa =ϵy +ϵw =ϵb1 +ϵb2 +ϵb3,
where ϵy = ϵw and ϵb1 = ϵb2 = ϵb3. All scenarios achieve about95% coverage, except for
the custom scenario (DM) ofϵtot = 0.1,. 03, which has some over-coverage. This may be



=== CHUNK 62 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 12, 'page_label': '13', 'start_index': 1317}
Length: 793 characters
End of Chunk 62 sentences... :
the custom scenario (DM) ofϵtot = 0.1,. 03, which has some over-coverage. This may be
because the estimator for the asymptotic variance has a non-negligible estimation error in
ﬁnite samples. The simulations in this section rely on the results of Section 3.2, 3.3, and 3.4
to build conﬁdence intervals. The fact that the intervals have correct95% coverage indicates
that the estimators 1) are in fact asymptotically normal, 2) are asymptotically unbiased,
and 3) have the stated asymptotic variance. For bias and MSE, we observe smaller bias and
MSE for larger privacy budgets. The custom scenario (IPW) yields lower MSE than the
joint scenario, which is also consistent with the discussion of the optimality in Section 3.2,
3.3, and 3.4, but the diﬀerence becomes negligible asϵtot increases.



=== CHUNK 63 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 12, 'page_label': '13', 'start_index': 2042}
Length: 750 characters
End of Chunk 63 sentences... :
3.3, and 3.4, but the diﬀerence becomes negligible asϵtot increases.
When we have a tight privacy budget ofϵtot = 0.1, 0.3, the length of the conﬁdence
intervals of the joint scenario are nearly2, which is almost non-informative about the
estimand. With strict budget constraints and a small sample size, the analysis results may
tell us little about the estimands, even though their consistency and conﬁdence intervals are
statistically valid. This is an inevitable trade-oﬀ between privacy protection and the accuracy
of the results. Custom (IPW) has the best ﬁnite sample performance, oﬀering informative
intervals and small bias and MSE for all privacy budgets.
Table 2 compares our Bayesian methodology under the three scenarios. We see that the



=== CHUNK 64 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 12, 'page_label': '13', 'start_index': 2650}
Length: 788 characters
End of Chunk 64 sentences... :
intervals and small bias and MSE for all privacy budgets.
Table 2 compares our Bayesian methodology under the three scenarios. We see that the
Bayes estimator yields well-calibrated coverage probabilities and smaller MSE and bias for
most cases. The diﬀerences in MSE between frequentist estimators and Bayesian estimators
become negligible asϵtot gets large (ϵtot = 3.0, 10.0). When the privacy budget is tight, the
Bayesian methodology outperforms the frequentist approach in all metrics. Speciﬁcally, the
interval length of the Bayes estimator forϵtot = 0.1 is around 0.35 for all scenarios, which is
informative about the estimands. In the Appendix, we provide additional simulation studies
for smaller sample sizes, as well as those for the OLS estimator under the joint scenario.
13



=== CHUNK 65 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 13, 'page_label': '14', 'start_index': 0}
Length: 752 characters
End of Chunk 65 sentences... :
Yuki Ohnishi and Jordan A w an
Table 1: Evaluation metrics for IPW estimator under diﬀerent privacy scenarios (N =
10, 000,Nsim = 2, 000). Nsim denotes the number of simulations.ϵtot denotes the
total privacy budget. “Custom (IPW)” and “Custom (DM)” columns are scenarios
in Section 3.3 and 3.4 respectively.
Coverage Bias MSE Interval Width
Custom Custom Custom Custom Custom Custom Custom Custom
ϵtot Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM)
0.1 94.7% 95 .05% 99 .5% −1.0975 −0.4434 0 .9025 0 .9766 0 .2813 0 .7527 1 .892 1 .64 1 .987
0.3 95.45% 94 .35% 98 .15% −0.8388 0 .2448 −0.3912 0 .7919 0 .0365 0 .2563 1 .896 0 .74 1 .646
1.0 95.45% 95 .0% 95 .25% 0 .0827 0 .043 −0.0241 0 .0539 0 .0033 0 .0205 0 .915 0 .225 0 .553



=== CHUNK 66 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 13, 'page_label': '14', 'start_index': 659}
Length: 711 characters
End of Chunk 66 sentences... :
1.0 95.45% 95 .0% 95 .25% 0 .0827 0 .043 −0.0241 0 .0539 0 .0033 0 .0205 0 .915 0 .225 0 .553
3.0 95.2% 95 .1% 94 .8% −0.0044 0 .0229 0 .0534 0 .0011 0 .0004 0 .0021 0 .13 0 .082 0 .182
10 94.3% 94 .3% 95 .1% −0.0025 −0.0104 −0.0083 0 .0001 0 .0001 0 .0002 0 .043 0 .043 0 .057
Table 2: Evaluation metrics of Bayesian estimators forN = 10, 000,Nsim = 1, 000.
Coverage Bias MSE Interval Width
Custom Custom Custom Custom Custom Custom Custom Custom
ϵtot Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM)
0.1 96.4% 98 .0% 96 .3% −0.0949 −0.0858 −0.0951 0 .0099 0 .0087 0 .0099 0.3400 0 .3542 0 .3410
0.3 96.9% 97 .0% 94 .6% −0.0953 −0.0585 −0.0897 0 .0099 0 .0057 0 .0094 0 .3420 0 .3021 0 .3340



=== CHUNK 67 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 13, 'page_label': '14', 'start_index': 1275}
Length: 759 characters
End of Chunk 67 sentences... :
0.3 96.9% 97 .0% 94 .6% −0.0953 −0.0585 −0.0897 0 .0099 0 .0057 0 .0094 0 .3420 0 .3021 0 .3340
1.0 93.4% 92 .0% 92 .2% −0.0691 −0.0197 −0.0511 0.0077 0 .0017 0 .0055 0.3200 0 .1590 0 .2630
3.0 93.2% 90 .5% 94 .2% −0.0081 −0.0070 −0.0098 0 .0006 0 .0004 0 .0010 0 .0930 0 .0698 0 .1170
10.0 95.0% 91 .5% 92 .3% −0.0023 −0.0052 −0.0045 0.0000 0 .0001 0 .0001 0.0260 0 .0325 0 .0360
6. Real Data Analysis
We applied our methodology to a real-world causal inference task. We analyzed a randomized
experiment that examined the impact of a cash transfer program on students’ attendance
rates (Barrera-Osorio et al., 2011). Conducted at San Cristobal in Colombia, the study
recruited households with one to ﬁve school children, randomly assigning children to either



=== CHUNK 68 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 13, 'page_label': '14', 'start_index': 1943}
Length: 781 characters
End of Chunk 68 sentences... :
recruited households with one to ﬁve school children, randomly assigning children to either
participate in the cash transfer program or not with probabilityp = 0.628. The number
of recruited students isN = 5, 240. With known treatment assignment, we assessed the
treatment eﬀect of the program on the attendance rate of the students, with eligible students
receiving cash subsidies if they attended school at least80% of the time in a given month.
We utilized the privatization techniques as outlined in Section 3, settingϵtot to values of
0.1, 0.3, 1.0, 3.0, and 10.0. Our methodologies were then benchmarked against non-private
baseline methods, which oﬀer target values for our private estimates. For the non-private
frequentist baseline, we employed the standard IPW estimator.



=== CHUNK 69 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 13, 'page_label': '14', 'start_index': 2663}
Length: 791 characters
End of Chunk 69 sentences... :
frequentist baseline, we employed the standard IPW estimator.
Table 6 presents point mean estimators alongside the lower (2.5%) and upper (97.5%)
bounds for interval estimators across each methodology. For the interval estimators, we
used central conﬁdence intervals for the frequentist approach and credible intervals for the
Bayesian approach. Both frequentist and Bayesian non-private interval estimators highlighted
a positive interval, indicating a signiﬁcant eﬀect. The point estimates showed a0.6% increase
in the frequentist non-private approach and a more modest0.5% increase in the Bayesian
approach. Given these results, our expectation for the private methodologies is, at best, to
approximate the non-private values, since better inferences are unlikely with privatized data.
14



=== CHUNK 70 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 14, 'page_label': '15', 'start_index': 0}
Length: 791 characters
End of Chunk 70 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
Note that as the experimental data is ﬁxed, the only randomness in this study is the privacy
mechanisms.
The point estimates for both frequentist and Bayesian methodologies are similar to
their non-private results whenϵtot≥ 3.0. In particular, we observe that the Custom (IPW)
scenario results in the narrowest conﬁdence intervals. In the joint and custom (DM) scenarios,
the frequentist estimators deviated more from the non-private one, showing larger intervals.
The frequentist methodologies yield non-informative intervals when the privacy budget is
tightest ϵtot = 0.1. The Bayesian methodology demonstrated strong performance across
all scenarios. These observations align with our simulation studies, further validating the



=== CHUNK 71 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 14, 'page_label': '15', 'start_index': 700}
Length: 123 characters
End of Chunk 71 sentences... :
all scenarios. These observations align with our simulation studies, further validating the
eﬃcacy of our methodologies.
15



=== CHUNK 72 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 15, 'page_label': '16', 'start_index': 0}
Length: 655 characters
End of Chunk 72 sentences... :
Yuki Ohnishi and Jordan A w an
Table 3: Empirical analysis evaluating privatized cash transfer programs in Colombia. In the “Non-private” columns, “Freq”
represents the standard IPW estimator, while “Bayes” represents the standard Dirichlet process mixture models for
non-private data.
Non-private Private
Joint Custom (IPW) Custom (DM)
Freq Bayes Freq Bayes Freq Bayes Freq Bayes
ϵtot Mean 2.5% 97.5% Mean 2.5% 97.5% Mean 2.5% 97.5% Mean 2.5% 97.5% Mean 2.5% 97.5% Mean 2.5% 97.5% Mean 2.5% 97.5% Mean 2.5% 97.5%
0.1 0.006 -0.042 0.054 0.005 0.001 0.008 1.0 −1.0 1 .0 0 .011 −0.178 0 .145 0.651 -1.0 1.0 0.072 -0.135 0.244 1.0 -1.0 1.0 0.032 -0.137 0.193



=== CHUNK 73 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 15, 'page_label': '16', 'start_index': 514}
Length: 762 characters
End of Chunk 73 sentences... :
0.1 0.006 -0.042 0.054 0.005 0.001 0.008 1.0 −1.0 1 .0 0 .011 −0.178 0 .145 0.651 -1.0 1.0 0.072 -0.135 0.244 1.0 -1.0 1.0 0.032 -0.137 0.193
0.3 0.006 -0.042 0.054 0.005 0.001 0.008 -1.0 -1.0 1.0 0.049 -0.082 0.190 0.220 -0.333 0.775 0.160 -0.038 0.389 -0.581 -1.0 1.0 0.049 -0.148 0.238
1.0 0.006 -0.042 0.054 0.005 0.001 0.008 -0.169 -0.898 0.559 0.041 -0.022 0.111 0.069 -0.104 0.243 0.073 -0.018 0.137 0.131 -0.546 0.809 0.054 -0.124 0.169
3.0 0.006 -0.042 0.054 0.005 0.001 0.008 0.008 -0.116 0.131 0.018 -0.007 0.044 0.0265 -0.051 0.104 -0.002 -0.018 0.015 -0.038 -0.248 0.170 0.048 0.004 0.098
10.0 0.006 -0.042 0.054 0.005 0.001 0.008 0.006 −0.051 0 .064 0 .009 0 .0 0 .018 0.011 -0.045 0.068 -0.002 -0.009 0.006 -0.006 -0.066 0.054 0.015 0.002 0.027
16



=== CHUNK 74 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 16, 'page_label': '17', 'start_index': 0}
Length: 789 characters
End of Chunk 74 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
7. Concluding Remarks
In this article we proposed causal inferential methodologies to analyze diﬀerential private data
from randomized experiments under the Rubin Causal Model. We considered three distinct
local privacy scenarios that have practical relevance: 1) jointly privatized variables with
knownp, 2) custom privatized variables with knownp, and 3) custom privatized variables
with unknownp. We showed that a naïve debiased estimator in the ﬁrst scenario results
in poor MSE compared to the minimax lower bound. In contrast, we show that by using
customized privacy mechanisms, we can achieve the lower bound and obtain minimax optimal
inference. We also presented a Bayesian methodology and its sampling algorithm as an



=== CHUNK 75 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 16, 'page_label': '17', 'start_index': 705}
Length: 744 characters
End of Chunk 75 sentences... :
inference. We also presented a Bayesian methodology and its sampling algorithm as an
alternative to the frequentist methodologies. We emphasize that despite the simplicity of
the Laplace and randomized response mechanisms we employ, our customized estimators
attain the minimax lower bound, thereby ensuring optimality across any privacy mechanisms.
Additionally, our analyses can readily be extended to other mechanisms that add independent
noise with a zero mean and known variance. Our Bayesian algorithm works eﬀectively across
a broad spectrum of privacy mechanisms if the privacy mechanism has a known likelihood.
Finally, we validated the performance of our estimators via simulation studies and empirical
analyses using real-world data.



=== CHUNK 76 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 16, 'page_label': '17', 'start_index': 1325}
Length: 732 characters
End of Chunk 76 sentences... :
Finally, we validated the performance of our estimators via simulation studies and empirical
analyses using real-world data.
A direction for future research is to develop an analytical framework for unbounded
variables. Our framework is currently limited to bounded variables due to considerations
of the sensitivity of DP mechanisms, however this can be relaxed by adopting the minimax
privacy mechanism for mean estimation for unbounded functions proposed by Duchi et al.
(2018).
Additionally, the ﬁnite-sample performance of our estimators may be improved by more
carefully designing the noise adding mechanisms; one may investigate using truncated-
uniform-Laplace (Awan and Slavković, 2018),K-norm mechanisms (Hardt and Talwar,



=== CHUNK 77 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 16, 'page_label': '17', 'start_index': 1978}
Length: 790 characters
End of Chunk 77 sentences... :
uniform-Laplace (Awan and Slavković, 2018),K-norm mechanisms (Hardt and Talwar,
2010; Awan and Slavković, 2021), or the minimax optimal noise mechanism for multivariate
mean estimation (Duchi et al., 2018). As mentioned in Section 3.5, the performance of
our frequentist estimators may be improved by incorporating knowledge about the DP
mechanisms (i.e., likelihood of mechanisms and boundedness of variables), as our Bayesian
approach does. We leave these directions for future research.
Finally, in this study, we speciﬁcally focused on experimental settings where the treatment
is randomly assigned to individuals.
Randomized experiments are the gold standard and provide a solid foundation for causal
inference. However, in many cases of interest, performing a randomized experiment is



=== CHUNK 78 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 16, 'page_label': '17', 'start_index': 2684}
Length: 726 characters
End of Chunk 78 sentences... :
inference. However, in many cases of interest, performing a randomized experiment is
impractical or impossible, whether due to feasibility issues or ethical concerns (e.g., it would
be unethical to force people to smoke to study health outcomes). In such situations, it
may be necessary to estimate causal eﬀects based solely on observational data. Estimating
causal eﬀects from observational data introduces signiﬁcantly more challenges compared to
settings where randomized experiments are possible. Speciﬁcally, in observational studies, the
treatment assignment mechanisms are unknown (Imbens and Rubin, 2015), and treatment is
typically assigned based on individuals’ covariates. This induces selection bias in estimating



=== CHUNK 79 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 16, 'page_label': '17', 'start_index': 3316}
Length: 371 characters
End of Chunk 79 sentences... :
typically assigned based on individuals’ covariates. This induces selection bias in estimating
true causal eﬀects, and this bias must be adjusted for valid inference. Various strategies
exist for this adjustment, such as matching, stratiﬁcation, and weighting. However, these
procedures require modeling the assignment mechanisms (i.e., propensity scores) and checking
17



=== CHUNK 80 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 17, 'page_label': '18', 'start_index': 0}
Length: 756 characters
End of Chunk 80 sentences... :
Yuki Ohnishi and Jordan A w an
covariate balances between treatment groups, which is particularly challenging in DP contexts.
Therefore, another future direction for research is to develop methodologies for PATE
estimation that address selection bias in observational studies.
Acknowledgments
This work was supported in part by the National Science Foundation (NSF) grant SES
2150615.
Appendix A. Details of Theorems and Proofs in Section 3
A.1 Conditional independence of{Yi(0),Yi(1)} and ˜Wi given Wi
We ﬁrst state a subtle yet important lemma that we will use to prove subsequent theorems.
Lemma 9 The potential outcomes are conditionally independent of the privatized treatment
assignments given the actual treatment assignment:
{Yi(0),Yi(1)}⊥ ⊥˜Wi|Wi.



=== CHUNK 81 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 17, 'page_label': '18', 'start_index': 682}
Length: 790 characters
End of Chunk 81 sentences... :
assignments given the actual treatment assignment:
{Yi(0),Yi(1)}⊥ ⊥˜Wi|Wi.
This result holds because the DP mechanism ﬂips the given treatment independently. This
result is subtle, but important because it plays a crucial role in proving the upcoming
theorems.
A.2 Proof of Lemma 4
Proof We ﬁrst acknowledge that
sup
P0=δ(0),
P1∈P1,
p=1
E[(ˆτ−τ)2] = sup
P1∈P1
E[(ˆτ−µ1)2], (6)
where δ(0) denotes a point mass at0 and µ1 = E[Yi(1)]. Equation (6) is equivalent to the
one-dimensional mean estimation problem in Duchi et al. (2018, Corollary 1). Therefore, by
Duchi et al. (2018), there exists some constantcl such that
cl min(1, (Nϵ 2)−1)≤ sup
P1∈P1
E[(ˆτ−µ1)2],
Finally, we note that
inf
Mϵ∈Mϵ
inf
ˆτ
sup
P0=δ(0),
P1∈P1,
p=1
E[(ˆτ−τ)2]≤ inf
Mϵ∈Mϵ
inf
ˆτ
sup
P0∈P0,
P1∈P1,
p∈[0,1]
E[(ˆτ−τ)2],



=== CHUNK 82 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 17, 'page_label': '18', 'start_index': 1324}
Length: 283 characters
End of Chunk 82 sentences... :
P1∈P1
E[(ˆτ−µ1)2],
Finally, we note that
inf
Mϵ∈Mϵ
inf
ˆτ
sup
P0=δ(0),
P1∈P1,
p=1
E[(ˆτ−τ)2]≤ inf
Mϵ∈Mϵ
inf
ˆτ
sup
P0∈P0,
P1∈P1,
p∈[0,1]
E[(ˆτ−τ)2],
where the inequality holds as the right side is taking supremum over a larger set. Putting
everything together, we prove our claim.
18



=== CHUNK 83 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 18, 'page_label': '19', 'start_index': 0}
Length: 720 characters
End of Chunk 83 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
A.3 Proof of Lemma 5
Proof Let ¯p = 1−p and ¯qϵw = 1−qϵw. The weak law of large numbers implies
1
N
N∑
i=1
˜Wi ˜Yi p→ E[ ˜Wi ˜Yi] = E[E[ ˜Wi ˜Yi|Wi]] = E[E[ ˜Wi|Wi]E[Yi|Wi]]
= E[P ( ˜Wi = 1|Wi)E[ ˜Yi|Wi]]
= E[P ( ˜Wi = 1|Wi)E[Yi|Wi]]
=p
(
P ( ˜Wi = 1|Wi = 1)E[Yi(1)]) + ¯p(P ( ˜Wi = 1|Wi = 0)E[Yi(0)])
=pqϵwµ1 + ¯p¯qϵwµ0,
where the second line follows from the law of total expectation and the third line follows
from Lemma 9. Similarly, we have1N∑Ni=1(1− ˜Wi) ˜Yi p→p¯qϵwµ1 + ¯pqϵwµ0. Therefore, we see
that ˜τnaive
p
→ 1Cp,ϵwτ, and, sinceCp,ϵw is a constant, we haveCp,ϵw ˜τnaive p→τ.
A.4 Details of Theorem 6
We provide the following central limit theorem.



=== CHUNK 84 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 18, 'page_label': '19', 'start_index': 578}
Length: 709 characters
End of Chunk 84 sentences... :
p
→ 1Cp,ϵwτ, and, sinceCp,ϵw is a constant, we haveCp,ϵw ˜τnaive p→τ.
A.4 Details of Theorem 6
We provide the following central limit theorem.
Theorem 10 The estimator Cp,ϵw ˜τnaive is unbiased and consistent forτ. Furthermore,√
N(Cp,ϵw ˜τnaive−τ) converges in distribution to
N
(
0,C 2p,ϵw
( 1
ρ1
V1 + 1ρ0V0 + ρ0ρ1E21 + ρ1ρ0E20 + 2E0E1
))
, (7)
where, forw = 0, 1,
Vw = Var( ˜Yi| ˜Wi =w) =P (Wi = 0| ˜Wi =w)Var[Yi(0)] +P (Wi = 1| ˜Wi =w)Var[Yi(1)]
+P (Wi = 0| ˜Wi =w)P (Wi = 1| ˜Wi =w)τ 2 + 2ϵ2y,
and Ew = E( ˜Yi| ˜Wi =w) =P (Wi = 0| ˜Wi =w)E[Yi(0)] +P (Wi = 1| ˜Wi =w)E[Yi(1)].
Proof Consistency is proven in Section A.3.
Cp,ϵw ˜τnaive = Cp,ϵw
N
N∑
i=1
{ ˜Wi ˜Yi
ρ1
− (1− ˜Wi) ˜Yi
ρ0
}
= Cp,ϵw
N
N∑
i=1
˜τi.



=== CHUNK 85 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 18, 'page_label': '19', 'start_index': 1158}
Length: 429 characters
End of Chunk 85 sentences... :
Proof Consistency is proven in Section A.3.
Cp,ϵw ˜τnaive = Cp,ϵw
N
N∑
i=1
{ ˜Wi ˜Yi
ρ1
− (1− ˜Wi) ˜Yi
ρ0
}
= Cp,ϵw
N
N∑
i=1
˜τi.
Note that ˜τi is i.i.d. fori = 1,...,N , E[Cp,ϵw ˜τi] =τ, and the second moment is bounded due
to the sensitivity ofY. Thus, it is suﬃcient to derive the variance of˜τi as Var[Cp,ϵw ˜τi] =
C2p,ϵw Var[˜τi].
Var[˜τi] = 1ρ21 Var[ ˜Wi ˜Yi] + 1ρ20 Var[(1− ˜Wi) ˜Yi]− 2ρ0ρ1 Cov[ ˜Wi ˜Yi, (1− ˜Wi) ˜Yi].
19



=== CHUNK 86 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 19, 'page_label': '20', 'start_index': 0}
Length: 760 characters
End of Chunk 86 sentences... :
Yuki Ohnishi and Jordan A w an
Then,
Var[ ˜Wi ˜Yi] = E[Var[ ˜Wi ˜Yi| ˜Wi]] + Var[E[ ˜Wi ˜Yi| ˜Wi]]
= E[ ˜W 2i Var[ ˜Yi| ˜Wi]] + Var[ ˜WiE[ ˜Yi| ˜Wi]]
=p( ˜Wi = 1)Var[ ˜Yi| ˜Wi] +p( ˜Wi = 1)p( ˜Wi = 0)E[ ˜Yi| ˜Wi]2
=ρ1Var[ ˜Yi| ˜Wi] +ρ0ρ1E[ ˜Yi| ˜Wi]2
=ρ1V1 +ρ0ρ1E21.
Similarly, we haveVar[(1− ˜Wi) ˜Yi] =ρ0V0 +ρ0ρ1E20. The covariance is given by
Cov[ ˜Wi ˜Yi, (1− ˜Wi) ˜Yi] =−E[ ˜Wi ˜Yi]E[(1− ˜Wi) ˜Yi]
=−E[ ˜WiE[ ˜Yi| ˜Wi]]E[(1− ˜Wi)E[ ˜Yi| ˜Wi]]
=−p( ˜Wi = 1)E[ ˜Yi| ˜Wi = 1]p( ˜Wi = 0)E[ ˜Yi| ˜Wi = 0]
=−ρ0ρ1E0E1.
Putting all together, we prove the central limit theorem in Theorem 10 and hence Theorem
6.
Next, we consider the decompositions ofEw and Vw. We have
Ew = E[ ˆYi| ˆWi =w]
= E[Yi| ˆWi =w]
=P (Wi = 0| ˜Wi =w)E[Yi(0)] +P (Wi = 1| ˜Wi =w)E[Yi(1)],



=== CHUNK 87 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 19, 'page_label': '20', 'start_index': 667}
Length: 660 characters
End of Chunk 87 sentences... :
Ew = E[ ˆYi| ˆWi =w]
= E[Yi| ˆWi =w]
=P (Wi = 0| ˜Wi =w)E[Yi(0)] +P (Wi = 1| ˜Wi =w)E[Yi(1)],
which follows from Lemma 9. By the law of total variance and SUTVA,
Var[Yi| ˜Wi = 1]
=
1∑
w=0
Var[Yi| ˜Wi = 1,Wi =w]P (Wi =w| ˜Wi = 1) + Var[E[Yi| ˜Wi = 1,Wi =w]].
The ﬁrst term simpliﬁes to
1∑
w=0
Var[Yi| ˜Wi = 1,Wi =w]P (Wi =w| ˜Wi = 1)
= ¯p¯qϵw
pqϵw + ¯p¯qϵw
Var[Yi(0)] + pqϵw
pqϵw + ¯p¯qϵw
Var[Yi(1)].
The second term simpliﬁes to
Var[E[Yi| ˜Wi = 1,Wi =w]]
= E
[
(E[Yi| ˜Wi = 1,Wi =w]− E[(E[Yi| ˜Wi = 1,Wi =w]])2| ˜Wi = 1]
=
1∑
w=0
(
E[Yi(w)]− ¯p¯qϵw
pqϵw + ¯p¯qϵw
E[Yi(0)]− pqϵw
pqϵw + ¯p¯qϵw
E[Yi(1)]
)2
P (Wi =w| ˜Wi = 1)
= pqϵw ¯p¯qϵw
(pqϵw + ¯p¯qϵw)2τ 2.
20



=== CHUNK 88 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 20, 'page_label': '21', 'start_index': 0}
Length: 787 characters
End of Chunk 88 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
Therefore, we have
V1 := Var[Yi| ˜Wi = 1] = ¯p¯qϵw
pqϵw + ¯p¯qϵw
Var[Yi(0)] + pqϵw
pqϵw + ¯p¯qϵw
Var[Yi(1)] + pqϵw ¯p¯qϵw
(pqϵw + ¯p¯qϵw)2τ 2.
Similarly, we have
V0 := Var[Yi| ˜Wi = 0] = ¯pqϵw
¯pqϵw +p¯qϵw
Var[Yi(0)] + p¯qϵw
¯pqϵw +p¯qϵw
Var[Yi(1)] + pqϵw ¯p¯qϵw
(¯pqϵw +p¯qϵw)2τ 2.
Finally, the order of the asymptotic variance is immediate from the fact thatC2p,ϵw =
O((ϵ2w)−1), which proves Theorem 6 and Corollary 12
We now turn to estimating the asymptotic variance ofCp,ϵw ˜τnaive in (7). We consider the
followingestimatorsfor Ew andVw: ˆEw = 1˜Nw∑i: ˜Wi=w ˜Yi and ˆVw = 1˜Nw−1∑i: ˜Wi=w( ˜Yi− ˆEw)2,
where ˜Nw =∑Ni=1 1 ( ˜Wi =w) for w = 0, 1.
Lemma 11 ˆVw and ˆEw are consistent forVw and Ew respectively. Also, we have



=== CHUNK 89 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 20, 'page_label': '21', 'start_index': 668}
Length: 729 characters
End of Chunk 89 sentences... :
where ˜Nw =∑Ni=1 1 ( ˜Wi =w) for w = 0, 1.
Lemma 11 ˆVw and ˆEw are consistent forVw and Ew respectively. Also, we have
E[ ˆEw| ˜Wi =w] =Ew and E[ ˆVw| ˜Wi =w] =Vw
Proof
ˆV1 = 1˜N1− 1 ∑i: ˜Wi=1( ˜Yi− ˆE1)2
= 1˜N1− 1 ∑i: ˜Wi=1( ˜Yi− E[ ˜Yi| ˜Wi = 1] + E[ ˜Yi| ˜Wi = 1]− ˆE1)2
= 1˜N1− 1 ∑i: ˜Wi=1{( ˜Yi− E[ ˜Yi| ˜Wi = 1])2 + (E[ ˜Yi| ˜Wi = 1]− ˆE1)2
− 2( ˜Yi− E[ ˜Yi| ˜Wi = 1])(E[ ˜Yi| ˜Wi = 1]− ˆE1)
}
=
˜N1
˜N1− 1
1
˜N1
∑
i: ˜Wi=1
( ˜Yi− E[ ˜Yi| ˜Wi = 1])2− ˜N1˜N1− 1( ˆE1− E[ ˜Yi| ˜Wi = 1])2.
Therefore,
E[ ˆV1| ˜Wi = 1] = ˜N1˜N1− 1 Var[ ˜Yi| ˜Wi = 1]− ˜N1˜N1− 1 Var[ ˆE1| ˜Wi = 1]
=
˜N1
˜N1− 1 Var[ ˜Yi| ˜Wi = 1]− 1˜N1− 1 Var[ ˜Yi| ˜Wi = 1]
= Var[ ˜Yi| ˜Wi = 1] =V1.
We can follow the same procedure forE[ ˆV0| ˜Wi = 0] =V0.
21



=== CHUNK 90 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 21, 'page_label': '22', 'start_index': 0}
Length: 739 characters
End of Chunk 90 sentences... :
Yuki Ohnishi and Jordan A w an
Using ˆEw and ˆVw, we can construct the plug-in estimator for the asymptotic variance
and the nominal central conﬁdence interval at the signiﬁcance levelα as:
(
Cp,ϵw ˜τnaive−zα2
√
ˆΣnaive
N ,Cp,ϵw ˜τnaive +zα2
√
ˆΣnaive
N
)
.
where ˆΣnaive =C2p,ϵw( 1ρ1 ˆV1 + 1ρ0 ˆV0 + ρ0ρ1 ˆE21 + ρ1ρ0 ˆE20 + 2 ˆE0 ˆE1), which is a consistent estimatorfor the asymptotic variance in (7).
Finally, we discuss the optimality of the naïve estimator.
Corollary 12 (Convergence rate)The naïve estimator under the joint scenario has the
MSE O((Nϵ 2yϵ2w)−1).
Settingϵy =ϵ2 =ϵ/2 givesO((Nϵ 4)−1). While we do not match the minimax lower bound of
mean estimation in terms ofϵ when bothW and Y are privatized, it should be emphasized



=== CHUNK 91 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 21, 'page_label': '22', 'start_index': 654}
Length: 787 characters
End of Chunk 91 sentences... :
mean estimation in terms ofϵ when bothW and Y are privatized, it should be emphasized
that the estimation of PATE is signiﬁcantly harder than the usual mean estimation when we
do not know who belongs to which treatment group, especially using a non-interactive LDP
mechanism as in the joint scenario.
A.5 Details of Theorem 7
By the standard central limit theorem, we have
√
N(˜τIPW −τ) D→ N
(
0,µ21 +σ21
p + µ20 +σ201−p −τ 2−µ0µ1 + 2∆Aϵ2a ), (8)
where µw = E[Yi(w)] and σ2w = Var[Yi(w)] for w = 0, 1. We can then construct the plug-in
estimator for the asymptotic variance and the nominal central conﬁdence interval at the
signiﬁcance levelα as:
(
˜τIPW −zα2
√
ˆΣIPW
N , ˜τIPW +zα2
√
ˆΣIPW
N
)
.
where ˆΣIPW = 1N−1∑Ni=1( ˜Ai− ˆEA)2 with ˆEA = 1N∑Ni=1 ˜Ai, which is an unbiased estimator



=== CHUNK 92 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 21, 'page_label': '22', 'start_index': 1301}
Length: 443 characters
End of Chunk 92 sentences... :
(
˜τIPW −zα2
√
ˆΣIPW
N , ˜τIPW +zα2
√
ˆΣIPW
N
)
.
where ˆΣIPW = 1N−1∑Ni=1( ˜Ai− ˆEA)2 with ˆEA = 1N∑Ni=1 ˜Ai, which is an unbiased estimator
for the asymptotic variance in (8).
A.6 Details of Theorem 8
First, we provide the following asymptotic results regarding this estimator.
Theorem 13 ˜τDM is consistent forτ and
√
N(˜τDM−τ) converges in distribution to
N
(
0, 4µ0µ1 + σ201−p + σ21p + 2ϵ2b1( µ01−p + µ1p)2 + 2p2ϵ2b2 + 2(1−p)2ϵ2b3). (9)
22



=== CHUNK 93 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 22, 'page_label': '23', 'start_index': 0}
Length: 766 characters
End of Chunk 93 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
Proof First, we have E[ ˜Bi,1] = pµ1, E[ ˜Bi,2] = (1 −p)µ0, E[ ˜Bi,3] = p, E[ ˜Bi,4] = 1 −p,
Var[ ˜Bi,1] =pσ21 +p(1−p)µ21 + 2ϵ2b1, Var[ ˜Bi,2] = (1−p)σ20 +p(1−p)µ20 + 2ϵ2b2, Var[ ˜Bi,3] =p(1−
p)+ 2ϵ2b3, Var[ ˜Bi,4] =p(1−p)+ 2ϵ2b3, Cov[ ˜Bi,1, ˜Bi,2] =−p(1−p)µ0µ1, Cov[ ˜Bi,1, ˜Bi,3] =p(1−p)µ1,
Cov[ ˜Bi,1, ˜Bi,4] = 0, Cov[ ˜Bi,2, ˜Bi,3] = 0, Cov[ ˜Bi,2, ˜Bi,4] = p(1−p)µ0, and Cov[ ˜Bi,3, ˜Bi,4] =
−p(1−p)µ0µ1. By the central limit theorem, we have
√
N


1
N
∑N
i=1 ˜Bi,1− E[ ˜Bi,1]
1
N
∑N
i=1 ˜Bi,2− E[ ˜Bi,2]
1
N
∑N
i=1 ˜Bi,3− E[ ˜Bi,3]
1
N
∑N
i=1 ˜Bi,4− E[ ˜Bi,4]

 D→ N




0
0
0
0

,S∗

,
where
S∗ =


Var[ ˜Bi,1] Cov[ ˜Bi,1, ˜Bi,2] Cov[ ˜Bi,1, ˜Bi,3] Cov[ ˜Bi,1, ˜Bi,4]



=== CHUNK 94 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 22, 'page_label': '23', 'start_index': 633}
Length: 775 characters
End of Chunk 94 sentences... :

 D→ N




0
0
0
0

,S∗

,
where
S∗ =


Var[ ˜Bi,1] Cov[ ˜Bi,1, ˜Bi,2] Cov[ ˜Bi,1, ˜Bi,3] Cov[ ˜Bi,1, ˜Bi,4]
Cov[ ˜Bi,2, ˜Bi,1] Var[ ˜Bi,2] Cov[ ˜Bi,2, ˜Bi,3] Cov[ ˜Bi,2, ˜Bi,4]
Cov[ ˜Bi,3, ˜Bi,1] Cov[ ˜Bi,3, ˜Bi,2] Var[ ˜Bi,3] Cov[ ˜Bi,3, ˜Bi,4]
Cov[ ˜Bi,4, ˜Bi,1] Cov[ ˜Bi,4, ˜Bi,2] Cov[ ˜Bi,4, ˜Bi,3] Var[ ˜Bi,4]

.
Deﬁne a functionh(a,b,c,d ) = ac− bd and∇h = (∂h∂a, ∂h∂b, ∂h∂c, ∂h∂d ), where
∂h
∂a = 1c,∂h∂b =−1d,∂h∂c =−ac2,∂h∂d = bd2.
Note that
τ =µ1−µ0 = E[ ˜Bi,1]E[ ˜Bi,3]− E[ ˜Bi,2]E[ ˜Bi,4] =h(E[ ˜Bi,1], E[ ˜Bi,2], E[ ˜Bi,3], E[ ˜Bi,4]),
and
˜τDM =
∑N
i=1 ˜Bi,1∑N
i=1 ˜Bi,3
−
∑N
i=1 ˜Bi,2∑N
i=1 ˜Bi,4
=h
(
1
N
N∑
i=1
˜Bi,1, 1N N∑i=1 ˜Bi,2, 1N N∑i=1 ˜Bi,3, 1N N∑i=1 ˜Bi,4).
By applying the delta method, we have
√
N(˜τDM−τ) D→ N(0, Σ∗),



=== CHUNK 95 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 22, 'page_label': '23', 'start_index': 1264}
Length: 595 characters
End of Chunk 95 sentences... :
i=1 ˜Bi,4
=h
(
1
N
N∑
i=1
˜Bi,1, 1N N∑i=1 ˜Bi,2, 1N N∑i=1 ˜Bi,3, 1N N∑i=1 ˜Bi,4).
By applying the delta method, we have
√
N(˜τDM−τ) D→ N(0, Σ∗),
where Σ∗ =∇h(E)′S∗∇h(E).∇h(E) denotes the gradient∇h evaluated at
E = (E[ ˜Bi,1], E[ ˜Bi,2, E[ ˜Bi,3], E[ ˜Bi,4]). Calculating Σ∗ proves our claim in Thereom 13. The
estimator ofΣ∗ that we adopt in Section 3.4 are a plug-in estimator with consistent estimators
of∇h(E) and S∗.
By Theorem 13, the asymptotic variance of˜τDM has the convergence rateO((N(ϵ2b1 +
ϵ2b2 +ϵ2b3))−1). Setting ϵb1 = ϵb2 = ϵb3 = ϵ/3 gives O((Nϵ 2)−1), which also matches the
23



=== CHUNK 96 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 23, 'page_label': '24', 'start_index': 0}
Length: 794 characters
End of Chunk 96 sentences... :
Yuki Ohnishi and Jordan A w an
minimax lower bound for the locally private mean estimation, indicating the optimality of
the estimator.
Let ˆEBj = 1N∑Ni=1 ˜Bi,j, ˆVBj = 1N−1∑Ni=1( ˜Bi,j− ˆEBj)2 for j = 1, 2, 3, 4 and ˆCovj,k =
1
N−1
∑N
i=1( ˜Bi,j− ˆEBj)( ˜Bi,k− ˆEBk) for j⁄=k. Then, we construct the plug-in estimator for
the asymptotic variance and the nominal central conﬁdence interval at the signiﬁcance level
α as:
(
˜τDM−zα2
√
ˆΣDM
N , ˜τDM +zα2
√
ˆΣDM
N
)
.
where ˆΣDM = ˆe′ˆSˆe, with ˆe = (1/ ˆEB3,−1/(1− ˆEB3),− ˆEB1/ ˆE2B3, ˆEB2/(1− ˆEB3)2)′ and
ˆS =


ˆVB1 ˆCov1,2 ˆCov1,3 ˆCov1,4
ˆCov2,1 ˆVB2 ˆCov2,3 ˆCov2,4
ˆCov3,1 ˆCov3,2 ˆVB3 ˆCov3,4
ˆCov4,1 ˆCov4,2 ˆCov4,3 ˆVB4

.
This is a consistent estimator for the asymptotic variance in (9).
Appendix B. Clamping Bias Analysis



=== CHUNK 97 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 23, 'page_label': '24', 'start_index': 656}
Length: 731 characters
End of Chunk 97 sentences... :
ˆCov4,1 ˆCov4,2 ˆCov4,3 ˆVB4

.
This is a consistent estimator for the asymptotic variance in (9).
Appendix B. Clamping Bias Analysis
In this section, we provide an analysis of the bias introduced by the clamping process for
the frequentist estimator in the joint scenario and the custom scenario with a knownp. The
custom scenario with an unknownp does not guarantee the bias in ﬁnite samples, so we do
not consider it, but the same analysis can be applied.
Let ˜τ and ˜τ∗ denote a generic unbiased estimator in each scenario and the clamped
estimator of ˜τ, respectively, that is:
˜τ∗ =



˜τ if − 1≤ ˜τ≤ 1
1 if ˜τ >1,
−1 if ˜τ <−1,
Under the joint scenario and the custom scenario with a knownp, we have already proved



=== CHUNK 98 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 23, 'page_label': '24', 'start_index': 1244}
Length: 775 characters
End of Chunk 98 sentences... :
˜τ∗ =



˜τ if − 1≤ ˜τ≤ 1
1 if ˜τ >1,
−1 if ˜τ <−1,
Under the joint scenario and the custom scenario with a knownp, we have already proved
the unbiasedness of˜τ: E[˜τ] =τ. Therefore, the bias of the clamped estimator is expressed
as:
E[˜τ∗]−τ = E[˜τ]P (−1≤ ˜τ≤ 1) +P (1< ˜τ)−P (˜τ <−1)−τ
=τP (−1≤ ˜τ≤ 1) +P (1< ˜τ)−P (˜τ <−1)−τ (10)
The exact distribution of˜τ is challenging to compute because the distribution of the
outcome Y is unknown. However, given our private estimators are the sample average of
independent samples, it is reasonable to apply the normal approximation to the estimator. By
Theorem 6 in the joint scenario, the unbiased estimator˜τ =Cp,ϵw· ˜τnaive can be approximated
by:
N
(
τ, C2p,ϵw
N
( 1
ρ1
V1 + 1ρ0V0 + ρ0ρ1E21 + ρ1ρ0E20 + 2E0E1
))
. (11)
24



=== CHUNK 99 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 24, 'page_label': '25', 'start_index': 0}
Length: 800 characters
End of Chunk 99 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
Therefore,
P (−1≤ ˜τ≤ 1) = Φ

 1−τ√C2p,ϵw
N
(
1
ρ1V1 + 1ρ0V0 + ρ0ρ1E21 + ρ1ρ0E20 + 2E0E1
)


− Φ

 −1−τ√C2p,ϵw
N
(
1
ρ1V1 + 1ρ0V0 + ρ0ρ1E21 + ρ1ρ0E20 + 2E0E1
)

,
P (1< ˜τ) = 1− Φ

 1−τ√C2p,ϵw
N
(
1
ρ1V1 + 1ρ0V0 + ρ0ρ1E21 + ρ1ρ0E20 + 2E0E1
)

,
P (˜τ <−1) = Φ

 −1−τ√C2p,ϵw
N
(
1
ρ1V1 + 1ρ0V0 + ρ0ρ1E21 + ρ1ρ0E20 + 2E0E1
)


Plugging in these probabilities for(10), we obtain the bias of the clamped estimator under
the joint scenario.
Similarly, for the custom scenario with a knownp, we have the unbiased estimator
˜τ = ˜τIPW , which can be approximated by:
N
(
τ,
ˆΣIPW
N
)
.
Therefore,
P (−1≤ ˜τ≤ 1) = Φ

 1−τ√
ˆΣIPW
N

− Φ

−1−τ√
ˆΣIPW
N

,
P (1< ˜τ) = 1− Φ

 1−τ√
ˆΣIPW
N

,
P (˜τ <−1) = Φ



=== CHUNK 100 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 24, 'page_label': '25', 'start_index': 653}
Length: 531 characters
End of Chunk 100 sentences... :
N
(
τ,
ˆΣIPW
N
)
.
Therefore,
P (−1≤ ˜τ≤ 1) = Φ

 1−τ√
ˆΣIPW
N

− Φ

−1−τ√
ˆΣIPW
N

,
P (1< ˜τ) = 1− Φ

 1−τ√
ˆΣIPW
N

,
P (˜τ <−1) = Φ

−1−τ√
ˆΣIPW
N

.
Plugging in these probabilities for(10), we obtain the bias of the clamped estimator under
the custom scenario with a knownp.
Appendix C. Randomized Response Mechanism for Binary Outcome
In this study, we are focusing on a continuous outcomeY ∈ [0, 1], rather than a binary
one. We chose the Laplace mechanism for its privacy mechanism because it can be used
25



=== CHUNK 101 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 25, 'page_label': '26', 'start_index': 0}
Length: 799 characters
End of Chunk 101 sentences... :
Yuki Ohnishi and Jordan A w an
for both continuous and binary outcomes, oﬀering a more general solution for our analysis.
Although we acknowledge that the Laplace mechanism has an unbounded domain—which can
introduce bias if we apply clamping post-process—we believe that its versatility outweighs
this limitation in our context. However, it indeed might be of practical interest to use the
Randomized Response mechanism when the outcome is binary in the joint scenario. In this
section, we provide another bias correction technique under the joint scenario with a binary
outcome Yi∈{ 0, 1} in which both treatment variables and outcomes are privatized by the
Randomized Response mechanism. We let
˜Yi =
{
Yi w.p. rϵy
1−Yi w.p. 1−rϵy,
where rϵy = exp(ϵy)1+exp(ϵy). Then, the following lemma follows.



=== CHUNK 102 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 25, 'page_label': '26', 'start_index': 660}
Length: 762 characters
End of Chunk 102 sentences... :
Randomized Response mechanism. We let
˜Yi =
{
Yi w.p. rϵy
1−Yi w.p. 1−rϵy,
where rϵy = exp(ϵy)1+exp(ϵy). Then, the following lemma follows.
Lemma 14Kp,ϵw,ϵy· ˜τnaive is an unbiased and consistent estimator forτ, whereKp,ϵw,ϵy =ρ0ρ1
p(1−p)(2qϵw−1)(2rϵy−1). The following interval is the nominal central conﬁdence interval at the
signiﬁcance levelα:

Kp,ϵw,ϵy· ˜τnaive−zα2
√
ˆΣnaive
N ,Kp,ϵw,ϵy· ˜τnaive +zα2
√
ˆΣnaive
N

,
where ˆΣnaive =K2p,ϵw,ϵy( 1ρ1 ˆV1 + 1ρ0 ˆV0 + ρ0ρ1 ˆE21 + ρ1ρ0 ˆE20 + 2 ˆE0 ˆE1).
Proof Note that
E[ ˜Wi ˜Yi] = E[E[ ˜Wi ˜Yi|Wi]]
= E[E[ ˜Wi|Wi]E[ ˜Yi|Wi]]
= E[P ( ˜Wi = 1|Wi)P ( ˜Yi = 1|Wi)]
=pE[qϵwP ( ˜Yi = 1|Wi = 1)] + (1−p)E[(1−qϵw)P ( ˜Yi = 1|Wi = 0)].
We also have:
P ( ˜Yi = 1|Wi = 1)
=P ( ˜Yi = 1|Yi = 1,Wi = 1)P (Yi = 1|Wi = 1)



=== CHUNK 103 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 25, 'page_label': '26', 'start_index': 1278}
Length: 374 characters
End of Chunk 103 sentences... :
=pE[qϵwP ( ˜Yi = 1|Wi = 1)] + (1−p)E[(1−qϵw)P ( ˜Yi = 1|Wi = 0)].
We also have:
P ( ˜Yi = 1|Wi = 1)
=P ( ˜Yi = 1|Yi = 1,Wi = 1)P (Yi = 1|Wi = 1)
+P ( ˜Yi = 1|Yi = 0,Wi = 1)P (Yi = 0|Wi = 1)
=rϵyµ1 + (1−rϵy)(1−µ1).
Similarly, we have
P ( ˜Yi = 1|Wi = 0) =rϵyµ0 + (1−rϵy)(1−µ0).
Thus, we have:
E[ ˜Wi ˜Yi] =pqϵw{rϵyµ1 + (1−rϵy)(1−µ1)} + (1−p)(1−qϵw){rϵyµ0 + (1−rϵy)(1−µ0)}.
26



=== CHUNK 104 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 26, 'page_label': '27', 'start_index': 0}
Length: 784 characters
End of Chunk 104 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
Similarly, we have:
E[(1− ˜Wi) ˜Yi] =p(1−qϵw){rϵyµ1 + (1−rϵy)(1−µ1)} + (1−p)qϵw{rϵyµ0 + (1−rϵy)(1−µ0)}.
We can then show thatKp,ϵw,ϵy· ˜τnaive is an unbiased estimator forτ, and, by the weak law
of large number, it is also a consistent estimator forτ.
The variance in the conﬁdence interval can be obtained following the same procedures in
the proof of Theorem 6.
This lemma also implies that the MSE ofKp,ϵw,ϵy· ˜τnaive is alsoO((Nϵ 2yϵ2w)−1), which is the
same convergence rate in Theorem 6.
Appendix D. Bayesian Methodology
D.1 Details of the DPM
We say the probability measureH is generated from a Dirichlet Process, DP(α,H 0), with a
concentration parameterα> 0 and a base probability measureH0 over a measurable space



=== CHUNK 105 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 26, 'page_label': '27', 'start_index': 700}
Length: 796 characters
End of Chunk 105 sentences... :
concentration parameterα> 0 and a base probability measureH0 over a measurable space
(Θ,S) (Ferguson, 1974) if, for any ﬁnite partition(S1,...,S k) ofS, we have
(
H(S1),...,H (Sk)
)
∼ Dir
(
αH0(S1),...,αH 0(Sk)
)
,
where Dir(α1,...,α k) denotes the Dirichlet distribution with positive parametersα1,...,α k.
The DPM is speciﬁed as
{Y1(0),Y 1(1)},...,{YN(0),YN(1)}| Φ1,..., ΦN ind∼ p(Yi(0),Yi(1)|Φi),
Φ1,..., ΦN|Hind∼ H,
Hind∼ DP (α,H 0).
We writeind∼ to sayindependently distributed. This model has unit-level parametersΦi for
i = 1,...,N , but the discreteness of the Dirichlet process (DP) distributed prior implies that
the vectorΦ = (Φ1,..., ΦN) can be rewritten in terms of its unique valuesΦ∗ = (Φ∗1,..., Φ∗K).
In particular, this can be represented in the following stick-breaking process.



=== CHUNK 106 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 26, 'page_label': '27', 'start_index': 1417}
Length: 666 characters
End of Chunk 106 sentences... :
In particular, this can be represented in the following stick-breaking process.
H =
∞∑
k=1
ukδΦk, uk =vk
∏
l<k
[1−vl], vlind∼ Beta(1,α ).
More speciﬁcally, the outcome model is speciﬁed by the following model.
P (Yi(w)|µ, Σ)∝
∞∑
k=1
ukTN(µkw, Σkw, 0, 1), (12)
where TN(µ,σ 2,u,l ) denotes the truncated normal distribution with the mean, variance,
upper bound and lower bound parameters. The atomsΦk = (µk0,µk1, Σk0, Σk1) and the weight
parameters uk are nonparametrically speciﬁed via DP(α,H 0). This can be regarded as the
inﬁnite mixture of normal distributions, whereµkw and Σkw is the location parameter and
variance parameter of each component respectively.
27



=== CHUNK 107 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 27, 'page_label': '28', 'start_index': 0}
Length: 784 characters
End of Chunk 107 sentences... :
Yuki Ohnishi and Jordan A w an
For inference, we adopt an approximated blocked Gibbs sampler based on a truncation of
the stick-breaking representation of the DP proposed by Ishwaran and Zarepour (2000), due
to its simplicity. In this algorithm, we ﬁrst set a conservatively large upper bound,K≤∞ ,
on the number of components that units potentially belong to. LetCi∈{ 1,...,K} denote the
latent class indicators with a multinomial distribution,Ci∼MN (w) where u = (u1,...,u K)
denote the weights of all components of the DPM. Conditional onCi =k, (12) is greatly
simpliﬁed to
P (Yi(w)|µ, Σ)∝ TN(µkw, Σkw, 0, 1).
Ishwaran and James (2001) showed that an accurate approximation to the exact DP is
obtained as long asK is chosen suﬃciently large. The DPM provides an automatic selection



=== CHUNK 108 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 27, 'page_label': '28', 'start_index': 696}
Length: 757 characters
End of Chunk 108 sentences... :
obtained as long asK is chosen suﬃciently large. The DPM provides an automatic selection
mechanism for the number of active componentsK∗<K . To ensure thatK is suﬃciently
large, we run several MCMC iterations with diﬀerent values ofK. If the current iteration
occupies all components, thenK is not large enough, so we increaseK for the next iteration.
We conduct this iterative process until the number of the occupied components is belowK.
D.2 Detailed Steps of Gibbs Sampler
In this section we present the detailed steps of the Gibbs sampler that is described in Section
4.2. The algorithm is inspired by Schwartz et al. (2011) and Ohnishi and Sabbaghi (2022b).
1. GivenYi(0),Yi(1), draw eachWi from
P (Wi = 1|−) = r1r0 +r1,
where, for uniti with ˜Wi = 0,



=== CHUNK 109 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 27, 'page_label': '28', 'start_index': 1360}
Length: 767 characters
End of Chunk 109 sentences... :
1. GivenYi(0),Yi(1), draw eachWi from
P (Wi = 1|−) = r1r0 +r1,
where, for uniti with ˜Wi = 0,
r0 = Lap( ˜Yi| Yi(0), 1/ϵy)qϵw(1−p) and r1 = Lap( ˜Yi| Yi(1), 1/ϵy)(1−qϵw)p,
and for uniti with ˜Wi = 1,
r0 = Lap( ˜Yi| Yi(0), 1/ϵy)(1−qϵw)(1−p) and r1 = Lap( ˜Yi| Yi(1), 1/ϵy)qϵwp.
where Lap(y|µ,σ ) is the pdf of the laplace distribution evaluated aty with the location
parameter µ and scale parameterσ.
2. Given µ, Σ, u, Ci and Wi =w, drawYi(1−w) according to:
Yi(1−w)∼ TN(µCi1−w, ΣCi1−w, 0, 1),
where TN(µ,σ 2,u,l ) denotes the truncated normal distribution with the mean, variance,
upper bound and lower bound parameters.
Then, drawYi(w) using the following Privacy-Aware Metropolis-within-Gibbs sampler
Ju et al. (2022):
(a) Draw a proposal:y∗∼ TN(µCiw , ΣCiw , 0, 1).



=== CHUNK 110 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 27, 'page_label': '28', 'start_index': 1980}
Length: 448 characters
End of Chunk 110 sentences... :
Then, drawYi(w) using the following Privacy-Aware Metropolis-within-Gibbs sampler
Ju et al. (2022):
(a) Draw a proposal:y∗∼ TN(µCiw , ΣCiw , 0, 1).
(b) Accept the proposal with probabilityα = min
(
1, Lap(y∗|˜Yi,1/ϵy)Lap(yprev|˜Yi,1/ϵy)),
where yprev is the value ofYi(w) in the previous step.
3. Given µ, Σ, u, Yi(0) and Yi(1), draw eachCi from
P (Ci =k|−)∝ukTN(Yi(0)|µk0, Σk0, 0, 1)TN(Yi(1)|µk1, Σk1, 0, 1).
This is a multinomial distribution.
28



=== CHUNK 111 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 28, 'page_label': '29', 'start_index': 0}
Length: 763 characters
End of Chunk 111 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
4. Let u′K = 1. Givenα, C, drawu′k for k∈{ 1,...,K − 1} from
P (u′k|−)∝ Beta
(
1 +
∑
i:Ci=k
1,α +
∑
i:Ci>k
1
)
.
Then, updateuk =u′k∏j<k(1−u′j).
5. Given C and u′, drawα from
P (α|−)∝P (α)
K∏
k=1
f
(
u′k
⏐⏐⏐⏐1 + ∑
i:Ci=k
1,α +
∑
i:Ci>k
1
)
,
where f is the pdf ofu′k, the beta distribution. The Metropolis-Hastings algorithm is
used for this step with a proposal distributionTN(αprev, 1.0, 0,∞). αprev is the value
of α in the previous step.
6. Given Y(0), Y(1) and C, draw µ and Σ from
(a) If Nk =∑Ni=1 1 (Ci =k)> 0, draw Σkw from IG(2 + 0.5Nk, 0.22 + 0.5skw) where
skw =∑i:Ci=k(Yi(w)−µkw)2 for w = 0, 1. IfNk = 0,then draw Σkw from the prior
IG(2, 0.22).
(b) IfNk > 0, drawµkw from TN
(
0.5∗Σkw+9.0sw



=== CHUNK 112 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 28, 'page_label': '29', 'start_index': 628}
Length: 771 characters
End of Chunk 112 sentences... :
skw =∑i:Ci=k(Yi(w)−µkw)2 for w = 0, 1. IfNk = 0,then draw Σkw from the prior
IG(2, 0.22).
(b) IfNk > 0, drawµkw from TN
(
0.5∗Σkw+9.0sw
Σkw+9.0Nk , 9.0ΣkwΣkw+9.0Nk, 0, 1),wheresw =∑Ni=1Yi(w).
If Nk = 0, drawµkw from TN(0.5, 9.0, 0, 1). We use a common choice of the base
measure H0: the Normal-Inverse-Gamma conjugateN(µ0,σ 20)N(µ0,σ 20)IG(a0,b 0)
IG(a0,b 0). The speciﬁc values of the hyperparameters in this step are:µ0 = 0.5,
σ0 = 3.0, a0 = 2.0 and b0 = 0.22 for bothw = 0, 1.
D.3 Modiﬁcations for Custom Scenario in Section 3.3
We need to modify Step 1 and 2 for the custom scenarios. Particularly,
1. Given Yi(0),Yi(1), draw eachWi from P (Wi = 1|−) = r1r0+r1, where rw = P ( ˜Ai|
Yi(0),Yi(1),Wi =w)P (Wi =w) for w = 0, 1. Speciﬁcally, since ˜Ai is generated by pri-



=== CHUNK 113 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 28, 'page_label': '29', 'start_index': 1314}
Length: 741 characters
End of Chunk 113 sentences... :
Yi(0),Yi(1),Wi =w)P (Wi =w) for w = 0, 1. Speciﬁcally, since ˜Ai is generated by pri-
vatizing either−Yi(0)/(1−p) orYi(1)/p given the value ofWi,P ( ˜Ai|Yi(0),Yi(1),Wi =
w) = Lap( ˜Ai|−Yi(0)/(1−p), ∆a/ϵa) for Wi = 0, andP ( ˜Ai|Yi(0),Yi(1),Wi =w) =
Lap( ˜Ai|Yi(1)/p, ∆a/ϵa) for Wi = 1.
2. Given µ, Σ, u, Ci and Wi, draw eachYi(0) and Yi(1) according to:
P (Yi(Wi)|−)∝P (Yi(Wi)|µCiWi, ΣCiWi)P ( ˜Ai|Yi(Wi))
P (Yi(1−Wi)|−)∝P (Yi(1−Wi)|µCi1−Wi, ΣCi1−Wi).
Speciﬁcally, P ( ˜Ai | Yi(Wi)) = Lap( ˜Ai | −Yi(0)/(1− p), ∆a/ϵa) for Wi = 0 and
P ( ˜Ai|Yi(Wi)) = Lap( ˜Ai|Yi(1)/p, ∆a/ϵa) for Wi = 1. The privacy-aware Metropolis-
within-Gibbs algorithm (Ju et al., 2022) is used for the draw ofYi(Wi).
D.4 Modiﬁcations for Custom Scenario in Section 3.4



=== CHUNK 114 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 28, 'page_label': '29', 'start_index': 1932}
Length: 324 characters
End of Chunk 114 sentences... :
within-Gibbs algorithm (Ju et al., 2022) is used for the draw ofYi(Wi).
D.4 Modiﬁcations for Custom Scenario in Section 3.4
Under the custom scenario in Section 3.4, we do not have access top. Therefore, we need an
additional step to inferp. Speciﬁcally, with a prior distributionp∼ Beta(1, 1), we add the
following step.
29



=== CHUNK 115 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 29, 'page_label': '30', 'start_index': 0}
Length: 733 characters
End of Chunk 115 sentences... :
Yuki Ohnishi and Jordan A w an
0. Drawp∼ Beta
(
1 +∑Ni=1 1 (Wi = 1), 1 +∑Ni=1 1 (Wi = 0)).
Then we proceed as follows.
1. GivenYi(0),Yi(1) and p, draw eachWi from P (Wi = 1|−) = r1r0+r1, where
rw =pw(1−p)1−wP ( ˜Bi,1|Yi(0),Yi(1),Wi =w)P ( ˜Bi,2|Yi(0),Yi(1),Wi =w)
×P ( ˜Bi,3|Yi(0),Yi(1),Wi =w)
for w = 0, 1. Speciﬁcally, considering the privatization of ˜Bi,1, ˜Bi,2 and ˜Bi,3, we
haveP ( ˜Bi,1| Yi(0),Yi(1),Wi = 0) = Lap( ˜Bi,1| 0, 1/ϵb2), P ( ˜Bi,2| Yi(0),Yi(1),Wi =
0) = Lap( ˜Bi,2 | Yi(0), 1/ϵb2), P ( ˜Bi,3 | Yi(0),Yi(1),Wi = 0) = Lap( ˜Bi,3 | 0, 1/ϵb3),
P ( ˜Bi,1| Yi(0),Yi(1),Wi = 1) = Lap( ˜Bi,1| Yi(1), 1/ϵb1), P ( ˜Bi,2| Yi(0),Yi(1),Wi =
1) = Lap( ˜Bi,2| 0, 1/ϵb2) and P ( ˜Bi,3|Yi(0),Yi(1),Wi = 1) = Lap( ˜Bi,3| 0, 1/ϵb3).



=== CHUNK 116 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 29, 'page_label': '30', 'start_index': 648}
Length: 781 characters
End of Chunk 116 sentences... :
1) = Lap( ˜Bi,2| 0, 1/ϵb2) and P ( ˜Bi,3|Yi(0),Yi(1),Wi = 1) = Lap( ˜Bi,3| 0, 1/ϵb3).
2. Given µ, Σ, u, Ci and Wi, draw eachYi(0) and Yi(1) according to:
P (Yi(Wi)|−)∝P (Yi(Wi)|µCiWi, ΣCiWi)P ( ˜Bi|Yi(Wi))
P (Yi(1−Wi)|−)∝P (Yi(1−Wi)|µCi1−Wi, ΣCi1−Wi).
Speciﬁcally, P ( ˜Bi| Yi(Wi)) = P ( ˜Bi,2| Yi(0)) = Lap( ˜Bi,2| Yi(0), 1/ϵb2) for Wi = 0
and P ( ˜Bi| Yi(Wi)) = P ( ˜Bi,1| Yi(1)) = Lap( ˜Bi,1| Yi(1), 1/ϵb1) for Wi = 1. The
privacy-aware Metropolis-within-Gibbs algorithm (Ju et al., 2022) is used for the draw
of Yi(Wi).
Appendix E. Simulation Details
E.1 Estimands
Under the data-generating processes and the re-parameterizations of the Beta regression
provided in Section 5.1, the expectations of each potential outcome are expressed as:
E[Y (0)] = EX1,X2,X3[µ(0)] = EX1,X2,X3



=== CHUNK 117 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 29, 'page_label': '30', 'start_index': 1305}
Length: 795 characters
End of Chunk 117 sentences... :
provided in Section 5.1, the expectations of each potential outcome are expressed as:
E[Y (0)] = EX1,X2,X3[µ(0)] = EX1,X2,X3
[ exp(1.0− 0.8X1 + 0.5X2− 2.0X3)
1 + exp(1.0− 0.8X1 + 0.5X2− 2.0X3)
]
= 0.359613,
E[Y (1)] = EX1,X2,X3[µ(1)] = EX1,X2,X3
[ exp(1.5− 0.8X1 + 0.5X2− 2.0X3)
1 + exp(1.5− 0.8X1 + 0.5X2− 2.0X3)
]
= 0.457068.
We refer readers to Ferrari and Cribari-Neto (2004) for further details about the Beta
regression.
E.2 Additional Simulations
Table 4 – 7 display the simulation results for smaller sample sizes ofN = 100 andN = 1, 000.
All scenarios achieve roughly95% coverage. Regarding Bias and MSE, custom scenarios
demonstrate superior performance compared to the joint scenario, consistent with the
observations in the main manuscript forN = 10, 000. As expected, the MSE of the



=== CHUNK 118 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 29, 'page_label': '30', 'start_index': 2021}
Length: 525 characters
End of Chunk 118 sentences... :
observations in the main manuscript forN = 10, 000. As expected, the MSE of the
frequentists estimators forN = 1, 000 is about 10 times that ofN = 10, 000, andN = 100
is about 10 times that ofN = 1, 000, which conﬁrms the validity of the convergence rates
we derived. All discussions regarding the comparison between the frequentist and Bayesian
estimators in the main manuscript are applicable to the case ofN = 100 or N = 1, 000.
Please refer to Section 5 in the main manuscript for a detailed discussion on this matter.
30



=== CHUNK 119 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 30, 'page_label': '31', 'start_index': 0}
Length: 765 characters
End of Chunk 119 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
Table 4: Evaluation metrics of frequentist estimators forN = 100,Nsim = 2, 000.
Coverage Bias MSE Interval Width
Custom Custom Custom Custom Custom Custom Custom Custom
ϵtot Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM)
0.1 94.75% 94 .6% 100 .0% 0 .9025 −1.0975 −1.0975 0 .9977 0 .9208 0 .7357 1 .895 1 .889 2 .0
0.3 93.4% 95 .05% 100 .0% 0 .9025 −1.0975 0 .9025 0 .9827 0 .729 0 .7877 1 .869 1 .877 2 .0
1.0 94.8% 95 .6% 99 .8% −0.0535 −0.6484 0 .9025 0 .7787 0 .2685 0 .7476 1 .883 1 .652 1 .986
3.0 94.65% 95 .4% 97 .6% −0.3555 0 .1663 −0.844 0 .1037 0 .0441 0 .2508 1 .237 0 .82 1 .673
10 95.85% 95 .0% 95 .7% 0 .1429 0 .1249 −0.1147 0 .0115 0 .0117 0 .0226 0 .433 0 .426 0 .591



=== CHUNK 120 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 30, 'page_label': '31', 'start_index': 673}
Length: 716 characters
End of Chunk 120 sentences... :
10 95.85% 95 .0% 95 .7% 0 .1429 0 .1249 −0.1147 0 .0115 0 .0117 0 .0226 0 .433 0 .426 0 .591
Table 5: Evaluation metrics of Bayesian estimators forN = 100,Nsim = 1, 000.
Coverage Bias MSE Interval Width
Custom Custom Custom Custom Custom Custom Custom Custom
ϵtot Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM)
0.1 100.0% 100 .0% 100 .0% −0.0961 −0.0982 −0.0966 0 .0093 0 .0097 0 .0094 0 .616 0 .5996 0 .575
0.3 100.0% 100 .0% 100 .0% −0.0958 −0.0964 −0.0970 0 .0092 0 .0096 0 .0095 0 .616 0 .5953 0 .586
1.0 100.0% 100 .0% 100 .0% −0.0952 −0.0897 −0.0951 0 .0093 0 .0101 0 .0096 0 .615 0 .5700 0 .580
3.0 99.5% 99 .5% 99 .5% −0.0657 −0.0584 −0.0864 0 .0106 0 .0086 0 .0113 0 .521 0 .4687 0 .540



=== CHUNK 121 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 30, 'page_label': '31', 'start_index': 1296}
Length: 798 characters
End of Chunk 121 sentences... :
3.0 99.5% 99 .5% 99 .5% −0.0657 −0.0584 −0.0864 0 .0106 0 .0086 0 .0113 0 .521 0 .4687 0 .540
10 94.4% 94 .5% 94 .3% −0.0155 −0.0352 −0.0259 0 .0034 0 .0052 0 .0068 0 .232 0 .2779 0 .304
Table 6: Evaluation metrics of frequentist estimators forN = 1, 000,Nsim = 2, 000.
Coverage Bias MSE Interval Width
Custom Custom Custom Custom Custom Custom Custom Custom
ϵtot Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM)
0.1 95.1% 95 .45% 100 .0% 0 .9025 −1.0975 0 .9025 0 .9995 0 .7129 0 .7832 1 .901 1 .877 2 .0
0.3 95.05% 95 .1% 99 .5% −1.0975 −0.189 −1.0975 0 .9412 0 .296 0 .7623 1 .9 1 .669 1 .987
1.0 94.6% 95 .2% 98 .5% 0 .2516 0 .2546 0 .7294 0 .3827 0 .033 0 .2147 1 .744 0 .71 1 .623
3.0 94.7% 95 .65% 95 .8% 0 .0154 0 .0101 0 .2328 0 .0109 0 .0042 0 .0229 0 .41 0 .261 0 .587



=== CHUNK 122 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 30, 'page_label': '31', 'start_index': 2002}
Length: 716 characters
End of Chunk 122 sentences... :
3.0 94.7% 95 .65% 95 .8% 0 .0154 0 .0101 0 .2328 0 .0109 0 .0042 0 .0229 0 .41 0 .261 0 .587
10 94.6% 94 .9% 94 .85% 0 .0057 0 .066 −0.0543 0 .0012 0 .0012 0 .0022 0 .137 0 .135 0 .181
Table 7: Evaluation metrics of Bayesian estimators forN = 1, 000,Nsim = 1, 000.
Coverage Bias MSE Interval Width
Custom Custom Custom Custom Custom Custom Custom Custom
ϵtot Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM) Joint (IPW) (DM)
0.1 100.0% 100 .0% 100 .0% −0.0973 −0.0965 −0.0987 0 .0096 0 .0096 0 .0099 0 .450 0 .4706 0 .462
0.3 100.0% 100 .0% 100 .0% −0.0972 −0.0859 −0.0974 0 .0096 0 .0084 0 .0099 0 .455 0 .4594 0 .463
1.0 100.0% 98 .0% 100 .0% −0.0928 −0.0597 −0.0916 0 .0093 0 .0070 0 .0099 0 .445 0 .3625 0 .433



=== CHUNK 123 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 30, 'page_label': '31', 'start_index': 2623}
Length: 285 characters
End of Chunk 123 sentences... :
1.0 100.0% 98 .0% 100 .0% −0.0928 −0.0597 −0.0916 0 .0093 0 .0070 0 .0099 0 .445 0 .3625 0 .433
3.0 96.1% 92 .5% 95 .7% −0.0265 −0.0219 −0.0469 0 .0040 0 .0030 0 .0056 0 .258 0 .2036 0 .303
10 92.7% 94 .5% 92 .0% −0.0103 −0.0161 −0.0144 0 .0004 0 .0007 0 .0009 0 .078 0 .0960 0 .107
31



=== CHUNK 124 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 31, 'page_label': '32', 'start_index': 0}
Length: 798 characters
End of Chunk 124 sentences... :
Yuki Ohnishi and Jordan A w an
Appendix F. Regression Adjustment
F.1 Overview
In the context of randomized experiments, causal eﬀectsτ can be identiﬁed solely using the
treatment assignment and outcome variables. Also, as demonstrated in prior sections, our
custom frequentist estimators achieve minimax optimality without the need for covariates.
However, there is a clear rationale for incorporating covariates when deducing causal eﬀects
in randomized settings: they can enhance the eﬃciency of inference by leveraging pertinent
individual data. This enhancement method is termed regression adjustment (Lin, 2013).
Nevertheless, applying regression adjustment within LDP presents challenges. Speciﬁcally,
it could incur additional privacy costs for the covariates, and these costs could escalate



=== CHUNK 125 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 31, 'page_label': '32', 'start_index': 708}
Length: 792 characters
End of Chunk 125 sentences... :
it could incur additional privacy costs for the covariates, and these costs could escalate
signiﬁcantly for high-dimensional covariates. In this section, we present another type of
frequentist estimator for the joint scenario, namely the OLS estimator. We explore its
advantages and constraints, compared to the IPW estimator in the same scenario.
Assume that the observed covariates are privatized by the Laplace mechanism. We
assume Xi,j∈ [0, 1] for i = 1,...,N and j = 1,...,d to ensure bounded𝓁1-sensitivity. The
privatized outcomes and covariates are˜Xi,j = Xi,j +νXi,j, where νXi,j∼i.i.d Lap(d/ϵx). By
composition, the joint release of( ˜Yi, ˜Xi,1,..., ˜Xi,d, ˜Wi)Ni=1 satisﬁes (ϵy +ϵx +ϵw)-LDP.
Without privacy considerations, it is well known that the covariate adjustment can further



=== CHUNK 126 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 31, 'page_label': '32', 'start_index': 1410}
Length: 758 characters
End of Chunk 126 sentences... :
Without privacy considerations, it is well known that the covariate adjustment can further
improve the eﬃciency, even without assuming a correctly speciﬁed outcome model (Lin,
2013). Speciﬁcally, we propose the following plug-in OLS estimator.
˜τOLS = ˜α(1)− ˜α(0) + ¯X( ˜β(1)− ˜β(0)), (13)
where ¯X = 1N∑Ni=1 ˜Xi and (˜α(w), ˜β(w)) = arg minα,β∑i: ˜Wi=w( ˜Yi−α− ˜X′iβ)2 for w = 0, 1.
Note that, under some regularity conditions (Lehmann and Casella, 1998, p. 440),(˜α(w), ˜β(w))
converges to(˜α∗(w), ˜β∗(w)), deﬁned as
(˜α∗(w), ˜β∗(w)) = arg minα,β E[( ˜Yi−α− ˜X′iβ)2| ˜Wi =w].
We investigate the potential bias of the naïve OLS estimator and propose a bias-corrected
version. The following theorem states that the naïve OLS estimator(13) is an inconsistent



=== CHUNK 127 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 31, 'page_label': '32', 'start_index': 2079}
Length: 614 characters
End of Chunk 127 sentences... :
version. The following theorem states that the naïve OLS estimator(13) is an inconsistent
estimator forτ, but multiplying by the same factorCp,ϵw makes it consistent. The central
limit theorem has also been developed.
Theorem 15 1. (Consistency) Cp,ϵw ˜τOLS is consistent forτ.
2. (CLT)
√
N(Cp,ϵw ˜τOLS−τ) converges in distribution to
N
(
0,C 2p,ϵw
(MSE1
ρ1
+ MSE0
ρ0
))
, (14)
where MSEw = E[( ˜Yi− ˜α∗(w)− ˜X′i ˜β∗(w))2| ˜Wi =w] for w = 0, 1.
3. (Conﬁdence Interval) The following interval is the nominal central conﬁdence at the
signiﬁcance levelα:
(
Cp,ϵw ˜τOLS−zα2
√
ˆΣOLS
N ,Cp,ϵw ˜τOLS +zα2
√
ˆΣOLS
N
)
,
32



=== CHUNK 128 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 32, 'page_label': '33', 'start_index': 0}
Length: 768 characters
End of Chunk 128 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
where ˆΣOLS = C2p,ϵw
( ˆMSE1
ρ1 + ˆMSE0ρ0 ) and ˆMSEw = 1˜Nw∑i: ˜Wi=w( ˜Yi− ˜α(w)− ˜Xi ˜β(w))2
for w = 0, 1.
Proof Consider the objective function
Q(α(w),β (w)) = E[( ˜Yi−α(w)− ˜X′iβ(w))2| ˜Wi =w]
= E[( ˜Yi−γ(w)− ( ˜X′i−µ ˜X)β(w))2| ˜Wi =w],
where γ(w) =α(w) +µ ˜Xβ(w). Note that, for bothw = 0, 1,
µ ˜X = E[ ˜Xi| ˜Wi =w] = E[Xi| ˜Wi =w] = E[Xi] =µX.
The second equality follows from the independence of noiseνXi , and the third equality follows
from the randomized assignment ofWi and the independence of the randomized response
mechanism. Minimizing the right-hand side overγ(w) and β(w) leads to the same values for
α(w) and β(w) as minimizing the left-hand side overα(w) and β(w), with the least squares



=== CHUNK 129 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 32, 'page_label': '33', 'start_index': 680}
Length: 786 characters
End of Chunk 129 sentences... :
α(w) and β(w) as minimizing the left-hand side overα(w) and β(w), with the least squares
estimate ofγ∗(w) =α∗(w) +µ ˜Xβ∗(w).
Q(γ(w),β (w))
= E[( ˜Yi−γ(w)− ( ˜X′i−µX)β(w))2| ˜Wi =w]
= E[( ˜Yi−γ(w))2| ˜Wi =w] + E[(( ˜X′i−µ ˜X)β(w))2| ˜Wi =w]
− 2E[( ˜Yi−γ(w))( ˜X′i−µ ˜X)β(w)| ˜Wi =w]
= E[( ˜Yi−γ(w))2| ˜Wi =w] + E[(( ˜X′i−µ ˜X)β(w))2| ˜Wi =w]
− 2E[ ˜Yi( ˜X′i−µ ˜X)β(w)| ˜Wi =w].
The last two terms do not depend onγ(w). Thus, minimizing Q(γ(w),β (w)) over γ(w) is
equivalent to minimizingE[( ˜Yi−γ(w))2| ˜Wi =w] overγ(w), which leads to the minimizer
˜γ∗(1) = E[ ˜Yi| ˜Wi = 1] = E[Yi| ˜Wi = 1] =
1∑
w=0
E[Yi| ˜Wi = 1,Wi =w]P (Wi =w| ˜Wi = 1)
= ¯p¯qϵw
pqϵw + ¯p¯qϵw
E[Yi(0)] + pqϵw
pqϵw + ¯p¯qϵw
E[Yi(1)].
Similarly, we have
˜γ∗(0) = ¯pqϵw¯pqϵw +p¯qϵw E[Yi(0)]− p¯qϵw¯pqϵw +p¯qϵw E[Yi(1)].



=== CHUNK 130 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 32, 'page_label': '33', 'start_index': 1320}
Length: 302 characters
End of Chunk 130 sentences... :
= ¯p¯qϵw
pqϵw + ¯p¯qϵw
E[Yi(0)] + pqϵw
pqϵw + ¯p¯qϵw
E[Yi(1)].
Similarly, we have
˜γ∗(0) = ¯pqϵw¯pqϵw +p¯qϵw E[Yi(0)]− p¯qϵw¯pqϵw +p¯qϵw E[Yi(1)].
Then, we have
˜γ∗(1)− ˜γ∗(0) = (qϵw− ¯qϵw)p¯p(¯pqϵw +p¯qϵw)(pqϵw + ¯p¯qϵw)(E[Yi(1)]− E[Yi(0)])
= (qϵw− ¯qϵw)p¯p(¯pqϵw +p¯qϵw)(pqϵw + ¯p¯qϵw)τ = 1Cp,ϵwτ.
33



=== CHUNK 131 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 33, 'page_label': '34', 'start_index': 0}
Length: 758 characters
End of Chunk 131 sentences... :
Yuki Ohnishi and Jordan A w an
Finally, noting the fact that˜γ∗(w) = ˜α∗(w) +µ ˜X ˜β∗(w) and, under some regularity conditions,
(˜α(w), ˜β(w)) converges to(˜α∗(w), ˜β∗(w)),
˜τOLS = ˜α(1)− ˜α(0) + ¯˜X( ˜β(1)− ˜β(0)) p→ ˜γ∗(1)− ˜γ∗(0) = 1Cp,ϵwτ.
Thus, by the continuous mapping theorem,Cp,ϵw ˜τOLS is a consistent estimator forτ.
Next, we obtain the central limit theorem. Again, it is convenient to parameterize the
model using(γw,βw) instead of(αw,βw). In terms of these parameters, the objective function
for ˜Wi =w is
∑
i: ˜Wi=w
( ˜Yi−γ− ( ˜Xi−µ ˜X)β)2.
The ﬁrst order conditions for the estimators(˜γw, ˜βw) are
∑
i: ˜Wi=w
ψ( ˜Yi, ˜Xi, ˜γw, ˜βw) = 0,
where ψ(·) is a two-component column vector:
ψ(y,x,γ,β ) =
( y−γ− (x−µ ˜X)β
(x−µ ˜X)(y−γ− (x−µ ˜X)β)
)
.



=== CHUNK 132 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 33, 'page_label': '34', 'start_index': 615}
Length: 797 characters
End of Chunk 132 sentences... :
∑
i: ˜Wi=w
ψ( ˜Yi, ˜Xi, ˜γw, ˜βw) = 0,
where ψ(·) is a two-component column vector:
ψ(y,x,γ,β ) =
( y−γ− (x−µ ˜X)β
(x−µ ˜X)(y−γ− (x−µ ˜X)β)
)
.
The standard M-estimation results imply that, under standard regularity conditions, the
estimator is consistent and asymptotically normally distributed:
√
Nw
(˜γw− ˜γ∗w
˜βw− ˜β∗w
)
D→ N
((0
0
)
, Γ−1w ∆w(Γ′w)−1
)
,
where Nw =∑Ni=1 1 ( ˜Wi =w) and the two components of the covariance matrix are
Γw = E
[ ∂
∂(γ,β )ψ( ˜Yi, ˜Xi,γ,β )| ˜Wi =w
]⏐⏐⏐⏐
(˜γ∗w,˜β∗w)
= E
[( −1 −( ˜Xi−µ ˜X)
−( ˜Xi−µ ˜X)′ −( ˜Xi−µ ˜X)′( ˜Xi−µ ˜X)
)
| ˜Wi =w
]
= E
[(−1 0
0 −E[( ˜Xi−µ ˜X)′( ˜Xi−µ ˜X)]
)
| ˜Wi =w
]
,
and
∆w = E
[
ψ( ˜Yi, ˜Xi, ˜γ∗w, ˜β∗w)·ψ( ˜Yi, ˜Xi, ˜γ∗w, ˜β∗w)′| ˜Wi =w
]
= E
[
( ˜Yi− ˜γ∗w− ( ˜Xi−µ ˜X) ˜β∗w)2·
( −1
( ˜Xi−µ ˜X)′
)( −1
( ˜Xi−µ ˜X)′
)′
| ˜Wi =w
]
.



=== CHUNK 133 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 33, 'page_label': '34', 'start_index': 1319}
Length: 96 characters
End of Chunk 133 sentences... :
]
= E
[
( ˜Yi− ˜γ∗w− ( ˜Xi−µ ˜X) ˜β∗w)2·
( −1
( ˜Xi−µ ˜X)′
)( −1
( ˜Xi−µ ˜X)′
)′
| ˜Wi =w
]
.
34



=== CHUNK 134 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 34, 'page_label': '35', 'start_index': 0}
Length: 784 characters
End of Chunk 134 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
The variance of ˜γw is the (1, 1) element of the covariance matrix. Because Γw is block
diagonal, the (1, 1) element is equal to
MSEw = E[( ˜Yi− ˜γ∗w− ( ˜Xi−µ ˜X) ˜β∗w)2| ˜Wi =w] = E[( ˜Yi− ˜α∗w− ˜X′i ˜β∗w)2| ˜Wi =w].
Therefore, we have
√
Nw
(˜γw− ˜γ∗w
˜βw− ˜β∗w
)
D→ N
((0
0
)
, MSEw
(1 0
0
(
E[( ˜Xi−µ ˜X)′( ˜Xi−µ ˜X)])−1
))
,
which implies
√
N(˜γ(w)− ˜γ∗(w)) D→ N
(
0, MSEw
P ( ˜Wi =w)
)
. (15)
As shown before,τ = Cp,ϵw(˜γ∗1− ˜γ∗0). Also, Cp,ϵw ˜τOLS = Cp,ϵw(˜γ1− ˜γ0) = Cp,ϵw{˜α1−
˜α0 + ¯˜X( ˜β1− ˜β0)} is the consistent estimator forτ. Noting that ˜β1, ˜β0, ˜γ1 and ˜γ0 are all
asymptotically independent, the asymptotic distribution of˜τOLS is expressed as
√
N(Cp,ϵw ˆτOLS−τ) D→ N
(
0,C 2p,ϵw
(MSE1
ρ1
+ MSE0
ρ0
))
.



=== CHUNK 135 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 34, 'page_label': '35', 'start_index': 645}
Length: 797 characters
End of Chunk 135 sentences... :
asymptotically independent, the asymptotic distribution of˜τOLS is expressed as
√
N(Cp,ϵw ˆτOLS−τ) D→ N
(
0,C 2p,ϵw
(MSE1
ρ1
+ MSE0
ρ0
))
.
F.2 Simulation setups for Regression Adjustment
We empirically evaluate the frequentist properties of the OLS estimator developed in Section
F. We consider the joint privacy mechanism in Section 3.2 and use the same data-generating
mechanisms in Section 5. We releaseXi,d after applying the Laplace mechanism. Speciﬁcally,
the generated covariates satisfy the following sensitivity:∆X = 3. Accordingly, we add the
Laplace noise Lap(3/ϵy) toXi,k fork = 1, 2, 3. Then, we obtain the private data˜Xi,k, ˜Yi, ˜Wi.
By composition, this privacy mechanism guarantees that( ˜Yi, ˜Wi) satisﬁes (ϵy +ϵw)-DP and
( ˜Xi,k, ˜Yi, ˜Wi) satisﬁes (ϵx +ϵy +ϵw)-DP.
F.3 Results



=== CHUNK 136 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 34, 'page_label': '35', 'start_index': 1295}
Length: 750 characters
End of Chunk 136 sentences... :
By composition, this privacy mechanism guarantees that( ˜Yi, ˜Wi) satisﬁes (ϵy +ϵw)-DP and
( ˜Xi,k, ˜Yi, ˜Wi) satisﬁes (ϵx +ϵy +ϵw)-DP.
F.3 Results
Tables 8 and 9 present the performance evaluation of the naïve and OLS estimators for
N = 1, 000, 10, 000 with various privacy budgets forϵx, ϵy and ϵw. We letϵtot =ϵx +ϵy +ϵw.
Both estimators achieve about95% coverage forN = 1, 000, 10, 000 as expected. For bias
and MSE, we observe smaller bias and MSE for larger privacy budgets. For the same levels of
privacy budgets, both bias and MSE improve whenN increases, which empirically supports
our consistency and asymptotically unbiased properties of the estimators.
When we have a tight privacy budget of(ϵx,ϵy,ϵw) = (0.1, 0.1, 0.1), the length of the



=== CHUNK 137 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 34, 'page_label': '35', 'start_index': 1960}
Length: 638 characters
End of Chunk 137 sentences... :
When we have a tight privacy budget of(ϵx,ϵy,ϵw) = (0.1, 0.1, 0.1), the length of the
conﬁdence interval of the frequentist estimators is nearly2, which is almost non-informative
about the estimand. When N increases, the interval length gets smaller and becomes
informative enough for some allocations, e.g.,(ϵx,ϵy,ϵw) = (1.25, 0.5, 1.25). However, with
strict budget constraints and a small sample size, the analysis results may tell us little about
the estimands, even though their consistency and conﬁdence intervals are statistically valid.
This is an inevitable trade-oﬀ between privacy protection and the accuracy of the results.
35



=== CHUNK 138 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 35, 'page_label': '36', 'start_index': 0}
Length: 792 characters
End of Chunk 138 sentences... :
Yuki Ohnishi and Jordan A w an
Table 8: Evaluation metrics for the naïve and OLS estimators (N = 1, 000,Nsim = 2, 000)
under the joint scenario.Nsim denotes the number of simulations.ϵtot denotes the
total privacy budget,ϵtot =ϵx +ϵy +ϵw.
Coverage Bias MSE Interval Width
ϵtot (ϵx,ϵy,ϵw) Naïve OLS Naïve OLS Naïve OLS Naïve OLS
3 (1, 1, 1) 95 .3% 95 .7% −0.00266 −0.00329 0 .0405 0 .0371 0 .798 0 .770
9 (3, 3, 3) 95 .4% 96 .4% −0.00105 −0.000422 0 .00208 0 .00126 0 .181 0 .142
30 (10, 10, 10) 95 .0% 96 .8% −0.000547 −0.000282 0 .000906 0 .000177 0 .120 0 .058
0.3 (0.1, 0.1, 0.1) 95 .5% 95 .5% −0.129 −0.128 0 .989 0 .984 1 .909 1 .910
3 (2, 0.5, 0.5) 94 .5% 94 .5% −0.00703 −0.00837 0 .378 0 .375 1 .748 1 .749
3 (0.5, 2, 0.5) 95 .2% 95 .4% −0.00576 −0.00406 0 .0484 0 .0373 0 .857 0 .754



=== CHUNK 139 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 35, 'page_label': '36', 'start_index': 715}
Length: 770 characters
End of Chunk 139 sentences... :
3 (0.5, 2, 0.5) 95 .2% 95 .4% −0.00576 −0.00406 0 .0484 0 .0373 0 .857 0 .754
3 (0.5, 0.5, 2) 95 .4% 95 .0% −0.00238 −0.00263 0 .0575 0 .0565 0 .929 0 .923
3 (0.5, 1.25, 1.25) 94 .6% 94 .5% 0 .00480 0 .00276 0 .0210 0 .0187 0 .547 0 .518
3 (1.25, 0.5, 1.25) 95 .3% 95 .2% −0.00101 −0.00246 0 .103 0 .101 1 .232 1 .225
3 (1.25, 1.25, 0.5) 94 .6% 95 .7% 0 .00137 0 .00150 0 .102 0 .0889 1 .195 1 .144
F.4 Discussions
In the simulations, we consider diﬀerent divisions of the same overall privacy budget,ϵtot = 3,
which suggests an allocation strategy of the budget. Among all the budget allocations
with ϵtot = 3, we see that(ϵx,ϵy,ϵw) = (0.5, 1.25, 1.25) achieves the lowest MSE for both
naïve and OLS estimators. Thus, it seems reasonable to assign a strict budget to X,



=== CHUNK 140 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 35, 'page_label': '36', 'start_index': 1402}
Length: 714 characters
End of Chunk 140 sentences... :
naïve and OLS estimators. Thus, it seems reasonable to assign a strict budget to X,
and larger budgets to Y and W. We also see that for most allocations with budgets
ϵtot≤ 3, there is minimal gain in MSE for the OLS over the naïve estimator. However, for
(ϵx,ϵy,ϵw) = (10, 10, 10), (3, 3, 3), (0.5, 2, 0.5), we see that the OLS estimator does signiﬁcantly
outperform the naïve estimator in terms of MSE. This result follows from the fact that the
regression adjustment technique in randomized experiments (Freedman, 2008; Lin, 2013)
helps reduce the variance of the OLS estimator, leading to better MSE. Intuitively, the
regression adjustment works for(ϵx,ϵy,ϵw) = (10, 10, 10) because the privatized data contains



=== CHUNK 141 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 35, 'page_label': '36', 'start_index': 2023}
Length: 761 characters
End of Chunk 141 sentences... :
regression adjustment works for(ϵx,ϵy,ϵw) = (10, 10, 10) because the privatized data contains
smaller noise, and ˜X still contains some information to explain˜Y. When the total budget is
smaller (ϵtot≤ 3), however, the gain is limited.
We here further discuss some limitations to the gains in precision of the estimator for the
PATE from including covariates from theoretical perspectives. In large samples, including
covariates in the regression function under usual randomized experiments will not lower the
precision (Imbens and Rubin, 2015). However, DP mechanisms under randomization pose
unique challenges. First,MSEw in Theorem 15 can be written as follows:
MSEw = Var[Yi| ˜Wi =w] + E[Yi| ˜Wi =w]2 + 1ϵ2y− E[ ˜Y′i ˜Xi( ˜X′i ˜Xi)−1 ˜X′i ˜Yi| ˜Wi =w]. (16)



=== CHUNK 142 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 35, 'page_label': '36', 'start_index': 2688}
Length: 649 characters
End of Chunk 142 sentences... :
MSEw = Var[Yi| ˜Wi =w] + E[Yi| ˜Wi =w]2 + 1ϵ2y− E[ ˜Y′i ˜Xi( ˜X′i ˜Xi)−1 ˜X′i ˜Yi| ˜Wi =w]. (16)
The last term, E[ ˜Y′i ˜Xi( ˜X′i ˜Xi)−1 ˜X′i ˜Yi| ˜Wi = w], is eﬀectively the gain in precision from
including covariates. This term implies that the gain is zero when˜Xi and ˜Yi are orthogonal,
but is always positive otherwise. As adding large independent noise toXi and Yi makes
the privatized observations less correlated, the gain becomes negligible whenϵx and ϵy are
small. We also note that the ﬁrst two terms in(16) are bounded due to the sensitivity ofY;
however, the last two terms are unbounded, making them the dominant precision factors,
36



=== CHUNK 143 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 36, 'page_label': '37', 'start_index': 0}
Length: 746 characters
End of Chunk 143 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
Table 9: Evaluation metrics for the naïve and OLS estimators (N = 10, 000,Nsim = 2, 000)
under the joint scenario.
Coverage Bias MSE Interval Width
ϵtot (ϵx,ϵy,ϵw) Naïve OLS Naïve OLS Naïve OLS Naïve OLS
3 (1, 1, 1) 95 .4% 95 .2% −0.00174 −0.00196 0 .00407 0 .00376 0 .252 0 .243
9 (3, 3, 3) 94 .7% 94 .7% −0.000154 −0.000149 0 .000216 0 .000136 0 .0573 0 .0454
30 (10, 10, 10) 94 .6% 96 .3% 0 .000213 −0.0000316 0 .0000962 0 .0000184 0 .0380 0 .0183
0.3 (0.1, 0.1, 0.1) 94 .4% 94 .3% −0.104 −0.101 0 .919 0 .921 1 .883 1 .885
3 (2, 0.5, 0.5) 94 .9% 95 .1% −0.00380 −0.00358 0 .0535 0 .0520 0 .915 0 .906
3 (0.5, 2, 0.5) 95 .7% 95 .7% 0 .00112 0 .000358 0 .00466 0 .00356 0 .271 0 .237



=== CHUNK 144 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 36, 'page_label': '37', 'start_index': 666}
Length: 742 characters
End of Chunk 144 sentences... :
3 (0.5, 2, 0.5) 95 .7% 95 .7% 0 .00112 0 .000358 0 .00466 0 .00356 0 .271 0 .237
3 (0.5, 0.5, 2) 95 .9% 95 .9% 0 .000703 0 .000989 0 .00524 0 .00512 0 .295 0 .292
3 (0.5, 1.25, 1.25) 95 .9% 95 .9% 0 .00133 0 .00124 0 .00187 0 .00170 0 .173 0 .163
3 (1.25, 0.5, 1.25) 95 .1% 95 .0% −0.000968 −0.000691 0 .0106 0 .0104 0 .405 0 .401
3 (1.25, 1.25, 0.5) 95 .4% 95 .4% 0 .00247 0 .00279 0 .00957 0 .00848 0 .391 0 .369
especially whenϵx and ϵy are small. Therefore, the gain from adding covariates in inference
is actually limited in our LDP scenarios.
References
Anish Agarwal and Rahul Singh. Causal inference with corrupted data: Measurement error,
missing values, discretization, and diﬀerential privacy.arXiv preprint arXiv:2107.02780,
2021.



=== CHUNK 145 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 36, 'page_label': '37', 'start_index': 1314}
Length: 785 characters
End of Chunk 145 sentences... :
missing values, discretization, and diﬀerential privacy.arXiv preprint arXiv:2107.02780,
2021.
D Apple. Learning with privacy at scale.Apple Machine Learning Journal, 1(8), 2017.
Jordan Awan and Aleksandra Slavković. Diﬀerentially private uniformly most powerful tests
for binomial data.Advances in Neural Information Processing Systems, 31, 2018.
Jordan Awan and Aleksandra Slavković. Structure and sensitivity in diﬀerential privacy:
Comparing k-norm mechanisms.Journal of the American Statistical Association, 116(534):
935–954, 2021.
Felipe Barrera-Osorio, Marianne Bertrand, Leigh L. Linden, and Francisco Perez-Calle.
Improving the design of conditional transfer programs: Evidence from a randomized
education experiment in colombia. American Economic Journal: Applied Economics,



=== CHUNK 146 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 36, 'page_label': '37', 'start_index': 2020}
Length: 705 characters
End of Chunk 146 sentences... :
education experiment in colombia. American Economic Journal: Applied Economics,
3(2):167–195, April 2011. doi: 10.1257/app.3.2.167. URL https://www.aeaweb.org/
articles?id=10.1257/app.3.2.167.
Herman Chernoﬀ and Lincoln E. Moses.Elementary decision theory.Elementary decision
theory. John Wiley, Oxford, England, 1959.
Vito D’Orazio, James Honaker, and Gary King. Diﬀerential privacy for social science inference.
SSRN Electronic Journal, 01 2015. doi: 10.2139/ssrn.2676160.
John C. Duchi, Michael I. Jordan, and Martin J. Wainwright. Minimax optimal procedures
for locally private estimation.Journal of the American Statistical Association, 113(521):
182–201, 2018. doi: 10.1080/01621459.2017.1389735.
37



=== CHUNK 147 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 37, 'page_label': '38', 'start_index': 0}
Length: 741 characters
End of Chunk 147 sentences... :
Yuki Ohnishi and Jordan A w an
Cynthia Dwork, Frank McSherry, Kobbi Nissim, and Adam Smith. Calibrating noise to
sensitivity in private data analysis. InTheory of Cryptography Conference, pages 265–284.
Springer, 2006.
Úlfar Erlingsson, Vasyl Pihur, and Aleksandra Korolova. Rappor: Randomized aggregatable
privacy-preserving ordinal response. InProceedings of the 2014 ACM SIGSAC Conference
on Computer and Communications Security, pages 1054–1067, 2014.
Georgina Evans and Gary King. Statistically valid inferences from diﬀerentially private data
releases, with application to the Facebook urls dataset.Political Analysis, pages 1–21,
2021 2022.
T. S. Ferguson.Mathematical statistics : a decision theoretic approach. Probability and Math-



=== CHUNK 148 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 37, 'page_label': '38', 'start_index': 637}
Length: 763 characters
End of Chunk 148 sentences... :
2021 2022.
T. S. Ferguson.Mathematical statistics : a decision theoretic approach. Probability and Math-
ematical Statistics. Academic Press, New York, 1967. ISBN 0122537505; 9780122537509.
Thomas S. Ferguson. Prior distributions on spaces of probability measures.The Annals of
Statistics, 2(4):615 – 629, 1974. doi: 10.1214/aos/1176342752.
Cecilia Ferrando, Shufan Wang, and Daniel Sheldon. Parametric bootstrap for diﬀerentially
private conﬁdence intervals. In Gustau Camps-Valls, Francisco J. R. Ruiz, and Isabel
Valera, editors,Proceedings of The 25th International Conference on Artiﬁcial Intelligence
and Statistics, volume 151 ofProceedings of Machine Learning Research, pages 1598–1618.
PMLR, 2022. URL https://proceedings.mlr.press/v151/ferrando22a.html.



=== CHUNK 149 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 37, 'page_label': '38', 'start_index': 1332}
Length: 745 characters
End of Chunk 149 sentences... :
PMLR, 2022. URL https://proceedings.mlr.press/v151/ferrando22a.html.
Silvia Ferrari and Francisco Cribari-Neto. Beta regression for modelling rates and proportions.
Journal of Applied Statistics, 31(7):799–815, 2004. doi: 10.1080/0266476042000214501.
Laura Forastiere, Fabrizia Mealli, and Tyler J. VanderWeele. Identiﬁcation and estimation
of causal mechanisms in clustered encouragement designs: Disentangling bed nets using
Bayesian principal stratiﬁcation. Journal of the American Statistical Association, 111:
510–525, 2016. ISSN 1537274X. doi: 10.1080/01621459.2015.1125788.
David A. Freedman. On regression adjustments in experiments with several treatments.The
Annals of Applied Statistics, 2(1):176 – 196, 2008. doi: 10.1214/07-AOAS143.



=== CHUNK 150 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 37, 'page_label': '38', 'start_index': 2001}
Length: 785 characters
End of Chunk 150 sentences... :
Annals of Applied Statistics, 2(1):176 – 196, 2008. doi: 10.1214/07-AOAS143.
Moritz Hardt and Kunal Talwar. On the geometry of diﬀerential privacy. InProceedings of
the Forty-second ACM Symposium on Theory of Computing, pages 705–714, 2010.
Guido W. Imbens and Donald B. Rubin. Causal Inference for Statistics, Social, and
Biomedical Sciences: An Introduction. Cambridge University Press, 2015. doi: 10.1017/
CBO9781139025751.
Hemant Ishwaran and Lancelot F James. Gibbs sampling methods for stick-breaking
priors. Journal of the American Statistical Association, 96(453):161–173, 2001. doi:
10.1198/016214501750332758.
Hemant Ishwaran and Mahmoud Zarepour. Markov chain Monte Carlo in approximate
Dirichlet and beta two-parameter process hierarchical models.Biometrika, 87(2):371–390,



=== CHUNK 151 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 37, 'page_label': '38', 'start_index': 2699}
Length: 111 characters
End of Chunk 151 sentences... :
Dirichlet and beta two-parameter process hierarchical models.Biometrika, 87(2):371–390,
2000. ISSN 00063444.
38



=== CHUNK 152 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 38, 'page_label': '39', 'start_index': 0}
Length: 730 characters
End of Chunk 152 sentences... :
Locally Priv ate Causal Inference for Randomized Experiments
Nianqiao Ju, Jordan Awan, Ruobin Gong, and Vinayak Rao. Data augmentation MCMC
for Bayesian inference from privatized data.Advances in Neural Information Processing
Systems, 35:12732–12743, 2022.
Tatiana Komarova and Denis Nekipelov. Identiﬁcation and formal privacy guarantees.arXiv
preprint arXiv:2006.14732, 2020.
Matt J. Kusner, Yu Sun, Karthik Sridharan, and Kilian Q. Weinberger. Private causal
inference. International Conference on Artiﬁcial Intelligence and Statistics, 51:1308–1317,
2016.
Si Kai Lee, Luigi Gresele, Mijung Park, and Krikamol Muandet. Privacy-preserving causal
inference via inverse probability weighting.arXiv preprint arXiv:1905.12592, 2019.



=== CHUNK 153 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 38, 'page_label': '39', 'start_index': 648}
Length: 797 characters
End of Chunk 153 sentences... :
inference via inverse probability weighting.arXiv preprint arXiv:1905.12592, 2019.
Erich L. Lehmann and George Casella.Theory of Point Estimation. Springer-Verlag, New
York, NY, USA, second edition, 1998.
Jing Lei, Anne-Sophie Charest, Aleksandra Slavkovic, Adam Smith, and Stephen Fienberg.
Diﬀerentially private model selection with penalized and constrained likelihood.Journal
of the Royal Statistical Society Series A: Statistics in Society, 181(3):609–633, 10 2017.
ISSN 0964-1998. doi: 10.1111/rssa.12324. URLhttps://doi.org/10.1111/rssa.12324.
Fan Li, Peng Ding, and Fabrizia Mealli. Bayesian causal inference: A critical re-
view. Philosophical Transactions of the Royal Society A: Mathematical, Physical and
Engineering Sciences, 381(2247):20220153, 2023. doi: 10.1098/rsta.2022.0153. URL



=== CHUNK 154 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 38, 'page_label': '39', 'start_index': 1365}
Length: 763 characters
End of Chunk 154 sentences... :
Engineering Sciences, 381(2247):20220153, 2023. doi: 10.1098/rsta.2022.0153. URL
https://royalsocietypublishing.org/doi/abs/10.1098/rsta.2022.0153.
Winston Lin. Agnostic notes on regression adjustments to experimental data: Reexamining
Freedman’s critique.The Annals of Applied Statistics, 7(1):295 – 318, 2013. doi: 10.1214/
12-AOAS583. URL https://doi.org/10.1214/12-AOAS583.
Steven Maceachern. Dependent nonparametric processes. Proceedings of the Section on
Bayesian Statistical Science, American Statistical Association, pages 50–55, 01 1999.
Fengshi Niu, Harsha Nori, Brian Quistorﬀ, Rich Caruana, Donald Ngwe, and Aadharsh Kan-
nan. Diﬀerentially private estimation of heterogeneous causal eﬀects. InFirst Conference
on Causal Learning and Reasoning, 2022.



=== CHUNK 155 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 38, 'page_label': '39', 'start_index': 2000}
Length: 720 characters
End of Chunk 155 sentences... :
nan. Diﬀerentially private estimation of heterogeneous causal eﬀects. InFirst Conference
on Causal Learning and Reasoning, 2022.
Yuki Ohnishi and Arman Sabbaghi. A Bayesian analysis of two-stage randomized experiments
in the presence of interference, treatment nonadherence, and missing outcomes.Bayesian
Analysis, pages 1 – 30, 2022a. doi: 10.1214/22-BA1347.
Yuki Ohnishi and Arman Sabbaghi. Degree of interference: A general framework for causal
inference under interference.arXiv preprint arXiv:2210.17516, 2022b.
Donald B. Rubin. Bayesian inference for causal eﬀects: The role of randomization.The
Annals of Statistics, 6(1):34 – 58, 1978. doi: 10.1214/aos/1176344064. URL https:
//doi.org/10.1214/aos/1176344064.
39



=== CHUNK 156 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 39, 'page_label': '40', 'start_index': 0}
Length: 724 characters
End of Chunk 156 sentences... :
Yuki Ohnishi and Jordan A w an
Aaron Schein, Zhiwei Steven Wu, Alexandra Schoﬁeld, Mingyuan Zhou, and Hanna Wallach.
Locally private Bayesian inference for count models. In Kamalika Chaudhuri and Ruslan
Salakhutdinov, editors, Proceedings of the 36th International Conference on Machine
Learning, volume 97 of Proceedings of Machine Learning Research, pages 5638–5648.
PMLR, 09–15 Jun 2019.
Scott L. Schwartz, Fan Li, and Fabrizia Mealli. A Bayesian semiparametric approach to
intermediate variables in causal inference.Journal of the American Statistical Association,
106:1331–1344, 12 2011. ISSN 01621459. doi: 10.1198/jasa.2011.ap10425.
David A. Stephens, Widemberg S. Nobre, Erica E. M. Moodie, and Alexandra M. Schmidt.



=== CHUNK 157 ===
Metadata: {'producer': 'pdfTeX-1.40.20', 'creator': 'LaTeX with hyperref', 'creationdate': '2025-01-17T00:01:43+00:00', 'author': '', 'title': '', 'subject': '', 'keywords': '', 'moddate': '2025-01-17T00:01:43+00:00', 'trapped': '/False', 'ptex.fullbanner': 'This is pdfTeX, Version 3.14159265-2.6-1.40.20 (TeX Live 2019/Debian) kpathsea version 6.3.1', 'source': 'documents/sample.pdf', 'total_pages': 40, 'page': 39, 'page_label': '40', 'start_index': 640}
Length: 652 characters
End of Chunk 157 sentences... :
David A. Stephens, Widemberg S. Nobre, Erica E. M. Moodie, and Alexandra M. Schmidt.
Causal inference under mis-speciﬁcation: adjustment based on the propensity score (with
discussion). Bayesian Analysis, 18(2):639 – 694, 2023. doi: 10.1214/22-BA1322. URL
https://doi.org/10.1214/22-BA1322.
Martin A. Tanner and Wing Hung Wong. The calculation of posterior distributions by data
augmentation. Journal of the American Statistical Association, 82(398):528–540, 1987.
ISSN 01621459.
Corwin Matthew Zigler. The central role of Bayes’ theorem for joint estimation of causal
eﬀects and propensity scores.The American Statistician, 70(1):47–54, March 2016.
40




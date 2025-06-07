
![Sydney Opera House](img/PAKDD2025_banner.jpg)

# Practical Online Continual Learning

Welcome to the Practical Online Continual Learning (OCL) tutorial at PAKDD 2025! 
This site provides all the resources necessary to follow along with or review the material presented during the tutorial. We do not expect you to code or run the notebooks in real time; instead, the aim is for you to be able to run and experiment with anything interesting.

Online Continual Learning (OCL) enables machine learning models to learn sequentially from non-stationary data while maintaining past knowledge.
This tutorial presents a practical guide to OCL, covering key concepts, challenges such as catastrophic forgetting and stability-plasticity trade-offs, and recent advances including prototype-based methods and prompt-based approaches.
The session includes hands-on demonstrations using CapyMOA, an open-source platform for online/stream/continual learning. By bridging research insights with practical implementation, this tutorial aims to equip attendees with the tools to develop robust OCL solutions.

## Setup

To get setup follow [these instructions](https://capymoa.org/installation.html) to get setup with CapyMOA.
It is recommended you install PyTorch with GPU support since we use neural networks in this tutorial. 


## Tutorial Outline

In this tutorial, we aim to give an overview of Online Continual Learning (OCL).
The tutorial is structured as follows:

1. Online Learning
2. Continual Learning
3. Online Continual Learning
4. OCL Evaluation: [`notebooks/00_evaluation.ipynb`](notebooks/00_evaluation.ipynb)
5. OCL Strategies

    1. Replay: [`notebooks/01_replay.ipynb`](notebooks/01_replay.ipynb)
    2. Regularization: [`notebooks/02_regularization.ipynb`](notebooks/02_regularization.ipynb)
    3. Prototype-based Methods: [`notebooks/03_prototype.ipynb`](notebooks/03_prototype.ipynb)
    4. Other Methods 

6. Conclusion

Slides can be found here: [`slides_PAKDD2025.pdf`](slides_PAKDD2025.pdf).

### Additional Resources

* [CapyMOA Online Learning Library](https://capymoa.org)
* [Avalanche CL Library](https://avalanche.continualai.org/)
* [RaptorMai OCL Library](https://github.com/RaptorMai/online-continual-learning)

## Organizer Biographies

**Anton Lee** is a PhD student in AI and a research assistant at the University of Wellington, where they study continual learning. As a research assistant, they maintain the CapyMOA open-source data-stream learning project.

**Heitor Murilo Gomes** is currently a senior lecturer at Victoria University of Wellington (VuW) in New Zealand. Previously, he served as co-director of the AI Institute at the University of Waikato (UoW), where he supervised PhD students and research assistants. From 2020 to 2022, he taught the “Data Stream Mining” course at UoW. His primary research focuses on applying machine learning to data streams, encompassing tasks such as ensemble learning, semi-supervised learning, drift detection and recovery, and the intersection of online continual learning with data streams. Heitor has also made significant contributions to several open-source projects specializing in online and stream learning, notably MOA (Massive Online Analysis), for over a decade.

**Nuwan Gunasekara** research interests include stream learning, online continual learning, and online streaming continual learning.

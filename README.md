 <div align="justify">   
 
 # Logical modelling of dysferlinopathies

Dysferlinopathies are a group of rare genetic myopathies caused by mutations in the DYSF gene. These mutations lead to a reduction or absence of dysferlin—a protein essential for muscle cell membrane repair. As a result, patients experience progressive skeletal muscle weakness and atrophy, eventually affecting all skeletal muscles. Typically, symptoms appear in late adolescence or early adulthood.

There are two primary forms of dysferlinopathies: Miyoshi myopathy (MM) and limb-girdle muscular dystrophy type 2B (LGMD2B). Although both result from mutations in DYSF, they differ in their muscle onset. In MM, the phenotype initially affects the distal skeletal muscles (the lower arms and legs) before progressing to involve the thighs and gluteal muscles.

The principal function of dysferlin is to mediate cellular membrane repair. In its absence, skeletal muscle cells exhibit impaired membrane repair, elevated intracellular calcium levels, and cellular leakage. Beyond defective membrane repair, dysferlin deficiency also affects muscle physiology more broadly. Patients show an increased rate of muscle fibre degeneration and regeneration, accompanied by an abnormal inflammatory response and dysregulation of calcium homeostasis. Additionally, muscle tissue is progressively replaced by connective tissue and adipocytes, and necrotic fibres are often present. I use logical modeling to uncover the molecular and cellular mechanisms that drive dysferlinopathy progression. Eventually the model will serve as a predictive tool to identify potential therapeutic target. 

## Project Overview

This repository hosts a logical model designed to simulate the molecular impact of dysferlin mutations. By representing key regulatory nodes and interactions in cellular pathways —those involved in calcium homeostasis, membrane repair, necrosis and inflammation— the model aims to elucidate the disease progression and identify potential therapeutic targets.

  
## Repository Contents

**Model:** The model is provided in Boolnet format. It currently contains 23 nodes representing components involved in pathways altered in dysferlinopathies. At this stage, the model is built upon a regulatory graph that integrates current knowledge on:

  - Calcium homeostasis
  - Cell membrane repair

The model contains 2 inputs (Lesion and Action potential (AP)) and two outputs (Contraction and Necrosis)
Additional components involved in necrosis, muscle regeneration and immune response will be incorporated. The current regulatory network summarizes the following events:


The regulatory graph:
![model](https://github.com/user-attachments/assets/44b73e31-e821-497f-927d-957830eace81)

**Documentation:** This directory contain the following files:
- A PDF file providing the necessary biological background on dysferlinopathies. This file serves as an introduction to this work.
- 3 HTML files containing tables summarising:
  - Symptoms
  - Treatments
  - Information regarding the regulation included in the model. This table contains explanations for each regulatory mechanism represented in the model, providing the underlying biological mechanisms and literature references.


**Code:** Python scripts for:
  - Simulating the logical model dynamics
  - Performing attractor analysis
  - Assessing attractor reachability from given inputs
    
</div>

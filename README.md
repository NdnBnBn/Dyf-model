# Logical modelling of dysferlinopathies

Dysferlinopathies are rare genetic myopathies caused by mutations in the DYSF gene. These mutations result in the absence or malfunction of dysferlin, a protein critical for muscle cell membrane repair. Patient with dysferlinopathies experience progressive skeletal muscle weakness and degeneration.

## Project Overview

This repository hosts a logical model designed to simulate the molecular impact of dysferlin mutations. By representing key regulatory nodes and interactions in cellular pathways —those involved in calcium homeostasis, membrane repair, necrosis and inflammation— the model aims to elucidate the disease progression and identify potential therapeutic targets.

## Objectives
- Use logical modeling to uncover the molecular and cellular mechanisms that drive dysferlinopathy progression.
- Pinpoint nodes within the model that could serve as novel targets for therapeutic intervention.
  
## Repository Contents

**Model:** The model is provided in Boolnet format. It currently contains 23 nodes representing components involved in pathways altered in dysferlinopathies. As today, the model is based on a regulatory graph that integrates current knowledge on:
  - Calcium homeostasis
  - Cell membrane repair

Further component involved in necrosis and inflammation are still to add.

The regulatory graph is visualized below:
![model](https://github.com/user-attachments/assets/44b73e31-e821-497f-927d-957830eace81)

**Documentation:** This section includes a detailed spreadsheet that summarizes the symptoms and treatments associated with dysferlinopathies. Additionally, it contains explanations for each regulatory mechanism represented in the model, providing the underlying biological mechanisms and literature references.

**Code:** Python scripts for:

    - Simulating the logical model dynamics
    - Performing attractor analysis
    - Assessing attractor reachability from given inputs
    - Generating phenotypic interpretations based on simulation results
    
**Preliminary Results:** A summary document is provided that describes the outcomes of the initial analyses.

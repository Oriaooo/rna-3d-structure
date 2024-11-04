# Exploration of the representations of a RNA 3D structure

RNA structures are typically stored in a PDB/mmCIF format, as other biomolecules (proteins, DNA...), as found in the [PDB database](https://www.rcsb.org/). However, this format isn't used as is in deep learning methods to predict the structures. Their goal is to predict the atoms coordinates, which are stored in the ``.pdb`` file, using different representations. 

This repo aims to expore the different representations of a RNA 3D structure : ``4Xw7``.

![RNA 3D structure of 4XW7.](4Xw7.gif)

## 1. The files formats 

➡️ [Jupyter Notebook](./1.%20Files%20formats.ipynb)

## 2. The distance matrices

➡️ [Jupyter Notebook](./2.%20Distance%20Matrix.ipynb)
from Bio.PDB import Structure
import numpy as np

def get_coordinates_from_structure(structure: Structure, atoms: list[str]=[]) -> np.ndarray:
    """Get the atom coordinates from the molecule structure

    Args:
        structure (Structure): the molecule structure
        cg_atom (str): the atom to keep coordinates from

    Returns:
        np.ndarray: a numpy array with the coordinates for each atom
    """
    all_atoms = []
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    if not atoms or atom.get_name() in atoms:
                        all_atoms.append(atom.get_coord().tolist())
    return np.array(all_atoms)
<!-- ...existing code... -->
# Augmented Reality Application for Maintenance Knowledge Management through Interactive Visualization

<center>Jose Daniel Sarmiento , Manuel Ayala  | { jose2192232, jose2195529 } @correo.uis.edu.co </center>

## Overview
This project focuses on creating an augmented reality (AR) application aimed at improving maintenance knowledge management. The core idea is to use interactive 3D visualizations to guide users through maintenance procedures. The Python scripts in this repository are used within Blender to generate the necessary 3D animations for these procedures.

## Project Goal
To develop a system where complex maintenance tasks can be easily understood and performed by leveraging AR to overlay interactive 3D animated instructions onto real-world equipment.

## Core Functionality of Simulation Scripts
The Python scripts (`routine_1.py`, `routine_2.py`) are designed to be run within Blender. They programmatically define and create animations for various maintenance tasks. These animations involve manipulating 3D objects (e.g., a screwdriver, a cover, a brush) by setting their location and rotation keyframes over time.

## Key Scripts

*   **`routine_1.py`**: This script animates an initial maintenance sequence. It includes:
    *   Animating a screwdriver to simulate unscrewing actions at multiple points.
    *   Animating the removal and return of a cover (`tapa_trasera`).
    *   Performing an initial cleaning animation with a brush (`brush`) in two different locations.
*   **`routine_2.py`**: This script focuses on detailed cleaning animations for the `brush` object. It defines five distinct cleaning routines, each with specific movement patterns (horizontal, vertical) and brush orientations, targeting different surfaces of an object.

## Technical Details

*   **Language**: Python
*   **Core Library**: Blender Python API (`bpy`)
*   **Key Concepts**:
    *   3D Animation: Programmatic creation of movement and transformation sequences.
    *   Keyframing: Defining object states (location, rotation) at specific points in time (frames).
    *   Object Manipulation: Direct control over 3D object properties within the Blender scene.
    *   Euler Rotations: Using `mathutils.Euler` for precise control over object orientation.

## Prerequisites / Requirements
To use these scripts, you will need:

*   **Blender**: A recent version of Blender (e.g., 3.x or later). The `bpy` module is an integral part of Blender.

A `requirements.txt` file would typically list Python packages installable via pip. Since `bpy` is specific to Blender's internal Python environment, the primary requirement is Blender itself.

```
# filepath: requirements.txt
# This project relies on the Blender Python API (bpy), which is included with Blender.
# No external packages are required to be installed via pip for the core animation scripts.
# Ensure you have Blender installed.
```

## How to Run the Scripts

1.  **Open Blender**.
2.  Navigate to the **Scripting** workspace tab.
3.  In the Text Editor window, click **Open** and browse to select one of the Python script files (e.g., `routine_1.py` or `routine_2.py`).
4.  Click the **Run Script** button (usually a play icon) in the Text Editor's header to execute the script.
5.  The script will modify the objects in your current Blender scene (specifically "destornillador ", "tapa_trasera", "brush") by adding animation keyframes. You can then play the animation in Blender's timeline.

**Note**: Ensure the objects named in the scripts (e.g., `brush`, `destornillador `, `tapa_trasera`) exist in your Blender scene before running the scripts, or modify the scripts to use the correct names of your objects.

<!-- ...existing code... -->
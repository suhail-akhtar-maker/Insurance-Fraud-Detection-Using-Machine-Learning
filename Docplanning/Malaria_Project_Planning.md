# Malaria Detection Project - Planning

## Project Overview
Team ID: PNT2026TMID-MLD
Project Complexity: Medium
Duration: 5h 0m
Progress: 90%

## Sprints

### Sprint 1: Dataset Collection (Days 1-6)
- Download and organize NIH Malaria Cell Images Dataset (27,558 images)
- Verify dataset integrity and check image formats
- Split dataset: Train 70%, Validation 15%, Test 15%
- Apply data augmentation (flip, zoom, rotation)
- **Story Points: 20**

### Sprint 2: Data Visualization (Days 7-12)
- Plot sample images from both classes (Parasitized/Uninfected)
- Generate class distribution charts
- Plot training/validation accuracy-loss curves
- Generate confusion matrix and classification reports
- Visualize sample predictions with labels
- **Story Points: 20**

### Sprint 3: Model Development (Days 13-18)
- Design CNN architecture with Conv2D, MaxPooling, Dense, Dropout
- Train model using Binary Cross-Entropy loss and Adam optimizer
- Evaluate on test set (Target: 90% accuracy)
- Save model in HDF5 format
- **Story Points: 20**

### Sprint 4: Application Building (Days 19-24)
- Build Flask web application with image upload functionality
- Implement server-side image validation (JPEG/PNG only)
- Design clean HTML/CSS frontend
- Deploy locally and verify end-to-end functionality
- Push final codebase to GitHub
- **Story Points: 20**

## Team Velocity
- Velocity: 20 story points per sprint
- Sprint Duration: 6 days
- Average Velocity: 3.33 pts/day
- Total Project Duration: 24 days

## Key Deliverables
✓ Trained CNN model (93.8% test accuracy)
✓ Flask web application
✓ Complete documentation
✓ GitHub repository

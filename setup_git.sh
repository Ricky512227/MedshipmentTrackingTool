#!/bin/bash

# Setup script to initialize git repository and prepare for first commit

echo "=== Setting up Git Repository for MedshipmentTrackingTool ==="
echo ""

# Initialize git repository
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git branch -M main
    echo "✓ Git repository initialized"
else
    echo "✓ Git repository already exists"
fi

echo ""
echo "Staging files..."
git add .

echo ""
echo "=== Files to be committed ==="
git status --short

echo ""
echo "=== Ready to commit ==="
echo ""
echo "To commit, run:"
echo "  git commit -m 'Initial commit: MedshipmentTrackingTool - Organized and modernized code'"
echo ""
echo "To push to GitHub, first create the repository on GitHub, then run:"
echo "  git remote add origin https://github.com/Ricky512227/MedshipmentTrackingTool.git"
echo "  git push -u origin main"
echo ""

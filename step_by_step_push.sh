#!/bin/bash

# Step-by-step script to push MedshipmentTrackingTool to GitHub
# Run each section one at a time

REPO_DIR="/Users/alwayskamalsai/CustomProjects/MedshipmentTrackingTool"
cd "$REPO_DIR"

echo "=========================================="
echo "STEP 1: Initialize Git Repository"
echo "=========================================="
git init
git branch -M main
echo "✓ Git initialized"
echo ""
read -p "Press Enter to continue to Step 2..."

echo "=========================================="
echo "STEP 2: Add Files to Git"
echo "=========================================="
git add .
echo "✓ Files added"
git status --short | head -20
echo ""
read -p "Press Enter to continue to Step 3..."

echo "=========================================="
echo "STEP 3: Commit Files"
echo "=========================================="
git commit -m "Initial commit: MedshipmentTrackingTool - Organized and modernized code

- Converted Python 2 to Python 3
- Organized code into modular structure
- Added comprehensive documentation
- Improved error handling and code quality
- Made paths configurable via config.json
- Added GUI dashboard and scheduler functionality"
echo "✓ Files committed"
echo ""
read -p "Press Enter to continue to Step 4..."

echo "=========================================="
echo "STEP 4: Add GitHub Remote"
echo "=========================================="
echo "IMPORTANT: Make sure you've created the repository on GitHub first!"
echo "Go to: https://github.com/new"
echo "Repository name: MedshipmentTrackingTool"
echo "Make it PUBLIC"
echo ""
read -p "Press Enter AFTER creating the repository on GitHub..."

git remote add origin https://github.com/Ricky512227/MedshipmentTrackingTool.git 2>&1 || {
    echo "Remote might already exist, removing and re-adding..."
    git remote remove origin
    git remote add origin https://github.com/Ricky512227/MedshipmentTrackingTool.git
}
echo "✓ Remote added"
echo ""
read -p "Press Enter to continue to Step 5..."

echo "=========================================="
echo "STEP 5: Push to GitHub"
echo "=========================================="
echo "Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ SUCCESS! Repository pushed to GitHub"
    echo "=========================================="
    echo "View your repository at:"
    echo "https://github.com/Ricky512227/MedshipmentTrackingTool"
else
    echo ""
    echo "=========================================="
    echo "✗ Push failed. Common issues:"
    echo "=========================================="
    echo "1. Repository not created on GitHub yet"
    echo "2. Authentication required (use Personal Access Token)"
    echo "3. Check your GitHub username is correct"
    echo ""
    echo "For authentication help, see PUSH_TO_GITHUB.md"
fi

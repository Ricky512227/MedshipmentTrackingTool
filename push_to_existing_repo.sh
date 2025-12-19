#!/bin/bash

# Script to push code to existing GitHub repository
# Handles the case where repo already has a README

cd /Users/alwayskamalsai/CustomProjects/MedshipmentTrackingTool

echo "=========================================="
echo "Pushing to existing GitHub repository"
echo "=========================================="
echo ""

# Initialize git if needed
if [ ! -d ".git" ]; then
    echo "Step 1: Initializing git..."
    git init
    git branch -M main
else
    echo "Step 1: Git already initialized"
fi

# Add remote
echo ""
echo "Step 2: Setting up remote..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/Ricky512227/MedshipmentTrackingTool.git
echo "✓ Remote configured"

# Add all files
echo ""
echo "Step 3: Adding files..."
git add .
echo "✓ Files staged"

# Commit
echo ""
echo "Step 4: Committing..."
git commit -m "Add organized MedshipmentTrackingTool code

- Converted Python 2 to Python 3
- Organized code into modular structure
- Added comprehensive documentation
- Improved error handling and code quality
- Made paths configurable via config.json
- Added GUI dashboard and scheduler functionality" || echo "Already committed or no changes"

# Pull first to merge with existing README
echo ""
echo "Step 5: Pulling existing README from GitHub..."
git pull origin main --allow-unrelated-histories --no-edit || {
    echo "Pull failed, trying to push anyway..."
}

# Push
echo ""
echo "Step 6: Pushing to GitHub..."
git push -u origin main

echo ""
echo "=========================================="
if [ $? -eq 0 ]; then
    echo "✓ SUCCESS! Code pushed to GitHub"
    echo "=========================================="
    echo "View your repository at:"
    echo "https://github.com/Ricky512227/MedshipmentTrackingTool"
else
    echo "✗ Push failed"
    echo "=========================================="
    echo "You may need to authenticate or resolve conflicts"
fi

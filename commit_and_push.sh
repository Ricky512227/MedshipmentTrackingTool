#!/bin/bash

# Script to commit and push MedshipmentTrackingTool to GitHub

set -e

REPO_DIR="/Users/alwayskamalsai/CustomProjects/MedshipmentTrackingTool"
GITHUB_REPO="https://github.com/Ricky512227/MedshipmentTrackingTool.git"

echo "=== Committing and Pushing MedshipmentTrackingTool ==="
echo ""

cd "$REPO_DIR"

# Initialize git if needed
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git branch -M main
fi

# Add all files
echo "Staging files..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "No changes to commit."
else
    echo "Committing changes..."
    git commit -m "Initial commit: MedshipmentTrackingTool - Organized and modernized code

- Converted Python 2 to Python 3
- Organized code into modular structure
- Added comprehensive documentation
- Improved error handling and code quality
- Made paths configurable via config.json
- Added GUI dashboard and scheduler functionality
- Created proper project structure with src/, config/, data/, output/ directories"
fi

# Check if remote exists
if git remote get-url origin >/dev/null 2>&1; then
    echo "Remote already configured: $(git remote get-url origin)"
else
    echo "Adding remote repository..."
    git remote add origin "$GITHUB_REPO"
fi

echo ""
echo "=== Ready to Push ==="
echo ""
echo "IMPORTANT: Make sure you've created the repository on GitHub first!"
echo "Go to: https://github.com/new"
echo "Repository name: MedshipmentTrackingTool"
echo "Make it PUBLIC"
echo ""
read -p "Press Enter after creating the repository on GitHub, or Ctrl+C to cancel..."

echo ""
echo "Pushing to GitHub..."
git push -u origin main

echo ""
echo "=== Success! ==="
echo "Repository pushed to: $GITHUB_REPO"

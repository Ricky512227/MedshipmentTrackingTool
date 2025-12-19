#!/bin/bash

# Auto-push script - runs all steps automatically
# Run this in your terminal: ./auto_push.sh

set -e

cd /Users/alwayskamalsai/CustomProjects/MedshipmentTrackingTool

echo "=========================================="
echo "STEP 1: Initialize Git Repository"
echo "=========================================="
git init
git branch -M main
echo "✓ Git initialized"
echo ""

echo "=========================================="
echo "STEP 2: Add Files to Git"
echo "=========================================="
git add .
echo "✓ Files added"
echo ""

echo "=========================================="
echo "STEP 3: Commit Files"
echo "=========================================="
git commit -m "Initial commit: MedshipmentTrackingTool - Organized and modernized code

- Converted Python 2 to Python 3
- Organized code into modular structure
- Added comprehensive documentation
- Improved error handling and code quality
- Made paths configurable via config.json
- Added GUI dashboard and scheduler functionality" || echo "Already committed or no changes"
echo "✓ Files committed"
echo ""

echo "=========================================="
echo "STEP 4: Add GitHub Remote"
echo "=========================================="
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/Ricky512227/MedshipmentTrackingTool.git
echo "✓ Remote added"
echo ""

echo "=========================================="
echo "STEP 5: Push to GitHub"
echo "=========================================="
echo "IMPORTANT: Make sure you've created the repository on GitHub first!"
echo "Go to: https://github.com/new"
echo "Repository name: MedshipmentTrackingTool (Public)"
echo ""
echo "Pushing to GitHub..."
git push -u origin main

echo ""
echo "=========================================="
echo "✓ SUCCESS! Repository pushed to GitHub"
echo "=========================================="
echo "View your repository at:"
echo "https://github.com/Ricky512227/MedshipmentTrackingTool"

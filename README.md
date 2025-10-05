# OOP 4 PILLARS demo

This repository demonstrates the **4 pillars of Object-Oriented Programming (OOP)** in Python and proficiency in **Git/GitHub** through a complete workflow: creating a repo, branching, committing, pushing, creating a pull request (PR), and pulling updates.

## Project Overview
- **Purpose**: Showcase OOP concepts (Encapsulation, Abstraction, Inheritance, Polymorphism) in 4 Python files.
- **Files**:
  - `encapsulation.py`: Hides data with private attributes in a `BankAccount` class.
  - `abstraction.py`: Uses abstract `Shape` class for `Rectangle` and `Circle`.
  - `inheritance.py`: `Dog` and `Cat` inherit from `Animal`.
  - `polymorphism.py`: `Bird` and `Airplane` share a `fly()` method with different behaviors.

## Git Workflow and Challenges

This project showcases a complete **Git/GitHub** workflow in Git Bash on Windows to demonstrate version control skills.

### Git Workflow
1. **Initialized Repo**: Ran `git init` in `~/PycharmProjects/oop-pillars-demo`, added `README.md`, and pushed to `master`:
git add README.md
git commit -m "Initial commit: Add README"
git remote add origin https://github.com/shahdkabi/oop-pillars-demo.git
git push -u origin master
2. **Created Branch**: Made `4-pillars` branch:
git checkout -b 4-pillars
3. **Added Files**: Committed 4 Python files:
git add *.py
git commit -m "Add 4 files demonstrating OOP pillars"
4. **Pushed**: Pushed branch:
git push origin 4-pillars
5. **Pull Request**: Created PR (`4-pillars` → `master`) via GitHub with title "Add OOP pillars examples".
6. **Pulled Updates**: Post-merge, updated `master`:
git checkout master
git pull origin master

### Challenges and Fixes
1. **Nested Repo**:
- **Issue**: Created `4-pillars` in nested folder (`oop-pillars-demo/oop-pillars-demo`), causing `git add` errors.
- **Fix**: Moved to parent dir (`cd ~/PycharmProjects/oop-pillars-demo`), removed nested `.git`:
rm -rf oop-pillars-demo/.git
2. **Authentication (403 Error)**:
- **Issue**: Push failed due to wrong old account .
- **Fix**: Cleared Windows Credential Manager, used PAT for `shahdkabi`.
3. **Commit History Mismatch**:
- **Problem**: PR failed because `main` and `4-pillars` had different commit histories.
- **Solution**: Reset `4-pillars` to `origin/main` while keeping files:
git fetch origin
git reset --soft origin/main
git add *.py
git commit -m "Add 4 files demonstrating OOP pillars"
git push --force-with-lease origin 4-pillars


**Repo**: [https://github.com/shahdkabi/oop-pillars-demo](https://github.com/shahdkabi/oop-pillars-demo)  
**Date**: October 5, 2025

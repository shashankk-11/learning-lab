# 📌 Git Version Control Assignment

## 🚀 Overview

This assignment demonstrates practical usage of Git version control concepts using a Flask-based application.
It includes branching, merging, conflict resolution, commit sequencing, reset, and rebasing.

---

## 🛠️ Tech Stack

* Python (Flask)
* MongoDB Atlas
* HTML (Jinja Templates)
* Git & GitHub

---

## 🌿 Branches Used

* `version-control-assignment` → Initial working branch
* `version-control-assignment_new` → JSON update branch
* `master_1` → Frontend development
* `master_2` → Backend API development
* `main` → Final integrated branch

---

## 🔧 Implementation Steps

### 1. Initial Setup

* Created branch `version-control-assignment`
* Added Flask project
* Committed and merged into `main`

---

### 2. JSON Update

* Created `version-control-assignment_new`
* Modified `data.json`
* Committed changes
* Merged into `main`

---

### 3. Parallel Development

#### Frontend (`master_1`)

* Created To-Do form
* Added:

  * Item Name
  * Item Description

#### Backend (`master_2`)

* Created API route:

```
/submittodoitem
```

* Accepts:

  * itemName
  * itemDescription
* Stores data in MongoDB

---

### 4. Merge to Main

* Merged `master_1` and `master_2` into `main`
* Verified integration

---

### 5. Commit Sequencing

Added fields in separate commits:

1. Added Item ID field
2. Added Item UUID field
3. Added Item Hash field

---

### 6. Git Reset

* Used:

```
git reset --soft <commit_hash>
```

* Rolled back to **Item ID commit**
* Recommitted changes
* Force pushed to `main`

---

### 7. Rebase

* Rebased:

```
git rebase main
```

* Resolved merge conflicts manually
* Preserved commit history

---

## ⚠️ Conflict Resolution

* Conflict occurred in `form.html`
* Resolved by:

  * Keeping all required fields
  * Removing duplicates
  * Maintaining correct order

---

## 📚 Conclusion

This assignment demonstrates real-world Git workflows including branching, merging, rebasing, and history management.

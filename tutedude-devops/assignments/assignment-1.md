# Assignment 1 – Linux Basics

## 1. Creating and Renaming Files/Directories

### Command:

```bash
mkdir test_dir
cd test_dir
touch example.txt
mv example.txt renamed_example.txt
```

### Explanation:

* `mkdir test_dir` → Creates a new directory
* `cd test_dir` → Navigates into the directory
* `touch example.txt` → Creates an empty file
* `mv` → Renames the file

---

## 2. Viewing File Contents

### Commands:

```bash
cat /etc/passwd
head -n 5 /etc/passwd
tail -n 5 /etc/passwd
```

### Explanation:

* `cat` → Displays full file content
* `head -n 5` → Shows first 5 lines
* `tail -n 5` → Shows last 5 lines

---

## 3. Searching for Patterns

### Command:

```bash
grep "root" /etc/passwd
```

### Explanation:

* `grep` searches for specific text patterns
* Finds all lines containing "root"

---

## 4. Zipping and Unzipping

### Commands:

```bash
zip -r test_dir.zip test_dir
unzip test_dir.zip -d unzipped_dir
```

### Explanation:

* `zip -r` → Compresses directory recursively
* `unzip -d` → Extracts into specific directory

---

## 5. Downloading Files

### Command:

```bash
wget https://example.com/sample.txt
```

### Explanation:

* `wget` downloads files from the internet

---

## 6. Changing Permissions

### Command:

```bash
touch secure.txt
chmod 444 secure.txt
```

### Explanation:

* `chmod 444` → Read-only for:

  * Owner
  * Group
  * Others

---

## 7. Working with Environment Variables

### Command:

```bash
export MY_VAR="Hello, Linux!"
echo $MY_VAR
```

### Explanation:

* `export` creates environment variable
* `echo` verifies the value

---
     

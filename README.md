# Hands_On_Minds_On-2-Mitesh_Shetkar
## **Project Euler Challenges**  

# Problem 71 - Ordered Fractions

## 📖 Problem Statement

Consider the fraction **n/d**, where **n** and **d** are positive integers. If **n**<**d** and **HCF(n, d) = 1**, it is called a **reduced proper fraction**.

If we list all reduced proper fractions for **d ≤ 8** in ascending order, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be observed that **2/5** is the fraction **immediately to the left** of **3/7**.

The task is to **find the numerator of the fraction immediately to the left of** **3/7** when listing all reduced proper fractions for **d ≤ 1,000,000**.

## 🎯 Expected Output
428570/999997


# Problem 321 - Swapping Counters

## 📖 Problem Statement

A horizontal row consisting of **2n + 1** squares has:
- **n red counters** placed at one end.
- **n blue counters** placed at the other end.
- A single empty square in the center.

For example, when **n = 3**, the initial state is:

R R R _ B B B

The goal is to **completely reverse the positions** of the red and blue counters.

### ✅ Allowed Moves:
1. A counter can **slide** into an adjacent empty square.
2. A counter can **hop** over another counter if the next square is empty.

Let **M(n)** represent the **minimum number of moves** required to reverse all counters.

It is verified that:

M(3) = 15

which is also a **triangle number**.

### 🔢 Triangle Number Sequence:
If we list values of **n** where **M(n) is a triangle number**, the first five terms are:
1, 3, 10, 22, 63
Their sum:
1 + 3 + 10 + 22 + 63 = 99


### 🎯 Task:
Find the **sum of the first 40 terms** of this sequence.

---

## ▶️ Output
2470433131948040

# Problem 599 - Distinct Colourings of a Rubik's Cube

## 📖 Problem Statement

The well-known **Rubik's Cube** puzzle has many fascinating mathematical properties. The **2×2×2** variant consists of:
- **8 cubelets** (small cubes)
- **24 visible faces** (stickers)

### 🎨 Non-Standard Colouring
We apply **n different colours** (with an unlimited supply of stickers per colour) to the **24 faces** of the cube in any arrangement.

- **All 24 stickers must be placed**.
- **Not all colours have to be used**.
- **The same colour may appear multiple times on the same cubelet**.

### 🔄 Essentially Distinct Colourings
Two colourings, **c₁** and **c₂**, are *essentially distinct* if one cannot be transformed into the other using mechanically possible **Rubik's Cube moves** (rotations, reflections).

For example, with **2 colours**, there are exactly **183 essentially distinct colourings**.

### 🎯 Task:
Find the **number of essentially distinct colourings** when **10 colours** are available.

---

## ▶️ Output
--

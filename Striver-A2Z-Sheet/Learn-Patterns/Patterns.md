# 📅 GOAL: Pattern Solving & Logic Building (Striver's A2Z Sheet)

## 🎯 Goal
The main objective for today was to get comfortable with nested loops, build solid logic-building intuition, and get a better grip on Python's control flow. I focused on cracking some basics patterns from Striver's sheet.


## 💻 Topics & Problems Solved

### 1. Pattern-1: Rectangular Star Pattern
* **Logic:** Printed a uniform $N \times N$ grid of stars using nested loops.
* **Key Takeaway:** Understood how the outer loop manages rows while the inner loop dictates the columns.

### 2. Pattern-2: Right-Angled Triangle Star Pattern
* **Logic:** Printed stars such that each row `i` contains exactly `i + 1` stars.
* **Key Takeaway:** Learned how to dynamically adjust the inner loop's boundary based on the current row index rather than keeping it static.

### 3. Pattern-3: Right-Angled Number Triangle
* **Logic:** Maintained the triangle shape but replaced stars with increasing column numbers starting from 1.
* **Key Takeaway:** Explored Python's `range(1, i + 1)` and saw how list comprehension can optimize string conversion.

### 4. Pattern-4: Same Number Right-Angled Triangle
* **Logic:** Printed a single constant number across an entire row, which matches the current row index.
* **Key Takeaway:** Got a crystal-clear understanding of the functional difference between using the row variable (`i`) versus the column variable (`j`) inside the print statement.

### 5. Pattern-5: Inverted Right-Angled Triangle
* **Logic:** Reversed the logic to decrease the number of printed elements as rows progress, using the formula `N - i`.
* **Key Takeaway:** Practiced running reverse loops effectively using `range(N, 0, -1)` to clean up the code.

### 6. Pattern-6: Inverted Number Triangle
* **Logic:** Combined inverted triangle spacing with dynamic sequential numbers starting from 1 up to `N - i`.
* **Key Takeaway:** Mastered boundary math like `N - i + 1` inside loop constraints to track dynamic column endpoints.


### 7. Pattern-7: Star Pyramid
* **Logic:** Built a centered pyramid structure by introducing leading spaces before printing odd sequences of stars.
* **Key Takeaway:** Cracked the logic of managing multiple independent inner loops—one for calculating spaces (`N - i - 1`) and another for stars (`2 * i + 1`) within a single row.

### 8. Pattern-8: Inverted Star Pyramid
* **Logic:** Built a top-heavy centered pyramid that shrinks down to a single star. 
* **Key Takeaway:** Realized that the leading spaces scale linearly with the row index (`i`), while the stars collapse at a rate of `2 * (N - i) - 1`.

### 9. Pattern-9: Diamond Star Pattern
* **Logic:** Created a symmetrical diamond structure by stacking a normal pyramid directly on top of an inverted pyramid.
* **Key Takeaway:** Deep-dived into pattern scalability. Understood that while the total visual output spans $2 \times N$ rows, the input constraint $N$ acts as the radius or growth cap (e.g., $N=5$ peaks at 5 layers of growth, yielding a 10-row matrix). Breaking composite patterns into independent structural loops keeps the logic highly maintainable.
---

## 🛠️ Python Powers Explored
* **String Multiplication (`*`):** Realized I can bypass explicit inner loops in Python by simply multiplying a string by an integer to repeat it.
* **`end=" "` Parameter:** Learned how to override the default newline behavior of Python’s `print()` function for inline printing.

## 📊 Complexity Checklist
* **Time Complexity:** $\mathcal{O}(N^2)$ for all traditional implementations.
* **Space Complexity:** $\mathcal{O}(1)$ since no extra data structures or dynamic memory allocations were required.

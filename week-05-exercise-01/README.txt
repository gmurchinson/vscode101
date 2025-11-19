Week 05 Exercise 01 — Interactive Buttons with Transitions

What I created:
- A scaffold HTML page with two completed button examples (Color Change and Scale & Shadow) and four placeholder sections for buttons 03–06.
- A CSS file with two example button styles showing how :hover and transition work together.
- CSS variables at the top for easy color management.

How to complete this exercise:

1. Open index.html and add a <button> element in each of the four placeholder sections (03, 04, 05, 06) with descriptive text.
   Example: <button class="button-03">Slide Effect</button>

2. In style.css, add styles for each new button class (.button-03, .button-04, .button-05, .button-06).
   Each button should have:
   - Default styles: background-color, color, padding, border, border-radius, font-family, cursor, and transition
   - A :hover state that changes at least two CSS properties
   - Try different combinations: colors, transform (scale, translateY, translateX, rotate), box-shadow, borders, opacity

3. Test in your browser:
   - Open index.html in a browser
   - Hover over each button to see the transitions
   - Adjust timing and effects until smooth and satisfying
   - Try different transition durations (0.2s, 0.3s, 0.5s) and timing functions (ease, ease-in-out, linear)

4. (Optional) Use CSS variables (defined in :root at the top) to manage colors across all buttons for consistency.

Tips:
- Study the two completed examples (button-01 and button-02) to understand the pattern.
- The transition property on the default button style applies to all changes on :hover.
- Try multiple transforms together: transform: scale(1.05) translateY(-3px);
- Box shadows can create depth: box-shadow: 0 8px 16px rgba(color, alpha);

Next steps:
- Complete the four placeholder button styles.
- Test thoroughly in your browser.
- Commit with a message like "Add interactive buttons 03-06 with transitions".

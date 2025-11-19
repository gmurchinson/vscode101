Week 06 Exercise 01 — Navigation Lab

What I added:
- Template pages: index.html, about.html
- Nested folders: projects/ (with index.html & project-detail.html), gallery/ (with index.html)
- Styles: css/style.css with three navigation patterns: .nav-simple, .nav-horizontal, .nav-centered

Fixes I applied:
- All navigation hrefs updated so links work from root and nested pages.
- CSS links fixed on nested pages (projects and gallery) to point to ../css/style.css.

How to test locally:
1. Open `week-06-exercise-01/index.html` in Live Server or in your browser.
2. Click the nav links and verify Projects and Gallery open their nested index pages and styling applies.

Next steps for you:
- Customize colors/spacing in `css/style.css` to your taste.
- Add more pages inside projects/ or gallery/ and ensure paths are correct.
- Commit with message: "fix: navigation links and css paths; add nav patterns"

Suggested commit commands (PowerShell):

cd "e:\School Documents\Texas Tech University(School Docs)\vscode101"

git add week-06-exercise-01

git commit -m "fix: add Week 06 Navigation Lab; fix paths and add nav patterns"

git push origin main


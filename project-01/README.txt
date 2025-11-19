Project 01 — Personal Landing Page

What I created:
- A semantic landing page scaffold with header, nav, main (multiple sections), and footer.
- Sections: About, Skills & Interests, Projects (placeholder cards), Contact in the footer.
- A style.css that demonstrates typography, CSS variables, color scheme, box model, Flexbox layouts, responsive behavior, and hover/transition effects.

How to use:
1. Open `project-01/index.html` in your browser to preview.
2. Replace the placeholder text and images with your own content.
3. Update the `mailto:` link in the footer with your email address.
4. Commit and push when you're ready.

Notes:
- The page uses a Google Font link (Inter + Merriweather). Remove the link tag in `index.html` if you prefer only system fonts.
- Several elements have :hover and transition styles (nav links, CTA, skill cards, project cards, footer links).

Next steps for you:
- Personalize content and project cards with real projects and descriptions.
- Replace `thumb.png` with real images (same filename or update HTML).
- Verify responsive behavior in DevTools and make style adjustments to taste.

Commit & publish (suggested steps)

Using Git (PowerShell):
```powershell
cd "e:\School Documents\Texas Tech University(School Docs)\vscode101"
git add project-01
git commit -m "Complete project-01: add content, styles, and accessibility polish"
git push origin main
```

After pushing, visit your GitHub Pages site (if enabled):
https://gmurchinson.github.io/vscode101/project-01/

If you prefer GitHub Desktop: stage `project-01` changes, commit with the message above, then push.

Accessibility & polish I added:
- Skip link for keyboard users
- Focus-visible outlines for interactive elements
- Lazy loading on project images for performance
- Extra responsive breakpoint for larger screens

If you'd like, I can make a final commit message history (3-4 small commits) to show development steps — tell me if you want that and I'll prepare the commands.

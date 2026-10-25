# Animation and portrait update

- Corrected portrait framing: the source `Profile.png` is portrait-oriented (1014 × 1550), so the hero now uses a taller frame and `object-fit: contain` with top alignment. No original photo pixels were changed.
- Added subtle floating code glyphs (`{ }`, `</>`, `SQL`, etc.) as decorative background elements on all pages.
- Added animated ambient gradients, hero name gradient, portrait hover, and project/skill card hover effects.
- Added reduced-motion support and mobile adjustments. No additional JavaScript libraries required.
- If the source photo itself has the head cut off, replace `app/static/images/Profile.png` with an uncropped original. CSS cannot restore missing pixels.

Run as before using the existing project instructions. Hard refresh browser with Ctrl+F5 after replacing files.

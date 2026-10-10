# Janvi Raj — Portfolio

A Flask/Jinja portfolio with a custom procedural Three.js Learning Core, responsive dark layouts, and locally served SVG fallback. Python serves the complete page; no Node backend or frontend build is required.

## Run locally (PowerShell)

```powershell
cd Janvi-portfolio
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000. From a terminal already inside this directory, omit `cd Janvi-portfolio`. Flask debug mode is off by default. Stop with Ctrl+C.

For production, use Waitress behind your hosting provider's HTTPS proxy:

```powershell
.\.venv\Scripts\waitress-serve.exe --host=127.0.0.1 --port=8000 app:app
```

## Structure and content

- `app.py`: Flask routes, template rendering, and response headers.
- `portfolio.py`: factual portfolio content, links, skills, projects, training, education and certificates.
- `templates/index.html`: semantic HTML rendered with Jinja.
- `static/css/style.css`: custom styling, mobile navigation and reduced-motion rules.
- `static/css/interaction.css`: perspective hover effects, scan lines, depth surfaces, and responsive artwork placement.
- `static/js/main.js`: mobile menu, active navigation, section-specific 3D entrances, pointer tilt, and scroll progress.
- `static/js/core.js`: seven procedural sculptures using one shared WebGL renderer, studio reflections, signal paths, resource cleanup and visibility controls.
- `static/js/vendor/`: pinned Three.js modules and their MIT license.
- `static/assets/`: original SVG learning sculpture and favicon.
- `app_streamlit_reference.py`, `app_3d.py`, `app_3d_fixed.py`: preserved original references, not the new site's entry points.

The workspace root car-price prediction application has not been changed. This website links to its supplied live demo and repository.

## Artwork and accessibility

The Learning Core is a conceptual illustration, not a running trained model. Curved node layers surround a faceted core, framed by two incomplete tilted arcs. Data particles follow selected connections. Hover, keyboard focus or click **Trace a signal** to illuminate the path. Meaningful labels and captions remain in HTML.

Motion uses elapsed time, pauses outside the viewport and in hidden tabs, and uses a static WebGL composition when reduced motion is requested. Smaller screens reduce curve geometry complexity and pixel ratio. Resource disposal handles navigation and WebGL context loss. If WebGL is unavailable, the designed local hero SVG and CSS section sculptures stay visible; its signal trace uses a brief brightness highlight. Reduced-motion visitors receive no animated trace. Content is readable without JavaScript; the navigation remains visible when scripts are disabled.

Three.js `0.180.0` is bundled locally, including its core module and MIT license. No remote dependency is required for any 3D scene. A procedural studio environment supplies reflections without downloaded textures. Google Fonts supplies Space Grotesk and Inter without blocking navigation; local sans-serif fallbacks work offline.

Each section has a distinct animated 3D study: the work pipeline, interlocking focus loops, computing stack, ascending journey, sculptural book, and folded message. Pointer movement changes their orientation. Project surfaces tilt with a moving highlight; workflow stages lift; skills, timeline entries and certificates respond to hover. Entrances use the Web Animations API with perspective transforms. These effects respect reduced motion and keep text available without hovering.

No portrait, fabricated model scores, skill ratings or unsupported availability claims are included. The reference LinkedIn URL points to the LinkedIn homepage rather than a personal profile; it is deliberately omitted. Contact opens the supplied email address in the visitor's email client; there is no form submission service.

## Verification

```powershell
.\.venv\Scripts\python.exe verify.py
```

Checks the Flask page and health route, every locally referenced static resource, content anchors, supplied links, and factual content. For browser review, test at 390px and 1440px, use Tab and Escape with the menu, enable reduced motion, disable network access, and disable WebGL. `/health` returns `{"status":"ok"}`.

Documentation: [Flask](https://flask.palletsprojects.com/en/stable/), [Three.js](https://threejs.org/docs/), [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

Verified in this workspace: Flask integration checks passed; headless Chrome checked all sections at 390px and 1440px without overflow, all seven WebGL scenes, a single renderer, hover tilt, mobile menu and Escape behavior, and no JavaScript exceptions. Screenshots taken apart under reduced motion were identical. Updated desktop, mobile, work, about and contact previews are saved beside this README.
The final browser run also blocked jsDelivr to verify locally bundled rendering, and simulated WebGL context loss to confirm renderer disposal and restoration of fallback artwork.

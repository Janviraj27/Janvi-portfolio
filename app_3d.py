import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Janvi Raj | AI/ML & Cybersecurity",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LINKS
# =========================================================

GITHUB_URL = "https://github.com/Janviraj27"

CAR_PROJECT_URL = "https://github.com/Janviraj27/car-price-prediction"

LIVE_DEMO_URL = (
    "https://car-price-prediction-gw68b5rgqrngux4w6aappab.streamlit.app/"
)

# Replace this with your real LinkedIn profile URL
LINKEDIN_URL = "https://www.linkedin.com/"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* =========================================================
   GLOBAL
   ========================================================= */

:root {
    --bg: #030507;
    --cyan: #00d9ff;
    --blue: #147cff;
    --white: #ffffff;
    --muted: #9aa5b2;
    --border: rgba(255,255,255,0.10);
    --glass: rgba(255,255,255,0.045);
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(0,217,255,0.09),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(20,124,255,0.08),
            transparent 28%
        ),
        #030507;

    color: white;
    font-family: 'Inter', sans-serif;
}

/* Subtle background grid */

.stApp::before {
    content: "";

    position: fixed;
    inset: 0;

    background-image:
        linear-gradient(
            rgba(0,217,255,0.025) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(0,217,255,0.025) 1px,
            transparent 1px
        );

    background-size: 60px 60px;

    pointer-events: none;
    z-index: 0;

    mask-image: linear-gradient(
        to bottom,
        black,
        transparent 75%
    );
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"] {
    display: none;
}

.block-container {
    max-width: 1200px;

    padding-top: 1rem;
    padding-bottom: 5rem;

    position: relative;
    z-index: 2;
}

/* =========================================================
   NAVBAR
   ========================================================= */

.navbar {
    position: sticky;

    top: 12px;

    z-index: 999;

    width: 100%;

    padding: 15px 24px;

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 18px;

    background: rgba(4,7,10,0.88);

    backdrop-filter: blur(18px);

    margin-bottom: 20px;
}

.nav-inner {
    display: flex;

    justify-content: space-between;

    align-items: center;

    gap: 25px;
}

.nav-logo {
    color: white;

    text-decoration: none;

    font-family: 'Space Grotesk', sans-serif;

    font-size: 19px;

    font-weight: 700;

    letter-spacing: 2px;
}

.nav-logo span {
    color: var(--cyan);
}

.nav-links {
    display: flex;

    gap: 24px;

    flex-wrap: wrap;

    justify-content: flex-end;
}

.nav-links a {
    color: #b8c0ca;

    text-decoration: none;

    font-size: 10px;

    font-weight: 700;

    letter-spacing: 1.3px;

    transition: 0.3s ease;
}

.nav-links a:hover {
    color: var(--cyan);
}

/* =========================================================
   HERO
   ========================================================= */

.hero {
    min-height: 82vh;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    padding: 70px 20px 100px;

    position: relative;
}

/* Background glow */

.hero::before {
    content: "";

    position: absolute;

    width: 500px;
    height: 500px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(0,217,255,0.12),
            rgba(0,217,255,0.02) 45%,
            transparent 70%
        );

    filter: blur(10px);

    z-index: -1;

    animation: heroPulse 4s ease-in-out infinite alternate;
}

/* Small badge */

.hero-badge {
    display: inline-block;

    padding: 9px 17px;

    border-radius: 999px;

    border: 1px solid rgba(0,217,255,0.35);

    background: rgba(0,217,255,0.045);

    color: var(--cyan);

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 4px;

    margin-bottom: 30px;

    animation: fadeUp 0.8s ease both;
}

/* MAIN NAME */

.hero-title {
    margin: 0;

    font-family: 'Space Grotesk', sans-serif;

    font-size: clamp(55px, 10vw, 115px);

    line-height: 1;

    font-weight: 600;

    letter-spacing: 3px;

    text-transform: uppercase;

    color: #ffffff;

    animation: fadeUp 1s ease 0.1s both;
}

.hero-title span {
    color: var(--cyan);

    margin-left: 25px;

    font-weight: 700;

    letter-spacing: 5px;

    text-shadow:
        0 0 15px rgba(0,217,255,0.35),
        0 0 45px rgba(0,217,255,0.12);
}

/* Role */

.hero-role {
    margin-top: 28px;

    font-family: 'Space Grotesk', sans-serif;

    color: #d9dee5;

    font-size: clamp(19px, 3vw, 27px);

    font-weight: 500;

    animation: fadeUp 1s ease 0.2s both;
}

.hero-role span {
    color: var(--cyan);

    padding: 0 6px;
}

/* Glow line */

.hero-line {
    width: 160px;

    height: 3px;

    margin: 30px auto;

    border-radius: 20px;

    background: var(--cyan);

    box-shadow:
        0 0 8px var(--cyan),
        0 0 28px rgba(0,217,255,0.55);

    animation: glow 2s ease-in-out infinite alternate;
}

/* Description */

.hero-description {
    max-width: 720px;

    color: var(--muted);

    font-size: 14px;

    line-height: 1.9;

    animation: fadeUp 1s ease 0.3s both;
}

/* Hero buttons */

.hero-buttons {
    display: flex;

    justify-content: center;

    flex-wrap: wrap;

    gap: 12px;

    margin-top: 30px;

    animation: fadeUp 1s ease 0.4s both;
}

.hero-button {
    display: inline-block;

    padding: 12px 19px;

    border-radius: 10px;

    text-decoration: none !important;

    font-size: 11px;

    font-weight: 700;

    transition: 0.35s ease;
}

.hero-primary {
    color: #001018 !important;

    background: var(--cyan);

    box-shadow:
        0 0 20px rgba(0,217,255,0.15);
}

.hero-primary:hover {
    transform: translateY(-4px);

    box-shadow:
        0 0 30px rgba(0,217,255,0.45);
}

.hero-secondary {
    color: white !important;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.12);
}

.hero-secondary:hover {
    color: var(--cyan) !important;

    border-color: var(--cyan);

    transform: translateY(-4px);
}

/* =========================================================
   SECTIONS
   ========================================================= */

.section {
    padding: 80px 0;

    scroll-margin-top: 100px;
}

.section-label {
    color: var(--cyan);

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 4px;

    margin-bottom: 10px;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif;

    color: white;

    font-size: clamp(30px, 5vw, 47px);

    font-weight: 700;

    letter-spacing: -1px;

    margin-bottom: 42px;
}

.section-title span {
    color: var(--cyan);
}

/* =========================================================
   GLASS
   ========================================================= */

.glass {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.06),
            rgba(255,255,255,0.018)
        );

    border: 1px solid var(--border);

    border-radius: 24px;

    backdrop-filter: blur(18px);

    transition:
        transform 0.4s ease,
        border-color 0.4s ease,
        box-shadow 0.4s ease;
}

.glass:hover {
    transform: translateY(-7px);

    border-color: rgba(0,217,255,0.40);

    box-shadow:
        0 20px 50px rgba(0,0,0,0.35),
        0 0 25px rgba(0,217,255,0.05);
}

/* =========================================================
   ABOUT
   ========================================================= */

.about-card {
    padding: 40px;
}

.about-heading {
    color: white;

    font-family: 'Space Grotesk', sans-serif;

    font-size: 25px;

    font-weight: 700;

    margin-bottom: 17px;
}

.about-text {
    color: #aeb7c2;

    font-size: 14px;

    line-height: 1.95;
}

.focus-card {
    padding: 25px;

    text-align: center;

    height: 100%;
}

.focus-icon {
    font-size: 30px;

    margin-bottom: 12px;
}

.focus-title {
    color: white;

    font-family: 'Space Grotesk', sans-serif;

    font-size: 16px;

    font-weight: 700;

    margin-bottom: 7px;
}

.focus-text {
    color: #858f9c;

    font-size: 11px;

    line-height: 1.7;
}

/* =========================================================
   STATS
   ========================================================= */

.stat-card {
    padding: 24px;

    text-align: center;
}

.stat-number {
    color: var(--cyan);

    font-family: 'Space Grotesk', sans-serif;

    font-size: 32px;

    font-weight: 700;
}

.stat-label {
    color: #7f8996;

    font-size: 10px;

    font-weight: 700;

    letter-spacing: 1px;

    text-transform: uppercase;

    margin-top: 5px;
}

/* =========================================================
   EXPERIENCE
   ========================================================= */

.timeline {
    position: relative;

    padding-left: 32px;
}

.timeline::before {
    content: "";

    position: absolute;

    left: 5px;

    top: 5px;

    bottom: 5px;

    width: 2px;

    background:
        linear-gradient(
            to bottom,
            var(--cyan),
            rgba(0,217,255,0.04)
        );
}

.timeline-item {
    position: relative;

    padding: 30px;

    margin-bottom: 30px;
}

.timeline-item::before {
    content: "";

    position: absolute;

    left: -32px;

    top: 35px;

    width: 13px;

    height: 13px;

    border-radius: 50%;

    background: var(--cyan);

    box-shadow:
        0 0 10px var(--cyan),
        0 0 25px rgba(0,217,255,0.45);
}

.timeline-date {
    display: inline-block;

    padding: 6px 11px;

    border-radius: 999px;

    color: var(--cyan);

    background: rgba(0,217,255,0.06);

    border: 1px solid rgba(0,217,255,0.20);

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1px;

    margin-bottom: 15px;
}

.timeline-title {
    color: white;

    font-family: 'Space Grotesk', sans-serif;

    font-size: 22px;

    font-weight: 700;
}

.timeline-company {
    color: var(--cyan);

    font-size: 13px;

    font-weight: 700;

    margin: 6px 0 18px;
}

.timeline-text {
    color: #9da6b2;

    font-size: 13px;

    line-height: 1.85;
}

/* =========================================================
   SKILLS
   ========================================================= */

.skill-card {
    padding: 27px;

    margin-bottom: 18px;
}

.skill-heading {
    color: white;

    font-family: 'Space Grotesk', sans-serif;

    font-size: 16px;

    font-weight: 700;

    margin-bottom: 17px;
}

.skill-pills {
    display: flex;

    flex-wrap: wrap;

    gap: 8px;
}

.skill-pill {
    padding: 8px 12px;

    border-radius: 999px;

    color: #cbd3dc;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.09);

    font-size: 10px;

    font-weight: 600;

    transition: 0.3s ease;
}

.skill-pill:hover {
    color: var(--cyan);

    border-color: var(--cyan);

    background: rgba(0,217,255,0.05);

    transform: translateY(-3px);
}

/* =========================================================
   PROJECTS
   ========================================================= */

.project-card {
    padding: 32px;

    position: relative;

    overflow: hidden;

    height: 100%;
}

.project-number {
    position: absolute;

    right: 22px;

    top: 12px;

    color: rgba(0,217,255,0.09);

    font-family: 'Space Grotesk', sans-serif;

    font-size: 65px;

    font-weight: 700;
}

.project-icon {
    font-size: 38px;

    margin-bottom: 18px;
}

.project-title {
    color: white;

    font-family: 'Space Grotesk', sans-serif;

    font-size: 24px;

    font-weight: 700;
}

.project-subtitle {
    color: var(--cyan);

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 1px;

    margin-top: 7px;

    margin-bottom: 18px;
}

.project-description {
    color: #9ca6b2;

    font-size: 12px;

    line-height: 1.85;
}

.project-tags {
    display: flex;

    flex-wrap: wrap;

    gap: 7px;

    margin-top: 20px;

    margin-bottom: 22px;
}

.project-tag {
    color: #bdc7d1;

    padding: 6px 9px;

    border-radius: 7px;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.07);

    font-size: 9px;
}

.project-buttons {
    display: flex;

    flex-wrap: wrap;

    gap: 10px;
}

.project-button {
    display: inline-block;

    color: white !important;

    text-decoration: none !important;

    padding: 10px 14px;

    border-radius: 9px;

    background: rgba(0,217,255,0.06);

    border: 1px solid rgba(0,217,255,0.23);

    font-size: 10px;

    font-weight: 700;

    transition: 0.3s ease;
}

.project-button:hover {
    color: #001018 !important;

    background: var(--cyan);

    border-color: var(--cyan);

    transform: translateY(-3px);
}

/* =========================================================
   EDUCATION
   ========================================================= */

.education-card {
    padding: 35px;
}

.education-icon {
    font-size: 35px;

    margin-bottom: 18px;
}

.education-title {
    color: white;

    font-family: 'Space Grotesk', sans-serif;

    font-size: 21px;

    font-weight: 700;
}

.education-place {
    color: var(--cyan);

    font-size: 13px;

    font-weight: 700;

    margin: 7px 0;
}

.education-date {
    color: #7f8996;

    font-size: 12px;
}

.cgpa {
    display: inline-block;

    margin-top: 20px;

    padding: 9px 14px;

    border-radius: 10px;

    color: var(--cyan);

    background: rgba(0,217,255,0.06);

    border: 1px solid rgba(0,217,255,0.20);

    font-size: 11px;

    font-weight: 800;
}

/* =========================================================
   CERTIFICATIONS
   ========================================================= */

.cert-card {
    padding: 21px;

    display: flex;

    gap: 15px;

    align-items: flex-start;

    margin-bottom: 14px;
}

.cert-icon {
    width: 40px;

    height: 40px;

    display: flex;

    align-items: center;

    justify-content: center;

    flex-shrink: 0;

    border-radius: 12px;

    color: var(--cyan);

    background: rgba(0,217,255,0.07);

    font-size: 17px;
}

.cert-name {
    color: white;

    font-size: 13px;

    font-weight: 700;
}

.cert-org {
    color: #7d8794;

    font-size: 10px;

    margin-top: 5px;

    line-height: 1.5;
}

/* =========================================================
   CONTACT
   ========================================================= */

.contact-card {
    padding: 60px 30px;

    text-align: center;

    background:
        radial-gradient(
            circle at center,
            rgba(0,217,255,0.08),
            transparent 60%
        ),
        rgba(255,255,255,0.035);
}

.contact-title {
    color: white;

    font-family: 'Space Grotesk', sans-serif;

    font-size: clamp(30px, 5vw, 48px);

    font-weight: 700;
}

.contact-title span {
    color: var(--cyan);
}

.contact-text {
    max-width: 650px;

    margin: 15px auto 28px;

    color: #929ca9;

    font-size: 13px;

    line-height: 1.8;
}

.contact-buttons {
    display: flex;

    justify-content: center;

    flex-wrap: wrap;

    gap: 12px;
}

.contact-button {
    display: inline-block;

    color: white !important;

    text-decoration: none !important;

    padding: 12px 18px;

    border-radius: 10px;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.10);

    font-size: 10px;

    font-weight: 700;

    transition: 0.3s ease;
}

.contact-button:hover {
    color: var(--cyan) !important;

    border-color: var(--cyan);

    transform: translateY(-3px);
}

/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;

    margin-top: 70px;

    padding: 40px 20px;

    border-top: 1px solid rgba(255,255,255,0.08);
}

.footer-name {
    font-family: 'Space Grotesk', sans-serif;

    color: white;

    font-size: 20px;

    font-weight: 700;

    letter-spacing: 2px;
}

.footer-name span {
    color: var(--cyan);
}

.footer-text {
    color: #69727f;

    font-size: 10px;

    margin-top: 8px;
}

/* =========================================================
   ANIMATIONS
   ========================================================= */

@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(25px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }

}

@keyframes glow {

    from {
        opacity: 0.55;
        transform: scaleX(0.85);
    }

    to {
        opacity: 1;
        transform: scaleX(1.05);
    }

}

@keyframes heroPulse {

    from {
        transform: scale(0.9);
        opacity: 0.5;
    }

    to {
        transform: scale(1.1);
        opacity: 1;
    }

}

/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .navbar {
        position: relative;
        top: 0;
    }

    .nav-inner {
        flex-direction: column;
    }

    .nav-links {
        justify-content: center;
        gap: 11px;
    }

    .nav-links a {
        font-size: 8px;
    }

    .hero {
        min-height: 70vh;

        padding-top: 45px;
    }

    .hero-title {
        font-size: clamp(48px, 15vw, 78px);

        letter-spacing: 1px;
    }

    .hero-title span {
        margin-left: 12px;

        letter-spacing: 2px;
    }

    .hero-badge {
        font-size: 8px;

        letter-spacing: 2px;
    }

    .hero-description {
        font-size: 13px;
    }

    .section {
        padding: 60px 0;
    }

    .about-card,
    .project-card,
    .education-card {
        padding: 25px;
    }

    .timeline {
        padding-left: 25px;
    }

    .timeline-item::before {
        left: -25px;
    }

}


/* ===== 3D PORTFOLIO HERO ===== */
.hero{
min-height:82vh;display:grid;grid-template-columns:1.05fr .95fr;align-items:center;gap:30px;
text-align:left;padding:55px 20px 90px;position:relative;perspective:1200px}
.hero-copy{position:relative;z-index:5;padding-left:18px}
.hero-copy .hero-badge{margin-bottom:24px}
.hero-copy .hero-title{font-size:clamp(55px,7vw,105px)}
.hero-copy .hero-description{max-width:620px}
.hero-copy .hero-buttons{justify-content:flex-start}
.hero-3d-stage{position:relative;min-height:450px;display:grid;place-items:center;perspective:1000px;transform-style:preserve-3d}
.hero-3d-stage:before{content:"";position:absolute;width:380px;height:380px;border-radius:50%;
background:radial-gradient(circle,rgba(0,217,255,.16),rgba(20,124,255,.08) 38%,transparent 70%);
filter:blur(15px);animation:coreGlow 4s ease-in-out infinite alternate}
.cyber-orb{width:245px;height:245px;position:relative;border-radius:50%;transform-style:preserve-3d;
animation:orbFloat 5s ease-in-out infinite;
background:radial-gradient(circle at 32% 27%,rgba(255,255,255,.65),transparent 5%),
radial-gradient(circle at 40% 35%,rgba(0,217,255,.22),transparent 26%),
radial-gradient(circle at 68% 70%,rgba(20,124,255,.18),transparent 34%),rgba(2,10,15,.72);
border:1px solid rgba(0,217,255,.65);
box-shadow:inset -25px -20px 50px rgba(0,0,0,.72),inset 15px 15px 40px rgba(0,217,255,.14),
0 0 35px rgba(0,217,255,.35),0 0 90px rgba(20,124,255,.16)}
.cyber-orb:before,.cyber-orb:after{content:"";position:absolute;inset:13px;border-radius:50%;border:1px solid rgba(0,217,255,.28)}
.cyber-orb:before{transform:rotateY(68deg)}.cyber-orb:after{transform:rotateX(68deg)}
.orb-grid{position:absolute;inset:26px;border-radius:50%;border:1px dashed rgba(0,217,255,.24);
transform:rotateY(35deg) rotateX(25deg);animation:orbGrid 8s linear infinite}
.orb-core{position:absolute;inset:83px;border-radius:50%;background:rgba(0,217,255,.18);
box-shadow:0 0 18px rgba(0,217,255,.9),0 0 45px rgba(0,217,255,.5);
animation:corePulse 2.2s ease-in-out infinite alternate}
.orbit{position:absolute;border:1px solid rgba(0,217,255,.38);border-radius:50%;transform-style:preserve-3d}
.orbit-one{width:330px;height:105px;transform:rotateX(68deg) rotateZ(-15deg);animation:orbitOne 8s linear infinite}
.orbit-two{width:350px;height:125px;transform:rotateY(67deg) rotateZ(12deg);animation:orbitTwo 10s linear infinite;border-color:rgba(20,124,255,.38)}
.orbit-three{width:300px;height:180px;transform:rotateX(62deg) rotateY(25deg);animation:orbitThree 12s linear infinite;border-color:rgba(0,217,255,.22)}
.orbit-dot{position:absolute;width:9px;height:9px;border-radius:50%;background:var(--cyan);box-shadow:0 0 14px var(--cyan),0 0 28px rgba(0,217,255,.7)}
.dot-a{top:-5px;left:42%}.dot-b{right:15px;top:42%;background:#147cff;box-shadow:0 0 14px #147cff,0 0 28px rgba(20,124,255,.65)}.dot-c{bottom:-5px;left:22%}
.particle{position:absolute;width:4px;height:4px;border-radius:50%;background:var(--cyan);box-shadow:0 0 12px var(--cyan);opacity:.7}
.p1{top:12%;left:12%;animation:particleFloat 4s ease-in-out infinite}.p2{top:18%;right:12%;animation:particleFloat 5s ease-in-out .8s infinite}
.p3{bottom:18%;left:17%;animation:particleFloat 4.5s ease-in-out 1.2s infinite}.p4{bottom:12%;right:16%;animation:particleFloat 5.5s ease-in-out .4s infinite}
.p5{top:47%;left:4%;animation:particleFloat 4.2s ease-in-out 1.7s infinite}.p6{top:55%;right:4%;animation:particleFloat 5s ease-in-out 1s infinite}
.three-d-label{position:absolute;bottom:12px;color:rgba(190,235,243,.7);font-size:9px;font-weight:800;letter-spacing:3px;text-transform:uppercase}
@keyframes orbFloat{0%,100%{transform:translateY(0) rotateX(4deg) rotateY(-8deg)}50%{transform:translateY(-14px) rotateX(-5deg) rotateY(12deg)}}
@keyframes orbGrid{from{transform:rotateY(0) rotateX(25deg)}to{transform:rotateY(360deg) rotateX(25deg)}}
@keyframes orbitOne{from{transform:rotateX(68deg) rotateZ(-15deg) rotate(0)}to{transform:rotateX(68deg) rotateZ(-15deg) rotate(360deg)}}
@keyframes orbitTwo{from{transform:rotateY(67deg) rotateZ(12deg) rotate(360deg)}to{transform:rotateY(67deg) rotateZ(12deg) rotate(0)}}
@keyframes orbitThree{from{transform:rotateX(62deg) rotateY(25deg) rotate(0)}to{transform:rotateX(62deg) rotateY(25deg) rotate(360deg)}}
@keyframes corePulse{from{transform:scale(.82);opacity:.65}to{transform:scale(1.18);opacity:1}}
@keyframes coreGlow{from{transform:scale(.85);opacity:.45}to{transform:scale(1.12);opacity:.9}}
@keyframes particleFloat{0%,100%{transform:translate3d(0,0,0);opacity:.35}50%{transform:translate3d(0,-22px,18px);opacity:1}}
.glass{transform-style:preserve-3d;perspective:900px}
.project-card,.skill-card,.focus-card,.timeline-item,.education-card,.cert-card,.stat-card,.contact-card{transform-style:preserve-3d}
.project-card:hover,.focus-card:hover,.skill-card:hover,.timeline-item:hover,.education-card:hover,.cert-card:hover,.stat-card:hover{transform:translateY(-7px) rotateX(1.5deg) rotateY(-1.5deg)}
@media(max-width:900px){.hero{grid-template-columns:1fr;text-align:center}.hero-copy{padding-left:0}.hero-copy .hero-description{margin-left:auto;margin-right:auto}.hero-copy .hero-buttons{justify-content:center}.hero-3d-stage{min-height:390px}}
@media(max-width:768px){.hero{padding-top:40px}.hero-3d-stage{min-height:330px;transform:scale(.82)}.cyber-orb{width:205px;height:205px}.orbit-one{width:275px;height:90px}.orbit-two{width:295px;height:105px}.orbit-three{width:260px;height:155px}}
@media(prefers-reduced-motion:reduce){.cyber-orb,.orb-grid,.orbit,.particle,.orb-core,.hero-3d-stage:before{animation:none!important}}


/* ===== 3D HERO FIXES ===== */
.hero-copy .hero-title {
    white-space: nowrap;
}
@media (max-width: 900px) {
    .hero-copy .hero-title {
        white-space: normal;
    }
}


/* ===== FINAL HERO RENDER FIX ===== */
.hero-copy .hero-title {
    white-space: nowrap;
}
.hero-copy .hero-title span {
    display: inline-block;
}
@media (max-width: 900px) {
    .hero-copy .hero-title {
        white-space: normal;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

st.markdown("""
<div class="navbar">

<div class="nav-inner">

<a class="nav-logo" href="#home">
JANVI <span>RAJ</span>
</a>

<div class="nav-links">
<a href="#about">ABOUT</a>
<a href="#experience">EXPERIENCE</a>
<a href="#skills">SKILLS</a>
<a href="#projects">PROJECTS</a>
<a href="#education">EDUCATION</a>
<a href="#certifications">CERTIFICATIONS</a>
<a href="#contact">CONTACT</a>
</div>

</div>

</div>

<div id="home"></div>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.html("""<div class="hero"><div class="hero-copy"><div class="hero-badge">AI / MACHINE LEARNING &nbsp;•&nbsp; CYBERSECURITY</div><h1 class="hero-title">JANVI <span>RAJ</span></h1><div class="hero-role">AI/ML <span>&</span> Cybersecurity Enthusiast</div><div class="hero-line"></div><div class="hero-description">I build machine learning solutions using Python and explore cybersecurity through practical projects, industry training and hands-on experimentation.</div><div class="hero-buttons"><a class="hero-button hero-primary" href="#projects">🚀 Explore Projects</a><a class="hero-button hero-secondary" href="mailto:rjanvi727@gmail.com">📧 Contact Me</a><a class="hero-button hero-secondary" href="https://github.com/Janviraj27" target="_blank">🐙 GitHub</a></div></div><div class="hero-3d-stage"><span class="particle p1"></span><span class="particle p2"></span><span class="particle p3"></span><span class="particle p4"></span><span class="particle p5"></span><span class="particle p6"></span><div class="orbit orbit-one"><span class="orbit-dot dot-a"></span></div><div class="orbit orbit-two"><span class="orbit-dot dot-b"></span></div><div class="orbit orbit-three"><span class="orbit-dot dot-c"></span></div><div class="cyber-orb"><div class="orb-grid"></div><div class="orb-core"></div></div><div class="three-d-label">AI • ML • SECURITY • 3D</div></div></div>""")


# =========================================================
# ABOUT
# =========================================================

st.markdown("""
<div class="section" id="about">

<div class="section-label">
WHO I AM
</div>

<div class="section-title">
ABOUT <span>ME</span>
</div>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:

    st.markdown("""
<div class="glass about-card">

<div class="about-heading">
AI/ML + Cybersecurity
</div>

<div class="about-text">

I am an AI/ML and Cybersecurity graduate with hands-on experience
in Python, machine learning, data preprocessing and cybersecurity
fundamentals.

I have worked with Pandas, NumPy, Scikit-learn and Streamlit to
develop machine learning solutions. I also have practical exposure
to penetration testing, vulnerability assessment and network
security through industry training and security projects.

I enjoy learning by building practical projects and connecting
machine learning with real-world applications.

</div>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="glass focus-card">

<div class="focus-icon">
🤖
</div>

<div class="focus-title">
Machine Learning
</div>

<div class="focus-text">
Python, Pandas, NumPy, Scikit-learn,
Regression, Classification and EDA
</div>

</div>

<br>

<div class="glass focus-card">

<div class="focus-icon">
🛡️
</div>

<div class="focus-title">
Cybersecurity
</div>

<div class="focus-text">
VAPT, OWASP Top 10, Networking,
Kali Linux and security tools
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# STATS
# =========================================================

st.markdown(
    "<div style='height:35px;'></div>",
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

stats = [
    ("02", "Core Projects"),
    ("815", "Processed Records"),
    ("7.27", "BCA CGPA"),
    ("02+", "Industry Experiences"),
]

for col, (number, label) in zip(
    [c1, c2, c3, c4],
    stats
):

    with col:

        st.markdown(
            f"""
<div class="glass stat-card">

<div class="stat-number">
{number}
</div>

<div class="stat-label">
{label}
</div>

</div>
""",
            unsafe_allow_html=True
        )


# =========================================================
# EXPERIENCE
# =========================================================

st.markdown("""
<div class="section" id="experience">

<div class="section-label">
MY JOURNEY
</div>

<div class="section-title">
EXPERIENCE <span>&</span> TRAINING
</div>

<div class="timeline">

<div class="glass timeline-item">

<div class="timeline-date">
JUN 2023 — AUG 2023
</div>

<div class="timeline-title">
ML Intern
</div>

<div class="timeline-company">
Param Consulting Services
</div>

<div class="timeline-text">

Worked with Python, Pandas and Scikit-learn for data cleaning
and preparation in machine learning workflows.

<br><br>

Implemented and evaluated regression and classification models
on structured datasets.

<br><br>

Applied data analysis and preprocessing techniques to prepare
datasets for machine learning tasks.

<br><br>

Gained practical experience in developing machine learning
solutions and analyzing model results.

</div>

</div>


<div class="glass timeline-item">

<div class="timeline-date">
JUN 2025 — SEP 2025
</div>

<div class="timeline-title">
Cyber Security Analyst
</div>

<div class="timeline-company">
Tata Strive — TCS ION
</div>

<div class="timeline-text">

Hands-on experience in networking fundamentals, TCP/IP,
routing, switching and security concepts.

<br><br>

Used Kali Linux for penetration testing, vulnerability assessment
and ethical hacking.

<br><br>

Worked with Nmap, Wireshark and Metasploit for threat detection
and network analysis.

<br><br>

Experienced in LAN/WAN simulation with Cisco Packet Tracer,
including firewall, VPN and access control configuration.

</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SKILLS
# =========================================================

st.markdown("""
<div class="section" id="skills">

<div class="section-label">
WHAT I WORK WITH
</div>

<div class="section-title">
TECHNICAL <span>SKILLS</span>
</div>

</div>
""", unsafe_allow_html=True)


skill_groups = [

    (
        "🤖",
        "AI / MACHINE LEARNING",
        [
            "Python",
            "Pandas",
            "NumPy",
            "Scikit-learn",
            "Machine Learning",
            "Regression",
            "Classification",
            "EDA",
            "Feature Engineering"
        ]
    ),

    (
        "📊",
        "DATA & VISUALIZATION",
        [
            "Matplotlib",
            "Data Cleaning",
            "Data Preprocessing"
        ]
    ),

    (
        "🚀",
        "DEPLOYMENT & DEVELOPMENT",
        [
            "Streamlit",
            "Git",
            "GitHub",
            "SQL"
        ]
    ),

    (
        "🌐",
        "NETWORKING",
        [
            "IP Addressing",
            "Subnetting",
            "Network Protocols"
        ]
    ),

    (
        "🛡️",
        "CYBERSECURITY",
        [
            "SOC",
            "VAPT",
            "CIA Triad",
            "Cryptography",
            "AAA",
            "MITRE ATT&CK",
            "Malware Analysis",
            "Incident Response",
            "OWASP TOP 10"
        ]
    ),

    (
        "⚙️",
        "TOOLS",
        [
            "Cisco Packet Tracer",
            "Kali Linux",
            "Nmap",
            "Splunk",
            "Wireshark",
            "Burp Suite",
            "Metasploit"
        ]
    )

]


for icon, title, skills in skill_groups:

    pills = ""

    for skill in skills:
        pills += f'<span class="skill-pill">{skill}</span>'

    st.markdown(
        f"""
<div class="glass skill-card">

<div class="skill-heading">
{icon} &nbsp; {title}
</div>

<div class="skill-pills">
{pills}
</div>

</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# PROJECTS
# =========================================================

st.markdown("""
<div class="section" id="projects">

<div class="section-label">
SELECTED WORK
</div>

<div class="section-title">
FEATURED <span>PROJECTS</span>
</div>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")


with col1:

    st.markdown(
        f"""
<div class="glass project-card">

<div class="project-number">
01
</div>

<div class="project-icon">
🚗
</div>

<div class="project-title">
Used Car Price Prediction
</div>

<div class="project-subtitle">
MACHINE LEARNING • STREAMLIT
</div>

<div class="project-description">

Built a machine learning regression solution to predict used-car
prices using the Quikr Car dataset.

Performed data cleaning, preprocessing, EDA and feature engineering
on 815 processed records.

Applied One-Hot Encoding and trained Linear Regression, Decision
Tree and Random Forest models.

Evaluated models using MAE, RMSE and R² with 5-fold cross-validation.

Developed and deployed an interactive Streamlit application.

</div>

<div class="project-tags">

<span class="project-tag">Python</span>
<span class="project-tag">Pandas</span>
<span class="project-tag">NumPy</span>
<span class="project-tag">Scikit-learn</span>
<span class="project-tag">Streamlit</span>
<span class="project-tag">GitHub</span>

</div>

<div class="project-buttons">

<a class="project-button"
href="{CAR_PROJECT_URL}"
target="_blank">
🐙 GitHub
</a>

<a class="project-button"
href="{LIVE_DEMO_URL}"
target="_blank">
🚀 Live Demo
</a>

</div>

</div>
""",
        unsafe_allow_html=True
    )


with col2:

    st.markdown("""
<div class="glass project-card">

<div class="project-number">
02
</div>

<div class="project-icon">
🔐
</div>

<div class="project-title">
PortSwigger Labs
</div>

<div class="project-subtitle">
WEB SECURITY • OWASP TOP 10
</div>

<div class="project-description">

Performed penetration testing on simulated web applications
targeting OWASP Top 10 vulnerabilities.

Worked with Clickjacking, Broken Access Control, Authentication
Bypass, Path Traversal and XSS labs.

Used Burp Suite, HTTP request manipulation and payload injection
for vulnerability discovery and proof-of-concept testing.

Conducted session analysis and risk assessment and documented
attack vectors and remediation strategies.

</div>

<div class="project-tags">

<span class="project-tag">Burp Suite</span>
<span class="project-tag">OWASP</span>
<span class="project-tag">HTTP</span>
<span class="project-tag">XSS</span>
<span class="project-tag">VAPT</span>
<span class="project-tag">Web Security</span>

</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# EDUCATION
# =========================================================

st.markdown("""
<div class="section" id="education">

<div class="section-label">
ACADEMIC BACKGROUND
</div>

<div class="section-title">
EDU<span>CATION</span>
</div>

<div class="glass education-card">

<div class="education-icon">
🎓
</div>

<div class="education-title">
Bachelor of Computer Applications — BCA
</div>

<div class="education-place">
Shree D.N. Institute of SPU
</div>

<div class="education-date">
2021 — 2023 &nbsp; • &nbsp; Anand
</div>

<div class="cgpa">
CGPA 7.27 / 10
</div>

</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# CERTIFICATIONS
# =========================================================

st.markdown("""
<div class="section" id="certifications">

<div class="section-label">
LEARNING
</div>

<div class="section-title">
CERTIFI<span>CATIONS</span>
</div>

</div>
""", unsafe_allow_html=True)


certs = [

    (
        "🤖",
        "Introduction to Modern AI",
        "Cisco Networking Academy • Sep 2025"
    ),

    (
        "📚",
        "Introduction to Machine Learning using Python",
        "Param Consulting Services • Jun 2024"
    ),

    (
        "🛡️",
        "Cyber Security Analyst",
        "Tata Strive — TCS ION • Sep 2025"
    ),

    (
        "🔐",
        "Introduction to Cybersecurity",
        "Cisco Networking Academy • Sep 2024"
    )

]


for icon, name, organization in certs:

    st.markdown(
        f"""
<div class="glass cert-card">

<div class="cert-icon">
{icon}
</div>

<div>

<div class="cert-name">
{name}
</div>

<div class="cert-org">
{organization}
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# CONTACT
# =========================================================

st.markdown(
    f"""
<div class="section" id="contact">

<div class="glass contact-card">

<div class="section-label">
GET IN TOUCH
</div>

<div class="contact-title">
LET'S <span>CONNECT.</span>
</div>

<div class="contact-text">

Interested in AI/ML, data science, cybersecurity and practical
technology projects. Feel free to connect with me for
opportunities, collaborations or project discussions.

</div>

<div class="contact-buttons">

<a class="contact-button"
href="mailto:rjanvi727@gmail.com">
📧 Email
</a>

<a class="contact-button"
href="{GITHUB_URL}"
target="_blank">
🐙 GitHub
</a>

<a class="contact-button"
href="{LINKEDIN_URL}"
target="_blank">
💼 LinkedIn
</a>

</div>

<div style="
margin-top:25px;
color:#737d8a;
font-size:11px;
">
📍 Vadodara, Gujarat &nbsp; • &nbsp;
rjanvi727@gmail.com
</div>

</div>

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

<div class="footer-name">
JANVI <span>RAJ</span>
</div>

<div class="footer-text">
AI/ML & Cybersecurity Enthusiast
</div>

<div class="footer-text">
Built with Python + Streamlit
</div>

</div>
""", unsafe_allow_html=True)
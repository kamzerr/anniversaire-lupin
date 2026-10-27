# 🎩 Quête d'Anniversaire « Arsène Lupin »

> *« L'impossible n'est qu'un mot pour les cambrioleurs sans imagination. »*

Jeu de piste immersif à domicile conçu pour un anniversaire de mariage, inspiré de l'univers d'**Arsène Lupin, gentleman cambrioleur**.  
Le parcours comporte **5 étapes physiques** chaînées par des QR codes élégants et des pages web interactives scellées par des codes secrets.

---

## 🧭 Matrice du Scénario & Parcours Physique

| Étape | Fichier HTML | Emplacement QR Code | Énigme & Thème | Codes secrets acceptés | Destination révélée |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | [`index.html`](index.html) | Chambre (téléphone / réveil) | Énigme du miroir et du reflet | `MIROIR`, `REFLET` | **Salle de bain (étage)** $\rightarrow$ flacons de parfum |
| **1** | [`les-elixirs.html`](les-elixirs.html) | Salle de bain (sous un parfum) | Charade *Toc* + *Hante* | `TOCANTE`, `TOCANTES` | **Salon** $\rightarrow$ armoire aux montres |
| **2** | [`le-maitre-du-temps.html`](le-maitre-du-temps.html) | Salon (boîte à montres) | Rébus phonétique (*Bu-An-Deux-Riz*) | `BUANDERIE` | **Buanderie** $\rightarrow$ tambour du sèche-linge |
| **3** | [`le-souffle-chaud.html`](le-souffle-chaud.html) | Buanderie (dans le sèche-linge) | Énigme d'Orient et des banquettes | `SEDARI`, `SDARI`, `CANAPE` | **Salon** $\rightarrow$ sous un coussin du sedari |
| **4** | [`l-escale-d-orient.html`](l-escale-d-orient.html) | Sedari (sous le coussin central) | Énigme du tissu floral | `FLEUR`, `FLEURS` | **Salon** $\rightarrow$ derrière le fauteuil fleuri (**Cadeau**) 🎁 |

---

## 🎨 Charte Graphique & Conception

- **Ambiance :** Bureau feutré début XXᵉ siècle, gentleman cambrioleur, mystère élégant.
- **Typographies :**
  - Titres et sceau : Google Fonts `Cinzel` (serif impérial, majuscules et interlettrage raffiné).
  - Textes d'énigmes : Google Fonts `Cormorant Garamond` (serif haute lisibilité, interligne 1.6).
- **Palette de couleurs :**
  - Fond ténébreux : `#0f1115`
  - Carte centrale : `#181a20` avec liseré or vieilli `#997d25`
  - Accents dorés : `#d4af37` (or classique) & `#f7e7a9` (or lumineux)
  - Typographie texte : `#e6e6e6`
  - Sceau monogramme : Émail carmin `#7a1f1d` cerclé d'or
  - Erreur de saisie : `#e06c75`
- **Expérience Mobile First :**
  - Conteneur centré compact (`max-width: 480px`).
  - Tolérance automatique aux accents, espaces et minuscules via normalisation Unicode NFD.
  - Champ de saisie optimisé mobile (`autocapitalize="none"`, `autocorrect="off"`, `spellcheck="false"`).
  - Animations de secousse (*shake*) en cas d'erreur et transition douce (*fadeIn*) lors du déverrouillage.

---

## 📁 Structure du Répertoire

```text
.
├── .gitignore               # Exclusions Git (fichiers temporaires, venv, cache)
├── style.css                # Feuille de style partagée (Design System Lupin)
├── index.html               # Prologue (Étape 0 — Chambre / Réveil)
├── les-elixirs.html         # Chapitre I (Étape 1 — Salle de bain / Parfums)
├── le-maitre-du-temps.html  # Chapitre II (Étape 2 — Armoire salon / Montres)
├── le-souffle-chaud.html    # Chapitre III (Étape 3 — Buanderie / Sèche-linge)
├── l-escale-d-orient.html   # Chapitre Final (Étape 4 — Sedari / Cadeau)
├── requirements.txt         # Dépendances Python (qrcode, Pillow)
├── generate_qrcodes.py      # Script de génération des cartes QR imprimables
└── README.md                # Documentation complète
```

---

## 🚀 Déploiement sur Cloudflare Pages (Gratuit & Instantané)

1. **Créer un dépôt GitHub** :
   ```bash
   git init
   git add .
   git commit -m "feat: Quête d'Anniversaire Arsène Lupin"
   git branch -M main
   git remote add origin https://github.com/<votre-utilisateur>/anniversaire-lupin.git
   git push -u origin main
   ```

2. **Connecter à Cloudflare Pages** :
   - Rendez-vous sur le dashboard [Cloudflare Pages](https://dash.cloudflare.com/).
   - Cliquez sur **Workers & Pages** > **Create application** > **Pages** > **Connect to Git**.
   - Sélectionnez votre dépôt `anniversaire-lupin`.
   - Paramètres de compilation :
     - **Framework preset** : `None`
     - **Build command** : *(laisser vide)*
     - **Build output directory** : `/`
   - Cliquez sur **Save and Deploy**.

3. **URL Finale** :
   Cloudflare vous attribue une adresse du type :  
   `https://anniversaire-lupin.pages.dev`

---

## 🖨️ Génération des QR Codes Prêts à Imprimer

1. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

2. **Ajuster le nom de domaine** :
   Modifiez la variable `BASE_URL` dans [`generate_qrcodes.py`](generate_qrcodes.py) ou passez-la en variable d'environnement :
   ```bash
   # Optionnel sous PowerShell :
   $env:BASE_URL="https://votre-sous-domaine.pages.dev"
   python generate_qrcodes.py
   ```

3. **Fichiers générés** :
   - `qr_0_chambre.png` (Étape 0 — Réveil)
   - `qr_1_salle_de_bain.png` (Étape 1 — Parfums)
   - `qr_2_armoire_salon.png` (Étape 2 — Montres)
   - `qr_3_buanderie.png` (Étape 3 — Sèche-linge)
   - `qr_4_sedari.png` (Étape 4 — Sedari)

4. **Impression & Installation le Jour J** :
   - Imprimez les 5 images (format vignette ou carte de visite).
   - Découpez-les le long du cadre doré.
   - Cachez chaque QR code à son emplacement prévu selon la matrice !

---

## 🧪 Test Local

Pour tester l'expérience localement sur votre navigateur :

```bash
# Avec le serveur HTTP intégré de Python :
python -m http.server 8000
```
Puis ouvrez [`http://localhost:8000`](http://localhost:8000) sur votre navigateur ou depuis votre smartphone connecté au même réseau Wi-Fi.

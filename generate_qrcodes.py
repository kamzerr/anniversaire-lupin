import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

# CONFIGURATION DU NOM DE DOMAINE CLOUDFLARE PAGES
# Remplacer si besoin par l'URL finale fournie par Cloudflare (ex: https://anniversaire-lupin.pages.dev)
BASE_URL = os.environ.get("BASE_URL", "https://anniversaire-lupin.pages.dev")

ETAPES = [
    {
        "filename": "qr_0_chambre.png",
        "url": f"{BASE_URL}/index.html",
        "titre": "ETAPE 0 - REVEIL"
    },
    {
        "filename": "qr_1_salle_de_bain.png",
        "url": f"{BASE_URL}/les-elixirs.html",
        "titre": "ETAPE 1 - PARFUMS"
    },
    {
        "filename": "qr_2_armoire_salon.png",
        "url": f"{BASE_URL}/le-maitre-du-temps.html",
        "titre": "ETAPE 2 - TOCANTES"
    },
    {
        "filename": "qr_3_buanderie.png",
        "url": f"{BASE_URL}/le-souffle-chaud.html",
        "titre": "ETAPE 3 - SECHE-LINGE"
    },
    {
        "filename": "qr_4_sedari.png",
        "url": f"{BASE_URL}/l-escale-d-orient.html",
        "titre": "ETAPE 4 - SEDARI"
    }
]

def obtenir_police(taille, gras=False):
    """Tente de charger une police serif élégante (Georgia/Times), sinon police par défaut."""
    polices_candidats = [
        "georgiab.ttf" if gras else "georgia.ttf",
        "timesbd.ttf" if gras else "times.ttf",
        "arialbd.ttf" if gras else "arial.ttf",
        "C:\\Windows\\Fonts\\georgiab.ttf" if gras else "C:\\Windows\\Fonts\\georgia.ttf",
        "C:\\Windows\\Fonts\\timesbd.ttf" if gras else "C:\\Windows\\Fonts\\times.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
    ]
    for nom in polices_candidats:
        try:
            return ImageFont.truetype(nom, taille)
        except Exception:
            continue
    return ImageFont.load_default()

def generer_carte_qr(item):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(item["url"])
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#181a20", back_color="#ffffff").convert("RGB")

    # Dimensions carte avec bandeau supérieur
    card_w = qr_img.width + 40
    card_h = qr_img.height + 90
    card = Image.new("RGB", (card_w, card_h), "#ffffff")
    draw = ImageDraw.Draw(card)

    # Bordure dorée extérieure (liseré chic)
    draw.rectangle([0, 0, card_w - 1, card_h - 1], outline="#d4af37", width=3)
    draw.rectangle([4, 4, card_w - 5, card_h - 5], outline="#997d25", width=1)
    
    # Polices adaptées
    font_header = obtenir_police(14, gras=True)
    font_titre = obtenir_police(12, gras=False)

    # Texte de repère
    draw.text((card_w // 2, 24), "— ARSÈNE LUPIN —", fill="#997d25", anchor="mm", font=font_header)
    draw.text((card_w // 2, 47), item["titre"], fill="#181a20", anchor="mm", font=font_titre)

    # Collage du QR Code
    card.paste(qr_img, (20, 65))
    card.save(item["filename"])
    print(f"[OK] Généré : {item['filename']} -> {item['url']}")

if __name__ == "__main__":
    print(f"Génération des QR Codes pour le domaine : {BASE_URL}")
    for etape in ETAPES:
        generer_carte_qr(etape)
    print("Terminé ! 5 cartes QR codes prêtes pour l'impression.")

"""
================================================================================
  GreatStore — Complete Database Management File
  Live Site : https://web-production-d1b6d.up.railway.app/
  Generated : 2026-07-08
================================================================================

  This single file contains the ENTIRE GreatStore database layer:

    CATEGORIES  (8)
      👕 Clothes  ⌚ Watches  👟 Shoes  👜 Bags
      💎 Jewelry  🕶️ Sunglasses  🧢 Hats  🎀 Accessories

    PRODUCTS  (47 across all 8 categories)
      Fields: name, slug, category, price, original_price, discount_percent,
              image_url, description, rating, stock, is_featured

    CART SYSTEM
      Cart  →  CartItem  (session-based, no login required)

    ORDER SYSTEM
      Order  →  OrderItem
      Statuses : pending | processing | shipped | delivered | cancelled
      Pay status: unpaid | paid | failed

    PAYMENT GATEWAYS
      💳 Credit/Debit Card  🔵 Khalti  🟢 eSewa  📱 Fonepay  🚚 Cash on Delivery

  ── HOW TO USE ────────────────────────────────────────────────────────────────
    python greatstore_database.py seed     # Add/update all categories & products
    python greatstore_database.py reset    # Delete everything then re-seed
    python greatstore_database.py report   # Print full database report
    python greatstore_database.py stats    # Print dashboard statistics
    python greatstore_database.py summary  # Print quick reference card
    python greatstore_database.py help     # Show this help
================================================================================
"""

import os
import sys
import django


# ─────────────────────────────────────────────────────────────────────────────
# Bootstrap Django when run as a standalone script
# ─────────────────────────────────────────────────────────────────────────────
def _bootstrap_django():
    if not os.environ.get("DJANGO_SETTINGS_MODULE"):
        here = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, here)
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Greatstore.settings")
    try:
        django.setup()
    except RuntimeError:
        pass  # Already set up (e.g. called from Django shell)


# =============================================================================
#  SECTION 1  —  CATEGORIES
# =============================================================================

CATEGORIES = [
    {
        "name": "Clothes",
        "slug": "clothes",
        "icon": "👕",
        "description": "Men and women fashion clothing — everyday essentials to luxury pieces.",
    },
    {
        "name": "Watches",
        "slug": "watches",
        "icon": "⌚",
        "description": "Luxury and sport timepieces for every style and budget.",
    },
    {
        "name": "Shoes",
        "slug": "shoes",
        "icon": "👟",
        "description": "Sneakers, heels, boots and more for men and women.",
    },
    {
        "name": "Bags",
        "slug": "bags",
        "icon": "👜",
        "description": "Handbags, backpacks, clutches, and wallets.",
    },
    {
        "name": "Jewelry",
        "slug": "jewelry",
        "icon": "💎",
        "description": "Rings, necklaces, bracelets, and earrings in gold and silver.",
    },
    {
        "name": "Sunglasses",
        "slug": "sunglasses",
        "icon": "🕶️",
        "description": "Designer and sport eyewear with UV400 protection.",
    },
    {
        "name": "Hats",
        "slug": "hats",
        "icon": "🧢",
        "description": "Caps, fedoras, beanies and more headwear styles.",
    },
    {
        "name": "Accessories",
        "slug": "accessories",
        "icon": "🎀",
        "description": "Scarves, belts, gloves, wallets and fashion accessories.",
    },
]


# =============================================================================
#  SECTION 2  —  PRODUCTS  (47 products, fetched from live site)
#
#  Exchange rate hardcoded in site: 1 USD = 133 NPR
#  All prices are in USD; NPR shown via price_npr property
# =============================================================================

PRODUCTS = [

    # ── CLOTHES (10 products) ─────────────────────────────────────────────────
    {
        "name": "Classic White T-Shirt",
        "slug": "classic-white-t-shirt",
        "category": "Clothes",
        "price": 29.99,
        "original_price": 49.99,
        "discount_percent": 40,
        "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=600&q=80",
        "description": "Soft premium cotton essential white tee. Pre-shrunk fabric ensures a consistent fit wash after wash. Available in XS–XXL. Perfect for any occasion.",
        "is_featured": True,
        "rating": 4.6,
        "stock": 150,
    },
    {
        "name": "Floral Summer Dress",
        "slug": "floral-summer-dress",
        "category": "Clothes",
        "price": 79.99,
        "original_price": 119.99,
        "discount_percent": 33,
        "image_url": "https://images.unsplash.com/photo-1572804013427-4d7ca7268217?w=600&q=80",
        "description": "Light floral print midi dress in breathable chiffon. Adjustable spaghetti straps, smocked back for a flattering fit. Ideal for sunny days and beach outings.",
        "is_featured": True,
        "rating": 4.8,
        "stock": 80,
    },
    {
        "name": "Denim Jacket",
        "slug": "denim-jacket",
        "category": "Clothes",
        "price": 99.99,
        "original_price": None,
        "discount_percent": 0,
        "image_url": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600&q=80",
        "description": "Versatile classic denim jacket in 100% cotton. Button-front closure with two chest pockets. Timeless casual look that pairs with anything.",
        "is_featured": False,
        "rating": 4.4,
        "stock": 60,
    },
    {
        "name": "Sports Hoodie",
        "slug": "sports-hoodie",
        "category": "Clothes",
        "price": 59.99,
        "original_price": 89.99,
        "discount_percent": 33,
        "image_url": "https://images.unsplash.com/photo-1556821840-3a63f15732ce?w=600&q=80",
        "description": "Heavyweight fleece-lined hoodie with kangaroo pocket and adjustable drawstring. Ideal for workouts, morning jogs, and casual wear.",
        "is_featured": True,
        "rating": 4.7,
        "stock": 120,
    },
    {
        "name": "Slim Fit Chinos",
        "slug": "slim-fit-chinos",
        "category": "Clothes",
        "price": 69.99,
        "original_price": 99.99,
        "discount_percent": 30,
        "image_url": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=600&q=80",
        "description": "Smart slim-fit chinos in stretch cotton blend. Available in khaki, navy, olive, and black. Versatile from office to weekend brunch.",
        "is_featured": False,
        "rating": 4.3,
        "stock": 90,
    },
    {
        "name": "Silk Evening Blouse",
        "slug": "silk-evening-blouse",
        "category": "Clothes",
        "price": 89.99,
        "original_price": 129.99,
        "discount_percent": 31,
        "image_url": "https://images.unsplash.com/photo-1562572159-4efc207f5aff?w=600&q=80",
        "description": "Elegant 100% silk blouse with lustrous sheen. V-neckline, flowy silhouette. Perfect for formal meetings and evening events.",
        "is_featured": True,
        "rating": 4.9,
        "stock": 40,
    },
    {
        "name": "Premium Leather Jacket",
        "slug": "premium-leather-jacket",
        "category": "Clothes",
        "price": 249.99,
        "original_price": 349.99,
        "discount_percent": 28,
        "image_url": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600&q=80",
        "description": "Genuine lambskin leather jacket with quilted lining and polished silver zips. Two side pockets, one inner pocket. Butter-soft feel that improves with age.",
        "is_featured": True,
        "rating": 4.9,
        "stock": 30,
    },
    {
        "name": "Velvet Cocktail Dress",
        "slug": "velvet-cocktail-dress",
        "category": "Clothes",
        "price": 139.99,
        "original_price": 199.99,
        "discount_percent": 30,
        "image_url": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600&q=80",
        "description": "Fitted velvet midi dress with elegant sweetheart neckline. Back zipper closure. Available in deep burgundy, midnight blue, and emerald green. Perfect for special evenings.",
        "is_featured": True,
        "rating": 4.8,
        "stock": 45,
    },
    {
        "name": "Linen Wide-Leg Trousers",
        "slug": "linen-wide-leg-trousers",
        "category": "Clothes",
        "price": 74.99,
        "original_price": 109.99,
        "discount_percent": 32,
        "image_url": "https://images.unsplash.com/photo-1509631179647-0177331693ae?w=600&q=80",
        "description": "Breathable 100% linen trousers in a relaxed wide-leg silhouette. Elastic waistband with drawstring. Ideal for summer travels and hot days.",
        "is_featured": False,
        "rating": 4.4,
        "stock": 70,
    },
    {
        "name": "Graphic Oversized Hoodie",
        "slug": "graphic-oversized-hoodie",
        "category": "Clothes",
        "price": 64.99,
        "original_price": 89.99,
        "discount_percent": 28,
        "image_url": "https://images.unsplash.com/photo-1556821840-3a63f15732ce?w=600&q=80",
        "description": "Heavyweight fleece hoodie in an oversized streetwear fit. Bold graphic front print, double-stitched seams for durability. Unisex sizing.",
        "is_featured": False,
        "rating": 4.4,
        "stock": 100,
    },

    # ── WATCHES (9 products) ──────────────────────────────────────────────────
    {
        "name": "Classic Silver Watch",
        "slug": "classic-silver-watch",
        "category": "Watches",
        "price": 299.99,
        "original_price": 399.99,
        "discount_percent": 25,
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&q=80",
        "description": "Swiss-inspired silver case watch with sapphire crystal glass. 50m water resistance. Stainless steel bracelet. Precise Japanese quartz movement.",
        "is_featured": True,
        "rating": 4.9,
        "stock": 25,
    },
    {
        "name": "Luxury Gold Watch",
        "slug": "luxury-gold-watch",
        "category": "Watches",
        "price": 599.99,
        "original_price": 799.99,
        "discount_percent": 25,
        "image_url": "https://images.unsplash.com/photo-1547996160-81dfa63595aa?w=600&q=80",
        "description": "Premium 18k gold-plated case watch with genuine brown leather strap. Roman numeral dial, exhibition caseback. The perfect luxury gift.",
        "is_featured": True,
        "rating": 4.8,
        "stock": 15,
    },
    {
        "name": "Smart Watch Pro",
        "slug": "smart-watch-pro",
        "category": "Watches",
        "price": 399.99,
        "original_price": None,
        "discount_percent": 0,
        "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=600&q=80",
        "description": "Advanced smartwatch with built-in GPS, heart rate monitor, SpO2 sensor, sleep tracking and 14-day battery life. Compatible with Android and iOS. IP68 rated.",
        "is_featured": True,
        "rating": 4.7,
        "stock": 50,
    },
    {
        "name": "Sports Chronograph",
        "slug": "sports-chronograph",
        "category": "Watches",
        "price": 149.99,
        "original_price": 199.99,
        "discount_percent": 25,
        "image_url": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=600&q=80",
        "description": "Sporty chronograph with three sub-dials and tachymeter bezel. Durable silicone strap, shock-resistant case. 100m water resistance — built for active lifestyles.",
        "is_featured": False,
        "rating": 4.4,
        "stock": 40,
    },
    {
        "name": "Minimalist Rose Gold Watch",
        "slug": "minimalist-rose-gold-watch",
        "category": "Watches",
        "price": 219.99,
        "original_price": 279.99,
        "discount_percent": 21,
        "image_url": "https://images.unsplash.com/photo-1585386959984-a4155224a1ad?w=600&q=80",
        "description": "Ultra-thin 6.5mm minimalist dial in elegant rose-gold PVD finish. Genuine leather strap, Japanese quartz movement. The epitome of understated elegance.",
        "is_featured": False,
        "rating": 4.6,
        "stock": 35,
    },
    {
        "name": "Blue Dial Automatic Watch",
        "slug": "blue-dial-automatic-watch",
        "category": "Watches",
        "price": 329.99,
        "original_price": 449.99,
        "discount_percent": 27,
        "image_url": "https://images.unsplash.com/photo-1526045612212-70caf35c14df?w=600&q=80",
        "description": "Japanese automatic self-winding movement with stunning ocean-blue sunray dial. Brushed and polished steel case, 100m water resistance, exhibition caseback.",
        "is_featured": True,
        "rating": 4.8,
        "stock": 20,
    },
    {
        "name": "Skeleton Mechanical Watch",
        "slug": "skeleton-mechanical-watch",
        "category": "Watches",
        "price": 549.99,
        "original_price": 749.99,
        "discount_percent": 26,
        "image_url": "https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=600&q=80",
        "description": "Open-heart skeleton dial revealing intricate mechanical movement. Swiss-inspired tourbillon-style display, genuine leather strap. A statement piece for watch enthusiasts.",
        "is_featured": True,
        "rating": 4.9,
        "stock": 12,
    },
    {
        "name": "Titanium Sport Watch",
        "slug": "titanium-sport-watch",
        "category": "Watches",
        "price": 459.99,
        "original_price": 599.99,
        "discount_percent": 23,
        "image_url": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=600&q=80",
        "description": "Lightweight Grade-5 titanium sport watch with solar charging and 100m water resistance. Eco-Drive movement, perpetual calendar, world time display.",
        "is_featured": True,
        "rating": 4.8,
        "stock": 18,
    },
    {
        "name": "Ladies Rose Crystal Watch",
        "slug": "ladies-rose-crystal-watch",
        "category": "Watches",
        "price": 199.99,
        "original_price": 269.99,
        "discount_percent": 25,
        "image_url": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=600&q=80",
        "description": "Elegant ladies watch with 72 Swarovski crystal-set bezel and rose-gold IP mesh bracelet. Mother-of-pearl dial with date window. A timeless gift for her.",
        "is_featured": True,
        "rating": 4.7,
        "stock": 28,
    },

    # ── SHOES (6 products) ────────────────────────────────────────────────────
    {
        "name": "Running Sneakers",
        "slug": "running-sneakers",
        "category": "Shoes",
        "price": 89.99,
        "original_price": 119.99,
        "discount_percent": 25,
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&q=80",
        "description": "Lightweight and breathable mesh upper with responsive foam midsole. Non-slip rubber outsole, reflective detailing for safety. Ideal for daily runs and gym sessions.",
        "is_featured": True,
        "rating": 4.6,
        "stock": 100,
    },
    {
        "name": "Leather Oxford",
        "slug": "leather-oxford",
        "category": "Shoes",
        "price": 149.99,
        "original_price": None,
        "discount_percent": 0,
        "image_url": "https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?w=600&q=80",
        "description": "Hand-stitched full-grain calf-leather Oxford shoes. Blake-construction sole for flexibility, leather insole. The definitive dress shoe for the modern gentleman.",
        "is_featured": True,
        "rating": 4.8,
        "stock": 45,
    },
    {
        "name": "High Heel Pumps",
        "slug": "high-heel-pumps",
        "category": "Shoes",
        "price": 109.99,
        "original_price": 159.99,
        "discount_percent": 31,
        "image_url": "https://images.unsplash.com/photo-1515347619252-60a4bf4fff4f?w=600&q=80",
        "description": "Classic 4-inch stiletto pumps in genuine suede. Pointed toe, covered heel, cushioned insole. Available in black, nude, and red.",
        "is_featured": False,
        "rating": 4.3,
        "stock": 55,
    },
    {
        "name": "Casual Slip-On Loafers",
        "slug": "casual-slip-on-loafers",
        "category": "Shoes",
        "price": 69.99,
        "original_price": 99.99,
        "discount_percent": 30,
        "image_url": "https://images.unsplash.com/photo-1600269452121-4f2416e55c28?w=600&q=80",
        "description": "Effortless slip-on penny loafers with memory foam insoles. Genuine leather upper, rubber outsole. All-day comfort without sacrificing style.",
        "is_featured": False,
        "rating": 4.4,
        "stock": 80,
    },
    {
        "name": "Chunky Platform Sneakers",
        "slug": "chunky-platform-sneakers",
        "category": "Shoes",
        "price": 129.99,
        "original_price": 179.99,
        "discount_percent": 27,
        "image_url": "https://images.unsplash.com/photo-1605348532760-6753d2c43329?w=600&q=80",
        "description": "Trendy chunky platform sneakers with 4.5cm thick rubber outsole. Padded ankle collar, lace-up closure, mixed-material upper. Add instant height and streetwear edge.",
        "is_featured": True,
        "rating": 4.5,
        "stock": 65,
    },
    {
        "name": "Suede Chelsea Boots",
        "slug": "suede-chelsea-boots",
        "category": "Shoes",
        "price": 169.99,
        "original_price": 219.99,
        "discount_percent": 22,
        "image_url": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=600&q=80",
        "description": "Genuine suede chelsea boots with elasticated side gussets for easy slip-on. Block heel, leather lining. Pairs perfectly with jeans or tailored trousers.",
        "is_featured": False,
        "rating": 4.6,
        "stock": 40,
    },

    # ── BAGS (5 products) ─────────────────────────────────────────────────────
    {
        "name": "Leather Handbag",
        "slug": "leather-handbag",
        "category": "Bags",
        "price": 129.99,
        "original_price": 189.99,
        "discount_percent": 32,
        "image_url": "https://images.unsplash.com/photo-1548036161-f5b1cfc3ec89?w=600&q=80",
        "description": "Structured genuine leather handbag with brushed gold hardware. Top handles + detachable shoulder strap. Suede lining with two interior pockets. Fits A4 documents.",
        "is_featured": True,
        "rating": 4.7,
        "stock": 30,
    },
    {
        "name": "Canvas Backpack",
        "slug": "canvas-backpack",
        "category": "Bags",
        "price": 79.99,
        "original_price": 109.99,
        "discount_percent": 27,
        "image_url": "https://images.unsplash.com/photo-1553062407-98d674fe1b79?w=600&q=80",
        "description": "Durable waxed canvas backpack with padded 15-inch laptop compartment. Leather trim, brass zippers, three compartments plus side water-bottle pockets.",
        "is_featured": True,
        "rating": 4.5,
        "stock": 60,
    },
    {
        "name": "Clutch Evening Bag",
        "slug": "clutch-evening-bag",
        "category": "Bags",
        "price": 59.99,
        "original_price": 79.99,
        "discount_percent": 25,
        "image_url": "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?w=600&q=80",
        "description": "Compact beaded satin clutch with detachable chain strap. Interior slip pocket for cards and essentials. Perfect for galas, weddings, and formal evenings.",
        "is_featured": False,
        "rating": 4.2,
        "stock": 50,
    },
    {
        "name": "Quilted Chain Shoulder Bag",
        "slug": "quilted-chain-shoulder-bag",
        "category": "Bags",
        "price": 179.99,
        "original_price": 249.99,
        "discount_percent": 28,
        "image_url": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=600&q=80",
        "description": "Classic diamond-quilted lambskin bag with gold-tone chain strap and turn-lock closure. Interior zip pocket, card slots. Icon handbag status at an accessible price.",
        "is_featured": True,
        "rating": 4.8,
        "stock": 22,
    },
    {
        "name": "Woven Raffia Beach Tote",
        "slug": "woven-raffia-beach-tote",
        "category": "Bags",
        "price": 59.99,
        "original_price": 84.99,
        "discount_percent": 29,
        "image_url": "https://images.unsplash.com/photo-1590739293931-a4f79cf92a55?w=600&q=80",
        "description": "Handwoven natural raffia tote with sturdy leather handles and cotton lining. Spacious enough for towels and sunscreen. Your perfect beach companion.",
        "is_featured": False,
        "rating": 4.3,
        "stock": 40,
    },

    # ── JEWELRY (6 products) ──────────────────────────────────────────────────
    {
        "name": "Gold Chain Necklace",
        "slug": "gold-chain-necklace",
        "category": "Jewelry",
        "price": 199.99,
        "original_price": 249.99,
        "discount_percent": 20,
        "image_url": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=600&q=80",
        "description": "18k gold-plated rope chain necklace, 45cm with lobster clasp. Tarnish-resistant finish. Comes in a luxury gift box.",
        "is_featured": True,
        "rating": 4.8,
        "stock": 60,
    },
    {
        "name": "Diamond Solitaire Ring",
        "slug": "diamond-solitaire-ring",
        "category": "Jewelry",
        "price": 499.99,
        "original_price": 699.99,
        "discount_percent": 28,
        "image_url": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=600&q=80",
        "description": "Brilliant-cut 0.5ct diamond set in a 14k white gold 6-prong solitaire band. GIA certified. Includes certificate and luxury jewellery box.",
        "is_featured": True,
        "rating": 4.9,
        "stock": 10,
    },
    {
        "name": "Silver Cuff Bracelet",
        "slug": "silver-cuff-bracelet",
        "category": "Jewelry",
        "price": 89.99,
        "original_price": 119.99,
        "discount_percent": 25,
        "image_url": "https://images.unsplash.com/photo-1611652022419-a9419f74343d?w=600&q=80",
        "description": "Sterling 925 silver adjustable cuff bracelet with intricate floral engravings. Hypoallergenic, nickel-free. One size fits most.",
        "is_featured": False,
        "rating": 4.4,
        "stock": 45,
    },
    {
        "name": "Pearl Drop Earrings",
        "slug": "pearl-drop-earrings",
        "category": "Jewelry",
        "price": 69.99,
        "original_price": 99.99,
        "discount_percent": 30,
        "image_url": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=600&q=80",
        "description": "Freshwater cultured pearl drop earrings with sterling silver hooks. 10mm pearl diameter. Timeless elegance for everyday wear and special occasions.",
        "is_featured": True,
        "rating": 4.7,
        "stock": 55,
    },
    {
        "name": "Layered Gold Chain Necklace Set",
        "slug": "layered-gold-chain-necklace-set",
        "category": "Jewelry",
        "price": 79.99,
        "original_price": 109.99,
        "discount_percent": 27,
        "image_url": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=600&q=80",
        "description": "Set of three delicate 18k gold-plated chains 40cm, 45cm, and 50cm, designed to be worn layered together for a trend-forward look.",
        "is_featured": False,
        "rating": 4.5,
        "stock": 35,
    },
    {
        "name": "Emerald Stud Earrings",
        "slug": "emerald-stud-earrings",
        "category": "Jewelry",
        "price": 149.99,
        "original_price": 199.99,
        "discount_percent": 25,
        "image_url": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=600&q=80",
        "description": "Natural emerald stone stud earrings set in 14k yellow gold with butterfly backs. Vibrant green colour, a meaningful gift for May birthdays.",
        "is_featured": False,
        "rating": 4.6,
        "stock": 20,
    },

    # ── SUNGLASSES (5 products) ───────────────────────────────────────────────
    {
        "name": "Aviator Sunglasses",
        "slug": "aviator-sunglasses",
        "category": "Sunglasses",
        "price": 79.99,
        "original_price": 109.99,
        "discount_percent": 27,
        "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=600&q=80",
        "description": "Classic metal-frame aviators with UV400 polarised lenses. Spring-hinge temples for adjustable fit. Scratch-resistant coating. Includes hard case and cleaning cloth.",
        "is_featured": True,
        "rating": 4.6,
        "stock": 75,
    },
    {
        "name": "Cat Eye Frames",
        "slug": "cat-eye-frames",
        "category": "Sunglasses",
        "price": 69.99,
        "original_price": 89.99,
        "discount_percent": 22,
        "image_url": "https://images.unsplash.com/photo-1556306535-0f09a537f0a3?w=600&q=80",
        "description": "Retro cat-eye frames in handmade tortoiseshell acetate. Gradient lenses, stainless steel hinges. The must-have sunglasses for vintage fashion lovers.",
        "is_featured": False,
        "rating": 4.3,
        "stock": 55,
    },
    {
        "name": "Oversized Square Shades",
        "slug": "oversized-square-shades",
        "category": "Sunglasses",
        "price": 59.99,
        "original_price": None,
        "discount_percent": 0,
        "image_url": "https://images.unsplash.com/photo-1473496169904-658ba7574b0d?w=600&q=80",
        "description": "Bold oversized square frames for a glamorous, celebrity-approved look. 100% UV protection, lightweight TR90 frame, anti-reflective lenses.",
        "is_featured": False,
        "rating": 4.5,
        "stock": 60,
    },
    {
        "name": "Round Tortoise Sunglasses",
        "slug": "round-tortoise-sunglasses",
        "category": "Sunglasses",
        "price": 84.99,
        "original_price": 114.99,
        "discount_percent": 26,
        "image_url": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=600&q=80",
        "description": "Classic round acetate frames in rich tortoiseshell. Gradient UV400 polarised lenses reduce glare. Inspires the classic bohemian aesthetic.",
        "is_featured": False,
        "rating": 4.5,
        "stock": 45,
    },
    {
        "name": "Sport Wraparound Shades",
        "slug": "sport-wraparound-shades",
        "category": "Sunglasses",
        "price": 54.99,
        "original_price": 79.99,
        "discount_percent": 31,
        "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=600&q=80",
        "description": "Wraparound sports sunglasses with rubberised nose pads and anti-slip temple tips. Polycarbonate impact-resistant lenses. Ideal for cycling, running, and outdoor sports.",
        "is_featured": False,
        "rating": 4.4,
        "stock": 80,
    },

    # ── HATS (4 products) ─────────────────────────────────────────────────────
    {
        "name": "Wool Fedora Hat",
        "slug": "wool-fedora-hat",
        "category": "Hats",
        "price": 49.99,
        "original_price": 69.99,
        "discount_percent": 28,
        "image_url": "https://images.unsplash.com/photo-1521369909029-2afed882baee?w=600&q=80",
        "description": "Classic wide-brim fedora crafted from 100% premium wool felt. Satin inner sweatband, grosgrain ribbon. Available in charcoal, camel, and ivory.",
        "is_featured": True,
        "rating": 4.6,
        "stock": 50,
    },
    {
        "name": "Snapback Baseball Cap",
        "slug": "snapback-baseball-cap",
        "category": "Hats",
        "price": 29.99,
        "original_price": 39.99,
        "discount_percent": 25,
        "image_url": "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=600&q=80",
        "description": "Adjustable 6-panel snapback cap in embroidered cotton twill. Structured flat brim, plastic snap closure. One size fits most adults.",
        "is_featured": False,
        "rating": 4.2,
        "stock": 100,
    },
    {
        "name": "Ribbed Knit Beanie",
        "slug": "ribbed-knit-beanie",
        "category": "Hats",
        "price": 24.99,
        "original_price": 34.99,
        "discount_percent": 28,
        "image_url": "https://images.unsplash.com/photo-1521369909029-2afed882baee?w=600&q=80",
        "description": "Soft ribbed-knit beanie in merino wool blend. Fold-up cuff, stretchy fit. Warm and stylish for cold days. Available in 8 solid colours.",
        "is_featured": False,
        "rating": 4.3,
        "stock": 90,
    },
    {
        "name": "Adjustable Corduroy Dad Cap",
        "slug": "adjustable-corduroy-dad-cap",
        "category": "Hats",
        "price": 27.99,
        "original_price": 39.99,
        "discount_percent": 30,
        "image_url": "https://images.unsplash.com/photo-1521369909029-2afed882baee?w=600&q=80",
        "description": "Unstructured 6-panel dad cap in soft corduroy fabric. Adjustable brass buckle strap. The perfect low-key accessory for casual outfits.",
        "is_featured": False,
        "rating": 4.4,
        "stock": 70,
    },

    # ── ACCESSORIES (5 products) ──────────────────────────────────────────────
    {
        "name": "Silk Printed Scarf",
        "slug": "silk-printed-scarf",
        "category": "Accessories",
        "price": 39.99,
        "original_price": 59.99,
        "discount_percent": 33,
        "image_url": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80",
        "description": "Luxurious 100% silk scarf with artistic botanical print. 90x90cm, hand-rolled edges. Wear as a neck scarf, hair tie, or bag accessory.",
        "is_featured": True,
        "rating": 4.5,
        "stock": 55,
    },
    {
        "name": "Braided Leather Belt",
        "slug": "braided-leather-belt",
        "category": "Accessories",
        "price": 34.99,
        "original_price": 49.99,
        "discount_percent": 30,
        "image_url": "https://images.unsplash.com/photo-1624806992066-5ffcf7ca186b?w=600&q=80",
        "description": "Hand-braided genuine leather belt with solid antique brass prong buckle. Width: 35mm. Available in sizes 28 to 46 inches.",
        "is_featured": False,
        "rating": 4.3,
        "stock": 60,
    },
    {
        "name": "Cashmere Gloves",
        "slug": "cashmere-gloves",
        "category": "Accessories",
        "price": 44.99,
        "original_price": 64.99,
        "discount_percent": 31,
        "image_url": "https://images.unsplash.com/photo-1617791160536-598cf32026fb?w=600&q=80",
        "description": "Soft Grade-A cashmere knit gloves with touchscreen-compatible fingertips. Ribbed cuffs, one-size-fits-most. Available in 6 neutral tones.",
        "is_featured": False,
        "rating": 4.7,
        "stock": 45,
    },
    {
        "name": "Slim RFID Leather Wallet",
        "slug": "slim-rfid-leather-wallet",
        "category": "Accessories",
        "price": 49.99,
        "original_price": 69.99,
        "discount_percent": 28,
        "image_url": "https://images.unsplash.com/photo-1548036161-f5b1cfc3ec89?w=600&q=80",
        "description": "Ultra-slim bi-fold wallet in top-grain vegetable-tanned leather. Built-in RFID-blocking lining. 8 card slots, full-length bill compartment, ID window.",
        "is_featured": False,
        "rating": 4.6,
        "stock": 75,
    },
    {
        "name": "Gold Sunglasses Chain",
        "slug": "gold-sunglasses-chain",
        "category": "Accessories",
        "price": 19.99,
        "original_price": 29.99,
        "discount_percent": 33,
        "image_url": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=600&q=80",
        "description": "18k gold-plated sunglasses chain, keep your eyewear safe and stylish. Universal silicone loops, 68cm length. Also doubles as a statement necklace.",
        "is_featured": False,
        "rating": 4.2,
        "stock": 100,
    },
]


# =============================================================================
#  SECTION 3  —  CART & ORDER SCHEMAS  (documentation / reference)
# =============================================================================

CART_SCHEMA = {
    "Cart": {
        "session_key": "CharField(40) — links to Django session (unique)",
        "created_at":  "DateTimeField auto_now_add=True",
        "methods": {
            "get_total()":  "Returns sum of all CartItem subtotals (Decimal)",
            "item_count()": "Returns sum of all CartItem quantities (int)",
        },
    },
    "CartItem": {
        "cart":     "ForeignKey(Cart, CASCADE, related_name='items')",
        "product":  "ForeignKey(Product, CASCADE)",
        "quantity": "PositiveIntegerField default=1",
        "size":     "CharField(10) choices: XS/S/M/L/XL/XXL/ONE  default='M'",
        "computed": {
            "subtotal": "product.price * quantity",
        },
    },
    "notes": [
        "Cart is session-based — no login required to shop",
        "AJAX endpoints: /cart/add/<id>/ and /cart/remove/<id>/",
        "Cart count shown in navbar via context_processor",
    ],
}

ORDER_SCHEMA = {
    "Order": {
        "user":             "ForeignKey(User, SET_NULL, null=True) — None for guests",
        "session_key":      "CharField(40) — links guest orders to session",
        "full_name":        "CharField(200)",
        "email":            "EmailField",
        "address":          "TextField",
        "phone":            "CharField(20)",
        "total":            "DecimalField(10,2) — captured at order time",
        "status":           ["pending", "processing", "shipped", "delivered", "cancelled"],
        "payment_method":   ["cod", "khalti", "esewa", "card", "fonepay"],
        "payment_status":   ["unpaid", "paid", "failed"],
        "payment_token":    "CharField(200) — pidx (Khalti) / ref_id (eSewa) / CARD-xxxx",
        "transaction_uuid": "CharField(100) — UUID for eSewa and Fonepay",
        "created_at":       "DateTimeField auto_now_add=True",
    },
    "OrderItem": {
        "order":        "ForeignKey(Order, CASCADE, related_name='items')",
        "product":      "ForeignKey(Product, SET_NULL, null=True)",
        "product_name": "CharField(200) — snapshot at order time",
        "price":        "DecimalField(10,2) — snapshot at order time",
        "quantity":     "PositiveIntegerField",
        "size":         "CharField(10)",
        "computed": {
            "subtotal": "price * quantity",
        },
    },
}


# =============================================================================
#  SECTION 4  —  PAYMENT GATEWAY DETAILS
# =============================================================================

PAYMENT_GATEWAYS = {

    # ── Khalti (Nepal's leading digital wallet) ───────────────────────────────
    "khalti": {
        "name": "Khalti",
        "icon": "🔵",
        "description": "Nepal's leading digital payment platform. Uses hosted payment pages.",
        "test_secret_key": "test_secret_key_dc74e0fd57cb46cd93832aee0a390234",
        "initiate_url":    "https://a.khalti.com/api/v2/epayment/initiate/",
        "verify_url":      "https://a.khalti.com/api/v2/epayment/lookup/",
        "currency":        "NPR (sent in paisa: amount * 100)",
        "auth_header":     "Authorization: Key <secret_key>",
        "flow": [
            "1. POST to initiate URL with order details → receive pidx + payment_url",
            "2. Redirect customer to payment_url",
            "3. Khalti redirects back: /payment/khalti/callback/?pidx=...&status=Completed&purchase_order_id=...",
            "4. Verify pidx via lookup API → if Completed, set order.payment_status='paid'",
        ],
        "payload_fields": {
            "return_url":           "your callback URL",
            "website_url":          "your site URL",
            "amount":               "amount in paisa (NPR * 100)",
            "purchase_order_id":    "order.id",
            "purchase_order_name":  "human-readable order name",
            "customer_info":        {"name": "str", "email": "str", "phone": "str"},
        },
        "routes": {
            "initiate": "/payment/khalti/<order_id>/",
            "callback": "/payment/khalti/callback/",
        },
        "settings_keys": ["KHALTI_SECRET_KEY", "KHALTI_INITIATE_URL", "KHALTI_VERIFY_URL"],
    },

    # ── eSewa (Nepal's first online payment service) ──────────────────────────
    "esewa": {
        "name": "eSewa",
        "icon": "🟢",
        "description": "Nepal's first and most popular online payment service. Uses HMAC-signed HTML form POST.",
        "test_merchant_code": "EPAYTEST",
        "test_secret_key":    "8gBm/:&EnhH.1/q",
        "payment_url":        "https://rc-epay.esewa.com.np/api/epay/main/v2/form",
        "verify_url":         "https://rc-epay.esewa.com.np/api/epay/transaction/statuscheck",
        "signature_algorithm": "HMAC-SHA256 → base64",
        "signed_fields":      "total_amount,transaction_uuid,product_code",
        "signature_message":  "total_amount={X},transaction_uuid={Y},product_code={Z}",
        "flow": [
            "1. Generate UUID transaction_id, compute HMAC-SHA256 signature",
            "2. Auto-submit HTML form to eSewa payment URL",
            "3. eSewa redirects to success_url with base64-encoded JSON in ?data=",
            "4. Decode JSON → verify via status API → set paid if status=COMPLETE",
        ],
        "form_fields": {
            "amount":                   "order.total",
            "tax_amount":               "0",
            "total_amount":             "order.total",
            "transaction_uuid":         "uuid4()",
            "product_code":             "ESEWA_MERCHANT_CODE",
            "product_service_charge":   "0",
            "product_delivery_charge":  "0",
            "success_url":              "your success callback URL",
            "failure_url":              "your failure callback URL",
            "signed_field_names":       "total_amount,transaction_uuid,product_code",
            "signature":                "HMAC-SHA256 base64 of signed_fields",
        },
        "callback_success_params": {
            "data": "base64-encoded JSON with transaction_uuid, status, total_amount, ref_id",
        },
        "routes": {
            "initiate":         "/payment/esewa/<order_id>/",
            "callback_success": "/payment/esewa/success/",
            "callback_failure": "/payment/esewa/failure/<order_id>/",
        },
        "settings_keys": [
            "ESEWA_MERCHANT_CODE", "ESEWA_SECRET_KEY",
            "ESEWA_PAYMENT_URL", "ESEWA_VERIFY_URL",
        ],
    },

    # ── Credit / Debit Card ───────────────────────────────────────────────────
    "card": {
        "name": "Credit / Debit Card",
        "icon": "💳",
        "description": "Built-in card form. Demo mode marks paid immediately. Production: integrate iPay or Stripe.",
        "form_fields": ["card_number", "expiry (MM/YY)", "cvv", "card_name"],
        "validation": {
            "card_number": "minimum 13 digits (spaces stripped)",
            "expiry":      "required",
            "cvv":         "minimum 3 digits",
            "card_name":   "required",
        },
        "demo_token_format": "CARD-{last4digits}",
        "flow": [
            "1. Customer fills card form at /payment/card/<order_id>/",
            "2. Server validates all fields",
            "3. Demo: marks order.payment_status='paid' immediately",
            "4. Production: tokenise via iPay/Stripe → charge → set paid on success",
        ],
        "routes": {
            "pay": "/payment/card/<order_id>/",
        },
    },

    # ── Fonepay (QR-based payment network) ───────────────────────────────────
    "fonepay": {
        "name": "Fonepay",
        "icon": "📱",
        "description": "Nepal's QR-based payment network. Merchants redirect with signed parameters.",
        "production_url": "https://fonepay.com/api/merchant/merchantDetailsForThirdParty",
        "sandbox_url":    "https://dev.fonepay.com/api/merchant/merchantDetailsForThirdParty",
        "request_params": {
            "PID":  "Fonepay Merchant ID",
            "MD":   "P (for payment)",
            "AMT":  "order total in NPR",
            "CRN":  "NPR",
            "DT":   "Date MM/DD/YYYY",
            "R1":   "order reference string",
            "R2":   "Payment",
            "RU":   "return / callback URL",
            "PRN":  "unique transaction UUID",
        },
        "callback_params": {
            "PS":   "success or failure",
            "PRN":  "must match sent PRN to prevent replay attacks",
            "BID":  "bank transaction ID (on success)",
        },
        "flow": [
            "1. Generate UUID, POST/redirect to Fonepay URL with signed params",
            "2. Customer scans QR / pays in Fonepay app",
            "3. Fonepay calls /payment/fonepay/callback/<order_id>/?PS=success&PRN=...",
            "4. Verify PS=success AND PRN matches stored UUID → set order paid",
        ],
        "routes": {
            "initiate": "/payment/fonepay/<order_id>/",
            "callback": "/payment/fonepay/callback/<order_id>/",
        },
        "settings_keys": ["FONEPAY_MERCHANT_ID"],
    },

    # ── Cash on Delivery ─────────────────────────────────────────────────────
    "cod": {
        "name": "Cash on Delivery",
        "icon": "🚚",
        "description": "No payment gateway. Customer pays cash when order arrives.",
        "payment_status_at_order":    "unpaid",
        "payment_status_at_delivery": "paid (manually updated by admin)",
        "flow": [
            "1. Customer selects COD at checkout",
            "2. Order saved with payment_status='unpaid', status='pending'",
            "3. Admin ships order → updates status='shipped'",
            "4. On delivery, admin marks payment_status='paid' and status='delivered'",
        ],
        "no_gateway": True,
    },
}


# =============================================================================
#  SECTION 5  —  FULL URL MAP  (all routes on the live site)
# =============================================================================

URL_MAP = {
    # ── Public browsing ───────────────────────────────────────────────────────
    "/":                              "Home — hero slider, featured & new arrivals",
    "/store/":                        "Store — full product grid with filters",
    "/store/?category=<slug>":        "Filter by category (clothes/watches/shoes/bags/jewelry/sunglasses/hats/accessories)",
    "/store/?sort=newest":            "Sort options: newest | price_low | price_high | rating",
    "/store/?min_price=X&max_price=Y":"Price range filter",
    "/product/<slug>/":               "Product detail page + related products",
    "/search/?q=<query>":            "Full-text search across name, description, category",

    # ── Cart ──────────────────────────────────────────────────────────────────
    "/cart/":                         "View cart (session-based, no login needed)",
    "/cart/add/<product_id>/":        "POST — Add item to cart (AJAX-enabled, returns JSON)",
    "/cart/remove/<item_id>/":        "POST — Remove item from cart (AJAX-enabled)",

    # ── Checkout & Orders ─────────────────────────────────────────────────────
    "/checkout/":                     "Checkout form (name, email, address, phone, payment method)",
    "/order/complete/<order_id>/":    "Order success / confirmation page",
    "/order/failed/<order_id>/":      "Payment failure page",

    # ── Authentication ────────────────────────────────────────────────────────
    "/signin/":                       "Login page",
    "/register/":                     "Registration page",
    "/logout/":                       "Logout (redirects to home)",
    "/dashboard/":                    "User order history (login required)",

    # ── Payment gateways ─────────────────────────────────────────────────────
    "/payment/khalti/<order_id>/":             "Initiate Khalti payment",
    "/payment/khalti/callback/":              "Khalti return callback",
    "/payment/esewa/<order_id>/":              "eSewa auto-submit form",
    "/payment/esewa/success/":                "eSewa success callback",
    "/payment/esewa/failure/<order_id>/":      "eSewa failure callback",
    "/payment/card/<order_id>/":              "Credit/Debit card payment form",
    "/payment/fonepay/<order_id>/":           "Fonepay QR redirect",
    "/payment/fonepay/callback/<order_id>/":  "Fonepay return callback",

    # ── Admin ─────────────────────────────────────────────────────────────────
    "/admin/":                        "Django admin panel (superuser required)",
}


# =============================================================================
#  SECTION 6  —  SITE SETTINGS & CONSTANTS
# =============================================================================

SITE_CONFIG = {
    "name":              "GreatStore",
    "tagline":           "Fashion & Lifestyle",
    "live_url":          "https://web-production-d1b6d.up.railway.app/",
    "contact_email":     "parasdhungana11@gmail.com",
    "contact_phone":     "9865947163",
    "social": {
        "instagram": "#",
        "facebook":  "#",
        "twitter":   "#",
    },
    "currency_usd":      "USD",
    "currency_npr":      "NPR",
    "usd_to_npr_rate":   133,               # 1 USD = 133 NPR (hardcoded in site)
    "free_shipping_min_npr": 75,            # Free shipping on orders over Rs 75
    "coupon_code":       "GREAT10",         # 10% off first order (min Rs 500)
    "coupon_discount":   10,                # percent
    "tech_stack": {
        "backend":   "Django 4.x",
        "database":  "SQLite (dev) / PostgreSQL (prod on Railway)",
        "frontend":  "Bootstrap 5.3 + Bootstrap Icons + Google Fonts (Inter)",
        "hosting":   "Railway.app",
        "payments":  ["Khalti", "eSewa", "Card", "Fonepay", "COD"],
    },
    "admin_site": {
        "header":      "🛍️ GreatStore Admin",
        "title":       "GreatStore",
        "index_title": "Welcome to GreatStore Dashboard",
        "url":         "/admin/",
    },
    "hero_slides": [
        {
            "theme":  "Warm Yellow",
            "badge":  "🔥 New Season Sale",
            "title":  "Discover Fashion That Defines You",
            "desc":   "Shop the latest clothes, luxury watches, shoes and accessories. Free delivery on orders over Rs 75.",
            "cta":    "Shop Now",
            "cta2":   "Luxury Watches",
        },
        {
            "theme":  "Sky Blue",
            "badge":  "🏷️ Limited Offer",
            "title":  "Flat 10% OFF Your First Order",
            "desc":   "Use code GREAT10 at checkout. Valid on all clothes, shoes, bags and accessories.",
            "cta":    "Claim Discount",
        },
        {
            "theme":  "Rose-Purple",
            "badge":  "🚚 Free Delivery",
            "title":  "New Arrivals Just Landed",
            "desc":   "Fresh styles added every week. Get free home delivery on all orders above Rs 75.",
            "cta":    "See New Arrivals",
            "cta2":   "Browse Clothes",
        },
    ],
    "trust_badges": [
        {"icon": "🚚", "title": "Free Shipping",  "desc": "On orders over Rs 75"},
        {"icon": "↩️",  "title": "Easy Returns",  "desc": "30-day hassle-free returns"},
        {"icon": "🔒", "title": "Secure Payment", "desc": "Khalti, eSewa, Card, Fonepay"},
        {"icon": "💬", "title": "24/7 Support",   "desc": "Always here to help you"},
    ],
}


# =============================================================================
#  SECTION 7  —  DATABASE HELPER FUNCTIONS
# =============================================================================

def seed_database(clear_existing=False):
    """
    Seed (or re-seed) the database with all categories and products.

    Args:
        clear_existing (bool): If True, deletes all existing data first.

    Usage:
        from greatstore_database import seed_database
        seed_database()            # safe upsert
        seed_database(clear=True)  # full reset
    """
    from django.utils.text import slugify
    from store.models import Category, Product

    if clear_existing:
        print("[seed] Clearing all products and categories...")
        Product.objects.all().delete()
        Category.objects.all().delete()

    # Create/update categories
    cat_map = {}
    print(f"[seed] Processing {len(CATEGORIES)} categories...")
    for c in CATEGORIES:
        cat, created = Category.objects.get_or_create(
            slug=c["slug"],
            defaults={
                "name":        c["name"],
                "icon":        c["icon"],
                "description": c["description"],
            },
        )
        if not created:
            cat.name        = c["name"]
            cat.icon        = c["icon"]
            cat.description = c["description"]
            cat.save()
        cat_map[c["name"]] = cat
        action = "CREATED" if created else "updated"
        print(f"  {c['icon']}  {c['name']} ({action})")

    # Create/update products
    print(f"\n[seed] Processing {len(PRODUCTS)} products...")
    created_count = updated_count = 0
    for p in PRODUCTS:
        cat = cat_map.get(p["category"])
        if not cat:
            print(f"  WARNING: Unknown category '{p['category']}' — skipped '{p['name']}'")
            continue

        product, created = Product.objects.get_or_create(
            slug=p["slug"],
            defaults={
                "name":           p["name"],
                "category":       cat,
                "price":          p["price"],
                "original_price": p.get("original_price"),
                "image_url":      p["image_url"],
                "description":    p["description"],
                "is_featured":    p.get("is_featured", False),
                "rating":         p.get("rating", 4.5),
                "stock":          p.get("stock", 50),
            },
        )
        if not created:
            product.name           = p["name"]
            product.category       = cat
            product.price          = p["price"]
            product.original_price = p.get("original_price")
            product.image_url      = p["image_url"]
            product.description    = p["description"]
            product.is_featured    = p.get("is_featured", False)
            product.rating         = p.get("rating", 4.5)
            product.stock          = p.get("stock", 50)
            product.save()
            updated_count += 1
        else:
            created_count += 1

        disc = f" (-{p['discount_percent']}%)" if p.get("discount_percent") else ""
        star = "★ " if p.get("is_featured") else "  "
        print(f"  {star}{p['name']}  ${p['price']}{disc}")

    from store.models import Category as C, Product as Pr
    print(
        f"\n[seed] Done! {C.objects.count()} categories | "
        f"{Pr.objects.count()} products "
        f"({created_count} created, {updated_count} updated)"
    )


def print_database_report():
    """
    Print a complete formatted database report to stdout.
    Covers categories, products, carts, and orders.
    """
    from store.models import Category, Product, Cart, CartItem, Order

    DIV = "-" * 80

    # Categories
    print(f"\n{'=' * 80}")
    print("  GREATSTORE — DATABASE REPORT")
    print(f"{'=' * 80}")

    cats = Category.objects.all()
    print(f"\n CATEGORIES ({cats.count()} total)")
    print(f"  {'Name':<20} {'Slug':<20} {'Icon':<6} {'Products':>8}")
    print(f"  {DIV[:56]}")
    for cat in cats:
        print(f"  {cat.name:<20} {cat.slug:<20} {cat.icon:<6} {cat.products.count():>8}")

    # Products
    prods = Product.objects.select_related("category").all()
    print(f"\n PRODUCTS ({prods.count()} total)")
    print(f"  {'ID':<5} {'F':<2} {'Name':<35} {'Category':<14} {'Price':>8} {'Orig':>8} {'Disc%':>6} {'Stock':>6} {'Rtg':>5}")
    print(f"  {DIV}")
    for p in prods.order_by("category__name", "name"):
        orig = f"${p.original_price}" if p.original_price else "—"
        disc = f"{p.discount_percent}%" if p.discount_percent else "—"
        feat = "★" if p.is_featured else " "
        print(f"  {p.id:<5} {feat:<2} {p.name:<35} {p.category.name:<14} ${float(p.price):>7.2f} {orig:>8} {disc:>6} {p.stock:>6} {float(p.rating):>5.1f}")

    # Carts
    carts = Cart.objects.all()
    active = [c for c in carts if c.item_count() > 0]
    print(f"\n CARTS ({carts.count()} total, {len(active)} active)")
    for cart in active[:10]:
        print(f"  Session: {cart.session_key[:20]}...  Items: {cart.item_count()}  Total: ${float(cart.get_total()):.2f}")

    # Orders
    orders = Order.objects.all()
    print(f"\n ORDERS ({orders.count()} total)")
    if orders.exists():
        print(f"  {'ID':<6} {'Name':<24} {'Total':>9} {'Method':<10} {'Pay':>7} {'Status':<12} {'Date'}")
        print(f"  {DIV}")
        for o in orders.order_by("-created_at")[:20]:
            print(
                f"  #{o.id:<5} {o.full_name:<24} ${float(o.total):>8.2f} "
                f"{o.payment_method:<10} {o.payment_status:>7}  "
                f"{o.status:<12} {o.created_at.strftime('%Y-%m-%d')}"
            )
        # Revenue
        from django.db.models import Sum
        rev = orders.filter(payment_status="paid").aggregate(s=Sum("total"))["s"] or 0
        print(f"\n  Revenue (paid): ${float(rev):,.2f}")
    else:
        print("  No orders yet.")

    print(f"\n{'=' * 80}\n")


def get_dashboard_stats():
    """
    Return a dict of key statistics for an admin dashboard widget.

    Returns:
        dict: keys — total_products, total_categories, total_orders,
                      total_revenue, paid_orders, pending_orders,
                      active_carts, category_breakdown
    """
    from django.db.models import Count, Sum
    from store.models import Category, Product, Cart, CartItem, Order

    total_revenue = (
        Order.objects.filter(payment_status="paid")
                     .aggregate(s=Sum("total"))["s"] or 0
    )
    return {
        "total_products":    Product.objects.count(),
        "total_categories":  Category.objects.count(),
        "total_orders":      Order.objects.count(),
        "total_revenue_usd": float(total_revenue),
        "total_revenue_npr": float(total_revenue) * SITE_CONFIG["usd_to_npr_rate"],
        "paid_orders":       Order.objects.filter(payment_status="paid").count(),
        "pending_orders":    Order.objects.filter(status="pending").count(),
        "active_carts":      sum(1 for c in Cart.objects.all() if c.item_count() > 0),
        "total_cart_items":  CartItem.objects.count(),
        "category_breakdown": list(
            Category.objects.annotate(n=Count("products"))
                            .values("name", "icon", "n")
                            .order_by("-n")
        ),
        "order_status_breakdown": list(
            Order.objects.values("status").annotate(n=Count("id"))
        ),
        "payment_method_breakdown": list(
            Order.objects.values("payment_method").annotate(n=Count("id"))
        ),
    }


def get_or_create_cart(session_key):
    """Get or create a Cart for the given Django session key."""
    from store.models import Cart
    cart, _ = Cart.objects.get_or_create(session_key=session_key)
    return cart


def add_item_to_cart(session_key, product_id, quantity=1, size="M"):
    """
    Add a product to the cart (increments if already present).

    Returns:
        tuple: (CartItem, cart_total, cart_item_count)
    """
    from store.models import Product, CartItem
    cart    = get_or_create_cart(session_key)
    product = Product.objects.get(id=product_id)
    item, created = CartItem.objects.get_or_create(
        cart=cart, product=product, size=size,
        defaults={"quantity": quantity},
    )
    if not created:
        item.quantity += quantity
        item.save()
    return item, cart.get_total(), cart.item_count()


def create_order_from_cart(session_key, form_data):
    """
    Convert an active cart into an Order and clear the cart.

    Args:
        session_key (str): Django session key.
        form_data   (dict): Keys: full_name, email, address, phone,
                            payment_method.  Optional: user (User instance).

    Returns:
        Order or None if cart is empty.

    Example:
        order = create_order_from_cart(
            session_key='abc123...',
            form_data={
                'full_name':      'Aarav Sharma',
                'email':          'aarav@example.com',
                'address':        'Kathmandu, Bagmati, Nepal',
                'phone':          '9841000000',
                'payment_method': 'khalti',
            }
        )
    """
    from store.models import Cart, Order, OrderItem

    try:
        cart = Cart.objects.get(session_key=session_key)
    except Cart.DoesNotExist:
        return None

    items = cart.items.select_related("product").all()
    if not items.exists():
        return None

    order = Order.objects.create(
        user           = form_data.get("user"),
        session_key    = session_key,
        full_name      = form_data["full_name"],
        email          = form_data["email"],
        address        = form_data["address"],
        phone          = form_data["phone"],
        total          = cart.get_total(),
        payment_method = form_data.get("payment_method", "cod"),
        payment_status = "unpaid",
    )
    for item in items:
        OrderItem.objects.create(
            order        = order,
            product      = item.product,
            product_name = item.product.name,
            price        = item.product.price,
            quantity     = item.quantity,
            size         = item.size,
        )
    cart.items.all().delete()
    return order


def search_products(query):
    """Search products by name, description, or category name."""
    from django.db.models import Q
    from store.models import Product
    return Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(category__name__icontains=query)
    ).select_related("category")


def get_products_by_category(slug):
    """Return all products in a category by slug (e.g. 'watches')."""
    from store.models import Product
    return Product.objects.filter(
        category__slug=slug
    ).select_related("category").order_by("-created_at")


def get_featured_products(limit=8):
    """Return featured products for the homepage."""
    from store.models import Product
    return Product.objects.filter(
        is_featured=True
    ).select_related("category")[:limit]


def get_new_arrivals(limit=8):
    """Return newest products for the homepage."""
    from store.models import Product
    return Product.objects.select_related(
        "category"
    ).order_by("-created_at")[:limit]


# =============================================================================
#  SECTION 8  —  QUICK REFERENCE SUMMARY
# =============================================================================

SUMMARY = """
+------------------------------------------------------------------------------+
|               GreatStore — Complete Site Quick Reference                     |
+------------------------------------------------------------------------------+
|  Live URL  : https://web-production-d1b6d.up.railway.app/                   |
|  Backend   : Django 4.x  |  DB: SQLite dev / PostgreSQL prod (Railway)      |
|  Frontend  : Bootstrap 5.3 + Bootstrap Icons + Google Fonts (Inter)          |
+------------------------------------------------------------------------------+
|  CATEGORIES (8)                                                              |
|    👕 Clothes   ⌚ Watches   👟 Shoes   👜 Bags                             |
|    💎 Jewelry   🕶️ Sunglasses  🧢 Hats   🎀 Accessories                     |
+------------------------------------------------------------------------------+
|  PRODUCTS (47 total)                                                         |
|    Clothes 10 | Watches 9 | Shoes 6 | Bags 5                                |
|    Jewelry  6 | Sunglasses 5 | Hats 4 | Accessories 5                       |
+------------------------------------------------------------------------------+
|  CART SYSTEM                                                                 |
|    Session-based (no login required)                                         |
|    CartItem: product, quantity, size (XS/S/M/L/XL/XXL/ONE)                  |
|    AJAX add: POST /cart/add/<id>/   AJAX remove: POST /cart/remove/<id>/    |
+------------------------------------------------------------------------------+
|  ORDER SYSTEM                                                                |
|    Status   : pending > processing > shipped > delivered (or cancelled)     |
|    Pay status: unpaid > paid (or failed)                                     |
|    Supports authenticated users AND guests (session-based)                  |
+------------------------------------------------------------------------------+
|  PAYMENT GATEWAYS                                                            |
|    💳 Card     /payment/card/<id>/        (demo / iPay / Stripe in prod)    |
|    🔵 Khalti   /payment/khalti/<id>/      (hosted redirect + pidx verify)   |
|    🟢 eSewa    /payment/esewa/<id>/       (HMAC-signed form POST + verify)  |
|    📱 Fonepay  /payment/fonepay/<id>/     (QR redirect + UUID verify)       |
|    🚚 COD      /checkout/                 (admin marks paid on delivery)     |
+------------------------------------------------------------------------------+
|  KEY SETTINGS                                                                |
|    Exchange rate  : 1 USD = 133 NPR                                          |
|    Free shipping  : orders over Rs 75                                        |
|    Coupon code    : GREAT10  (10% off, min order Rs 500)                    |
|    Contact email  : parasdhungana11@gmail.com                                |
|    Contact phone  : 9865947163                                               |
|    Admin panel    : /admin/                                                  |
+------------------------------------------------------------------------------+
"""


# =============================================================================
#  MAIN — run as: python greatstore_database.py <command>
# =============================================================================

if __name__ == "__main__":
    _bootstrap_django()

    cmd = sys.argv[1].lower() if len(sys.argv) > 1 else "help"

    if cmd == "seed":
        print("[GreatStore] Seeding database (safe upsert — no data loss)...")
        seed_database(clear_existing=False)

    elif cmd == "reset":
        confirm = input("WARNING: This will DELETE all products & categories. Type YES to confirm: ")
        if confirm.strip() == "YES":
            seed_database(clear_existing=True)
        else:
            print("Aborted.")

    elif cmd == "report":
        print_database_report()

    elif cmd == "stats":
        stats = get_dashboard_stats()
        print("\n[GreatStore] Dashboard Statistics:")
        print(f"  Products     : {stats['total_products']}")
        print(f"  Categories   : {stats['total_categories']}")
        print(f"  Orders       : {stats['total_orders']} ({stats['paid_orders']} paid)")
        print(f"  Revenue      : ${stats['total_revenue_usd']:,.2f}  /  Rs {stats['total_revenue_npr']:,.0f}")
        print(f"  Pending      : {stats['pending_orders']} orders")
        print(f"  Active carts : {stats['active_carts']}")
        print("\n  By category:")
        for row in stats["category_breakdown"]:
            print(f"    {row['icon']} {row['name']:<15} {row['n']} products")

    elif cmd == "summary":
        print(SUMMARY)

    else:
        print(__doc__)
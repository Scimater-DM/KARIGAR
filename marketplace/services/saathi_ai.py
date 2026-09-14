"""
Saathi AI Assistant & Copilot Engine for KARIGAR (Scimater-DM / friend repo)
Integrates Google Gemini 2.5 Flash API & Google Cloud Vertex AI with
an offline intelligent cultural heritage knowledge graph fallback.
"""

import os
import re
import json
import urllib.request
import urllib.error


# Configuration
DEFAULT_GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"

SAATHI_SYSTEM_PROMPT = (
    "You are 'Saathi' (साथी), the dedicated AI companion, cultural advisor, and co-creator for Indian artisans on KARIGAR. "
    "You understand living craft traditions deeply (such as Bankura terracotta, Varanasi brocades, Madhubani folk art, "
    "Banjara embroidery, Bastar Dhokra bell metal, Channapatna toys, Jaipur blue pottery, and Bidriware). "
    "You uphold the philosophy: 'Every hand leaves a story. A craft is Person → Place → Practice → Story → Craft → Discovery → Commerce.' "
    "You advocate for fair living artisan wages, GI tag heritage recognition, and direct trade. "
    "Respond warmly, concisely (2-4 clear paragraphs/bullet points), and respectfully in English or Hindi as prompted."
)


def get_gemini_api_key() -> str:
    """Retrieve primary or fallback Gemini/Google API key."""
    return (
        os.environ.get("GEMINI_API_KEY")
        or os.environ.get("GOOGLE_API_KEY")
        or os.environ.get("GOOGLE_API_KEY_1")
        or os.environ.get("GOOGLE_API_KEY_2")
        or ""
    )


def call_gemini_llm(prompt: str, system_instruction: str = SAATHI_SYSTEM_PROMPT, model: str = DEFAULT_GEMINI_MODEL) -> dict:
    """
    Invoke Google Gemini API directly using Python standard library (zero external dependencies).
    Returns dict with 'success' and 'text' or 'error'.
    """
    api_key = get_gemini_api_key()
    if not api_key:
        return {"success": False, "error": "No Google Gemini API key configured."}

    url = GEMINI_API_URL.format(model=model, key=api_key)

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ],
        "system_instruction": {
            "parts": [{"text": system_instruction}]
        },
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024,
        }
    }

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            result = json.loads(response.read().decode("utf-8"))
            text = (
                result.get("candidates", [{}])[0]
                .get("content", {})
                .get("parts", [{}])[0]
                .get("text", "")
                .strip()
            )
            if text:
                return {"success": True, "text": text, "engine": f"google_{model}"}
            return {"success": False, "error": "Empty response received from Gemini."}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        return {"success": False, "error": f"Gemini HTTP error {e.code}: {err_body}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def ask_saathi_agent(query: str, action: str = "general", context: dict = None, language: str = "auto") -> dict:
    """
    Main dialogue router for Saathi AI Bot.
    Processes user query or action, attempts Gemini API, and falls back gracefully to domain heuristics.
    Supports multilingual prompt conditioning (English, Hindi, Bengali, Telugu, Tamil).
    """
    query_clean = (query or "").strip()
    action = (action or "general").lower().strip()
    context = context or {}
    lang_code = (language or "auto").lower().strip()

    lang_instructions = {
        "hi": "Important: Respond in fluent, warm, and respectful Hindi (हिन्दी) in Devanagari script.",
        "bn": "Important: Respond in fluent, warm, and respectful Bengali (বাংলা).",
        "te": "Important: Respond in fluent, warm, and respectful Telugu (తెలుగు).",
        "ta": "Important: Respond in fluent, warm, and respectful Tamil (தமிழ்).",
        "en": "Respond in English with cultural warmth and depth.",
    }
    lang_prefix = lang_instructions.get(lang_code, "")

    # Format specialized prompts according to Saathi's 4 core pillars
    if action in ["tell_story", "tell my story"]:
        prompt = (
            f"{lang_prefix}\n"
            f"An artisan wants you to draft their personal story and craft biography for KARIGAR.\n"
            f"Details provided: '{query_clean}'.\n"
            f"Please write an evocative, culturally grounded narrative draft (3-4 paragraphs) emphasizing their roots, "
            f"generations of practice, materials used, and the soulful dedication in each handmade piece. Include a suggested title."
        )
    elif action in ["price_work", "price my work"]:
        prompt = (
            f"{lang_prefix}\n"
            f"An artisan is seeking pricing advice on their work.\n"
            f"Craft information: '{query_clean}'.\n"
            f"Calculate a fair price structure based on:\n"
            f"1. Estimated raw materials cost\n"
            f"2. Living daily wage (respecting manual hours, minimum ₹600-₹800/day)\n"
            f"3. Heritage rarity / master skill margin\n"
            f"Explain clearly how this fair price is reached and remind them that KARIGAR charges 0% platform commission."
        )
    elif action in ["show_work", "show my work"]:
        prompt = (
            f"{lang_prefix}\n"
            f"An artisan wants advice on how to showcase and present their craft on KARIGAR.\n"
            f"Craft query: '{query_clean}'.\n"
            f"Give 3-4 actionable tips on photographing textures, highlighting natural handmade tool marks, "
            f"capturing short video process clips, and describing unique details collectors look for."
        )
    elif action in ["find_buyers", "find buyers"]:
        prompt = (
            f"{lang_prefix}\n"
            f"An artisan wants guidance on finding buyers and connecting with audiences.\n"
            f"Craft query: '{query_clean}'.\n"
            f"Suggest specific types of collectors (e.g. interior designers, cultural institutions, export buyers, "
            f"conscious luxury consumers) and advise how to tell their story effectively."
        )
    elif action == "voice":
        prompt = (
            f"{lang_prefix}\n"
            f"The following is a spoken audio transcript from an Indian artisan:\n"
            f"Transcript: '{query_clean}'\n"
            f"Acknowledge what they said with warm companionship and offer the immediate next step to assist them."
        )
    else:
        prompt = f"{lang_prefix}\nArtisan / User Query: '{query_clean}'\nAnswer as Saathi, the helpful companion on KARIGAR."

    # Try Gemini 2.5 Flash
    llm_res = call_gemini_llm(prompt)
    if llm_res.get("success"):
        return {
            "success": True,
            "reply": llm_res["text"],
            "engine": llm_res["engine"],
            "action": action,
        }

    # Offline Intelligent Heuristic Fallback
    fallback_text = _offline_saathi_response(query_clean, action)
    return {
        "success": True,
        "reply": fallback_text,
        "engine": "heritage_knowledge_graph_offline",
        "action": action,
        "notice": "Generated via Saathi local knowledge graph."
    }


def _offline_saathi_response(query: str, action: str) -> str:
    """Deterministic, high-fidelity cultural knowledge base fallback."""
    q_low = query.lower()

    if action in ["price_work", "price my work"] or any(k in q_low for k in ["price", "cost", "wage", "rupee", "₹", "keemat"]):
        return (
            "⚖️ **Saathi Fair Living Wage Assessment**:\n\n"
            "Under the Fair Craft Index, every authentic piece must ensure dignity of manual labor:\n"
            "• **Raw Materials**: Natural river silt / organic dyes / seasoned timber (~₹800 - ₹1,500)\n"
            "• **Living Daily Wage**: ₹750/day × manual artisan hours\n"
            "• **Generational Heritage Margin**: 15–25% for GI-recognized master craftsmanship\n\n"
            "💡 **KARIGAR Promise**: 100% of your listed price settles directly into your account with 0% platform commission."
        )

    if action in ["tell_story", "tell my story"] or any(k in q_low for k in ["story", "kahani", "history", "about", "lineage"]):
        return (
            "📜 **Your Story Draft**:\n\n"
            "\"Carrying forward generations of sacred craftsmanship, each piece is born from earth, memory, and patient hands. "
            "Free from industrial shortcuts, our process honors the raw texture of natural materials and ancestral techniques passed down like quiet heirlooms.\n\n"
            "When you hold this craft, you hold the living heartbeat of our village and centuries of unhurried artistry.\"\n\n"
            "✨ *AI drafts. You decide. You can adapt or copy this text directly into your profile!*"
        )

    if action in ["show_work", "show my work"] or any(k in q_low for k in ["photo", "picture", "video", "show", "camera"]):
        return (
            "📸 **4 Rules to Showcase Your Craft on KARIGAR**:\n\n"
            "1. **Morning Sunlight**: Photograph outdoors or near a window—natural light captures genuine clay and textile tones.\n"
            "2. **The Maker's Touch**: Take a close-up with your hands holding or shaping the piece. Buyers value human touch.\n"
            "3. **Process Video**: Share a 15-30 second clip showing the rhythmic hand movements (the wheel turning, the chisel striking).\n"
            "4. **Celebrate Imperfections**: Show natural glaze crazing or handloom weft variations—this is proof of 100% handmade purity."
        )

    if action in ["find_buyers", "find buyers"] or any(k in q_low for k in ["buyer", "customer", "market", "sell", "order"]):
        return (
            "🤝 **Connecting with Your Ideal Patrons**:\n\n"
            "• **Conscious Connoisseurs**: Modern buyers seek authenticity and provenance, not mass-produced replicas.\n"
            "• **Architects & Curators**: Premium interior studios look for bespoke pottery, hand-carved wood, and heritage tapestries.\n"
            "• **Story-Driven Discovery**: By tagging your regional tradition, collectors discovering Indian living heritage find you directly."
        )

    # Specific craft queries
    if "terracotta" in q_low or "clay" in q_low or "mitti" in q_low:
        return (
            "🏺 **Terracotta Tradition**: Sourced from alluvial riverbeds and fired in low-oxygen kilns. "
            "Whether it is Bankura's guardian horses or Gorakhpur's terracotta figures, highlight the porous natural texture and sun-baked resilience."
        )
    if "wood" in q_low or "channapatna" in q_low or "lakdi" in q_low:
        return (
            "🪵 **Lacquerware & Woodcraft**: Using sustainable Wrightia tinctoria (Aale mara) wood and non-toxic natural lac colored with turmeric and indigo. Safe, timeless, and silky smooth."
        )
    if "silk" in q_low or "saree" in q_low or "banarasi" in q_low:
        return (
            "🧵 **Handloom Weaving**: Authentic pit-loom weaving requires weeks of coordinated pedaling and shuttle movement. Real zari threads woven into Kadhwa patterns signify living royalty."
        )

    return (
        f"Namaste! I am Saathi, your companion on KARIGAR. "
        f"I can help you articulate your story, calculate fair living wages, prepare photographs and videos of your process, "
        f"or connect with discerning collectors. What would you like to work on today?"
    )


def catalog_craft_with_saathi(transcript: str) -> dict:
    """
    Structured extraction: converts spoken artisan audio transcript or unstructured notes into a valid JSON craft object.
    """
    if not transcript or not transcript.strip():
        return {"success": False, "error": "Transcript is empty."}

    text = transcript.strip()
    api_key = get_gemini_api_key()

    if api_key:
        prompt = (
            f"You are Saathi AI cataloger for KARIGAR.\n"
            f"Convert this artisan's spoken transcript or notes into structured JSON:\n"
            f"'{text}'\n\n"
            f"Return ONLY valid JSON matching this schema:\n"
            f"{{\n"
            f'  "name": "Title of craft",\n'
            f'  "category": "e.g. Pottery, Handloom, Woodcraft, Metalcraft, Folk Art",\n'
            f'  "description": "2-3 evocative sentences describing the craft, heritage and materials",\n'
            f'  "materials": "Comma-separated materials",\n'
            f'  "suggested_price": 1250.0,\n'
            f'  "minimum_price": 950.0,\n'
            f'  "selling_method": "fixed"\n'
            f"}}"
        )
        try:
            res = call_gemini_llm(prompt, system_instruction="You output ONLY raw JSON without markdown code fences.")
            if res.get("success"):
                cleaned_text = res["text"]
                if "```json" in cleaned_text:
                    cleaned_text = cleaned_text.split("```json")[1].split("```")[0].strip()
                elif "```" in cleaned_text:
                    cleaned_text = cleaned_text.split("```")[1].split("```")[0].strip()
                parsed = json.loads(cleaned_text)
                parsed["success"] = True
                parsed["engine"] = res["engine"]
                return parsed
        except Exception:
            pass

    # Heuristic fallback
    return {
        "success": True,
        "engine": "heuristic_fallback",
        "name": "Handcrafted Artisanal Creation",
        "category": "Traditional Indian Craft",
        "description": f"Authentic handmade piece created with ancestral care. {text[:140]}",
        "materials": "Indigenous natural materials",
        "suggested_price": 1500.0,
        "minimum_price": 1200.0,
        "selling_method": "fixed",
    }


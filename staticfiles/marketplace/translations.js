/**
 * KARIGAR Multilingual Translation Engine
 * Supports instantaneous client-side UI switching across English, Hindi (हिन्दी),
 * Bengali (বাংলা), Telugu (తెలుగు), and Tamil (தமிழ்).
 */

const KARIGAR_TRANSLATIONS = {
    en: {
        nav_discover: "Discover",
        nav_stories: "Stories",
        nav_traditions: "Traditions",
        nav_for_artisans: "For artisans",
        hero_tagline: "हर हाथ की अपनी कहानी",
        hero_title: "Every hand leaves a story.",
        hero_sub: "KARIGAR is a living digital sanctuary connecting master Indian artisans directly to discerning patrons with 0% platform fee.",
        hero_cta_crafts: "Explore crafts ↗",
        hero_cta_artisans: "Meet the artisans ↗",
        filter_all_categories: "All categories",
        filter_all_regions: "All regions",
        filter_search_placeholder: "Search crafts, techniques, regions...",
        filter_button: "Filter",
        fixed_price: "Fixed Price",
        accept_offers: "Accept Offers",
        auction: "Auction",
        view_craft: "View craft ↗",
        view_artisan: "View artisan ↗",
        view_practice: "Explore tradition ↗",
        saathi_eyebrow: "YOUR CRAFT COPILOT",
        saathi_title_prefix: "Namaste,",
        saathi_title_sub: "I'm Saathi.",
        saathi_desc: "Powered by Google Gemini. From drafting your artisan story to calculating fair living wages, I am here to assist your living heritage.",
        saathi_act1_title: "Tell my story",
        saathi_act1_sub: "Turn your oral memory into a profile bio",
        saathi_act2_title: "Price my work",
        saathi_act2_sub: "Fair Craft living wage assessment",
        saathi_act3_title: "Show my work",
        saathi_act3_sub: "Photography & process video guidance",
        saathi_act4_title: "Find buyers",
        saathi_act4_sub: "Connect with cultural connoisseurs",
        saathi_input_ph: "Ask anything or describe your piece...",
        saathi_send: "Ask ↗",
        saathi_voice_title: "Speak to Saathi",
        saathi_voice_sub: "Tap to speak · English / Hindi / Hinglish",
        saathi_voice_listening: "Listening... Speak your craft details",
        saathi_footer_tag: "AI drafts. You decide.",
        saathi_badge: "साथी · AI Companion",
        footer_brand_sub: "Every hand leaves a story",
        footer_tagline: "A digital identity and discovery platform for Indian artisans and living craft traditions.",
        copy_text: "📋 Copy text",
        use_in_form: "✍️ Use in Form",
        copied: "✓ Copied!"
    },
    hi: {
        nav_discover: "कलाकृतियाँ",
        nav_stories: "कारीगर",
        nav_traditions: "परंपराएं",
        nav_for_artisans: "कारीगरों के लिए",
        hero_tagline: "हर हाथ की अपनी कहानी",
        hero_title: "हर हाथ की अपनी एक कहानी होती है।",
        hero_sub: "कारीगर एक जीवंत डिजिटल मंच है जो भारत के पारंपरिक शिल्पकारों को सीधे कला-प्रेमियों से जोड़ता है।",
        hero_cta_crafts: "कलाकृतियाँ देखें ↗",
        hero_cta_artisans: "कारीगरों से मिलें ↗",
        filter_all_categories: "सभी श्रेणियाँ",
        filter_all_regions: "सभी क्षेत्र",
        filter_search_placeholder: "शिल्प, तकनीक या स्थान खोजें...",
        filter_button: "खोजें",
        fixed_price: "निश्चित मूल्य",
        accept_offers: "प्रस्ताव स्वीकार्य",
        auction: "नीलामी",
        view_craft: "विवरण देखें ↗",
        view_artisan: "कारीगर प्रोफ़ाइल ↗",
        view_practice: "परंपरा जानें ↗",
        saathi_eyebrow: "आपका शिल्प साथी",
        saathi_title_prefix: "नमस्ते,",
        saathi_title_sub: "मैं साथी हूँ।",
        saathi_desc: "गूगल जेमिनी द्वारा संचालित। आपकी शिल्प कहानी लिखने से लेकर उचित दैनिक मेहनताना तय करने तक, मैं आपके साथ हूँ।",
        saathi_act1_title: "मेरी कहानी बनाएं",
        saathi_act1_sub: "अपनी मौखिक विरासत को प्रोफ़ाइल में बदलें",
        saathi_act2_title: "उचित कीमत आंकें",
        saathi_act2_sub: "उचित दैनिक मेहनताना और लागत गणना",
        saathi_act3_title: "काम प्रदर्शित करें",
        saathi_act3_sub: "फ़ोटोग्राफ़ी और प्रक्रिया वीडियो मार्गदर्शन",
        saathi_act4_title: "खरीदार खोजें",
        saathi_act4_sub: "संस्कृति-प्रेमी संरक्षकों से जुड़ें",
        saathi_input_ph: "कुछ भी पूछें या अपनी कला का वर्णन करें...",
        saathi_send: "पूछें ↗",
        saathi_voice_title: "साथी से बात करें",
        saathi_voice_sub: "बोलने के लिए दबाएं · हिन्दी / English",
        saathi_voice_listening: "सुन रहा हूँ... अपनी कला के बारे में बताएं",
        saathi_footer_tag: "एआई सुझाव देता है। निर्णय आपका है।",
        saathi_badge: "साथी · AI साथी",
        footer_brand_sub: "हर हाथ की अपनी कहानी",
        footer_tagline: "भारतीय कारीगरों और जीवंत शिल्प परंपराओं के लिए एक डिजिटल पहचान मंच।",
        copy_text: "📋 कॉपी करें",
        use_in_form: "✍️ फ़ॉर्म में जोड़ें",
        copied: "✓ कॉपी हो गया!"
    },
    bn: {
        nav_discover: "অনুসন্ধান",
        nav_stories: "কারিগর",
        nav_traditions: "ঐতিহ্য",
        nav_for_artisans: "কারিগরদের জন্য",
        hero_tagline: "প্রতিটি হাতের একটি গল্প আছে",
        hero_title: "প্রতিটি হাতের নিজস্ব গল্প থাকে।",
        hero_sub: "কারিগর হলো ঐতিহ্যবাহী ভারতীয় শিল্পীদের শিল্পপ্রেমীদের সাথে সরাসরি যুক্ত করার একটি ডিজিটাল প্ল্যাটফর্ম।",
        hero_cta_crafts: "শিল্পকর্ম দেখুন ↗",
        hero_cta_artisans: "কারিগরদের সাথে পরিচিত হন ↗",
        filter_all_categories: "সব বিভাগ",
        filter_all_regions: "সব অঞ্চল",
        filter_search_placeholder: "শিল্প, পদ্ধতি বা এলাকা খুঁজুন...",
        filter_button: "অনুসন্ধান",
        fixed_price: "নির্দিষ্ট মূল্য",
        accept_offers: "প্রস্তাব গ্রহণযোগ্য",
        auction: "নিলাম",
        view_craft: "বিবরণ দেখুন ↗",
        view_artisan: "কারিগর প্রোফাইল ↗",
        view_practice: "ঐতিহ্য জানুন ↗",
        saathi_eyebrow: "আপনার শিল্প সহচর",
        saathi_title_prefix: "নমস্কার,",
        saathi_title_sub: "আমি সাথী।",
        saathi_desc: "গুগল জেমিনাই চালিত। আপনার গল্প লেখা থেকে শুরু করে ন্যায্য পারিশ্রমিক নির্ধারণ—আমি সর্বদা আপনার সাথে আছি।",
        saathi_act1_title: "আমার গল্প লিখুন",
        saathi_act1_sub: "আপনার মুখের কথা প্রোফাইলে রূপান্তর করুন",
        saathi_act2_title: "ন্যায্য মূল্য নির্ধারণ",
        saathi_act2_sub: "ন্যায্য দৈনিক মজুরি ও খরচ মূল্যায়ন",
        saathi_act3_title: "কাজ প্রদর্শন করুন",
        saathi_act3_sub: "ফটোগ্রাফি ও তৈরির ভিডিও নির্দেশিকা",
        saathi_act4_title: "ক্রেতা খুঁজুন",
        saathi_act4_sub: "সংস্কৃতিপ্রেমী সংগ্রাহকদের সাথে যোগাযোগ করুন",
        saathi_input_ph: "কিছু জিজ্ঞাসা করুন বা আপনার শিল্প বর্ণনা করুন...",
        saathi_send: "জিজ্ঞাসা ↗",
        saathi_voice_title: "সাথীর সাথে কথা বলুন",
        saathi_voice_sub: "বলতে ট্যাপ করুন · বাংলা / English",
        saathi_voice_listening: "শুনছি... আপনার শিল্প সম্পর্কে বলুন",
        saathi_footer_tag: "এআই ড্রাফ্ট করে। সিদ্ধান্ত আপনার।",
        saathi_badge: "সাথী · AI সহযোগী",
        footer_brand_sub: "প্রতিটি হাতের নিজস্ব গল্প থাকে",
        footer_tagline: "ভারতীয় কারিগর এবং জীবন্ত ঐতিহ্যের একটি ডিজিটাল পরিচয় মঞ্চ।",
        copy_text: "📋 কপি করুন",
        use_in_form: "✍️ ফর্মে যোগ করুন",
        copied: "✓ কপি করা হয়েছে!"
    },
    te: {
        nav_discover: "అన్వేషించండి",
        nav_stories: "కథలు",
        nav_traditions: "సంప్రదాయాలు",
        nav_for_artisans: "చేతివృత్తుల వారి కోసం",
        hero_tagline: "ప్రతి చేతికీ ఒక కథ ఉంటుంది",
        hero_title: "ప్రతి చేతికీ ఒక కథ ఉంటుంది.",
        hero_sub: "భారతీయ సాంప్రదాయ కళాకారులను నేరుగా కళాభిమానులతో అనుసంధానించే వేదిక కారిగర్.",
        hero_cta_crafts: "కళలను చూడండి ↗",
        hero_cta_artisans: "కళాకారులను కలవండి ↗",
        filter_all_categories: "అన్ని వర్గాలు",
        filter_all_regions: "అన్ని ప్రాంతాలు",
        filter_search_placeholder: "కళలు, సాంకేతికతలు శోధించండి...",
        filter_button: "శోధన",
        fixed_price: "స్థిర ధర",
        accept_offers: "ఆఫర్లు స్వీకరిస్తాం",
        auction: "వేలం",
        view_craft: "వివరాలు చూడండి ↗",
        view_artisan: "కళాకారుడి ప్రొఫైల్ ↗",
        view_practice: "సంప్రదాయాన్ని తెలుసుకోండి ↗",
        saathi_eyebrow: "మీ కళా సహచరుడు",
        saathi_title_prefix: "నమస్కారం,",
        saathi_title_sub: "నేను సాథీని.",
        saathi_desc: "గూగుల్ జెమినీ ద్వారా ఆధారితం. మీ కళా ప్రయాణాన్ని రికార్డ్ చేయడం నుండి సరైన ధర నిర్ణయించే వరకు సాథీ సహాయం చేస్తుంది.",
        saathi_act1_title: "నా కథ రాయండి",
        saathi_act1_sub: "మీ జ్ఞాపకాలను ప్రొఫైల్ గా మార్చుకోండి",
        saathi_act2_title: "ధర నిర్ణయించండి",
        saathi_act2_sub: "న్యాయమైన రోజువారీ వేతన లెక్కింపు",
        saathi_act3_title: "పనిని ప్రదర్శించండి",
        saathi_act3_sub: "ఫోటోలు మరియు తయారీ వీడియో సలహాలు",
        saathi_act4_title: "కొనుగోలుదారులను కనుగొనండి",
        saathi_act4_sub: "కళాభిమానులతో అనుసంధానం అవ్వండి",
        saathi_input_ph: "ఏదైనా అడగండి లేదా మీ కళను వివరించండి...",
        saathi_send: "అడగండి ↗",
        saathi_voice_title: "సాథీతో మాట్లాడండి",
        saathi_voice_sub: "మాట్లాడటానికి నొక్కండి · తెలుగు / English",
        saathi_voice_listening: "వింటున్నాను... మీ కళ గురించి చెప్పండి",
        saathi_footer_tag: "AI డ్రాఫ్ట్ చేస్తుంది. నిర్ణయం మీదే.",
        saathi_badge: "సాథీ · AI సహచరి",
        footer_brand_sub: "ప్రతి చేతికీ ఒక కథ ఉంటుంది",
        footer_tagline: "భారతీయ కళాకారులు మరియు సంప్రదాయాల కోసం డిజిటల్ గుర్తింపు.",
        copy_text: "📋 కాపీ చేయండి",
        use_in_form: "✍️ ఫారంలో వాడండి",
        copied: "✓ కాపీ అయింది!"
    }
};

// Current Active Language
let CURRENT_LANG = localStorage.getItem("karigar_lang") || "en";

function setLanguage(lang) {
    if (!KARIGAR_TRANSLATIONS[lang]) lang = "en";
    CURRENT_LANG = lang;
    localStorage.setItem("karigar_lang", lang);

    // Apply translations across DOM
    applyTranslations(lang);

    // Update active state in switcher UI
    document.querySelectorAll(".lang-btn").forEach(btn => {
        if (btn.getAttribute("data-lang") === lang) {
            btn.classList.add("is-active");
        } else {
            btn.classList.remove("is-active");
        }
    });

    // Notify speech recognition language
    if (window.RecognitionLangMap) {
        window.activeSpeechLang = window.RecognitionLangMap[lang] || "en-IN";
    }

    console.log(`KARIGAR language switched to: ${lang}`);
}

function applyTranslations(lang) {
    const dict = KARIGAR_TRANSLATIONS[lang] || KARIGAR_TRANSLATIONS.en;

    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (dict[key]) {
            if (el.tagName === "INPUT" || el.tagName === "TEXTAREA") {
                el.placeholder = dict[key];
            } else {
                el.textContent = dict[key];
            }
        }
    });

    document.querySelectorAll("[data-i18n-html]").forEach(el => {
        const key = el.getAttribute("data-i18n-html");
        if (dict[key]) {
            el.innerHTML = dict[key];
        }
    });
}

// Initialize on DOMContentLoaded
document.addEventListener("DOMContentLoaded", function () {
    setLanguage(CURRENT_LANG);
});


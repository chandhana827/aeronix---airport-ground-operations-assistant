from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum

# --- Types ---

class AirportStage(str, Enum):
    CHECK_IN = 'Check-in'
    SECURITY = 'Security'
    TERMINAL = 'Terminal/Lounge'
    BOARDING = 'Boarding'
    BAGGAGE = 'Baggage Claim'

@dataclass
class GroundOpGuide:
    id: str
    title: str
    description: str
    steps: List[str]
    icon: str
    color: str 

@dataclass
class TerminalZone:
    id: str
    name: str
    status: str 
    difficulty: int = 0
    waitTime: int = 0
    description: str = ""
    x: int = 0
    y: int = 0

@dataclass
class FAQItem:
    category: str
    question: str
    answer: str

@dataclass
class KBEntry:
    keywords: List[str]
    content: str

@dataclass
class LanguageOption:
    code: str
    name: str
    flag: str

@dataclass
class PassengerTypeOption:
    id: str
    name: str
    icon: str
    description: str

# --- Constants ---

LANGUAGES = [
    LanguageOption('en', 'English', '🇺🇸'),
    LanguageOption('es', 'Español', '🇪🇸'),
    LanguageOption('fr', 'Français', '🇫🇷'),
    LanguageOption('hi', 'हिन्दी', '🇮🇳'),
    LanguageOption('bn', 'বাংলা', '🇮🇳'),
    LanguageOption('te', 'తెలుగు', '🇮🇳'),
    LanguageOption('ta', 'தமிழ்', '🇮🇳'),
    LanguageOption('mr', 'मराठी', '🇮🇳'),
    LanguageOption('de', 'Deutsch', '🇩🇪'),
    LanguageOption('zh', '中文', '🇨🇳'),
    LanguageOption('ja', '日本語', '🇯🇵'),
]

PASSENGER_TYPES = [
    PassengerTypeOption('standard', 'Standard', '👤', 'General travelers'),
    PassengerTypeOption('business', 'Business', '💼', 'Speed & efficiency'),
    PassengerTypeOption('family', 'Family', '👨‍👩‍👧', 'Strollers & play areas'),
    PassengerTypeOption('mobility', 'Reduced Mobility', '♿', 'Access & support'),
]


# We will change TERMINAL_ZONES to be a function that returns the list with proper names
# But first, let's define the raw data with translation keys or logic.
# To minimize refactoring impact, let's keep TERMINAL_ZONES as the base (English/Structure) 
# and add a translation map for the names/descriptions.

TERMINAL_ZONES_BASE = [
    {'id': 'z1', 'x': 20, 'y': 30, 'waitTime': 25, 'status': 'Busy'},
    {'id': 'z2', 'x': 50, 'y': 25, 'waitTime': 8, 'status': 'Clear'},
    {'id': 'z3', 'x': 60, 'y': 50, 'waitTime': 0, 'status': 'Crowded'},
    {'id': 'z4', 'x': 80, 'y': 70, 'waitTime': 12, 'status': 'Busy'},
    {'id': 'z5', 'x': 30, 'y': 80, 'waitTime': 15, 'status': 'Clear'},
]

ZONE_TRANSLATIONS = {
    'en': {
        'z1': {'name': 'Zone A: Main Check-in', 'desc': 'International departures hub.'},
        'z2': {'name': 'Zone B: Security North', 'desc': 'Fast-track and priority lane.'},
        'z3': {'name': 'Zone C: Duty Free Central', 'desc': 'Main shopping and dining plaza.'},
        'z4': {'name': 'Zone D: Gate 1-20', 'desc': 'Regional flight departures.'},
        'z5': {'name': 'Zone E: Baggage Hall', 'desc': 'Arrivals and customs area.'},
    },
    'es': {
        'z1': {'name': 'Zona A: Facturación Principal', 'desc': 'Centro de salidas internacionales.'},
        'z2': {'name': 'Zona B: Seguridad Norte', 'desc': 'Carril rápido y prioritario.'},
        'z3': {'name': 'Zona C: Duty Free Central', 'desc': 'Plaza principal de compras y restaurantes.'},
        'z4': {'name': 'Zona D: Puerta 1-20', 'desc': 'Salidas de vuelos regionales.'},
        'z5': {'name': 'Zona E: Sala de Equipajes', 'desc': 'Área de llegadas y aduanas.'},
    },
    'fr': {
        'z1': {'name': 'Zone A: Enregistrement Principal', 'desc': 'Hub des départs internationaux.'},
        'z2': {'name': 'Zone B: Sécurité Nord', 'desc': 'File rapide et prioritaire.'},
        'z3': {'name': 'Zone C: Duty Free Central', 'desc': 'Zone principale de shopping et restauration.'},
        'z4': {'name': 'Zone D: Porte 1-20', 'desc': 'Départs des vols régionaux.'},
        'z5': {'name': 'Zone E: Salle des Bagages', 'desc': 'Zone des arrivées et douanes.'},
    },
    'de': {
        'z1': {'name': 'Zone A: Haupt-Check-in', 'desc': 'Drehkreuz für internationale Abflüge.'},
        'z2': {'name': 'Zone B: Sicherheit Nord', 'desc': 'Schnellspur und Prioritätsspur.'},
        'z3': {'name': 'Zone C: Duty Free Zentrum', 'desc': 'Haupteinkaufs- und Essbereich.'},
        'z4': {'name': 'Zone D: Gate 1-20', 'desc': 'Regionale Abflüge.'},
        'z5': {'name': 'Zone E: Gepäckhalle', 'desc': 'Ankunfts- und Zollbereich.'},
    },
    'hi': {
        'z1': {'name': 'ज़ोन A: मुख्य चेक-इन', 'desc': 'अंतर्राष्ट्रीय प्रस्थान केंद्र।'},
        'z2': {'name': 'ज़ोन B: सुरक्षा उत्तर', 'desc': 'फास्ट-ट्रैक और प्राथमिकता लेन।'},
        'z3': {'name': 'ज़ोन C: ड्यूटी फ्री सेंट्रल', 'desc': 'मुख्य खरीदारी और भोजन प्लाजा।'},
        'z4': {'name': 'ज़ोन D: गेट 1-20', 'desc': 'क्षेत्रीय उड़ान प्रस्थान।'},
        'z5': {'name': 'ज़ोन E: बैगेज हॉल', 'desc': 'आगमन और सीमा शुल्क क्षेत्र।'},
    },
    # Fallbacks for others can default to English logic in the getter
}

TERMINAL_ZONES = [] # Kept for backward compatibility if imports expect it, but we should switch to getter.
# Actually, let's redefine TERMINAL_ZONES as a getter property or just a list for default EN to avoid breaking imports immediately,
# but really we want `get_terminal_zones(lang)`.

def get_terminal_zones(lang_code):
    zones = []
    # Default to English if lang not found in ZONE_TRANSLATIONS
    trans_map = ZONE_TRANSLATIONS.get(lang_code, ZONE_TRANSLATIONS['en'])
    
    for base in TERMINAL_ZONES_BASE:
        t = trans_map.get(base['id'], ZONE_TRANSLATIONS['en'][base['id']])
        zones.append(TerminalZone(
            id=base['id'],
            name=t['name'],
            status=base['status'],
            description=t['desc'],
            x=base['x'],
            y=base['y'],
            waitTime=base['waitTime']
        ))
    return zones

# For initial import compatibility before we update app.py
TERMINAL_ZONES = get_terminal_zones('en')

PEAK_HOURS_DATA = [
    {'hour': '04:00', 'load': 30},
    {'hour': '06:00', 'load': 85},
    {'hour': '08:00', 'load': 95},
    {'hour': '10:00', 'load': 70},
    {'hour': '12:00', 'load': 60},
    {'hour': '14:00', 'load': 80},
    {'hour': '16:00', 'load': 90},
    {'hour': '18:00', 'load': 85},
    {'hour': '20:00', 'load': 50},
    {'hour': '22:00', 'load': 20},
]

KNOWLEDGE_BASE = [
    KBEntry(["power", "charging", "plug", "outlet"], "Charging stations are available at every gate. Premium USB-C ports are found near Gate A5 and B10."),
    KBEntry(["water", "refill", "drink", "fountain"], "Filtered water refill stations are located next to every set of restrooms throughout the terminal."),
    KBEntry(["pharmacy", "medicine", "doctor", "health"], "A 24/7 pharmacy is located in Terminal 1, landside, near the main entrance."),
    KBEntry(["pet", "dog", "animal", "relief"], "Pet relief areas are located outside Terminal 1 (Area B) and inside Terminal 2 near Gate D1."),
    KBEntry(["smoking", "cigarette"], "The terminal is smoke-free. Designated smoking areas are available outside the departure level.")
]

# --- Translations ---

UI_TRANSLATIONS = {
  'en': {
    'nav': { 'map': "Operations Map", 'terminals': "Terminals", 'safety': "Safety", 'helpdesk': "Helpdesk" },
    'hero': { 'tag': "Local Ground Ops Context", 'title': "Airport Navigation, Personalized.", 'desc': "Aeronix provides tailored support for your journey. Choose your language and traveler type for the most accurate ground operations guidance.", 'cta1': "Launch Terminal Map", 'cta2': "Status: OPERATIONAL" },
    'sections': { 'mapTitle': "Terminal Map & Knowledge", 'mapDesc': "Explore terminal facilities and live zone status.", 'faqTitle': "Quick Help Center", 'analyticsTitle': "Congestion Analytics", 'analyticsDesc': "Live load metrics based on peak hours.", 'checklistTitle': "Operational Checklist", 'checklistDesc': "Follow these mandatory procedures for a smooth departure.", 'assistantTitle': "Operational Assistant", 'assistantDesc': "Chatting for your journey." },
    'stats': { 'waitTime': "Current Wait Time", 'securityStatus': "Security Status", 'normal': "Normal operations", 'staffing': "Staffing level: Medium", 'traffic': "High Traffic Expected", 'loadDesc': "Live average load based on historical peak hours" },
    'proTips': { 'family': "Look for the 'Family Fast Track' near Security Zone B. It has extra space for strollers and helpful staff.", 'business': "Need to work? The Business Lounge near Gate B12 offers high-speed Wi-Fi and quiet workspaces.", 'mobility': "Accessible elevators are conveniently located near every set of escalators in the central atrium.", 'standard': "Always keep your boarding pass and ID in a side pocket for quick access during security checks." },
    'chat': { 'placeholder': "Ask a question...", 'send': "Send", 'assistantGreeting': "Hello! I'm Aeronix. I can help you understand airport security, baggage rules, and boarding procedures. How can I assist you today?" },
  },
  'hi': {
    'nav': { 'map': "संचालन मानचित्र", 'terminals': "टर्मिनल", 'safety': "सुरक्षा", 'helpdesk': "सहायता डेस्क" },
    'hero': { 'tag': "स्थानीय ग्राउंड ऑप्स संदर्भ", 'title': "हवाई अड्डा नेविगेशन, व्यक्तिगत।", 'desc': "एरोनिक्स (Aeronix) आपकी यात्रा के लिए व्यक्तिगत सहायता प्रदान करता है। सबसे सटीक ग्राउंड ऑपरेशन मार्गदर्शन के लिए अपनी भाषा और यात्री प्रकार चुनें।", 'cta1': "टर्मिनल मानचित्र लॉन्च करें", 'cta2': "स्थिति: चालू" },
    'sections': { 'mapTitle': "टर्मिनल मानचित्र और ज्ञान", 'mapDesc': "टर्मिनल सुविधाओं और लाइव ज़ोन स्थिति का अन्वेषण करें।", 'faqTitle': "त्वरित सहायता केंद्र", 'analyticsTitle': "भीड़ विश्लेषण", 'analyticsDesc': "पीक ऑवर्स के आधार पर लाइव लोड मेट्रिक्स।", 'checklistTitle': "परिचालन चेकलिस्ट", 'checklistDesc': "सुचारू प्रस्थान के लिए इन अनिवार्य प्रक्रियाओं का पालन करें।", 'assistantTitle': "परिचालन सहायक", 'assistantDesc': "आपकी यात्रा के लिए बातचीत।" },
    'stats': { 'waitTime': "वर्तमान प्रतीक्षा समय", 'securityStatus': "सुरक्षा स्थिति", 'normal': "सामान्य संचालन", 'staffing': "स्टाफिंग स्तर: मध्यम", 'traffic': "उच्च यातायात की उम्मीद", 'loadDesc': "ऐतिहासिक पीक ऑवर्स के आधार पर लाइव औसत लोड" },
    'proTips': { 'family': "सुरक्षा क्षेत्र बी के पास 'फैमिली फास्ट ट्रैक' देखें। इसमें स्ट्रोलर के लिए अतिरिक्त जगह है।", 'business': "काम करने की ज़रूरत है? गेट बी 12 के पास बिजनेस लाउंज हाई-स्पीड वाई-फाई प्रदान करता है।", 'mobility': "सुलभ लिफ्ट केंद्रीय प्रांगण में हर एस्केलेटर के पास स्थित हैं।", 'standard': "सुरक्षा जांच के दौरान त्वरित पहुंच के लिए हमेशा अपना बोर्डिंग पास और आईडी पास रखें।" },
    'chat': { 'placeholder': "सवाल पूछें...", 'send': "भेजें", 'assistantGreeting': "नमस्ते! मैं एरोनिक्स (Aeronix) हूं। मैं आपको हवाई अड्डे की सुरक्षा, सामान के नियमों और बोर्डिंग प्रक्रियाओं को समझने में मदद कर सकता हूं। मैं आज आपकी कैसे सहायता कर सकता हूं?" },
  },
  'ta': {
    'nav': { 'map': "இயக்க வரைபடம்", 'terminals': "முனையங்கள்", 'safety': "பாதுகாப்பு", 'helpdesk': "உதவி மையம்" },
    'hero': { 'tag': "உள்ளூர் தரை செயல்பாடுகள்", 'title': "விமான நிலைய வழிசெலுத்தல், தனிப்பயனாக்கப்பட்டது.", 'desc': "ஏரோனிக்ஸ் (Aeronix) உங்கள் பயணத்திற்குத் தேவையான தனிப்பயனாக்கப்பட்ட ஆதரவை வழங்குகிறது.", 'cta1': "வரைபடத்தைத் தொடங்கு", 'cta2': "நிலை: செயல்பாட்டில் உள்ளது" },
    'sections': { 'mapTitle': "முனைய வரைபடம் மற்றும் அறிவு", 'mapDesc': "முனைய வசதிகள் மற்றும் நேரடி மண்டல நிலையை ஆராயுங்கள்.", 'faqTitle': "விரைவு உதவி மையம்", 'analyticsTitle': "நெரிசல் பகுப்பாய்வு", 'analyticsDesc': "நேரடி சுமை அளவீடுகள்.", 'checklistTitle': "இயக்க சரிபார்ப்புப் பட்டியல்", 'checklistDesc': "தடையற்ற பயணத்திற்கு இந்த கட்டாய நடைமுறைகளைப் பின்பற்றவும்.", 'assistantTitle': "இயக்க உதவியாளர்", 'assistantDesc': "உங்கள் பயணத்திற்கான உரையாடல்." },
    'stats': { 'waitTime': "தற்போதைய காத்திருப்பு நேரம்", 'securityStatus': "பாதுகாப்பு நிலை", 'normal': "சாதாரண செயல்பாடுகள்", 'staffing': "பணியாளர் நிலை: நடுத்தரம்", 'traffic': "அதிக போக்குவரத்து எதிர்பார்க்கப்படுகிறது", 'loadDesc': "நேரடி சராசரி சுமை" },
    'proTips': { 'family': "பாதுகாப்பு மண்டலம் B க்கு அருகில் 'குடும்ப விரைவுப் பாதை'யைத் தேடுங்கள்.", 'business': "வேலை செய்ய வேண்டுமா? கேட் B12 அருகில் பிசினஸ் லவுஞ்ச் உள்ளது.", 'mobility': "அனைத்து நகரும் படிக்கட்டுகளுக்கும் அருகில் மின்தூக்கிகள் உள்ளன.", 'standard': "பாதுகாப்பு சோதனையின் போது எளிதாக எடுக்க போர்டிங் பாஸை கைவசம் வைத்திருங்கள்." },
    'chat': { 'placeholder': "கேள்வி கேளுங்கள்...", 'send': "அனுப்பு", 'assistantGreeting': "வணக்கம்! நான் ஏரோனிக்ஸ் (Aeronix). விமான நிலைய பாதுகாப்பு, சாமான்கள் விதிகள் மற்றும் போர்டிங் நடைமுறைகளை புரிந்து கொள்ள நான் உங்களுக்கு உதவ முடியும். இன்று நான் உங்களுக்கு எப்படி உதவ முடியும்?" },
  },
  'te': {
    'nav': { 'map': "ఆపరేషన్స్ మ్యాప్", 'terminals': "టెర్మినల్స్", 'safety': "భద్రత", 'helpdesk': "హెల్ప్‌డెస్క్" },
    'hero': { 'tag': "స్థానిక గ్రౌండ్ ఆప్స్ సందర్భం", 'title': "విమానాశ్రయ నావిగేషన్, వ్యక్తిగతీకరించబడింది.", 'desc': "ఏరోనిక్స్ (Aeronix) మీ ప్రయాణానికి తగిన మద్దతును అందిస్తుంది.", 'cta1': "మ్యాప్‌ను ప్రారంభించండి", 'cta2': "స్థితి: పని చేస్తోంది" },
    'sections': { 'mapTitle': "టెర్మినల్ మ్యాప్ & జ్ఞానం", 'mapDesc': "టెర్మినల్ సౌకర్యాలను అన్వేషించండి.", 'faqTitle': "త్వరిత సహాయ కేంద్రం", 'analyticsTitle': "రద్దీ విశ్లేషణ", 'analyticsDesc': "లైవ్ లోడ్ మెట్రిక్స్.", 'checklistTitle': "ఆపరేషనల్ చెక్లిస్ట్", 'checklistDesc': "సులభమైన ప్రయాణం కోసం ఈ తప్పనిసరి విధానాలను అనుసరించండి.", 'assistantTitle': "ఆపరేషనల్ అసిస్టెంట్", 'assistantDesc': "మీ ప్రయాణం కోసం చాటింగ్." },
    'stats': { 'waitTime': "ప్రస్తుత వేచి ఉండే సమయం", 'securityStatus': "భద్రత స్థితి", 'normal': "సాధారణ కార్యకలాపాలు", 'staffing': "సిబ్బంది స్థాయి: మధ్యస్థం", 'traffic': "ఎక్కువ రద్దీ అవకాశం ఉంది", 'loadDesc': "లైవ్ సగటు లోడ్" },
    'proTips': { 'family': "సెక్యూరిటీ జోన్ B దగ్గర 'ఫ్యామిలీ ఫాస్ట్ ట్రాక్' కోసం చూడండి.", 'business': "పని చేయాలా? గేట్ B12 దగ్గర బిజినెస్ లాంజ్ ఉంది.", 'mobility': "ప్రతి ఎస్కలేటర్ దగ్గర లిఫ్టులు అందుబాటులో ఉన్నాయి.", 'standard': "సెక్యూరిటీ చెక్ కోసం బోర్డింగ్ పాస్ సిద్ధంగా ఉంచుకోండి." },
    'chat': { 'placeholder': "ప్రశ్న అడగండి...", 'send': "పంపండి", 'assistantGreeting': "నమస్కారం! నేను ఏరోనిక్స్ (Aeronix). విమానాశ్రయ భద్రత, సామాను నిబంధనలు మరియు బోర్డింగ్ విధానాలను అర్థం చేసుకోవడంలో నేను మీకు సహాయపడగలను. ఈరోజు నేను మీకు ఎలా సహాయం చేయగలను?" },
  },
  'bn': {
    'nav': { 'map': "অপারেশন ম্যাপ", 'terminals': "টার্মিনাল", 'safety': "নিরাপত্তা", 'helpdesk': "হেল্পডেস্ক" },
    'hero': { 'tag': "স্থানীয় গ্রাউন্ড অপারেশন", 'title': "ব্যক্তিগতকৃত বিমানবন্দর নেভিগেশন।", 'desc': "Aeronix আপনার যাত্রার জন্য উপযুক্ত সহায়তা প্রদান করে।", 'cta1': "ম্যাপ দেখুন", 'cta2': "অবস্থা: সচল" },
    'sections': { 'mapTitle': "টার্মিনাল ম্যাপ ও তথ্য", 'mapDesc': "টার্মিনাল সুবিধাগুলি দেখুন।", 'faqTitle': "সহায়তা কেন্দ্র", 'analyticsTitle': "ভিড় বিশ্লেষণ", 'analyticsDesc': "লাইভ ভিড় পরিমাপ।", 'checklistTitle': "অপারেশনাল চেকলিস্ট", 'checklistDesc': "একটি মসৃণ প্রস্থানের জন্য এই বাধ্যতামূলক পদ্ধতিগুলি অনুসরণ করুন।", 'assistantTitle': "অপারেশনাল অ্যাসিস্ট্যান্ট", 'assistantDesc': "আপনার যাত্রার জন্য চ্যাট।" },
    'stats': { 'waitTime': "বর্তমান অপেক্ষার সময়", 'securityStatus': "নিরাপত্তা অবস্থা", 'normal': "স্বাভাবিক অপারেশন", 'staffing': "কর্মী সংখ্যা: মাঝারি", 'traffic': "অধিক ভিড় প্রত্যাশিত", 'loadDesc': "লাইভ গড় ভিড়" },
    'proTips': { 'family': "সিকিউরিটি জোন B-এর কাছে 'ফ্যামিলি ফাস্ট ট্র্যাক' খুঁজুন।", 'business': "কাজ করার প্রয়োজন? গেট B12-এর কাছে বিজনেস লাউঞ্জ আছে।", 'mobility': "লিফটগুলি কেন্দ্রীয় চত্বরে অবস্থিত।", 'standard': "বোর্ডিং পাস এবং আইডি কার্ড সাথে রাখুন।" },
    'chat': { 'placeholder': "প্রশ্ন জিজ্ঞাসা করুন...", 'send': "পাঠান", 'assistantGreeting': "হ্যালো! আমি এরোনিক্স (Aeronix)। আমি আপনাকে বিমানবন্দরের নিরাপত্তা, লাগেজের নিয়ম এবং বোর্ডিং প্রক্রিয়া বুঝতে সাহায্য করতে পারি। আজ আমি আপনাকে কীভাবে সাহায্য করতে পারি?" },
  },
  'mr': {
    'nav': { 'map': "ऑपरेशन्स मॅप", 'terminals': "टर्मिनल्स", 'safety': "सुरक्षा", 'helpdesk': "हेल्पडेस्क" },
    'hero': { 'tag': "स्थानिक ग्राउंड ऑप्स संदर्भ", 'title': "विमानतळ नेव्हिगेशन, वैयक्तिकृत.", 'desc': "एरोनिक्स (Aeronix) तुमच्या प्रवासासाठी वैयक्तिक मदत प्रदान करते.", 'cta1': "मॅप सुरू करा", 'cta2': "स्थिती: कार्यरत" },
    'sections': { 'mapTitle': "टर्मिनल मॅप आणि माहिती", 'mapDesc': "टर्मिनल सुविधांची माहिती घ्या.", 'faqTitle': "त्वरीत मदत केंद्र", 'analyticsTitle': "गर्दीचे विश्लेषण", 'analyticsDesc': "लाईव्ह गर्दीची आकडेवारी.", 'checklistTitle': "ऑपरेशनल चेकलिस्ट", 'checklistDesc': "सुरळीत प्रवासासाठी या अनिवार्य नियमांचे पालन करा.", 'assistantTitle': "ऑपरेशनल असिस्टंट", 'assistantDesc': "तुमच्या प्रवासासाठी चॅट करा." },
    'stats': { 'waitTime': "सध्याची प्रतीक्षा वेळ", 'securityStatus': "सुरक्षा स्थिती", 'normal': "सामान्य कामकाज", 'staffing': "कर्मचारी संख्या: मध्यम", 'traffic': "जास्त गर्दीची शक्यता", 'loadDesc': "लाईव्ह सरासरी लोड" },
    'proTips': { 'family': "सुरक्षा झोन B जवळ 'फॅमिली फास्ट ट्रॅक' पहा.", 'business': "कामासाठी गेट B12 जवळ बिझनेस लाउंज उपलब्ध आहे.", 'mobility': "प्रत्येक एस्केलेटर जवळ लिफ्ट उपलब्ध आहेत.", 'standard': "सुरक्षा तपासणीसाठी बोर्डिंग पास तयार ठेवा." },
    'chat': { 'placeholder': "प्रश्न विचारा...", 'send': "पाठवा", 'assistantGreeting': "नमस्कार! मी एरोनिक्स (Aeronix) आहे. मी तुम्हाला विमानतळ सुरक्षा, बॅगेज नियम आणि बोर्डिंग प्रक्रिया समजून घेण्यास मदत करू शकतो. आज मी तुम्हाला कशी मदत करू शकतो?" },
  },
  'es': {
    'nav': { 'map': "Mapa de Operaciones", 'terminals': "Terminales", 'safety': "Seguridad", 'helpdesk': "Mesa de Ayuda" },
    'hero': { 'tag': "Contexto de Operaciones Terrestres", 'title': "Navegación Aeroportuaria, Personalizada.", 'desc': "Aeronix brinda apoyo personalizado para su viaje. Elija su idioma y tipo de viajero para la guía de operaciones terrestres más precisa.", 'cta1': "Iniciar Mapa de Terminal", 'cta2': "Estado: OPERATIVO" },
    'sections': { 'mapTitle': "Mapa de la Terminal y Conocimiento", 'mapDesc': "Explore las instalaciones de la terminal y el estado de las zonas en vivo.", 'faqTitle': "Centro de Ayuda Rápida", 'analyticsTitle': "Análisis de Congestión", 'analyticsDesc': "Métricas de carga en vivo basadas en horas pico.", 'checklistTitle': "Lista de Verificación Operativa", 'checklistDesc': "Siga estos procedimientos obligatorios para una salida sin contratiempos.", 'assistantTitle': "Asistente Operativo", 'assistantDesc': "Chateando para su viaje." },
    'stats': { 'waitTime': "Tiempo de Espera Actual", 'securityStatus': "Estado de Seguridad", 'normal': "Operaciones normales", 'staffing': "Nivel de personal: Medium", 'traffic': "Se Espera Tráfico Alto", 'loadDesc': "Carga promedio en vivo basada en horas pico históricas" },
    'proTips': { 'family': "Busque el 'Family Fast Track' cerca de la Zona de Seguridad B. Tiene espacio extra para cochecitos.", 'business': "¿Necesita trabajar? La Sala VIP de Negocios cerca de la Puerta B12 ofrece Wi-Fi de alta velocidad.", 'mobility': "Los ascensores accesibles se encuentran cerca de cada conjunto de escaleras mecánicas.", 'standard': "Mantenga siempre su tarjeta de embarque e identificación a mano para los controles de seguridad." },
    'chat': { 'placeholder': "Haz una pregunta...", 'send': "Enviar", 'assistantGreeting': "¡Hola! Soy Aeronix. Puedo ayudarte a entender la seguridad del aeropuerto, las reglas de equipaje y los procedimientos de embarque. ¿Cómo puedo ayudarte hoy?" },
  },
  'fr': {
    'nav': { 'map': "Carte des Opérations", 'terminals': "Terminaux", 'safety': "Sécurité", 'helpdesk': "Assistance" },
    'hero': { 'tag': "Contexte des Opérations au Sol", 'title': "Navigation Aéroportuaire Personnalisée.", 'desc': "Aeronix offre un soutien sur mesure pour votre voyage. Choisissez votre langue et votre type de voyageur.", 'cta1': "Lancer la Carte", 'cta2': "Statut: OPÉRATIONNEL" },
    'sections': { 'mapTitle': "Carte du Terminal", 'mapDesc': "Explorez les installations et l'état des zones.", 'faqTitle': "Aide Rapide", 'analyticsTitle': "Analyse de Congestion", 'analyticsDesc': "Métriques de charge en direct.", 'checklistTitle': "Check-list Opérationnelle", 'checklistDesc': "Suivez ces procédures obligatoires pour un départ serein.", 'assistantTitle': "Assistant Opérationnel", 'assistantDesc': "En discussion pour votre voyage." },
    'stats': { 'waitTime': "Attente Actuelle", 'securityStatus': "Statut Sécurité", 'normal': "Opérations normales", 'staffing': "Effectif: Moyen", 'traffic': "Trafic Intense Prévu", 'loadDesc': "Charge moyenne historique" },
    'proTips': { 'family': "Cherchez le 'Family Fast Track' près de la Zone B. Plus d'espace pour les poussettes.", 'business': "Le salon Business près de la porte B12 offre un Wi-Fi haut débit.", 'mobility': "Des ascenseurs accessibles sont situés près de chaque escalator.", 'standard': "Gardez votre carte d'embarquement accessible pour la sécurité." },
    'chat': { 'placeholder': "Posez une question...", 'send': "Envoyer", 'assistantGreeting': "Bonjour ! Je suis Aeronix. Je peux vous aider à comprendre la sécurité aéroportuaire, les règles relatives aux bagages et les procédures d'embarquement. Comment puis-je vous aider aujourd'hui ?" },
  },
  'de': {
    'nav': { 'map': "Betriebskarte", 'terminals': "Terminals", 'safety': "Sicherheit", 'helpdesk': "Hilfe" },
    'hero': { 'tag': "Bodenabfertigungskontext", 'title': "Flughafennavigation, Personalisiert.", 'desc': "Aeronix bietet maßgeschneiderte Unterstützung für Ihre Reise.", 'cta1': "Karte Starten", 'cta2': "Status: BETRIEBSBEREIT" },
    'sections': { 'mapTitle': "Terminal-Karte", 'mapDesc': "Einrichtungen und Zonenstatus erkunden.", 'faqTitle': "Schnellhilfe", 'analyticsTitle': "Stau-Analyse", 'analyticsDesc': "Live-Auslastungsmetriken.", 'checklistTitle': "Checkliste", 'checklistDesc': "Befolgen Sie diese Verfahren für einen reibungslosen Abflug.", 'assistantTitle': "KI-Assistent", 'assistantDesc': "Chat für Ihre Reise." },
    'stats': { 'waitTime': "Aktuelle Wartezeit", 'securityStatus': "Sicherheitsstatus", 'normal': "Normaler Betrieb", 'staffing': "Personalstand: Mittel", 'traffic': "Hohes Verkehrsaufkommen Erwartet", 'loadDesc': "Durchschnittliche Auslastung" },
    'proTips': { 'family': "Nutzen Sie den 'Family Fast Track' bei Zone B. Mehr Platz für Kinderwagen.", 'business': "Business Lounge bei Gate B12 mit Highspeed-WLAN.", 'mobility': "Barrierefreie Aufzüge bei jeder Rolltreppe.", 'standard': "Bordkarte und Ausweis griffbereit halten." },
    'chat': { 'placeholder': "Frage stellen...", 'send': "Senden", 'assistantGreeting': "Hallo! Ich bin Aeronix. Ich kann Ihnen helfen, die Flughafensicherheit, die Gepäckregeln und die Boarding-Verfahren zu verstehen. Wie kann ich Ihnen heute behilflich sein?" },
  },
  'zh': {
    'nav': { 'map': "运行地图", 'terminals': "航站楼", 'safety': "安全", 'helpdesk': "帮助台" },
    'hero': { 'tag': "地面运营背景", 'title': "个性化机场导航", 'desc': "Aeronix 为您的旅程提供定制化支持。选择语言和旅客类型以获取最准确的指导。", 'cta1': "启动地图", 'cta2': "状态：正常运行" },
    'sections': { 'mapTitle': "航站楼地图与知识", 'mapDesc': "探索设施和实时区域状态。", 'faqTitle': "快速帮助中心", 'analyticsTitle': "拥堵分析", 'analyticsDesc': "基于高峰时段的实时负荷指标。", 'checklistTitle': "运营清单", 'checklistDesc': "请遵循以下必要程序，确保顺利出发。", 'assistantTitle': "运营助手", 'assistantDesc': "为您提供旅程咨询。" },
    'stats': { 'waitTime': "当前等待时间", 'securityStatus': "安检状态", 'normal': "运行正常", 'staffing': "人员配置：中等", 'traffic': "预计流量较大", 'loadDesc': "基于历史高峰的平均负荷" },
    'proTips': { 'family': "安检B区附近有“家庭快速通道”，空间更宽敞。", 'business': "B12登机口附近的商务休息室提供高速Wi-Fi。", 'mobility': "中庭扶梯附近均设有无障碍电梯。", 'standard': "将登机牌和身份证件放在侧袋，方便安检时快速取用。" },
    'chat': { 'placeholder': "提问...", 'send': "发送", 'assistantGreeting': "你好！我是 Aeronix。我可以帮你了解机场安检、行李规定和登机程序今天我能为你做些什么？" },
  },
  'ja': {
    'nav': { 'map': "運航マップ", 'terminals': "ターミナル", 'safety': "安全", 'helpdesk': "ヘルプデスク" },
    'hero': { 'tag': "地上業務コンテキスト", 'title': "パーソナライズされた空港ナビ", 'desc': "Aeronixは、あなたの旅をサポートします。言語と旅行者タイプを選択してください。", 'cta1': "マップを起動", 'cta2': "ステータス：稼働中" },
    'sections': { 'mapTitle': "ターミナルマップ", 'mapDesc': "施設とゾーンの状況を確認。", 'faqTitle': "ヘルプセンター", 'analyticsTitle': "混雑状況分析", 'analyticsDesc': "リアルタイムの混雑指標。", 'checklistTitle': "チェックリスト", 'checklistDesc': "スムーズな出発のために、以下の手順に従ってください。", 'assistantTitle': "AIアシスタント", 'assistantDesc': "旅のサポートをします。" },
    'stats': { 'waitTime': "現在の待ち時間", 'securityStatus': "保安検査状況", 'normal': "通常通り", 'staffing': "スタッフ数：普通", 'traffic': "混雑が予想されます", 'loadDesc': "過去のデータに基づく平均負荷" },
    'proTips': { 'family': "保安検査B付近の「ファミリーファストトラック」はベビーカーに便利です。", 'business': "ゲートB12付近のビジネスラウンジには高速Wi-Fiがあります。", 'mobility': "エスカレーター付近にバリアフリーのエレベーターがあります。", 'standard': "搭乗券と身分証はすぐに取り出せるようにしておきましょう。" },
    'chat': { 'placeholder': "質問する...", 'send': "送信", 'assistantGreeting': "こんにちは！Aeronixです。空港のセキュリティ、手荷物のルール、搭乗手続きについてお手伝いできます。今日はどのようなご用件でしょうか？" },
  }
}

# Ensure fallback for missing languages in UI_TRANSLATIONS
for lang in LANGUAGES:
    if lang.code not in UI_TRANSLATIONS:
        UI_TRANSLATIONS[lang.code] = UI_TRANSLATIONS['en']

# Base Icons and Colors from Constants
GUIDE_METADATA = {
    'Check-in': {'icon': "🎟️", 'color': "bg-blue-500"},
    'Security': {'icon': "🛡️", 'color': "bg-amber-500"},
    'Terminal/Lounge': {'icon': "🏬", 'color': "bg-indigo-500"},
    'Boarding': {'icon': "✈️", 'color': "bg-emerald-500"},
    'Baggage Claim': {'icon': "🧳", 'color': "bg-rose-500"},
}

GUIDES_DATA = {
  'en': [
    { 'id': 'Check-in', 'title': "Step 1: Check-in", 'desc': "Register your presence and drop off luggage.", 'steps': ["Locate your airline's check-in kiosk.", "Prepare your Passport and booking reference.", "Print and attach luggage tags.", "Collect your boarding pass."] },
    { 'id': 'Security', 'title': "Step 2: Security", 'desc': "Mandatory passenger screening.", 'steps': ["Remove liquids (max 100ml).", "Remove large electronics.", "Place jacket and metal items in bins.", "Pass through scanner."] },
    { 'id': 'Terminal/Lounge', 'title': "Step 3: Terminal", 'desc': "Navigate to your gate.", 'steps': ["Check screens for gate number.", "Listen for announcements.", "Stay close to boarding zone.", "Arrive 45 mins before departure."] },
    { 'id': 'Boarding', 'title': "Step 4: Boarding", 'desc': "Entering the aircraft.", 'steps': ["Wait for your group being called.", "Have pass and ID ready.", "Find your seat.", "Stow carry-on luggage."] },
    { 'id': 'Baggage Claim', 'title': "Step 5: Baggage", 'desc': "Retrieve checked luggage.", 'steps': ["Follow signs to Baggage Claim.", "Find your flight's carousel.", "Check tag name.", "Report missing bags."] }
  ],
  'hi': [
    { 'id': 'Check-in', 'title': "चरण 1: चेक-इन", 'desc': "अपनी उपस्थिति दर्ज करें और सामान छोड़ें।", 'steps': ["आगमन पर अपनी एयरलाइन के चेक-इन कियोस्क या काउंटर का पता लगाएं।", "अपना पासपोर्ट, राष्ट्रीय आईडी और उड़ान बुकिंग संदर्भ तैयार रखें।", "अपने चेक किए गए बैग पर लगेज टैग प्रिंट करें और सुरक्षित रूप से लगाएं।", "अपना बोर्डिंग पास (प्रिंटेड या डिजिटल) प्राप्त करें और प्रस्थान की ओर बढ़ें।"] },
    { 'id': 'Security', 'title': "चरण 2: सुरक्षा", 'desc': "यात्री और हैंड-लगेज की अनिवार्य जांच।", 'steps': ["सभी तरल पदार्थ (अधिकतम 100ml) निकालें और उन्हें एक पारदर्शी बैग में रखें।", "अपने बैग से लैपटॉप या टैबलेट जैसे बड़े इलेक्ट्रॉनिक उपकरण बाहर निकालें।", "अपनी जैकेट, बेल्ट और धातु की वस्तुओं को दिए गए डिब्बों में रखें।", "निर्देशानुसार स्कैनर से गुजरें और अपना सारा सामान वापस लें।"] },
    { 'id': 'Terminal/Lounge', 'title': "चरण 3: टर्मिनल", 'desc': "अपने गेट तक पहुंचें और उड़ान से पहले आराम करें।", 'steps': ["अपने गेट नंबर और बोर्डिंग समय के लिए डिजिटल स्क्रीन पर नज़र रखें।", "गेट परिवर्तन या देरी के संबंध में टर्मिनल घोषणाओं को सुनें।", "दुकानों या लाउंज का आनंद लें, लेकिन अपने बोर्डिंग क्षेत्र के पास रहें।", "प्रस्थान से कम से कम 45 मिनट पहले अपने निर्धारित गेट पर पहुंचें।"] },
    { 'id': 'Boarding', 'title': "चरण 4: बोर्डिंग", 'desc': "प्राथमिकता समूहों में विमान में प्रवेश।", 'steps': ["अपने विशिष्ट बोर्डिंग समूह या ज़ोन के बुलाए जाने की प्रतीक्षा करें।", "गेट एजेंट के लिए अपना बोर्डिंग पास और फोटो आईडी तैयार रखें।", "जेट ब्रिज पथ का पालन करें और अपनी निर्धारित सीट संख्या खोजें।", "अपना हैंड-लगेज ओवरहेड बिन में या सीट के नीचे रखें।"] },
    { 'id': 'Baggage Claim', 'title': "चरण 5: सामान दावा", 'desc': "आगमन के बाद चेक किए गए सामान को प्राप्त करना।", 'steps': ["आगमन हॉल में 'सामान दावा' (Baggage Claim) संकेतों का पालन करें।", "अपनी विशिष्ट उड़ान संख्या के लिए निर्धारित बेल्ट नंबर खोजें।", "टैग पर नाम की जांच करके पुष्टि करें कि सामान आपका है।", "किसी भी क्षतिग्रस्त या खोए हुए बैग की सूचना एयरलाइन डेस्क पर दें।"] }
  ],
  'ta': [
    { 'id': 'Check-in', 'title': "படி 1: செக்-இன்", 'desc': "பதிவு செய்து சாமான்களை ஒப்படைக்கவும்.", 'steps': ["விமான நிலையம் வந்ததும் உங்கள் ஏர்லைனின் செக்-இன் கியோஸ்க்கைக் கண்டறியவும்.", "கடவுச்சீட்டு (Passport), அடையாள அட்டை மற்றும் முன்பதிவு விவரங்களைத் தயார் செய்யவும்.", "பயணப்பைகளில் லக்கேஜ் டேகுகளை அச்சிட்டு பாதுகாப்பாக இணைக்கவும்.", "போர்டிங் பாஸைப் பெற்றுக்கொண்டு பாதுகாப்புச் சோதனைக்குச் செல்லவும்."] },
    { 'id': 'Security', 'title': "படி 2: பாதுகாப்பு", 'desc': "பயணிகள் மற்றும் கைப்பைகள் சோதனை.", 'steps': ["திரவங்களை (அதிகபட்சம் 100ml) எடுத்து ஒரு வெளிப்படையான பையில் வைக்கவும்.", "லேப்டாப் அல்லது டேப்லெட் போன்ற மின்னணு சாதனங்களை பையிலிருந்து வெளியே எடுக்கவும்.", "கோட், பெல்ட் மற்றும் உலோகப் பொருட்களை வழங்கப்பட்ட தட்டுகளில் வைக்கவும்.", "ஸ்கேனர் வழியாகச் சென்று, உங்கள் பொருட்கள் அனைத்தையும் திரும்பப் பெறவும்."] },
    { 'id': 'Terminal/Lounge', 'title': "படி 3: முனையம்", 'desc': "கேட்டைக் கண்டுபிடித்து ஓய்வெடுக்கவும்.", 'steps': ["கேட் எண் மற்றும் நேரத்தை டிஜிட்டல் திரைகளில் தொடர்ந்து கண்காணிக்கவும்.", "கேட் மாற்றம் அல்லது தாமதம் குறித்த அறிவிப்புகளைக் கவனமாகக் கேட்கவும்.", "கடைகளுக்குச் சென்றாலும், உங்கள் போர்டிங் பகுதிக்கு அருகிலேயே இருக்கவும்.", "விமானம் புறப்படுவதற்கு 45 நிமிடங்களுக்கு முன்பே கேட்டைச் சென்றடையவும்."] },
    { 'id': 'Boarding', 'title': "படி 4: ஏறுதல்", 'desc': "விமானத்திற்குள் முறையான வரிசையில் செல்லுதல்.", 'steps': ["உங்கள் போர்டிங் குரூப் அல்லது மண்டலம் அழைக்கப்படும் வரை காத்திருக்கவும்.", "போர்டிங் பாஸ் மற்றும் அடையாள அட்டையை அதிகாரியிடம் காட்டத் தயார் செய்யவும்.", "பாலத்தின் வழியாகச் சென்று உங்கள் இருக்கை எண்ணைக் கண்டறியவும்.", "கைப்பைகளை தலைக்கு மேலேயுள்ள பெட்டியில் அல்லது இருக்கைக்கு அடியில் வைக்கவும்."] },
    { 'id': 'Baggage Claim', 'title': "படி 5: சாமான்கள் மீட்பு", 'desc': "சாமான்களைத் திரும்பப் பெறுங்கள்.", 'steps': ["விமான நிலையம் வந்ததும் 'Baggage Claim' அடையாளங்களைப் பின்தொடரவும்.", "உங்கள் விமான எண்ணுக்கான சுழல் மேடையைக் (Carousel) கண்டறியவும்.", "டேகில் உள்ள பெயரைச் சரிபார்த்து உங்கள் பையை உறுதி செய்யவும்.", "ஏதேனும் சேதம் அல்லது பை காணாமல் போனால் ஏர்லைன் டெஸ்க்கில் புகாரளிக்கவும்."] }
  ],
  'te': [
    { 'id': 'Check-in', 'title': "దశ 1: చెక్-ఇన్", 'desc': "నమోదు చేసుకోండి మరియు సామాను ఇవ్వండి.", 'steps': ["విమానాశ్రయానికి చేరుకున్నాక మీ ఎయిర్‌లైన్ చెక్-ఇన్ కియోస్క్ లేదా కౌంటర్‌ను గుర్తించండి.", "మీ పాస్‌పోర్ట్, ఐడి కార్డ్ మరియు బుకింగ్ వివరాలను సిద్ధంగా ఉంచుకోండి.", "మీ బ్యాగులకు లగేజీ ట్యాగ్‌లను ప్రింట్ చేసి సురక్షితంగా అతికించండి.", "మీ బోర్డింగ్ పాస్ తీసుకుని డిపార్చర్ జోన్‌కు వెళ్ళండి."] },
    { 'id': 'Security', 'title': "దశ 2: భద్రత", 'desc': "ప్రయాణీకుల మరియు చేతి సామాను తనిఖీ.", 'steps': ["ద్రవ పదార్థాలను (గరిష్టంగా 100ml) తీసి పారదర్శక సంచిలో ఉంచండి.", "ల్యాప్‌టాప్ లేదా టాబ్లెట్ వంటి ఎలక్ట్రానిక్ పరికరాలను బ్యాగ్ నుండి బయటకు తీయండి.", "మీ జాకెట్, బెల్ట్ మరియు లోహ వస్తువులను ట్రేలలో ఉంచండి.", "స్కానర్ ద్వారా వెళ్లి, మీ వస్తువులన్నీ తిరిగి సేకరించుకోండి."] },
    { 'id': 'Terminal/Lounge', 'title': "దశ 3: టెర్మినల్", 'desc': "గేట్ కనుగొని విశ్రాంతి తీసుకోండి.", 'steps': ["గేట్ నంబర్ మరియు సమయం కోసం డిజిటల్ స్క్రీన్లను గమనించండి.", "గేట్ మార్పులు లేదా ఆలస్యం గురించి అనౌన్స్‌మెంట్లను వినండి.", "షాపులు లేదా లాంజ్‌లకు వెళ్ళినా, మీ బోర్డింగ్ ఏరియాకు సమీపంలో ఉండండి.", "ప్రయాణానికి కనీసం 45 నిమిషాల ముందే గేట్ వద్దకు చేరుకోండి."] },
    { 'id': 'Boarding', 'title': "దశ 4: బోర్డింగ్", 'desc': "విమానంలోకి వెళ్ళండి.", 'steps': ["మీ బోర్డింగ్ గ్రూప్ లేదా జోన్ పిలిచే వరకు వేచి ఉండండి.", "గేట్ ఏజెంట్ కోసం బోర్డింగ్ పాస్ మరియు ఫోటో ఐడి సిద్ధంగా ఉంచుకోండి.", "జెట్ బ్రిడ్జ్ మార్గం ద్వారా వెళ్లి మీ సీటు నంబర్‌ను కనుగొనండి.", "మీ చేతి సామాను సీటు పైన ఉన్న బిన్లలో లేదా సీటు కింద ఉంచండి."] },
    { 'id': 'Baggage Claim', 'title': "దశ 5: సామాను సేకరణ", 'desc': "సామాను తిరిగి పొందండి.", 'steps': ["అరైవల్ హాల్‌లో 'Baggage Claim' గుర్తులను అనుసరించండి.", "మీ ఫ్లైట్ నంబర్ కేటాయించిన బెల్ట్ నంబర్‌ను కనుగొనండి.", "ట్యాగ్‌పై పేరు చూసి అది మీ బ్యాగ్ అని నిర్ధారించుకోండి.", "బ్యాగ్ దెబ్బతిన్నా లేదా కనిపించకపోయినా ఎయిర్‌లైన్ డెస్క్‌లో ఫిర్యాదు చేయండి."] }
  ],
  'bn': [
    { 'id': 'Check-in', 'title': "ধাপ ১: চেক-ইন", 'desc': "নিবন্ধন করুন এবং ব্যাগ জমা দিন।", 'steps': ["বিমানবন্দরে পৌঁছে আপনার এয়ারলাইন্সের চেক-ইন কিয়স্ক বা কাউন্টার খুঁজুন।", "আপনার পাসপোর্ট, আইডি এবং বুকিং রেফারেন্স সাথে রাখুন।", "আপনার ব্যাগে লাগেজ ট্যাগগুলি প্রিন্ট করে সুরক্ষিতভাবে লাগিয়ে দিন।", "বোর্ডিং পাস সংগ্রহ করুন এবং সিকিউরিটির দিকে এগিয়ে যান।"] },
    { 'id': 'Security', 'title': "ধাপ ২: নিরাপত্তা", 'desc': "যাত্রী এবং হ্যান্ড লাগেজের স্ক্রিনিং।", 'steps': ["সব তরল (সর্বোচ্চ ১০০ মিলি) বের করে স্বচ্ছ প্লাস্টিকের ব্যাগে রাখুন।", "ল্যাপটপ বা ট্যাবলেটের মতো বড় ইলেকট্রনিক ডিভাইস ব্যাগ থেকে বের করুন।", "আপনার জ্যাকেট, বেল্ট এবং ধাতব বস্তুগুলি বিনে রাখুন।", "স্ক্যানার পার হয়ে আপনার সব জিনিসপত্র সংগ্রহ করুন।"] },
    { 'id': 'Terminal/Lounge', 'title': "ধাপ ৩: টার্মিনাল", 'desc': "গেট খুঁজুন এবং বিশ্রাম নিন।", 'steps': ["গেট নম্বর এবং সময়ের জন্য ডিজিটাল স্ক্রিনগুলি খেয়াল রাখুন।", "গেট পরিবর্তন বা দেরি সংক্রান্ত ঘোষণাগুলি মনোযোগ দিয়ে শুনুন।", "দোকান বা লাউঞ্জে গেলেও আপনার বোর্ডিং জোনের কাছেই থাকুন।", "প্রস্থানের অন্তত ৪৫ মিনিট আগে আপনার গেটে পৌঁছান।"] },
    { 'id': 'Boarding', 'title': "ধাপ ৪: বোর্ডিং", 'desc': "গ্রুপ অনুযায়ী বিমানে প্রবেশ।", 'steps': ["আপনার নির্দিষ্ট বোর্ডিং গ্রুপ বা জোন ডাকা না হওয়া পর্যন্ত অপেক্ষা করুন।", "বোর্ডিং পাস এবং আইডি কার্ড গেট এজেন্টের কাছে দেখানোর জন্য তৈরি রাখুন।", "জেট ব্রিজের পথ অনুসরণ করে আপনার নির্দিষ্ট সিট নম্বর খুঁজুন।", "আপনার হ্যান্ড লাগেজ ওভারহেড বিনে বা সিটের নিচে রাখুন।"] },
    { 'id': 'Baggage Claim', 'title': "ধাপ ৫: লাগেজ প্রাপ্তি", 'desc': "ব্যাগ বুঝে নিন।", 'steps': ["টার্মিনাল থেকে বের হওয়ার সময় 'Baggage Claim' চিহ্ন অনুসরণ করুন।", "আপনার ফ্লাইটের জন্য নির্ধারিত বেল্ট নম্বরটি খুঁজে বের করুন।", "ট্যাগে আপনার নাম মিলিয়ে নিয়ে নিশ্চিত হোন যে ব্যাগটি আপনার।", "ব্যাগ ক্ষতিগ্রস্ত হলে বা খুঁজে না পাওয়া গেলে এয়ারলাইন ডেস্কে জানান।"] }
  ],
  'mr': [
    { 'id': 'Check-in', 'title': "पायरी १: चेक-इन", 'desc': "नोंदणी करा आणि बॅगा द्या।", 'steps': ["विमानतळावर पोहोचल्यावर तुमच्या एअरलाईनच्या चेक-इन किओस्क किंवा काउंटरचा शोध घ्या।", "तुमचा पासपोर्ट, आयडी आणि बुकिंग संदर्भ तयार ठेवा।", "तुमच्या बॅगेला लगेज टॅग प्रिंट करून सुरक्षितपणे लावा।", "तुमचा बोर्डिंग पास मिळवा आणि पुढील प्रक्रियेसाठी जा।"] },
    { 'id': 'Security', 'title': "पायरी २: सुरक्षा", 'desc': "प्रवासी आणि हातातील सामानाची तपासणी।", 'steps': ["सर्व द्रव्ये (जास्तीत जास्त १०० मिली) बाहेर काढून पारदर्शक बॅगेत ठेवा।", "लॅपटॉप किंवा टॅब्लेट सारखी इलेक्ट्रॉनिक उपकरणे बॅगेतून बाहेर काढा।", "तुमचे जॅकेट, बेल्ट आणि धातूच्या वस्तू ट्रे मध्ये ठेवा।", "स्कॅनरमधून जा आणि तुमच्या सर्व वस्तू परत गोळा करा।"] },
    { 'id': 'Terminal/Lounge', 'title': "पायरी ३: टर्मिनल", 'desc': "गेट शोधा आणि आराम करा।", 'steps': ["तुमच्या गेट नंबरसाठी डिजिटल स्क्रीनवर लक्ष ठेवा।", "गेट बदल किंवा उशिराबाबत होणाऱ्या घोषणा लक्षपूर्वक ऐका।", "दुकानांना भेट दिली तरी तुमच्या बोर्डिंग एरियाच्या जवळ राहा।", "विमानाच्या वेळेच्या किमान ४५ मिनिटे आधी गेटवर पोहोचा।"] },
    { 'id': 'Boarding', 'title': "पायरी ४: बोर्डिंग", 'desc': "विमानात प्रवेश।", 'steps': ["तुमच्या बोर्डिंग ग्रुपची हाक येईपर्यंत वाट पहा।", "बोर्डिंग पास आणि फोटो आयडी एजंटला दाखवण्यासाठी तयार ठेवा।", "ब्रिजने जाऊन तुमचा सीट नंबर शोधा।", "तुमचे सामान वरच्या कप्प्यात किंवा सीटच्या खाली ठेवा।"] },
    { 'id': 'Baggage Claim', 'title': "पायरी ५: बॅगेज क्लेम", 'desc': "बॅगा परत घ्या।", 'steps': ["बाहेर येताना 'Baggage Claim' चिन्हांचे पालन करा।", "तुमच्या फ्लाईट नंबरसाठी नियुक्त केलेला बेल्ट नंबर शोधा।", "टॅगवरील नाव तपासून बॅग तुमचीच असल्याची खात्री करा।", "बॅग खराब झाल्यास किंवा न मिळाल्यास एअरलाईन डेस्कवर कळवा।"] }
  ],
  'es': [
    { 'id': 'Check-in', 'title': "Paso 1: Check-in", 'desc': "Regístrese y deje su equipaje.", 'steps': ["Ubique el kiosco o mostrador de su aerolínea al llegar.", "Prepare su pasaporte, identificación y referencia de reserva.", "Imprima y coloque las etiquetas de equipaje de forma segura.", "Recoja su tarjeta de embarque y diríjase a salidas."] },
    { 'id': 'Security', 'title': "Paso 2: Seguridad", 'desc': "Inspección de pasajeros y equipaje de mano.", 'steps': ["Saque todos los líquidos (máx. 100 ml) y póngalos en una bolsa transparente.", "Extraiga dispositivos electrónicos grandes de su equipaje.", "Coloque su chaqueta, cinturón y objetos metálicos en las bandejas.", "Pase por el escáner según las instrucciones y recoja sus pertenencias."] },
    { 'id': 'Terminal/Lounge', 'title': "Paso 3: Terminal", 'desc': "Busque su puerta y relájese.", 'steps': ["Vigile las pantallas digitales para confirmar su puerta y hora.", "Escuche los anuncios por si hay cambios de última hora.", "Explore la terminal, pero permanezca cerca de su zona de embarque.", "Llegue a su puerta asignada al menos 45 minutos antes del vuelo."] },
    { 'id': 'Boarding', 'title': "Paso 4: Embarque", 'desc': "Suba al avión en grupos de prioridad.", 'steps': ["Espere a que llamen a su grupo o zona específica.", "Tenga listos su pase de abordar y una identificación con foto.", "Siga el puente de acceso y localice su número de asiento.", "Guarde su equipaje de mano en el compartimento superior."] },
    { 'id': 'Baggage Claim', 'title': "Paso 5: Equipaje", 'desc': "Recoja sus maletas facturadas.", 'steps': ["Siga las señales de 'Recogida de equipaje' hacia la sala de llegadas.", "Busque el número de cinta asignado a su vuelo.", "Verifique que el equipaje sea suyo revisando el nombre en la etiqueta.", "Informe de cualquier daño o extravío en el mostrador de la aerolínea."] }
  ],
  'fr': [
    { 'id': 'Check-in', 'title': "Étape 1: Enregistrement", 'desc': "Enregistrez-vous et déposez vos bagages.", 'steps': ["Localisez la borne ou le comptoir de votre compagnie à l'arrivée.", "Préparez votre passeport, ID et référence de réservation.", "Imprimez et fixez les étiquettes sur vos bagages enregistrés.", "Récupérez votre carte d'embarquement et allez vers les départs."] },
    { 'id': 'Security', 'title': "Étape 2: Sécurité", 'desc': "Contrôle obligatoire des passagers.", 'steps': ["Sortez les liquides (max 100ml) et placez-les dans un sac transparent.", "Sortez les ordinateurs et tablettes de votre sac.", "Placez votre veste, ceinture et objets métalliques dans les bacs.", "Passez le scanner et récupérez tous vos effets personnels."] },
    { 'id': 'Terminal/Lounge', 'title': "Étape 3: Terminal", 'desc': "Attente et détente avant le vol.", 'steps': ["Surveillez les écrans pour votre porte et l'heure d'embarquement.", "Écoutez les annonces concernant les changements de porte.", "Explorez les boutiques, mais restez proche de votre zone.", "Arrivez à votre porte au moins 45 minutes avant le départ."] },
    { 'id': 'Boarding', 'title': "Étape 4: Embarquement", 'desc': "Accès à l'avion par groupes prioritaires.", 'steps': ["Attendez l'appel de votre groupe ou zone d'embarquement.", "Préparez votre carte d'embarquement et une pièce d'identité.", "Suivez la passerelle et trouvez votre numéro de siège.", "Rangez votre bagage à main dans le coffre ou sous le siège."] },
    { 'id': 'Baggage Claim', 'title': "Étape 5: Bagages", 'desc': "Récupération après l'arrivée.", 'steps': ["Suivez les panneaux 'Livraison bagages' vers la salle d'arrivée.", "Trouvez le numéro de carrousel assigné à votre vol.", "Vérifiez que le bagage est le vôtre via l'étiquette nominative.", "Signalez tout bagage endommagé ou manquant au comptoir."] }
  ],
  'de': [
    { 'id': 'Check-in', 'title': "Schritt 1: Check-in", 'desc': "Anmelden und Koffer abgeben.", 'steps': ["Suchen Sie den Check-in-Automaten oder Schalter Ihrer Airline.", "Halten Sie Reisepass, Ausweis und Buchungscode bereit.", "Drucken Sie Kofferanhänger aus und bringen Sie diese sicher an.", "Holen Sie Ihre Bordkarte ab und gehen Sie zum Abflugbereich."] },
    { 'id': 'Security', 'title': "Schritt 2: Sicherheit", 'desc': "Passagier- und Handgepäckkontrolle.", 'steps': ["Nehmen Sie Flüssigkeiten (max. 100ml) in einem Klarsichtbeutel heraus.", "Nehmen Sie Laptops und Tablets aus Ihrer Tasche.", "Legen Sie Jacke, Gürtel und Metallgegenstände in die Wannen.", "Gehen Sie durch den Scanner und holen Sie Ihre Sachen wieder ab."] },
    { 'id': 'Terminal/Lounge', 'title': "Schritt 3: Terminal", 'desc': "Warten und entspannen vor dem Flug.", 'steps': ["Achten Sie auf die Bildschirme für Gate-Nummer und Zeit.", "Hören Sie auf Durchsagen bezüglich Gate-Änderungen.", "Nutzen Sie Shops, aber bleiben Sie in der Nähe Ihres Gates.", "Seien Sie mindestens 45 Minuten vor Abflug an Ihrem Gate."] },
    { 'id': 'Boarding', 'title': "Schritt 4: Boarding", 'desc': "Einsteigen nach Prioritätsgruppen.", 'steps': ["Warten Sie, bis Ihre Gruppe oder Zone aufgerufen wird.", "Halten Sie Bordkarte und Lichtbildausweis bereit.", "Folgen Sie der Fluggastbrücke und suchen Sie Ihren Sitzplatz.", "Verstauen Sie Ihr Handgepäck im Fach oder unter dem Sitz."] },
    { 'id': 'Baggage Claim', 'title': "Schritt 5: Gepäck", 'desc': "Abholung nach der Landung.", 'steps': ["Folgen Sie den Schildern 'Gepäckausgabe' zur Ankunftshalle.", "Suchen Sie die Bandnummer, die Ihrem Flug zugeordnet ist.", "Prüfen Sie am Anhänger, ob es wirklich Ihr Koffer ist.", "Melden Sie beschädigtes oder fehlendes Gepäck am Schalter."] }
  ],
  'zh': [
    { 'id': 'Check-in', 'title': "步骤 1: 值机", 'desc': "办理登机手续并托运行李。", 'steps': ["到达后寻找所属航空公司的自助值机柜台或人工柜台。", "准备好护照、身份证和预订编号。", "打印并牢固地贴好托运行李标签。", "领取登机牌（纸质或电子版）并前往出发区。"] },
    { 'id': 'Security', 'title': "步骤 2: 安检", 'desc': "强制性旅客及随身行李检查。", 'steps': ["取出所有液体（单件不超过100毫升）并放入透明袋。", "从包中取出笔记本电脑等大型电子设备。", "将外套、皮带和金属物品放入提供的托盘中。", "按指示通过扫描仪，并取回所有个人物品。"] },
    { 'id': 'Terminal/Lounge', 'title': "步骤 3: 候机区", 'desc': "寻找登机口并在飞行前休息。", 'steps': ["监控显示屏，查看登机口编号和登机时间。", "留意有关登机口变更或延误的广播通知。", "可以逛商店或休息室，但请确保留在登机区域附近。", "请至少在起飞前45分钟到达指定的登机口。"] },
    { 'id': 'Boarding', 'title': "步骤 4: 登机", 'desc': "按优先顺序登机。", 'steps': ["等待您的特定登机小组或区域被呼叫。", "向工作人员出示登机牌和带有照片的身份证件。", "通过廊桥并找到您分配的座位号。", "将随身行李存放在行李架内或座位下方。"] },
    { 'id': 'Baggage Claim', 'title': "步骤 5: 行李提取", 'desc': "到达后领取托运行李。", 'steps': ["跟随“行李提取”指示牌前往到达大厅。", "查找分配给您航班号的行李转盘编号。", "通过检查标签上的姓名，确认行李属于您。", "如行李损坏或丢失，请立即前往航空公司服务台报告。"] }
  ],
  'ja': [
    { 'id': 'Check-in', 'title': "ステップ 1: チェックイン", 'desc': "搭乗手続きと手荷物預け。", 'steps': ["到着後、利用する航空会社のキオスクまたはカウンターを探します。", "パスポート、身分証、予約番号を準備してください。", "手荷物タグを印刷し、預け入れ荷物にしっかりと取り付けます。", "搭乗券（印刷またはデジタル）を受け取り、出発口へ進みます。"] },
    { 'id': 'Security', 'title': "ステップ 2: 保安検査", 'desc': "旅客と手荷物のスクリーニング。", 'steps': ["全ての液体類（各100ml以下）を取り出し、透明な袋に入れます。", "ノートPCやタブレットなどの電子機器をバッグから出します。", "上着、ベルト、金属類を専用のトレイに置きます。", "指示に従ってスキャナーを通り、全ての持ち物を回収します。"] },
    { 'id': 'Terminal/Lounge', 'title': "ステップ 3: ターミナル", 'desc': "搭乗開始までリラックス。", 'steps': ["モニターで搭乗ゲート番号と搭乗開始時間を確認します。", "ゲート変更や遅延に関するアナウンスに注意してください。", "ショップを利用する際も、搭乗エリアから離れすぎないようにします。", "出発の45分前までには指定されたゲートに到着してください。"] },
    { 'id': 'Boarding', 'title': "ステップ 4: 搭乗", 'desc': "優先順位に従って機内へ。", 'steps': ["自分の搭乗グループまたはゾーンが呼ばれるまで待機します。", "搭乗券と写真付き身分証を係員に提示できるよう準備します。", "ボーディングブリッジを通って、指定の座席番号を探します。", "手荷物を頭上の棚または座席の下に収納します。"] },
    { 'id': 'Baggage Claim', 'title': "ステップ 5: 手荷物受取", 'desc': "預け入れ荷物の回収。", 'steps': ["「手荷物受取」の案内に従って到着ロビーへ進みます。", "利用した便名に割り当てられたターンテーブルの番号を探します。", "タグの名前を確認し、自分の荷物であることを確かめます。", "破損や紛失がある場合は、航空会社のカウンターへ申し出てください。"] }
  ]
}

# FAQs
FAQs_DATA = {
  'en': [
    { 'category': "Liquids", 'question': "How much liquid can I bring?", 'answer': "100ml or less per container." },
    { 'category': "Documents", 'question': "Do I need physical pass?", 'answer': "Digital is usually fine." }
  ],
  'hi': [
    { 'category': "तरल पदार्थ", 'question': "मैं कितना तरल पदार्थ ला सकता हूँ?", 'answer': "प्रति कंटेनर 100 मिलीलीटर या उससे कम।" },
    { 'category': "दस्तावेज़", 'question': "क्या मुझे भौतिक पास की आवश्यकता है?", 'answer': "डिजिटल आमतौर पर ठीक है।" }
  ],
  'ta': [
    { 'category': "திரவங்கள்", 'question': "நான் எவ்வளவு திரவம் கொண்டு வரலாம்?", 'answer': "ஒரு கொள்கலனுக்கு 100 மி.லி அல்லது அதற்கும் குறைவானது." },
    { 'category': "ஆவணங்கள்", 'question': "எனக்கு அசல் போர்டிங் பாஸ் தேவையா?", 'answer': "டிஜிட்டல் பாஸ் போதுமானது." }
  ],
  'te': [
    { 'category': "ద్రవాలు", 'question': "నేను ఎంత ద్రవాన్ని తీసుకురాగలను?", 'answer': "ఒక్కో కంటైనర్‌కు 100ml లేదా అంతకంటే తక్కువ." },
    { 'category': "పత్రాలు", 'question': "నాకు ఫిజికల్ పాస్ అవసరమా?", 'answer': "డిజిటల్ సాధారణంగా సరిపోతుంది." }
  ],
  'bn': [
    { 'category': "তরল", 'question': "আমি কতটা তরল আনতে পারি?", 'answer': "প্রতিটি পাত্রে ১০০ মিলি বা তার কম।" },
    { 'category': "নথি", 'question': "আমার কি কাগজের পাস দরকার?", 'answer': "ডিজিটাল সাধারণত ঠিক আছে।" }
  ],
  'mr': [
    { 'category': "द्रव्ये", 'question': "मी किती द्रव्ये आणू शकतो?", 'answer': "प्रत्येक बाटलीत १०० मिली किंवा त्यापेक्षा कमी।" },
    { 'category': "कागदपत्रे", 'question': "मला कागदी पास हवा का?", 'answer': "डिजिटल पास सहसा चालतो।" }
  ],
  'es': [
    { 'category': "Líquidos", 'question': "¿Cuánto líquido puedo llevar?", 'answer': "100ml or less per container." },
    { 'category': "Documentos", 'question': "¿Necesito pase físico?", 'answer': "El digital suele bastar." }
  ],
  'fr': [
    { 'category': "Liquides", 'question': "Quelle quantité de liquide ?", 'answer': "100ml maximum par flacon." },
    { 'category': "Documents", 'question': "Pass physique nécessaire ?", 'answer': "Le numérique suffit." }
  ],
  'de': [
    { 'category': "Flüssigkeiten", 'question': "Wieviel Flüssigkeit?", 'answer': "Maximal 100ml pro Behälter." },
    { 'category': "Dokumente", 'question': "Physischer Pass nötig?", 'answer': "Digital reicht meist aus." }
  ],
  'zh': [
    { 'category': "液体", 'question': "可以带多少液体？", 'answer': "每瓶不超过100毫升。" },
    { 'category': "证件", 'question': "需要纸质登机牌吗？", 'answer': "电子版通常即可。" }
  ],
  'ja': [
    { 'category': "液体", 'question': "液体はどのくらい？", 'answer': "各100ml以下です。" },
    { 'category': "書類", 'question': "搭乗券は必要？", 'answer': "通常はデジタルでOK。" }
  ]
}

def get_guides(lang_code):
    guides = GUIDES_DATA.get(lang_code, GUIDES_DATA['en'])
    # Inject metadata if missing (for non-english if we didn't hardcode it)
    # But I hardcoded English metadata into the English block so I need to merge it for others?
    # Actually, the user asked to fix languages not working.
    # In my construction above, I only have valid Python dictionaries.
    # But wait, I didn't actually add the 'icon' and 'color' to the non-en blocks in the big dictionary I wrote above!
    # I only updated the `en` block in previous steps, and now I just pasted the `translations.ts` content which lacks icon/color.
    
    # We need to systematically inject them.
    enriched_guides = []
    for guide in guides:
        # Create a copy to avoid mutating the global if we were doing this in memory, but here we are returning new list
        meta = GUIDE_METADATA.get(guide['id'], {'icon': '❓', 'color': 'bg-gray-500'})
        enriched_guide = guide.copy()
        enriched_guide.update(meta)
        enriched_guides.append(enriched_guide)
        
    return enriched_guides

def get_faqs(lang_code):
    return FAQs_DATA.get(lang_code, FAQs_DATA['en'])

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton, MDRoundFlatButton
from kivymd.uix.list import OneLineAvatarListItem




Window.size = (320, 556)


navigation_helper = """

ScreenManager:

    MainScreen:
    NorthAmericaScreen:
        id: NA
    SouthAmericaScreen:
        id: SA
    EuropeScreen:
        id: Eu
    AsiaScreen:
        id: As
    AfricaScreen:
        id: Af
    AustraliaandOceaniaScreen:
        id: AAO

    SearchCountryScreen:
        id: search

    CanadaScreen:
    USAScreen:
    MexicoScreen:
    GuatemalaScreen:
    BelizeScreen:
    SalvadorScreen:
    HondurasScreen:
    NicaraguaScreen:
    CostaRicaScreen:
    PanamaScreen:
    TheBahamasScreen:
    CubaScreen:
    JamaicaScreen:
    HaitiScreen:
    DominicanRepublicScreen:
    SaintKittsandNevisScreen:
    AntiguaandBarbudaScreen:
    DominicaScreen:
    SaintLuciaScreen:
    SaintVincentandtheGrenadinesScreen:
    BarbadosScreen:
    GrenadaScreen:
    TrinidadandTobagoScreen:

    ColombiaScreen:
    VenezuelaScreen:
    GuyanaScreen:
    SurinameScreen:
    EcuadorScreen:
    PeruScreen:
    BrazilScreen:
    BoliviaScreen:
    ChileScreen:
    ArgentinaScreen:
    ParaguayScreen:
    UruguayScreen:

    PortugalScreen:
    SpainScreen:
    AndorraScreen:
    FranceScreen:
    UKScreen:
    IrelandScreen:
    IcelandScreen:
    NetherlandsScreen:
    BelgiumScreen:
    LuxembourgScreen:
    GermanyScreen:
    DenmarkScreen:
    SwitzerlandScreen:
    LiechtensteinScreen:
    AustriaScreen:
    ItalyScreen:
    VaticanScreen:
    SanMarinoScreen:
    MonacoScreen:
    MaltaScreen:
    GreeceScreen:
    NorwayScreen:
    SwedenScreen:
    FinlandScreen:
    EstoniaScreen:
    LatviaScreen:
    LithuaniaScreen:
    PolandScreen:
    BelarusScreen:
    CzechRepublicScreen:
    SlovakiaScreen:
    UkraineScreen:
    KazakhstanScreen:
    RussiaScreen:
    GeorgiaScreen:
    AzerbaijanScreen:
    SloveniaScreen:
    HungaryScreen:
    RomaniaScreen:
    MoldovaScreen:
    CroatiaScreen:
    BosniaAndHerzegovinaScreen:
    SerbiaScreen:
    MontenegroScreen:
    KosovoScreen:
    AlbaniaScreen:
    NorthMacedoniaScreen:
    BulgariaScreen:
    TurkeyScreen:

    ArmeniaScreen:
    CyprusScreen:
    IranScreen:
    IraqScreen:
    SyriaScreen:
    LebanonScreen:
    IsraelScreen:
    PalestineScreen:
    JordanScreen:
    SaudiArabiaScreen:
    KuwaitScreen:
    QatarScreen:
    BahrainScreen:
    UnitedArabEmiratesScreen:
    OmanScreen:
    YemenScreen:
    UzbekistanScreen:
    KyrgyzstanScreen:
    TurkmenistanScreen:
    TajikistanScreen:
    AfghanistanScreen:
    PakistanScreen:
    IndiaScreen:
    SriLankaScreen:
    MaldivesScreen:
    NepalScreen:
    BhutanScreen:
    BangladeshScreen:
    ChinaScreen:
    MongoliaScreen:
    NorthKoreaScreen:
    SouthKoreaScreen:
    JapanScreen:
    TaiwanScreen:
    MyanmarScreen:
    ThailandScreen:
    LaosScreen:
    VietnamScreen:
    CambodiaScreen:
    MalaysiaScreen:
    SingaporeScreen:
    PhilippinesScreen:
    BruneiScreen:
    EastTimorScreen:

    MoroccoScreen:
    AlgeriaScreen:
    TunisiaScreen:
    LibyaScreen:
    EgyptScreen:
    MauritaniaScreen:
    MaliScreen:
    NigerScreen:
    ChadScreen:
    SudanScreen:
    EritreaScreen:
    DjiboutiScreen:
    SenegalScreen:
    TheGambiaScreen:
    GuineaBissauScreen:
    GuineaScreen:
    SierraLeoneScreen:
    LiberiaScreen:
    IvoryCoastScreen:
    BurkinaFasoScreen:
    GhanaScreen:
    TogoScreen:
    BeninScreen:
    NigeriaScreen:
    CameroonScreen:
    CentralAfricanRepublicScreen:
    SouthSudanScreen:
    EthiopiaScreen:
    SomaliaScreen:
    EquatorialGuineaScreen:
    GabonScreen:
    RepublicoftheCongoScreen:
    DemocraticRepublicoftheCongoScreen:
    RwandaScreen:
    BurundiScreen:
    UgandaScreen:
    KenyaScreen:
    AngolaScreen:
    ZambiaScreen:
    MalawiScreen:
    MozambiqueScreen:
    MadagascarScreen:
    NamibiaScreen:
    BotswanaScreen:
    ZimbabweScreen:
    RepublicofSouthAfricaScreen:
    EswatiniScreen:
    LesothoScreen:
    SeychellesScreen:
    MauritiusScreen:
    ComorosScreen:
    SaoTomeandPrincipeScreen:
    CapeVerdeScreen:

    AustraliaScreen:
    NewZealandScreen:
    IndonesiaScreen:
    PapuaNewGuineaScreen:
    SolomonIslandsScreen:
    VanuatuScreen:
    FijiScreen:
    TongaScreen:
    SamoaScreen:
    TuvaluScreen:
    KiribatiScreen:
    NauruScreen:
    MarshallIslandsScreen:
    MicronesiaScreen:
    PalauScreen:


#1
<NorthAmericaScreen>:
    name: "North America"
    BoxLayout:
        orientation: 'vertical'
        spacing: '8dp'
        MDToolbar:
            elevation: 25
            title: 'World countries'
            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
            MDIconButton:
                icon: "magnify"
                icon_color: (255/255, 255/255, 255/255, 1)
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release:
                    root.manager.current = "SearchCountryScreen"
                    app.past_page = "North America"
        MDLabel:
            text: '   North America'
            font_style: 'H6'
            size_hint_y: None
            height: self.texture_size[1]  
        ScrollView:
            MDList:
                OneLineAvatarListItem:
                    id: Canada
                    text: 'Canada   -   Ottawa'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ca.png'
                OneLineAvatarListItem:
                    id: USA
                    text: 'USA   -   Washington'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'united_states.png'
                OneLineAvatarListItem:
                    id: Mexico
                    text: 'Mexico   -   Mexico city'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'mex.png'
                OneLineAvatarListItem:
                    id: Guatemala
                    text: 'Guatemala   -   Guatemala city'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'gua.png'
                OneLineAvatarListItem:
                    id: Belize
                    text: 'Belize   -   Belmopan'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'beli.png'
                OneLineAvatarListItem:
                    id: El Salvador
                    text: 'El Salvador   -   San Salvador'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'el_sal.png'
                OneLineAvatarListItem:
                    id: Honduras
                    text: 'Honduras   -   Tegucigalpa'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'hon.png'
                OneLineAvatarListItem:
                    id: Nicaragua
                    text: 'Nicaragua   -   Managua'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'nic.png'
                OneLineAvatarListItem:
                    id: Costa Rica
                    text: 'Costa Rica   -   San Jose'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'cos.png'
                OneLineAvatarListItem:
                    id: Panama
                    text: 'Panama   -   Panama city'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'pan.png'
                OneLineAvatarListItem:
                    id: The Bahamas
                    text: 'The Bahamas   -   Nassau'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bah.png'
                OneLineAvatarListItem:
                    id: Cuba
                    text: 'Cuba   -   Havana'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'cub.png'
                OneLineAvatarListItem:
                    id: Jamaica
                    text: 'Jamaica   -   Kingston'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'jam.png'
                OneLineAvatarListItem:
                    id: Haiti
                    text: 'Haiti   -   Port au Prince'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'hai.png'
                TwoLineAvatarListItem:
                    id: Dominican Republic
                    text: 'Dominican Republic   -   '
                    secondary_text: "Santo Domingo"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'dom_r.png'
                TwoLineAvatarListItem:
                    id: Saint Kitts and Nevis
                    text: 'Saint Kitts and Nevis   -   '
                    secondary_text: "Basseterre"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'saint_kit.png'
                TwoLineAvatarListItem:
                    id: Antigua and Barbuda
                    text: 'Antigua and Barbuda    -   '
                    secondary_text: "Saint Johns"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ant.png'
                OneLineAvatarListItem:
                    id: Dominica
                    text: 'Dominica   -   Roseau'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'dom.png'
                OneLineAvatarListItem:
                    id: Saint Lucia
                    text: 'Saint Lucia   -   Castries'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'saint_luc.png'
                TwoLineAvatarListItem:
                    id: Saint Vincent and the Grenadines
                    text: 'Saint Vincent and the   '
                    secondary_text: "Grenadines   -   Kingstown"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'saint_vinc.png'
                OneLineAvatarListItem:
                    id: Barbados
                    text: 'Barbados   -   Bridgetown'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bar.png'
                OneLineAvatarListItem:
                    id: Grenada
                    text: 'Grenada   -   Saint Georges'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'gren.png'
                TwoLineAvatarListItem:
                    id: Trinidad and Tobago
                    text: 'Trinidad and Tobago   -   '
                    secondary_text: "Port of Spain"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'trini.png'
                Widget:

    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'continents.png'
            MDLabel:
                text: '              Continents'
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'North America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "North America"
                    OneLineListItem:
                        text: 'South America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "South America"
                    OneLineListItem:
                        text: 'Europe'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Europe"
                    OneLineListItem:
                        text: 'Asia'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Asia"
                    OneLineListItem:
                        text: 'Africa'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Africa"
                    OneLineListItem:
                        text: 'Australia and Oceania'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Australia and Oceania"

<CanadaScreen>
    name: "Canada"
    Image:
        source: 'canada.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  9,984,670 km2 (3,855,100 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  8,436,447"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  67.2% Christianity, 23.9% No religion, 3.2% Islam, 1.5% Hinduism, 5.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Toronto"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Canadian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Canadian dollar (CAD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page
                

        
        
<USAScreen>
    name: "USA"
    Image:
        source: 'usa.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  9,833,520 km2 (3,796,742 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  331,893,745"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  63% Christianity, 29% No religion, 8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  New York City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  American"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  U.S. dollar (USD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<MexicoScreen>
    name: "Mexico"
    Image:
        source: 'mexico.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,972,550 km2 (761,610 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  126,014,024"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  88.9% Christianity, 10.6% No religion, 0.5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Mexico City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Mexican"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Mexican peso (MXN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +52"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<GuatemalaScreen>
    name: "Guatemala"
    Image:
        source: 'guatemala.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  108,889 km2 (42,042 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  17,263,239"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  88% Christianity, 11% No religion, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Guatemala City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Guatemalan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Quetzal (GTQ)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +502"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<BelizeScreen>
    name: "Belize"
    Image:
        source: 'belize.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  22,966 km2 (8,867 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  419,199"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  74.3% Christianity, 15.6% No religion, 10.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Belize City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Belizean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Belize dollar (BZD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +501"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SalvadorScreen>
    name: "El Salvador"
    Image:
        source: 'el_salvador.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  21,041 km2 (8,124 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  6,830,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  84.1% Christianity, 15.2% No religion, 0.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  San Salvador"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Salvadorian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  United States dollar (USD), Bitcoin"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +503"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<HondurasScreen>
    name: "Honduras"
    Image:
        source: 'honduras.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  112,492 km2 (43,433 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  9,587,522"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  87% Christianity, 10% Unaffiliated, 3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Tegucigalpa"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Honduran"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Lempira (HNL)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +504"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<NicaraguaScreen>
    name: "Nicaragua"
    Image:
        source: 'nicaragua.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  130,375 km2 (50,338 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  6,486,201"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  84.4% Christianity, 14.7% No Religion, 0.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Managua"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Nicaraguan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Córdoba (NIO)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +505"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page               



<CostaRicaScreen>
    name: "Costa Rica"
    Image:
        source: 'costa_rica.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  51,100 km2 (19,700 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  5,094,118"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  72.6% Christianity, 27% No Religion, 0.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  San José"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Costa Rican"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Costa Rican colón (CRC)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +506"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<PanamaScreen>
    name: "Panama"
    Image:
        source: 'panama.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  75,417 km2 (29,119 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  4,379,039"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  91.5% Christianity, 7.6% No Religion, 0.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Panama City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Panamanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Balboa (PAB), United States dollar (USD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +507"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<BahamasScreen>
    name: "The Bahamas"
    Image:
        source: 'bahamas.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  13,878 km2 (5,358 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  385,637"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  95.8% Christianity, 3.1% No Religion, 1.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Nassau"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Bahamian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Bahamian dollar (BSD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1 242"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<CubaScreen>
    name: "Cuba"
    Image:
        source: 'cuba.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  109,884 km2 (42,426 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  11,181,595"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  59.9% Christianity, 23.2% No Religion, 17.6% Folk religions,  0.3S% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Havana"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Cuban"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Cuban peso (CUP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +53"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<JamaicaScreen>
    name: "Jamaica"
    Image:
        source: 'jamaica.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  10,991  km2 (4,244 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,726,667"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  68.9% Christianity, 21.3% No Religion, 1.1% Rastafarianism,  8.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kingston"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Jamaican"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Jamaican dollar (JMD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1-876, +1-658"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<HaitiScreen>
    name: "Haiti"
    Image:
        source: 'haiti.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  27,750  km2 (10,710 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  11,439,646"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  86.9% Christianity, 10.6% No Religion, 2.2% Folk religions,  0.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Port-au-Prince"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French, Haitian Creole"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Haitian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Gourde (G) (HTG)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +509"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<DominicanRepublicScreen>
    name: "Dominican Republic"
    Image:
        source: 'dominican_republic.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  48,671  km2 (18,792 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  10,878,246"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  66.7% Christianity, 29.6% No Religion, 3.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Santo Domingo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Dominican, Quisqueyan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Dominican peso (DOP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1-809, +1-829, +1-849"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SaintKittsandNevisScreen>
    name: "Saint Kitts and Nevis"
    Image:
        source: 'saint_kitts_and_nevis.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  261 km2 (101 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  52,441"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  87.6% Christianity, 1.8% Hinduism, 8.7% No Religion, 1.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Basseterre"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Kittitian, Nevisian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  East Caribbean dollar (EC$) (XCD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1 869"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<AntiguaandBarbudaScreen>
    name: "Antigua and Barbuda"
    Image:
        source: 'antigua_and_barbuda.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  440 km2 (170 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  97,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  76.5% Christianity, 12.1% Other, 11.4% No Religion"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  St. Johns"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Antiguan, Barbudan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  East Caribbean dollar (EC$) (XCD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1 268"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<DominicaScreen>
    name: "Dominica"
    Image:
        source: 'dominica.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  750 km2 (290 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  71,625"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  94.4% Christianity, 3.0% Folk religions, 1.7% Other, 0.9% No Religion"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Roseau"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Dominican"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  East Caribbean dollar (EC$) (XCD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1-767"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SaintLuciaScreen>
    name: "Saint Lucia"
    Image:
        source: 'saint_lucia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  617 km2 (238 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:   184,401"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  90.4% Christianity, 5.9% No Religion, 1.9% Rastafari, 1.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Castries"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Saint Lucian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  East Caribbean dollar (EC$) (XCD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1 758"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SaintVincentandtheGrenadinesScreen>
    name: "Saint Vincent and the Grenadines"
    Image:
        source: 'saint_vincent_and_the_grenadines.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  389 km2 (150 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:   110,211"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  82.1% Christianity, 7.5% No Religion, 1.1% Rastafari, 9.3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kingstown"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Saint Vincentian or Vincentian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  East Caribbean dollar (EC$) (XCD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1 784"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<BarbadosScreen>
    name: "Barbados"
    Image:
        source: 'barbados.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  439 km2 (169 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:   287,025"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  75.6% Christianity, 20.6% No Religion, 3.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bridgetown"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Barbadian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Barbadian dollar (BBD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1 246"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<GrenadaScreen>
    name: "Grenada"
    Image:
        source: 'grenada.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  348.5 km2 (134.6 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:   111.454"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  86.4% Christianity, 5.7% No Religion, 1.2% Rastafari, 6.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  St. Georges"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Grenadian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  East Caribbean dollar (XCD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1-473"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<TrinidadandTobagoScreen>
    name: "Trinidad and Tobago"
    Image:
        source: 'trinidad_and_tobago.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  5,131 km2 (1,981 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:   1,367,558"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  63.2% Christianity, 20.4% Hinduism, 5.6% Islam, 10.8% Rastafari"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Port of Spain"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Trinidadian and Tobagonian, Trini"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Trinidad and Tobago dollar (TTD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +1 (868)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page

#2
<SouthAmericaScreen>:
    name: "South America"
    BoxLayout:
        orientation: 'vertical'
        spacing: '8dp'
        MDToolbar:
            elevation: 25
            title: 'World countries'
            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
            MDIconButton:
                icon: "magnify"
                icon_color: (255/255, 255/255, 255/255, 1)
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release:
                    root.manager.current = "SearchCountryScreen"
                    app.past_page = "South America"
        MDLabel:
            text: '   South America'
            font_style: 'H6'
            size_hint_y: None
            height: self.texture_size[1]  
        ScrollView:
            MDList:
                OneLineAvatarListItem:
                    id: Colombia
                    text: 'Colombia  -  Bogota'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'col.png'
                OneLineAvatarListItem:
                    id: Venezuela
                    text: 'Venezuela  -  Caracas'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ven.png'
                OneLineAvatarListItem:
                    id: Guyana
                    text: 'Guyana  -  Georgtown'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'guy.png'
                OneLineAvatarListItem:
                    id: Suriname
                    text: 'Suriname  -  Paramaribo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'suri.png'
                OneLineAvatarListItem:
                    id: Ecuador
                    text: 'Ecuador  -  Quito'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ecu.png'
                OneLineAvatarListItem:
                    id: Peru
                    text: 'Peru  -  Lima'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'per.png'
                OneLineAvatarListItem:
                    id: Brazil
                    text: 'Brazil  -  Brasilia'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bra.png'
                OneLineAvatarListItem:
                    id: Bolivia
                    text: 'Bolivia  -  La Paz, Sucre'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bol.png'
                OneLineAvatarListItem:
                    id: Chile
                    text: 'Chile  -  Santiago'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'chi.png'
                OneLineAvatarListItem:
                    id: Argentina
                    text: 'Argentina  -  Buenos Aires'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'arg.png'
                OneLineAvatarListItem:
                    id: Paraguay
                    text: 'Paraguay  -  Asuncion'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'para.png'
                OneLineAvatarListItem:
                    id: Uruguay
                    text: 'Uruguay  -  Montevideo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'uru.png'
                Widget:

    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'continents.png'
            MDLabel:
                text: '              Continents'
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'North America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "North America"
                    OneLineListItem:
                        text: 'South America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "South America"
                    OneLineListItem:
                        text: 'Europe'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Europe"
                    OneLineListItem:
                        text: 'Asia'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Asia"
                    OneLineListItem:
                        text: 'Africa'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Africa"
                    OneLineListItem:
                        text: 'Australia and Oceania'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Australia and Oceania"



<ColombiaScreen>
    name: "Colombia"
    Image:
        source: 'colombia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,141,748 km2 (440,831 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  50,372,424"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  88.6% Christianity, 10.3% No Religion, 1.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bogotá"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Colombian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Colombian peso (COP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +57"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<VenezuelaScreen>
    name: "Venezuela"
    Image:
        source: 'venezuela.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  916,445 km2 (353,841 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  28,887,118"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  91% Christianity, 8% No Religion, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Caracas"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Venezuelan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Bolívar digital (VED)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +58"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<GuyanaScreen>
    name: "Guyana"
    Image:
        source: 'guyana.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  214,970 km2 (83,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  743,700"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  62.7% Christianity, 24.8% Hinduism, 6.8% Islam, 3.1% No Religion, 2.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Georgetown"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Guyanese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Guyanese dollar (GYD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +592"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SurinameScreen>
    name: "Suriname"
    Image:
        source: 'suriname.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  163,821 km2 (63,252 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  575,990"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  48.4% Christianity, 22.3% Hinduism, 13.9% Islam, 1.8% Winti, 0.8% Javanism"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Paramaribo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Dutch"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Surinamese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Surinamese dollar (SRD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +597"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<EcuadorScreen>
    name: "Ecuador"
    Image:
        source: 'ecuador.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  283,561 km2 (109,484 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  17,715,822"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  93.1% Christianity, 6.1% No religion, 0.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Quito"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Ecuadorian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  United States dollar (USD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +593"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<PeruScreen>
    name: "Peru"
    Image:
        source: 'peru.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,285,216 km2 (496,225 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  34,294,231"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  94.51% Christianity, 5.09% No religion, 0.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Lima"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Peruvian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Sol (PEN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +51"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<BrazilScreen>
    name: "Brazil"
    Image:
        source: 'brazil.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  8,515,767 km2 (3,287,956 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  210,147,125"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  88.8% Christianity, 8% No religion, 2% Spiritism, 1.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Brasília"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Portuguese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Brazilian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Real (BRL)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +55"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<BoliviaScreen>
    name: "Bolivia"
    Image:
        source: 'bolivia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,098,581 km2 (424,164 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  11,428,245"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  89.3% Christianity, 10.1% No religion, 0.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Santa Cruz de la Sierra"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Bolivian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Boliviano (BOB)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +591"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<ChileScreen>
    name: "Chile"
    Image:
        source: 'chile.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  756,096.3 km2 (291,930.4 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  17,574,003"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  63% Christianity, 36% No religion, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Santiago"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Chilean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Chilean peso (CLP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +56"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<ArgentinaScreen>
    name: "Argentina"
    Image:
        source: 'argentina.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  2,780,400 km2 (1,073,500 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  45,605,826"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  79.6% Christianity, 19.2% No religion, 1.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Buenos Aires"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Argentinian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Argentine peso (ARS)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +54"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<ParaguayScreen>
    name: "Paraguay"
    Image:
        source: 'paraguay.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  406,796 km2 (157,065 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  7,359,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  96.1% Christianity, 2.6% No religion, 1.3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Asunción"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish, Guarani"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Paraguayan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Guaraní (PYG)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +595"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<UruguayScreen>
    name: "Uruguay"
    Image:
        source: 'uruguay.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  176,215 km2 (68,037 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  3,518,552"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  57% Christianity, 41.5% No religion, 1.5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Montevideo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Uruguayan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Uruguayan peso (UYU)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +598"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page

#3
<EuropeScreen>:
    name: "Europe"
    BoxLayout:
        orientation: 'vertical'
        spacing: '8dp'
        MDToolbar:
            elevation: 25
            title: 'World countries'
            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
            MDIconButton:
                icon: "magnify"
                icon_color: (255/255, 255/255, 255/255, 1)
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release:
                    root.manager.current = "SearchCountryScreen"
                    app.past_page = "Europe"
        MDLabel:
            text: '   Europe'
            font_style: 'H6'
            size_hint_y: None
            height: self.texture_size[1]  
        ScrollView:
            MDList:
                OneLineAvatarListItem:
                    id: Portugal
                    text: 'Portugal  -  Lisbon'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'por.png'
                OneLineAvatarListItem:
                    id: Spain
                    text: 'Spain  -  Madrid'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'spa.png'
                OneLineAvatarListItem:
                    id: Andorra
                    text: 'Andorra  -  Andorra la Vella'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'and.png'
                OneLineAvatarListItem:
                    id: France
                    text: 'France  -  Paris'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'fra.png'
                OneLineAvatarListItem:
                    id: United Kingdom
                    text: 'United Kingdom  -  London'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'united_kingdom.png'
                OneLineAvatarListItem:
                    id: Republic of Ireland
                    text: 'Republic of Ireland  -  Dublin'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'irel.png'
                OneLineAvatarListItem:
                    id: Iceland
                    text: 'Iceland  -  Reykjavik'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ice.png'
                OneLineAvatarListItem:
                    id: Netherlands
                    text: 'Netherlands  -  Amsterdam'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'net.png'
                OneLineAvatarListItem:
                    id: Belgium
                    text: 'Belgium  -  Brussels'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'belg.png'
                TwoLineAvatarListItem:
                    id: Luxembourg
                    text: 'Luxembourg  -  '
                    secondary_text: "Luxembourg City"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'lux.png'
                OneLineAvatarListItem:
                    id: Germany
                    text: 'Germany  -  Berlin'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ger.png'
                OneLineAvatarListItem:
                    id: Denmark
                    text: 'Denmark  -  Copenhagen'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'den.png'
                OneLineAvatarListItem:
                    id: Switzerland
                    text: 'Switzerland  -  Bern'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'switz.png'
                OneLineAvatarListItem:
                    id: Liechtenstein
                    text: 'Liechtenstein  -  Vaduz'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'liec.png'
                OneLineAvatarListItem:
                    id: Austria
                    text: 'Austria  -  Vienna'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'aus.png'
                OneLineAvatarListItem:
                    id: Italy
                    text: 'Italy  -  Rome'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ital.png'
                OneLineAvatarListItem:
                    id: Vatican City State
                    text: 'Vatican City State  -  Vatican'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'vat.png'
                OneLineAvatarListItem:
                    id: San Marino
                    text: 'San Marino  -  San Marino'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'san_mar.png'
                OneLineAvatarListItem:
                    id: Monaco
                    text: 'Monaco  -  Monaco'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'mon.png'
                OneLineAvatarListItem:
                    id: Malta
                    text: 'Malta  -  Valleta'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'malt.png'
                OneLineAvatarListItem:
                    id: Greece
                    text: 'Greece  -  Athens'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'gre.png'
                OneLineAvatarListItem:
                    id: Norway
                    text: 'Norway  -  Oslo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'nor.png'
                OneLineAvatarListItem:
                    id: Sweden
                    text: 'Sweden  -  Stockholm'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'swed.png'
                OneLineAvatarListItem:
                    id: Finland
                    text: 'Finland  -  Helsinki'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'fin.png'
                OneLineAvatarListItem:
                    id: Estonia
                    text: 'Estonia  -  Tallinn'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'est.png'
                OneLineAvatarListItem:
                    id: Latvia
                    text: 'Latvia  -  Riga'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'lat.png'
                OneLineAvatarListItem:
                    id: Lithuania
                    text: 'Lithuania  -  Vilnius'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'lit.png'
                OneLineAvatarListItem:
                    id: Poland
                    text: 'Poland  -  Warsaw'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'pol.png'
                OneLineAvatarListItem:
                    id: Belarus
                    text: 'Belarus  -  Minsk'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bel.png'
                OneLineAvatarListItem:
                    id: Czech Republic
                    text: 'Czech Republic  -  Prague'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'cze.png'
                OneLineAvatarListItem:
                    id: Slovakia
                    text: 'Slovakia  -  Bratislava'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'slov.png'
                OneLineAvatarListItem:
                    id: Ukraine
                    text: 'Ukraine  -  Kyiv'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ukr.png'
                OneLineAvatarListItem:
                    id: Russia
                    text: 'Russia  -  Moscow'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'russ.png'
                OneLineAvatarListItem:
                    id: Kazakhstan
                    text: 'Kazakhstan  -  Nur Sultan'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'kaz.png' 
                OneLineAvatarListItem:
                    id: Georgia
                    text: 'Georgia  -  Tbilisi'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'geo.png'
                OneLineAvatarListItem:
                    id: Azerbaijan
                    text: 'Azerbaijan   -   Baku'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'aze.png'
                OneLineAvatarListItem:
                    id: Slovenia
                    text: 'Slovenia  -  Ljubljana'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'slove.png'
                OneLineAvatarListItem:
                    id: Hungary
                    text: 'Hungary  -  Budapest'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'hun.png'
                OneLineAvatarListItem:
                    id: Romania
                    text: 'Romania  -  Bucharest'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'roma.png'
                OneLineAvatarListItem:
                    id: Moldova
                    text: 'Moldova  -  Chisinau'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'mol.png'
                OneLineAvatarListItem:
                    id: Croatia
                    text: 'Croatia  -  Zagreb'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'cro.png'
                TwoLineAvatarListItem:
                    id: Bosnia and Herzegovina
                    text: 'Bosnia and Herzegovina  -  '
                    secondary_text: "Sarajevo"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bos.png'
                OneLineAvatarListItem:
                    id: Serbia
                    text: 'Serbia  -  Belgrade'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'serb.png'
                OneLineAvatarListItem:
                    id: Montenegro
                    text: 'Montenegro  -  Podgorica'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'mont.png'
                OneLineAvatarListItem:
                    id: Kosovo
                    text: 'Kosovo  -  Pristina'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'kos.png'
                OneLineAvatarListItem:
                    id: Albania
                    text: 'Albania  -  Tirana'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'alb.png'
                OneLineAvatarListItem:
                    id: North Macedonia
                    text: 'North Macedonia  -  Skopje'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'mac.png'
                OneLineAvatarListItem:
                    id: Bulgaria
                    text: 'Bulgaria  -  Sofia'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bul.png'
                OneLineAvatarListItem:
                    id: Turkey
                    text: 'Turkey   -   Ankara'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'turke.png'
                Widget:

    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'continents.png'
            MDLabel:
                text: '              Continents'
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'North America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "North America"
                    OneLineListItem:
                        text: 'South America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "South America"
                    OneLineListItem:
                        text: 'Europe'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Europe"
                    OneLineListItem:
                        text: 'Asia'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Asia"
                    OneLineListItem:
                        text: 'Africa'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Africa"
                    OneLineListItem:
                        text: 'Australia and Oceania'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Australia and Oceania"



<PortugalScreen>
    name: "Portugal"
    Image:
        source: 'portugal.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  92,212 km2 (35,603 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  10,344,802"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  84.3% Christianity, 6.8% No religion, 8.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Lisbon"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Portuguese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Portuguese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +351"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SpainScreen>
    name: "Spain"
    Image:
        source: 'spain.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  505,990 km2 (195,360  sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:   47,450,795"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  57.6% Christianity, 37.7% No religion, 4.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Madrid"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Spanish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +34"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<AndorraScreen>
    name: "Andorra"
    Image:
        source: 'andorra.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  467.63 km2 (180.55 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  77,543"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Roman Catholicism"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Andorra la Vella"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Catalan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Andorran"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +376"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<FranceScreen>
    name: "France"
    Image:
        source: 'france.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  640,679 km2 (247,368 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  67,413,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  50% Christianity, 33% No religion, 4% Islam, 2% Buddhist, 11% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Paris"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR), CFP franc (XPF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +33"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<UKScreen>
    name: "United Kingdom"
    Image:
        source: 'uk.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  242,495 km2 (93,628 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  67,081,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  59.5% Christianity, 25.7% No religion, 4.4% Islam, 10.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  London"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  British"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Pound sterling (GBP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +44"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<IrelandScreen>
    name: "Republic of Ireland"
    Image:
        source: 'ireland.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  70,273 km2 (27,133 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  5,011,500"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  85.1% Christianity, 10.1% No religion, 4.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Dublin"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Irish, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Irish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +353"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<IcelandScreen>
    name: "Iceland"
    Image:
        source: 'iceland.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  102,775 km2 (39,682 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  371,580"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  75.1% Christianity, 21.5% No religion, 3.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Reykjavík"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Icelandic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Icelander"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Icelandic króna (ISK)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +354"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<NetherlandsScreen>
    name: "Netherlands"
    Image:
        source: 'netherlands.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  41,865 km2 (16,164 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  17,685,200"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  54.1% No religion, 38.3% Christianity, 5.0% Islam, 2.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Amsterdam"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Dutch"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Dutch"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR), US dollar ($) (USD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +31, +599"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<BelgiumScreen>
    name: "Belgium"
    Image:
        source: 'belgium.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  30,689 km2 (11,849 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  11,492,641"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  60% Christianity, 31% No religion, 7% Islam, 2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Brussels"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Dutch, French, German"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Belgian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +32"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<LuxembourgScreen>
    name: "Luxembourg"
    Image:
        source: 'luxembourg.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  2,586.4 km2 (998.6 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  633,622"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  73.2% Christianity, 23.4% No religion, 3.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Luxembourg City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Luxembourgish, French, German"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Luxembourger"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +352"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<GermanyScreen>
    name: "Germany"
    Image:
        source: 'germany.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  357,022 km2 (137,847 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  83,190,556"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  54% Christianity, 40.1% No religion, 5.0% Islam,  0.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Berlin"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  German"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  German"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +49"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SwitzerlandScreen>
    name: "Switzerland"
    Image:
        source: 'switzerland.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  41,285 km2 (15,940 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  8,570,146"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  65.5% Christianity, 26.3% No religion, 5.3% Islam, 2.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Zürich"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  German, French, Italian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Swiss"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Swiss franc (CHF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +41"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<LiechtensteinScreen>
    name: "Liechtenstein"
    Image:
        source: 'liechtenstein.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  160 km2 (62 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  38,896"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  83.2% Christianity, 7% No religion, 5.9% Islam, 3.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Vaduz"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  German"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Liechtensteiner"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Swiss franc (CHF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +423"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<AustriaScreen>
    name: "Austria"
    Image:
        source: 'austria.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  83,879 km2 (32,386 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  8,935,112"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  69% Christianity, 22% No religion, 7.9% Islam, 1.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Vienna"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  German"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Austrian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +43"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<ItalyScreen>
    name: "Italy"
    Image:
        source: 'italy.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  301,230 km2 (116,310 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  60,317,116"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  84.4% Christianity, 11.6% No religion, 1.0% Islam, 3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Rome"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Italian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Italian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +39"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<VaticanScreen>
    name: "Vatican City State"
    Image:
        source: 'vatican.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  0.49 km2 (0.19 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  453"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Christianity"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Vatican city"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Italian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Italian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +379"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SanMarinoScreen>
    name: "San Marino"
    Image:
        source: 'san_marino.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  61.2 km2 (23.6 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  33,600"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  97% Christianity, 3% other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Dogana"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Italian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Sammarinese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +378 (+39 0549 calling via Italy)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MonacoScreen>
    name: "Monaco"
    Image:
        source: 'monaco.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  2.02 km2 (0.78 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  38,300"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  86% Christianity, 11.7% No religion, 1.7% Judaism, 0.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Monte Carlo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Italian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +377"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<MaltaScreen>
    name: "Malta"
    Image:
        source: 'malta.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  316 km2 (122 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  516,100"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  90% Christianity, 5% No religion, 1.7% Islam, 3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Valletta"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Maltese, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Maltese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +356"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<GreeceScreen>
    name: "Greece"
    Image:
        source: 'greece.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  131,957 km2 (50,949 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  10,678,632"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  93% Christianity, 4% No religion, 2% Islam, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Athens"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Greek"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Greek"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +30"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<NorwayScreen>
    name: "Norway"
    Image:
        source: 'norway.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  385,207 km2 (148,729 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  5,402,171"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  75.6% Christianity, 20.2% No religion, 3.4% Islam, 0.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Oslo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Norwegian, Sámi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Norwegian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Norwegian krone (NOK)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +47"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SwedenScreen>
    name: "Sweden"
    Image:
        source: 'sweden.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  385,207 km2 (173,860 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  10,402,070"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  66.8% Christianity, 27% No religion, 5% Islam, 1.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Stockholm"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Swedish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Swedish, Swede"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Swedish krona (SEK)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +46"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<FinlandScreen>
    name: "Finland"
    Image:
        source: 'finland.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  338,455 km2 (130,678 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  5,536,146"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  69.8% Christianity, 29.4% No religion, 0.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Helsinki"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Finnish, Swedish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Finnish, Finn"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +358"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<EstoniaScreen>
    name: "Estonia"
    Image:
        source: 'estonia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  45,339 km2 (17,505 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,328,439"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  64.87% No religion, 34.03% Christianity, 0.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Tallinn"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Estonian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Estonian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +372"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<LatviaScreen>
    name: "Latvia"
    Image:
        source: 'latvia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  64,589 km2 (24,938 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,907,675"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  80% Christianity, 20% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Riga"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Latvian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Latviana"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +371"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<LithuaniaScreen>
    name: "Lithuania"
    Image:
        source: 'lithuania.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  65,300 km2 (25,200 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,775,810"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  79.4% Christianity, 20.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Vilnius"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Lithuanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Lithuanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +370"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<PolandScreen>
    name: "Poland"
    Image:
        source: 'poland.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  312,696 km2 (120,733 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  38,179,800"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  90% Christianity, 6% No religion, 4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Warsaw"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Polish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Polish, Pole"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Złoty (PLN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +48"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<BelarusScreen>
    name: "Belarus"
    Image:
        source: 'belarus.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  207,595 km2 (80,153 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  9,349,645"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  55.4% Christianity, 41.1% No religion, 3.5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Minsk"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Belarusian, Russiana"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Belarusian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Belarusian ruble (BYN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +375"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<CzechRepublicScreen>
    name: "Czech Republic"
    Image:
        source: 'czech_republic.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  78,871 km2 (30,452 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  10,701,777"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  47.8% No religion, 11.7% Christianity, 9.1% No organized religion, 31.3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Prague"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Czech"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Czech"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Czech koruna (CZK)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +420"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SlovakiaScreen>
    name: "Slovakia"
    Image:
        source: 'Slovakia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  49,035 km2 (18,933 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  5,449,270"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  67.6% Christianity, 23.8% No religion, 8.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bratislava"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Slovak"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Slovak"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +421"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<UkraineScreen>
    name: "Ukraine"
    Image:
        source: 'ukraine.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  603,628 km2 (233,062 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  41,319,838"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  87.3% Christianity, 11.0% Irreligion, 1.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kyiv"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Ukrainian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Ukrainian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Hryvnia (UAH)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +380"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<RussiaScreen>
    name: "Russia"
    Image:
        source: 'russia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  17,125,191 km2 (6,601,670 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  145,478,097"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  73% Christianity, 15% No religion, 10% Islam, 2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Moscow"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Russian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Russian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Russian ruble (RUB)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +7"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<KazakhstanScreen>
    name: "Kazakhstan"
    Image:
        source: 'kazakhstan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  2,724,900 km2 (1,052,100 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  19,082,467"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  72% Islam, 23% Christianity, 5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Almaty"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Kazakh, Russian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Kazakhstani"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Tenge (KZT)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +7"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<GeorgiaScreen>
    name: "Georgia"
    Image:
        source: 'georgia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  69,700 km2 (26,900 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  3,728,573"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  88.1% Christianity, 10.7% Islam, 1.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Tbilisi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Georgian, Abkhaz"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Georgian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Georgian lari (GEL)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +995"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<AzerbaijanScreen>
    name: "Azerbaijan"
    Image:
        source: 'azerbaijan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  86,600 km2 (33,400 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  10,130,100"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  96.9% Islam, 3.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Baku"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Azerbaijani"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Azerbaijani, Azeri"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Manat (AZN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +994"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SloveniaScreen>
    name: "Slovenia"
    Image:
        source: 'slovenia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  20,271 km2 (7,827 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,107,126"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  77.8% Christianity, 18.3% No religion, 3.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Ljubljana"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Slovene"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Slovene, Slovenian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +386"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<HungaryScreen>
    name: "Hungary"
    Image:
        source: 'hungary.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  93,030 km2 (35,920 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  9,730,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  54.3% Christianity, 18.2% No religion, 27.5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Budapest"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Hungarian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Hungarian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Forint (HUF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +36"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<RomaniaScreen>
    name: "Romania"
    Image:
        source: 'romania.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  238,397 km2 (92,046 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  19,186,201"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  92.3% Christianity, 6.2% No religion, 1.5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bucharest"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Romanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Romanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Romanian leu (RON)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +40"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MoldovaScreen>
    name: "Moldova"
    Image:
        source: 'moldova.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  33,843.5 km2 (13,067.0 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,597,107"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  91.8% Christianity, 5.5% No religion, 2.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Chisinau"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Moldovan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Moldovan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Moldovan leu (MDL)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +373"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<CroatiaScreen>
    name: "Croatia"
    Image:
        source: 'croatia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  56,594 km2 (21,851 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  3,888,529"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  91.06% Christianity, 4.57% No religion, 4.37% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Zagreb"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Croatian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Croatian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Croatian kuna (HRK)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +385"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BosniaAndHerzegovinaScreen>
    name: "Bosnia and Herzegovina"
    Image:
        source: 'bosnia_and_herzegovina.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  51,129 km2 (19,741 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  3,824,782"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  50.7% Islam, 45.9% Christianity, 1.1% No religion, 1.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Sarajevo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Bosnian, Serbian, Croatian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Bosnian, Herzegovinian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Convertible mark (BAM)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +387"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SerbiaScreen>
    name: "Serbia"
    Image:
        source: 'Serbia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  88,361 km2 (34,116 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  6,871,547"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  90.6% Christianity, 3.1% Islam, 1.1% No religion, 5.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Belgrade"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Serbian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Serbian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Serbian dinar (RSD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +381"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MontenegroScreen>
    name: "Montenegro"
    Image:
        source: 'montenegro.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  13,812 km2 (5,333 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  621,873"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  75.93% Christianity, 19.21% Islam, 3.31% No religion, 1.55% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Podgorica"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Montenegrin"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Montenegrin"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +382"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<KosovoScreen>
    name: "Kosovo"
    Image:
        source: 'kosovo.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  10,887 km2 (4,203 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,935,259"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  97.4% Islam, 1.6% Christianity, 0.1% No religion, 0.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Pristina"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages: Albanian, Serbian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Kosovar, Kosovan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR), unofficial use: Serbian dinar (RSD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +383"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<AlbaniaScreen>
    name: "Albania"
    Image:
        source: 'albania.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  28,748 km2 (11,100 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,845,955"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  59% Islam, 17% Christianity, 9% No religion, 15% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Tirana"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Albanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Albanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Lek (ALL)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +355"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<NorthMacedoniaScreen>
    name: "North Macedonia"
    Image:
        source: 'north_macedonia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  25,713 km2 (9,928 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,832,696"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  70.7% Christianity, 28.6% Islam, 0.5% No religion, 0.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Skopje"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Macedonian, Albanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Macedonian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Macedonian denar (MKD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +389"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BulgariaScreen>
    name: "Bulgaria"
    Image:
        source: 'bulgaria.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  110,993.6 km2 (42,854.9 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  6,875,040"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  61.1% Christianity, 7.9% Islam, 9.3% No religion, 21.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Sofia"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Bulgarian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Bulgarian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Lev (BGN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +359"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<TurkeyScreen>
    name: "Turkey"
    Image:
        source: 'turkey.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  783,356 km2 (302,455 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  83,614,362"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  89.5% Islam, 9.9% Irreligion, 2.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Istanbul"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Turkish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Turkish, Turk"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Turkish lira (TRY)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +90"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


#4
<AsiaScreen>:
    name: "Asia"
    BoxLayout:
        orientation: 'vertical'
        spacing: '8dp'
        MDToolbar:
            elevation: 25
            title: 'World countries'
            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
            MDIconButton:
                icon: "magnify"
                icon_color: (255/255, 255/255, 255/255, 1)
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release:
                    root.manager.current = "SearchCountryScreen"
                    app.past_page = "Asia"
        MDLabel:
            text: '   Asia'
            font_style: 'H6'
            size_hint_y: None
            height: self.texture_size[1]  
        ScrollView:
            MDList:
                OneLineAvatarListItem:
                    id: Russia
                    text: 'Russia  -  Moscow'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'russ.png'   
                OneLineAvatarListItem:
                    id: Georgia
                    text: 'Georgia  -  Tbilisi'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'geo.png'
                OneLineAvatarListItem:
                    id: Azerbaijan
                    text: 'Azerbaijan   -   Baku'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'aze.png'
                OneLineAvatarListItem:
                    id: Armenia
                    text: 'Armenia   -   Yerevan'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'arm.png'
                OneLineAvatarListItem:
                    id: Turkey
                    text: 'Turkey   -   Ankara'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'turke.png'
                OneLineAvatarListItem:
                    id: Cyprus
                    text: 'Cyprus  -  Nicosia'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'cyp.png'
                OneLineAvatarListItem:
                    id: Iran
                    text: 'Iran   -   Tehran'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ira.png'
                OneLineAvatarListItem:
                    id: Iraq
                    text: 'Iraq   -   Baghdad'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'iraq_.png'
                OneLineAvatarListItem:
                    id: Syria
                    text: 'Syria   -   Damascus'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'syr.png'
                OneLineAvatarListItem:
                    id: Lebanon
                    text: 'Lebanon   -   Beirut'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'leb.png'
                OneLineAvatarListItem:
                    id: Israel
                    text: 'Israel   -   Jerusalem'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'isra.png'
                OneLineAvatarListItem:
                    id: Palestine
                    text: 'Palestine   -   Ramallah'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'pale.png'
                OneLineAvatarListItem:
                    id: Jordan
                    text: 'Jordan   -   Amman'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'jor.png'
                OneLineAvatarListItem:
                    id: Egypt
                    text: 'Egypt  -  Cairo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'egy.png'
                OneLineAvatarListItem:
                    id: Saudi Arabia
                    text: 'Saudi Arabia   -   Riyadh'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'saudi_arabia_.png'
                OneLineAvatarListItem:
                    id: Kuwait
                    text: 'Kuwait   -   Kuwait City'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'kuw.png'
                OneLineAvatarListItem:
                    id: Qatar
                    text: 'Qatar   -   Doha'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'qat.png'
                OneLineAvatarListItem:
                    id: Bahrain
                    text: 'Bahrain   -   Manama'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bahr.png'
                TwoLineAvatarListItem:
                    id: United Arab Emirates
                    text: 'United Arab Emirates   -   '
                    secondary_text: "Abu Dabi"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'united_arab.png'
                OneLineAvatarListItem:
                    id: Oman
                    text: 'Oman    -   Muscat'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'oma.png'
                OneLineAvatarListItem:
                    id: Yemen
                    text: 'Yemen    -   Sanaa'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'yem.png'
                OneLineAvatarListItem:
                    id: Kazakhstan
                    text: 'Kazakhstan  -  Nur Sultan'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'kaz.png'
                OneLineAvatarListItem:
                    id: Uzbekistan
                    text: 'Uzbekistan   -   Tashkent'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'uzb.png'
                OneLineAvatarListItem:
                    id: Kyrgyzstan
                    text: 'Kyrgyzstan   -   Bishkek'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'kyr.png'
                OneLineAvatarListItem:
                    id: Turkmenistan
                    text: 'Turkmenistan   -   Ashgabat'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'turkm.png'
                OneLineAvatarListItem:
                    id: Tajikistan
                    text: 'Tajikistan   -   Dushanbe'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'tajik.png'
                OneLineAvatarListItem:
                    id: Afghanistan
                    text: 'Afghanistan   -   Kabul'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'afg.png'
                OneLineAvatarListItem:
                    id: Pakistan
                    text: 'Pakistan   -   Islamabad'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'pak.png'
                OneLineAvatarListItem:
                    id: India
                    text: 'India  -  New Delhi'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ind.png'
                TwoLineAvatarListItem:
                    id: Sri Lanka
                    text: 'Sri Lanka  -  '
                    secondary_text: "Sri Jayawardenepura Kotte"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'sri_lan.png'
                OneLineAvatarListItem:
                    id: Maldives
                    text: 'Maldives  -  Male'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'mald.png'
                OneLineAvatarListItem:
                    id: Nepal
                    text: 'Nepal  -  Kathmandu'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'nep.png'
                OneLineAvatarListItem:
                    id: Bhutan
                    text: 'Bhutan  -  Thimphu'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bhu.png'
                OneLineAvatarListItem:
                    id: Bangladesh
                    text: 'Bangladesh   -   Dhaka'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ban.png'
                OneLineAvatarListItem:
                    id: China
                    text: 'China   -   Beijing'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'chin.png'
                OneLineAvatarListItem:
                    id: Mongolia
                    text: 'Mongolia   -   Ulaanbaatar'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'mong.png'
                OneLineAvatarListItem:
                    id: North Korea
                    text: 'North Korea   -   Pyongyang'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'kor_n.png'
                OneLineAvatarListItem:
                    id: South Korea
                    text: 'South Korea   -   Seoul'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'kor_s.png'
                OneLineAvatarListItem:
                    id: Japan
                    text: 'Japan   -   Tokyo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'jap.png'
                OneLineAvatarListItem:
                    id: Taiwan
                    text: 'Taiwan   -   Taipei'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget: 
                        source: 'tai.png'
                OneLineAvatarListItem:
                    id: Myanmar
                    text: 'Myanmar   -   Naypyidaw'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'myan.png'
                OneLineAvatarListItem:
                    id: Thailand
                    text: 'Thailand   -   Bangkok'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'thail.png'
                OneLineAvatarListItem:
                    id: Laos
                    text: 'Laos   -   Vientiane'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'lao.png'
                OneLineAvatarListItem:
                    id: Vietnam
                    text: 'Vietnam   -   Hanoi'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'vie.png'
                OneLineAvatarListItem:
                    id: Cambodia
                    text: 'Cambodia   -   Phnom Penh'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'cam.png'
                OneLineAvatarListItem:
                    id: Malaysia
                    text: 'Malaysia   -   Kuala Lumpur'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ma.png'
                OneLineAvatarListItem:
                    id: Singapore
                    text: 'Singapore   -   Singapore'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'sing.png'
                OneLineAvatarListItem:
                    id: Philippines
                    text: 'Philippines    -   Manila'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'phil.png'
                TwoLineAvatarListItem:
                    id: Brunei
                    text: 'Brunei    -   '
                    secondary_text: "Bandar Seri Begawan"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'bru.png'
                OneLineAvatarListItem:
                    id: Indonesia
                    text: 'Indonesia   -   Jakarta'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'indo.png'
                OneLineAvatarListItem:
                    id: East Timor
                    text: 'East Timor   -   Dili'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'east_t.png'
                Widget:

    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'continents.png'
            MDLabel:
                text: '              Continents'
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'North America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "North America"
                    OneLineListItem:
                        text: 'South America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "South America"
                    OneLineListItem:
                        text: 'Europe'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Europe"
                    OneLineListItem:
                        text: 'Asia'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Asia"
                    OneLineListItem:
                        text: 'Africa'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Africa"
                    OneLineListItem:
                        text: 'Australia and Oceania'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Australia and Oceania"


<ArmeniaScreen>
    name: "Armenia"
    Image:
        source: 'armenia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  29,743 km2 (11,484 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,963,900"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Christianity (Armenian Apostolic Church)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Yerevan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Armenian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Armenian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Dram (AMD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +374"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page




<CyprusScreen>
    name: "Cyprus"
    Image:
        source: 'cyprus.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  9,251 km2 (3,572 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,189,265"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  72.3% Christianity, 25% Islam, 1.9% No religion, 0.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Nicosia"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Greek, Turkish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Cypriot"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Euro (€) (EUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +357"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<IranScreen>
    name: "Iran"
    Image:
        source: 'iran.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  1,648,195 km2 (636,372 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  83,183,741"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  99.98% Islam, 0.02% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Tehran"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Persian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Iranian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Iranian rial (IRR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +98"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<IraqScreen>
    name: "Iraq"
    Image:
        source: 'iraq.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  438,317 km2 (169,235 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  40,222,503"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  95% Islam, 5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Baghdad"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic, Kurdish"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Iraqi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Iraqi dinar (IQD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +964"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SyriaScreen>
    name: "Syria"
    Image:
        source: 'syria.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  185,180 km2 (71,500 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  17,500,657"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  87% Islam, 10% Christianity, 3% Druze"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Damascus"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Syrian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Syrian pound (SYP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +963"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<LebanonScreen>
    name: "Lebanon"
    Image:
        source: 'lebanon.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  10,452 km2 (4,036 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  6,859,408"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  57.7% Islam, 40% Christianity, 2.3% Druze"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Beirut"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Lebanese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Lebanese pound (LBP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +961"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<IsraelScreen>
    name: "Israel"
    Image:
        source: 'israel.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  20,770-22,072 km2 (8,019-8,522 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  9,467,900"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  74.2% Judaism, 17.8% Islam, 20% Christianity, 1.6% Druze, 4.4% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Jerusalem"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Hebrew"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Israeli"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  New shekel (ILS)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +972"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<PalestineScreen>
    name: "Palestine"
    Image:
        source: 'palestine.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  6,020 km2 (2,320 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  5,159,076"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Islam"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Gaza City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Palestinian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Egyptian pound (EGP), Israeli new shekel (ILS), Jordanian dinar (JOD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +970"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<JordanScreen>
    name: "Jordan"
    Image:
        source: 'jordan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  89,342 km2 (34,495 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  11,042,719"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  95% Islam, 4% Christianity, 1% Druze, Bahai"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Amman"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Jordanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Jordanian dinar (JOD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +962"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SaudiArabiaScreen>
    name: "Saudi Arabia"
    Image:
        source: 'saudi_arabia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  2,149,690 km2 (830,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  34,218,169"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  93% Islam, 4.4% Christianity, 1.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Riyadh"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Saudi Arabian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Saudi Riyal (SR) (SAR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +966"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<KuwaitScreen>
    name: "Kuwait"
    Image:
        source: 'kuwait.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  17,818 km2 (6,880 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  4,420,110"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  74.36% Islam, 18.17% Christianity, 7.47% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kuwait City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Kuwaiti"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Kuwaiti dinar (KWD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +965"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<QatarScreen>
    name: "Qatar"
    Image:
        source: 'qatar.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  11,581 km2 (4,471 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,795,484"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  65.5% Islam, 15.1% Hinduism, 14.2% Christianity, 3.3% Buddhism, 1.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Doha"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Qatari"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Qatari riyal (QAR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +974"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BahrainScreen>
    name: "Bahrain"
    Image:
        source: 'bahrain.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  785.08 km2 (303.12 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,569,446"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  70.3% Islam, % Hinduism, 14.2% Christianity, 3.3% Buddhism, 1.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Manama"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Bahraini"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Bahraini dinar (BHD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +973"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<UnitedArabEmiratesScreen>
    name: "United Arab Emirates"
    Image:
        source: 'united_arab_emirates.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  83,600 km2 (32,300 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  9,890,400"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  76% Islam, 12.7% Christianity, 7.5% Hinduism, 1.8% Buddhism, 2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Dubai"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Emirati"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  UAE dirham (AED)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +971"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<OmanScreen>
    name: "Oman"
    Image:
        source: 'oman.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  309,500 km2 (119,500 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  4,829,473"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  85.9% Islam, 6.5% Christianity, 5.5% Hinduism, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Muscat"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Omani"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Omani rial (OMR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +968"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<YemenScreen>
    name: "Yemen"
    Image:
        source: 'yemen.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  555,000 km2 (214,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  30,491,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  99% Islam, 1% Christianity and Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Sanaa"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Yemeni, Yemenite"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Yemeni rial (YER)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +967"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<UzbekistanScreen>
    name: "Uzbekistan"
    Image:
        source: 'uzbekistan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  448,978 km2 (173,351 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  35,200,180"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  88% Islam, 9% Christianity, 3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Tashkent"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Uzbek"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Uzbekistani, Uzbek"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Uzbek som (UZS)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +998"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<KyrgyzstanScreen>
    name: "Kyrgyzstan"
    Image:
        source: 'kyrgyzstan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  199,951 km2 (77,202 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  6,586,600"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  90% Islam, 8% Christianity, 2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bishkek"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Kyrgyz"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Kyrgyz"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Kyrgyzstani som (KGS)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +996"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<TurkmenistanScreen>
    name: "Turkmenistan"
    Image:
        source: 'turkmenistan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  491,210 km2 (189,660 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  6,031,187"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  96.1% Islam, 3.6% Christianity, 0.3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Ashgabat"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Turkmen"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Turkmen, Turkmenistani, Turkmenian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Turkmenistan manat (TMT)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +993"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<TajikistanScreen>
    name: "Tajikistan"
    Image:
        source: 'tajikistan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  143,100 km2 (55,300 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  9,537,645"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  98% Islam, 0.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Dushanbe"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Tajik"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Tajik, Tajikistani"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Somoni (TJS)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +992"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<AfghanistanScreen>
    name: "Afghanistan"
    Image:
        source: 'afghanistan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  652,864 km2 (252,072 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  40,218,234"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  99.7% Islam, 0.3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kabul"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Pashto, Dari"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Afghan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Afghani (AFN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +93"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<PakistanScreen>
    name: "Pakistan"
    Image:
        source: 'pakistan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  881,913 km2 (340,509 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  226,992,332"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  96.47% Islam, 2.14% Hinduism, 1.27% Christianity, 0.91% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Karachi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Urdu, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Pakistani"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Pakistani rupee (PKR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +92"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<IndiaScreen>
    name: "India"
    Image:
        source: 'india.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  3,287,263 km2 (1,269,219 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,352,642,280"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  79.8% Hinduism, 14.2% Islam, 2.3% Christianity, 1.7% Sikhism, 1.28% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Mumbai"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Hindi, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Indian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Indian rupee (INR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +91"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SriLankaScreen>
    name: "Sri Lanka"
    Image:
        source: 'sri_lanka.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  65,610 km2 (25,330 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  22,156,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  70.2% Buddhism, 12.6% Hinduism, 9.7% Islam, 7.4% Christianity, 0.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Colombo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Sinhala, Tamil"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Sri Lankan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Sri Lankan rupee (LKR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +94"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MaldivesScreen>
    name: "Maldives"
    Image:
        source: 'maldives.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  300 km2 (120 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  557,426"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Sunni Islam"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Malé"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Dhivehi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Maldivian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Maldivian rufiyaa (MVR), United States dollar (USD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +960"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<NepalScreen>
    name: "Nepal"
    Image:
        source: 'nepal.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  147,516 km2 (56,956 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  28,095,714"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  81.3% Hinduism, 9% Buddhism, 4.4% Islam, 5.3% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kathmandu"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Nepali"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Nepali, Nepalese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Nepalese rupee (NPR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +977"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BhutanScreen>
    name: "Bhutan"
    Image:
        source: 'bhutan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  38,394 km2 (14,824 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  754,388"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  74.8% Buddhism, 22.6% Hinduism, 1.9% Bon or Folk, 0.6% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Thimphu"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Dzongkha"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Bhutanese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Ngultrum (BTN), Indian rupee (INR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +975"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BangladeshScreen>
    name: "Bangladesh"
    Image:
        source: 'bangladesh.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  148,460 km2 (57,320 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  161,376,708"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  90.4% Islam, 8.5% Hinduism, 0.6% Buddhism, 0.4% Christianity, 0.1% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Dhaka"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Bengali"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Bangladeshi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Taka (BDT)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +880"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<ChinaScreen>
    name: "China"
    Image:
        source: 'china.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  9,596,961 km2 (3,705,407 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,412,600,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  74.5%  Folk, 18.3% Buddhism, 5.2% Christianity, 1.6% Islam, 0.1% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Beijing"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Standard Chinese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Chinese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Renminbi (CNY)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +86, +852(Hong Kong), +853(Macau)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MongoliaScreen>
    name: "Mongolia"
    Image:
        source: 'mongolia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  1,564,116 km2 (603,909 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  3,353,470"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  51.7% Buddhism, 40.6% No religion, 3.2% Islam, 2.5% Shamanism, 0.1% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Ulaanbaatar"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Mongolian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Mongolian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Tögrög (MNT)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +976"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<NorthKoreaScreen>
    name: "North Korea"
    Image:
        source: 'korea_north.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  120,540 km2 (46,540 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  25,549,604"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  State atheism"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Pyongyang"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Korean (Munhwaŏ)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  North Korean, Korean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Korean People won (KPW)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +850"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SouthKoreaScreen>
    name: "South Korea"
    Image:
        source: 'korea_south.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  100,363 km2 (38,750 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  51,709,098"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  56.1% No religion, 27.6% Christianity, 15.5% Korean Buddhism, 0.8% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Seoul"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Korean, Korean Sign Language"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Sorth Korean, Korean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Korean Republic won (KRW)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +82"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<JapanScreen>
    name: "Japan"
    Image:
        source: 'japan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  377,975 km2 (145,937 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  125,440,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  62% No religion, 31% Buddhism, 3% Shintoism, 1% Christianity, 3% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Tokyo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Japanese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Japanese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Japanese yen (¥)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +81"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<TaiwanScreen>
    name: "Taiwan"
    Image:
        source: 'taiwan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  36,197 km2 (13,976 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  23,451,837"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  43.8% Folk, 21.2% Buddhism, 13.7% No religion, 5.6% Christianity 16.5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  New Taipei City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Standard Chinese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Taiwanese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  New Taiwan dollar (TWD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +886"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MyanmarScreen>
    name: "Myanmar"
    Image:
        source: 'myanmar.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  676,578 km2 (261,228 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  53,582,855"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  87.9% Buddhism, 6.2% Christianity, 4.3% Islam, 1.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Yangon"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Burmese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Burmese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Kyat (K) (MMK)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +95"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<ThailandScreen>
    name: "Thailand"
    Image:
        source: 'thailand.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  513,120 km2 (198,120 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  69,950,850"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  93.5% Buddhism, 5.4% Islam, 1.1% Christianity, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bangkok"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Thai"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Thai"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Baht (THB)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +66"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<LaosScreen>
    name: "Laos"
    Image:
        source: 'laos.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  237,955 km2 (91,875 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  7,123,205"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  66% Buddhism, 30.7% Tai folk religion, 1.5% Christianity, 1.8% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Vientiane"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Lao"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Lao, Laotian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Kip (LAK)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +856"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<VietnamScreen>
    name: "Vietnam"
    Image:
        source: 'vietnam.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  331,699 km2 (128,070 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  96,208,984"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  45.3% Folk, 28.4% No religion, 14.9% Buddhism, 8.5% Christianity, 2.9% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Ho Chi Minh City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Vietnamese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Vietnamese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  dong (VND)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +84"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<CambodiaScreen>
    name: "Cambodia"
    Image:
        source: 'cambodia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  181,035 km2 (69,898 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  15,552,211"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  97.1% Buddhism, 2.0% Islam, 0.3% Christianity, 0.5% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Phnom Penh"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Khmer"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Cambodian, Khmer"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Riel (KHR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +855"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MalaysiaScreen>
    name: "Malaysia"
    Image:
        source: 'malaysia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  330,803 km2 (127,724 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  32,730,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  61.3% Islam, 19.8% Buddhism, 9.2% Christianity, 6.3% Hinduism, 04.6% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kuala Lumpur"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Malaysian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Malaysian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Ringgit (RM) (MYR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +60"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SingaporeScreen>
    name: "Singapore"
    Image:
        source: 'singapore.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  733.1 km2 (283.1 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  5,453,600"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  31.1% Buddhism, 20.0% No religion, 18.9% Christianity, 15.6% Islam, 14.4% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Singapore"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Malay, Mandarin, Tamil"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Singaporean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Singapore dollar (SGD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +65"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<PhilippinesScreen>
    name: "Philippines"
    Image:
        source: 'philippines.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  300,000 km2 (120,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  109,035,343"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  88.7% Christianity, 6% Islam, 5.3% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Quezon City"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Filipino, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Filipino(Pinoy), Filipina(Pinay), Philippine"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Philippine peso (PHP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +63"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BruneiScreen>
    name: "Brunei"
    Image:
        source: 'brunei.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  5,765 km2 (2,226 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  460,345"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  80.9% Sunni Islam, 7.1% Christian, 7% Buddhist, 5% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bandar Seri Begawan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Malay"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Bruneian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Brunei dollar (BND)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +673"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<EastTimorScreen>
    name: "East Timor"
    Image:
        source: 'east_timor.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  15,007 km2 (5,794 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,340,513"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  99.53% Christianity, 0.24% Islam, 0.23% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Dili"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Portuguese, Tetum"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  East Timorese, Timorese, Maubere"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  United States dollar (USD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +670"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



#5
<AfricaScreen>:
    name: "Africa"
    BoxLayout:
        orientation: 'vertical'
        spacing: '8dp'
        MDToolbar:
            elevation: 25
            title: 'World countries'
            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
            MDIconButton:
                icon: "magnify"
                icon_color: (255/255, 255/255, 255/255, 1)
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release:
                    root.manager.current = "SearchCountryScreen"
                    app.past_page = "Africa"
        MDLabel:
            text: '   Africa'
            font_style: 'H6'
            size_hint_y: None
            height: self.texture_size[1]  
        ScrollView:
            MDList:
                OneLineAvatarListItem:
                    id: Morocco
                    text: 'Morocco  -  Rabat'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'moroc.png'
                OneLineAvatarListItem:
                    id: Algeria
                    text: 'Algeria  -  Algiers'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'alger.png'
                OneLineAvatarListItem:
                    id: Tunisia
                    text: 'Tunisia  -  Tunis'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'tuni.png'
                OneLineAvatarListItem:
                    id: Libya
                    text: 'Libya  -  Tripoli'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'liby.png'
                OneLineAvatarListItem:
                    id: Egypt
                    text: 'Egypt  -  Cairo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'egy.png'
                OneLineAvatarListItem:
                    id: Mauritania
                    text: 'Mauritania  -  Nouakchott'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'maurita.png'
                OneLineAvatarListItem:
                    id: Mali
                    text: 'Mali  -  Bamako'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'mal.png'
                OneLineAvatarListItem:
                    id: Niger
                    text: 'Niger  -  Niamey'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'nig.png'
                OneLineAvatarListItem:
                    id: Chad
                    text: 'Chad  -  NDjamena'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'cha.png'
                OneLineAvatarListItem:
                    id: Sudan
                    text: 'Sudan  -  Khartoum'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'suda.png'
                OneLineAvatarListItem:
                    id: Eritrea
                    text: 'Eritrea  -  Asmara'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'eritre.png'
                OneLineAvatarListItem:
                    id: Djibouti
                    text: 'Djibouti  -  Djibouti'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'djibo.png'
                OneLineAvatarListItem:
                    id: Senegal
                    text: 'Senegal  -  Dakar'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'sene.png'
                OneLineAvatarListItem:
                    id: The Gambia
                    text: 'The Gambia  -  Banjul'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'gamb.png'
                OneLineAvatarListItem:
                    id: Guinea Bissau
                    text: 'Guinea Bissau  -  Bissau'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'guinea_bis.png'
                OneLineAvatarListItem:
                    id: Guinea
                    text: 'Guinea  -  Conakry'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'guin.png'
                OneLineAvatarListItem:
                    id: Sierra Leone
                    text: 'Sierra Leone  -  Freetown'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'sier.png'
                OneLineAvatarListItem:
                    id: Liberia
                    text: 'Liberia  -  Monrovia'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'liber.png'
                OneLineAvatarListItem:
                    id: Ivory Coast
                    text: 'Ivory Coast  -  Yamoussoukro'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'cote_d_Ivoire.png'
                OneLineAvatarListItem:
                    id: Burkina Faso
                    text: 'Burkina Faso  -  Ouagadougou'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'burkina_faso.png'
                OneLineAvatarListItem:
                    id: Ghana
                    text: 'Ghana  -  Accra'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ghan.png'
                OneLineAvatarListItem:
                    id: Togo
                    text: 'Togo  -  Lome'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'tog.png'
                OneLineAvatarListItem:
                    id: Benin
                    text: 'Benin  -  Porto Novo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'beni.png'
                OneLineAvatarListItem:
                    id: Nigeria
                    text: 'Nigeria  -  Abuja'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'nigeri.png'
                OneLineAvatarListItem:
                    id: Cameroon
                    text: 'Cameroon  -  Yaounde'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'camer.png'
                TwoLineAvatarListItem:
                    id: Central African Republic
                    text: 'Central African Republic  -  '
                    secondary_text: "Bangui"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'central_africa.png'
                OneLineAvatarListItem:
                    id: South Sudan
                    text: 'South Sudan  -  Juba'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'south_sud.png'
                OneLineAvatarListItem:
                    id: Ethiopia
                    text: 'Ethiopia  -  Addis Ababa'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ethiop.png'
                OneLineAvatarListItem:
                    id: Somalia
                    text: 'Somalia  -  Mogadishu'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'somal.png'
                OneLineAvatarListItem:
                    id: Equatorial Guinea
                    text: 'Equatorial Guinea  -  Malabo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'equatorial_gui.png'
                OneLineAvatarListItem:
                    id: Gabon
                    text: 'Gabon  -  Libreville'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'gabo.png'
                TwoLineAvatarListItem:
                    id: Republic of the Congo
                    text: 'Republic of the Congo  -  '
                    secondary_text: "Brazzaville"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'republic_cong.png'
                TwoLineAvatarListItem:
                    id: Democratic Republic of the Congo
                    text: 'Democratic Republic of the Congo  -  '
                    secondary_text: "Kinshasa"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'democratic_cong.png'
                OneLineAvatarListItem:
                    id: Rwanda
                    text: 'Rwanda  -  Kigali'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'rwanda.png'
                OneLineAvatarListItem:
                    id: Burundi
                    text: 'Burundi  -  Gitega'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'burun.png'
                OneLineAvatarListItem:
                    id: Uganda
                    text: 'Uganda  -  Kampala'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'ugan.png'
                OneLineAvatarListItem:
                    id: Kenya
                    text: 'Kenya  -  Nairobi'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'keny.png'
                OneLineAvatarListItem:
                    id: Angola
                    text: 'Angola  -  Luanda'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'angol.png'
                OneLineAvatarListItem:
                    id: Zambia
                    text: 'Zambia  -  Lusaka'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'zamb.png'
                OneLineAvatarListItem:
                    id: Malawi
                    text: 'Malawi  -  Lilongwe'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'malaw.png'
                OneLineAvatarListItem:
                    id: Mozambique
                    text: 'Mozambique  -  Maputo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'mozambi.png'
                OneLineAvatarListItem:
                    id: Madagascar
                    text: 'Madagascar  -  Antananarivo'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'madag.png'
                OneLineAvatarListItem:
                    id: Namibia
                    text: 'Namibia  -  Windhoek'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'namib.png'
                OneLineAvatarListItem:
                    id: Botswana
                    text: 'Botswana  -  Gaborone'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'botswana.png'
                OneLineAvatarListItem:
                    id: Zimbabwe
                    text: 'Zimbabwe  -  Harare'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'zimba.png'
                TwoLineAvatarListItem:
                    id: Republic of South Africa
                    text: 'Republic of South Africa  -  '
                    secondary_text: "Pretoria"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'south_afric.png'
                OneLineAvatarListItem:
                    id: Eswatini
                    text: 'Eswatini  -  Mbabane'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'swazi.png'
                OneLineAvatarListItem:
                    id: Lesotho
                    text: 'Lesotho  -  Maseru'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'leso.png'
                OneLineAvatarListItem:
                    id: Seychelles
                    text: 'Seychelles  -  Victoria'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'seychelles.png'
                OneLineAvatarListItem:
                    id: Mauritius
                    text: 'Mauritius  -  Port Louis'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'maurit.png'
                OneLineAvatarListItem:
                    id: Comoros
                    text: 'Comoros  -  Moroni'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'comor.png'
                TwoLineAvatarListItem:
                    id: Sao Tome and Principe
                    text: 'Sao Tome and Principe  -  '
                    secondary_text: "Sao Tome"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'sao_tom.png'
                OneLineAvatarListItem:
                    id: Cape Verde
                    text: 'Cape Verde  -  Praia'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'cape_verd.png'
                Widget:

    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'continents.png'
            MDLabel:
                text: '              Continents'
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'North America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "North America"
                    OneLineListItem:
                        text: 'South America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "South America"
                    OneLineListItem:
                        text: 'Europe'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Europe"
                    OneLineListItem:
                        text: 'Asia'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Asia"
                    OneLineListItem:
                        text: 'Africa'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Africa"
                    OneLineListItem:
                        text: 'Australia and Oceania'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Australia and Oceania"


<MoroccoScreen>
    name: "Morocco"
    Image:
        source: 'morocco.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  710,850 km2 (274,460 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  37,112,080"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  99% Islam, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Casablanca"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic, Berber"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Moroccan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Moroccan dirham (MAD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +212"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<AlgeriaScreen>
    name: "Algeria"
    Image:
        source: 'algeria.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  2,381,741 km2 (919,595 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  44,700,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  99% Sunni Islam, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Algiers"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic, Berber"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Algerian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Algerian dinar (DZD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +213"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<TunisiaScreen>
    name: "Tunisia"
    Image:
        source: 'tunisia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  163,610 km2 (63,170 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  11,708,370"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Islam"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Tunis"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Tunisian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Tunisian dinar (TND)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +216"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<LibyaScreen>
    name: "Libya"
    Image:
        source: 'libya.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,759,541 km2 (679,363 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  6,992,701"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  97% Islam, 2.7% Christianity, 0.3% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Tripoli"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Libyan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Libyan dinar (LYD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +218"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<EgyptScreen>
    name: "Egypt"
    Image:
        source: 'egypt.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  1,010,408 km2 (390,121 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  102,674,145"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  90.3% Islam, 9.6% Christianity, 0.1% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Cairo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Egyptian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Egyptian pound (EGP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +20"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MauritaniaScreen>
    name: "Mauritania"
    Image:
        source: 'mauritania.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,030,000 km2 (400,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  4,403,313"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Islam"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Nouakchott"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Mauritanian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Ouguiya (MRU)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +222"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MaliScreen>
    name: "Mali"
    Image:
        source: 'mali.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,240,192 km2 (478,841 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  20,250,833"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  94.5% Islam, 2.5% Traditional African religions, 2.3% Christianity, 0.5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bamako"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Malian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  West African CFA franc (XOF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +223"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<NigerScreen>
    name: "Niger"
    Image:
        source: 'niger.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,267,000 km2 (489,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  24,112,753"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  99.3% Islam, 0.3% Christianity, 0.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Niamey"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Nigerien"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  West African CFA franc (XOF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +227"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<ChadScreen>
    name: "Chad"
    Image:
        source: 'chad.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,284,000 km2 (496,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  16,244,513"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  51.8% Islam, 44.1% Christianity, 4.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  NDjamena"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic, French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Chadian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  West African CFA franc (XOF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +235"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SudanScreen>
    name: "Sudan"
    Image:
        source: 'sudan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,886,068 km2 (728,215 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  44,909,353"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  90.7% Islam, 5.4% Christianity, 2.9% African traditional, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Omdurman"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Arabic, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Sudanese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Sudanese pound (SDG)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +249"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<EritreaScreen>
    name: "Eritrea"
    Image:
        source: 'eritrea.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  117,600 km2 (45,400 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  6,081,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  50% Christianity, 48% Islam, 2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Asmara"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Tigrinya, Arabic, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Eritrean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Nakfa (ERN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +291"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<DjiboutiScreen>
    name: "Djibouti"
    Image:
        source: 'djibouti.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  23,200 km2 (9,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  921,804"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  94% Islam, 6% Christianity"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Djibouti"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French, Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Djiboutian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Djiboutian franc (DJF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +253"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SenegalScreen>
    name: "Senegal"
    Image:
        source: 'senegal.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  196,712 km2 (75,951 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  15,854,323"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  90.1% Islam, 5.5% Christianity, 4.4% Other "
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Dakar"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Senegalese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  West African CFA franc (XOF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +221"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<TheGambiaScreen>
    name: "The Gambia"
    Image:
        source: 'gambia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  10,689 km2 (4,127 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,173,999"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  96% Islam, 3% Christianity, 4.4% African Traditional Religion "
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Banjul"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Gambian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Dalasi (GMD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +220"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<GuineaBissauScreen>
    name: "Guinea Bissau"
    Image:
        source: 'guinea_bissau.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  36,125 km2 (13,948 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,726,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  46.1% Islam, 30.6% Folk religions, 18.9% Christianity, 4.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bissau"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Portuguese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Bissau-Guinean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  West African CFA franc (XOF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +245"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<GuineaScreen>
    name: "Guinea"
    Image:
        source: 'guinea.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  245,857 km2 (94,926 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  12,414,293"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  85% Islam, 8% Christianity, 7% Indigenous beliefs"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Conakry"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Guinean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Guinean franc (GNF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +224"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SierraLeoneScreen>
    name: "Sierra Leone"
    Image:
        source: 'sierra_leone.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  71,740 km2 (27,700 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  8,059,155"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  78% Islam, 21% Christianity, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Freetown"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Sierra Leonean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Leone (SLL)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +232"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<LiberiaScreen>
    name: "Liberia"
    Image:
        source: 'liberia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  111,369 km2 (43,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  5,214,030"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  86.2% Christianity, 11.7% Islam, 1.4% No religion, 0.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Monrovia"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Liberian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Liberian dollar (LRD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +231"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<IvoryCoastScreen>
    name: "Ivory Coast"
    Image:
        source: 'ivory_coast.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  322,463 km2 (124,504 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  26,378,274"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  43% Islam, 33% Christianity, 10.5% Traditional faiths, 13.5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Abidjan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Ivorian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  West African CFA franc (XOF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +225"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BurkinaFasoScreen>
    name: "Burkina Faso"
    Image:
        source: 'burkina_faso.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  274,200 km2 (105,900 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  21,510,181"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  60.5% Islam, 23.2% Christianity, 15.3% Indigenous beliefs, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Ouagadougou"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Burkinabé, Burkinese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  West African CFA franc (XOF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +226"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<GhanaScreen>
    name: "Ghana"
    Image:
        source: 'ghana.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  239,567 km2 (92,497 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  31,072,940"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  71.2% Christianity, 17.6% Islam, 6.2% Traditional faiths, 5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Accra"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Ghanaian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Cedi (GHS)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +233"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<TogoScreen>
    name: "Togo"
    Image:
        source: 'togo.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  56,785 km2 (21,925 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  8,608,444"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  43.7% Christianity, 35.6% Traditional faiths, 14% Islam, 6.7% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Lomé"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Togolese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  West African CFA franc (XOF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +228"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BeninScreen>
    name: "Benin"
    Image:
        source: 'benin.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  114,763 km2 (44,310 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  11,733,059"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  52.2% Christianity, 24.6% Islam, 17.9% Traditional faiths, 5.3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Cotonou"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Beninese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  West African CFA franc (XOF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +229"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<NigeriaScreen>
    name: "Nigeria"
    Image:
        source: 'nigeria.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  923,769 km2 (356,669 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  211,400,708"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  53.5% Islam, 45.9% Christianity, 0.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Lagos"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Nigerian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Naira (NGN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +234"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<CameroonScreen>
    name: "Cameroon"
    Image:
        source: 'cameroon.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  475,442 km2 (183,569 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  26,545,864"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  70.7% Christianity, 24.4% Islam, 2.3% Traditional faiths, 2.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Douala"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Cameroonian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Central African CFA franc (XAF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +237"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<CentralAfricanRepublicScreen>
    name: "Central African Republic"
    Image:
        source: 'central_african_republic.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  622,984 km2 (240,535 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  4,666,368"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  89.5% Christianity, 8.5% Islam, 1% Traditional faiths, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bangui"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French, Sango"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Central African"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Central African CFA franc (XAF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +236"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SouthSudanScreen>
    name: "South Sudan"
    Image:
        source: 'south_sudan.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  644,329 km2 (248,777 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  12,778,250"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  60.5% Christianity, 32.9% Traditional faiths, 6.2% Islam, 0.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Juba"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  South Sudanese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  South Sudanese pound (SSP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +211"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<EthiopiaScreen>
    name: "Ethiopia"
    Image:
        source: 'ethiopia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,104,300 km2 (426,400 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  117,876,227"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  67.3% Christianity, 31.3% Islam, 0.6% Traditional faiths, 0.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Addis Ababa"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Afar, Amharic, Oromo, Somali, Tigrinya"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Ethiopian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Birr (ETB)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +251"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SomaliaScreen>
    name: "Somalia"
    Image:
        source: 'somalia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  637,657 km2 (246,201 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  15,893,219"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Sunni Islam"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Mogadishu"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Somali, Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Somali, Somalian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Somali shilling (SOS)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +252"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<EquatorialGuineaScreen>
    name: "Equatorial Guinea"
    Image:
        source: 'equatorial_guinea.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  28,050 km2 (10,830 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,468,777"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  88.7% Christianity, 5.0% No religion, 4.0% Islam, 2.3% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bata"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Spanish, French, Portuguese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Equatoguinean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Central African CFA franc (XAF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +240"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<GabonScreen>
    name: "Gabon"
    Image:
        source: 'gabon.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  267,667 km2 (103,347 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,119,275"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  75.6% Christianity, 9.8% Islam, 5.7% Traditional faiths, 8.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Libreville"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Gabonese, Gabonaise"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Central African CFA franc (XAF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +241"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<RepublicoftheCongoScreen>
    name: "Republic of the Congo"
    Image:
        source: 'republic_congo.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  342,000 km2 (132,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  5,657,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  88.5% Christianity, 4.7% Traditional faiths, 3% No religion, 3.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Brazzaville"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Congolese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Central African CFA franc (XAF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +242"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<DemocraticRepublicoftheCongoScreen>
    name: "Democratic Republic of the Congo"
    Image:
        source: 'democratic_congo.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  2,345,409 km2 (905,567 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  92,377,993"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  95.8% Christianity, 1.8% Traditional faiths, 1.5% Islam, 0.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kinshasa"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Congolese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Congolese franc (CDF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +243"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<RwandaScreen>
    name: "Rwanda"
    Image:
        source: 'rwanda.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  26,338 km2 (10,169 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  12,374,397"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  93.8% Christianity, 3.0% No religion, 2.2% Islam, 0.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kigali"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Kinyarwanda, French, English, Swahili"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Rwandan, Rwandese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Rwandan franc (RWF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +250"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BurundiScreen>
    name: "Burundi"
    Image:
        source: 'burundi.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  27,834 km2 (10,747 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  11,865,821"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  91.5% Christianity, 5.5% Traditional faiths, 2.1% Islam, 0.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Bujumbura"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Kirundi, French, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Burundian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Burundian franc (FBu) (BIF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +257"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<UgandaScreen>
    name: "Uganda"
    Image:
        source: 'uganda.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  241,038 km2 (93,065 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  42,729,036"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  39.3% Roman Catholic, 32% Anglican, 13.7% Islam, 11.1% Pentecostal, 3.9% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Kampala"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Swahili"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Ugandan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Ugandan shilling (UGX)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +256"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<KenyaScreen>
    name: "Kenya"
    Image:
        source: 'kenya.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  580,367 km2 (224,081 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  54,985,698"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  85.5% Christianity, 10.9% Islam, 1.6% No religion, 2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Nairobi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Swahili"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Kenyan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Kenyan shilling (KES)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +254"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<AngolaScreen>
    name: "Angola"
    Image:
        source: 'angola.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,246,700 km2 (481,400 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  31,127,674"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  93.4% Christianity, 4.5% Traditional faiths, 2.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Luanda"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Portuguese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Angolan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Kwanza (AOA)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +244"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<ZambiaScreen>
    name: "Zambia"
    Image:
        source: 'zambia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  752,617 km2 (290,587 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  17,351,708"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Christianity"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Lusaka"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Zambian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Zambian kwacha (ZMW)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +260"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MalawiScreen>
    name: "Malawi"
    Image:
        source: 'malawi.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  118,484 km2 (45,747 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  19,129,952"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  82.3% Christianity, 13.8% Islam, 1.2% Traditional faiths, 2.7% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Lilongwe"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Chewa"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Malawian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Malawian kwacha (D) (MWK)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +265"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MozambiqueScreen>
    name: "Mozambique"
    Image:
        source: 'mozambique.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  801,590 km2 (309,500 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  30,066,648"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  57.6% Christianity, 18.3% Islam, 9.6% Traditional faiths, 14.5% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Maputo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Portuguese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Mozambican"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Metical (MZN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +258"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MadagascarScreen>
    name: "Madagascar"
    Image:
        source: 'madagascar.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  587,041 km2 (226,658 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  28,427,328"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  85.3% Christianity, 4.5% Traditional faiths, 3% Islam, 7.2% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Antananarivo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Malagasy, French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Malagasy"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Ariary (MGA)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +261"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<NamibiaScreen>
    name: "Namibia"
    Image:
        source: 'namibia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  825,615 km2 (318,772 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,550,226"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  87.9% Christianity, 10.2% Traditional faiths, 1.9% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Windhoek"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Namibian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Namibian dollar (NAD), South African rand (ZAR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +264"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<BotswanaScreen>
    name: "Botswana"
    Image:
        source: 'botswana.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  581,730 km2 (224,610 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,254,068"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  73% Christianity, 20% No religion, 6% Traditional faiths, 1% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Gaborone"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Setswana, English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Batswana (plural), Motswana (singular)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Pula (BWP)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +267"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<ZimbabweScreen>
    name: "Zimbabwe"
    Image:
        source: 'zimbabwe.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  390,757 km2 (150,872 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  15,092,171"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  84.1% Christianity, 10.2% No religion, 4.5% Traditional faiths, 1.2% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Harare"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Chewa, Chibarwe, English, Kalanga, Nambya, Ndau"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Zimbabwean, Zimbo"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Zimbabwean dollar"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +263"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<RepublicofSouthAfricaScreen>
    name: "Republic of South Africa"
    Image:
        source: 'south_africa.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,221,037 km2 (471,445 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  60,142,978"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  78% Christianity, 10.9% No religion, 4.4% Traditional faiths, 6.7% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Johannesburg"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Zulu, Swazi, Afrikaans, Sepedi, Sesotho, Setswana"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  South African"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  South African rand (ZAR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +27"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<EswatiniScreen>
    name: "Eswatini"
    Image:
        source: 'eswatini.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  17,364 km2 (6,704 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,160,164"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  89.3% Christianity, 7.4% No religion, 3.3% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Manzini"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Swazi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Emaswati (plural), Liswati (singular)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Lilangeni (SZL), South African rand (ZAR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +268"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<LesothoScreen>
    name: "Lesotho"
    Image:
        source: 'lesotho.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  30,355 km2 (11,720 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  2,108,328"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  92.3% Christianity, 6.4% Traditional faiths, 1.3% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Maseru"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Sesotho"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Basotho (plural), Mosotho (singular)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Loti (LSL), South African rand (ZAR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +266"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SeychellesScreen>
    name: "Seychelles"
    Image:
        source: 'seychelles.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  459 km2 (177 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  98,462"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  89.2% Christianity, 2.4% Hinduism, 1.6% Islam, 6.8% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Victoria"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, French, Seychellois"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Seychellois, Seselwa"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Seychellois rupee (SCR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +248"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<MauritiusScreen>
    name: "Mauritius"
    Image:
        source: 'mauritius.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  2,040 km2 (790 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  1,265,475"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  48.54% Hinduism, 32.71% Christianity, 17.3% Islam, 1.45% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Port Louis"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Mauritian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Mauritian rupee (MUR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +230"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<ComorosScreen>
    name: "Comoros"
    Image:
        source: 'comoros.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,861 km2 (719 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  850,886"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  98% Islam, 2% Christianity"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Moroni"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Comorian, French, Arabic"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Comorian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Comorian franc (KMF)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +269"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<SaoTomeandPrincipeScreen>
    name: "Sao Tome and Principe"
    Image:
        source: 'sao_tome_and_principe.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,001 km2 (386 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  211,028"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  81.1% Christianity, 13.2% No religion, 3.1% Folk religions, 2.4% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Sao Tome"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Portuguese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Sao Tomean, Santomean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Dobra (STN)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +239"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


<CapeVerdeScreen>
    name: "Cape Verde"
    Image:
        source: 'cape_verde.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  4,033 km2 (1,557 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  483,628"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  85.3% Christianity, 10.8% No religion, 3.9% Others"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Praia"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Portuguese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Cape Verdean or Cabo Verdean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Cape Verdean escudo (CVE)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +238"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page


#6
<AustraliaandOceaniaScreen>:
    name: "Australia and Oceania"
    BoxLayout:
        orientation: 'vertical'
        spacing: '8dp'
        MDToolbar:
            elevation: 25
            title: 'World countries'
            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
            MDIconButton:
                icon: "magnify"
                icon_color: (255/255, 255/255, 255/255, 1)
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release:
                    root.manager.current = "SearchCountryScreen"
                    app.past_page = "Australia and Oceania"
        MDLabel:
            text: '   Australia and Oceania'
            font_style: 'H6'
            size_hint_y: None
            height: self.texture_size[1]  
        ScrollView:
            MDList:
                OneLineAvatarListItem:
                    id: Australia
                    text: 'Australia  -  Canberra'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'austral.png'
                OneLineAvatarListItem:
                    id: New Zealand
                    text: 'New Zealand  -  Wellington'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'new_zeal.png'
                OneLineAvatarListItem:
                    id: Indonesia
                    text: 'Indonesia   -   Jakarta'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'indo.png'
                TwoLineAvatarListItem:
                    id: Papua New Guinea
                    text: 'Papua New Guinea   -   '
                    secondary_text: "Port Moresby"
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'papu.png'
                OneLineAvatarListItem:
                    id: Solomon Islands
                    text: 'Solomon Islands   -   Honiara'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'solom.png'
                OneLineAvatarListItem:
                    id: Vanuatu
                    text: 'Vanuatu   -   Port Vila'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'vanu.png'
                OneLineAvatarListItem:
                    id: Fiji
                    text: 'Fiji   -   Suva'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'fij.png'
                OneLineAvatarListItem:
                    id: Tonga
                    text: 'Tonga   -   Nukualofa'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'tong.png'
                OneLineAvatarListItem:
                    id: Samoa
                    text: 'Samoa   -   Apia'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'samo.png'
                OneLineAvatarListItem:
                    id: Tuvalu
                    text: 'Tuvalu   -   Funafuti'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'tuval.png'
                OneLineAvatarListItem:
                    id: Kiribati
                    text: 'Kiribati   -   Tarawa'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'kirib.png'
                OneLineAvatarListItem:
                    id: Nauru
                    text: 'Nauru   -   Yaren'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'naur.png'
                OneLineAvatarListItem:
                    id: Marshall Islands
                    text: 'Marshall Islands   -   Majuro'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'marsh.png'
                OneLineAvatarListItem:
                    id: Micronesia
                    text: 'Micronesia   -   Palikir'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'micro.png'
                OneLineAvatarListItem:
                    id: Palau
                    text: 'Palau   -   Ngerulmud'
                    on_release:
                        root.ids.nav_drawer.set_state("close")
                        app.change_screen(self)
                    ImageLeftWidget:
                        source: 'pala.png'
                Widget:

    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'continents.png'
            MDLabel:
                text: '              Continents'
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'North America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "North America"
                    OneLineListItem:
                        text: 'South America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "South America"
                    OneLineListItem:
                        text: 'Europe'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Europe"
                    OneLineListItem:
                        text: 'Asia'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Asia"
                    OneLineListItem:
                        text: 'Africa'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Africa"
                    OneLineListItem:
                        text: 'Australia and Oceania'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Australia and Oceania"



<AustraliaScreen>
    name: "Australia"
    Image:
        source: 'australia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  7,692,024 km2 (2,969,907 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  25,940,500"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  62.1% Christianity, 30.1% No religion, 2.6% Islam, 2.4% Buddhism, 2.8% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Sydney"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Australian, Aussie"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Australian dollar (AUD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +61"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<NewZealandScreen>
    name: "New Zealand"
    Image:
        source: 'new_zealand.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  268,021 km2 (103,483 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:   5,138,030"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  48.5% No religion, 37% Christianity, 2.6% Hinduism, 1.3% Islam, 10.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Auckland"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Māori"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  New Zealander, Kiwi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  New Zealand dollar (NZD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +64"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<IndonesiaScreen>
    name: "Indonesia"
    Image:
        source: 'indonesia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  1,904,569 km2 (735,358 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  270,203,917"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  86.7% Islam, 10.72% Christianity, 1.74% Hinduism, 0.84% Folk/Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Jakarta"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Indonesian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Indonesian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Indonesian rupiah (Rp) (IDR)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +62"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<PapuaNewGuineaScreen>
    name: "Papua New Guinea"
    Image:
        source: 'papua_new_guinea.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  462,840 km2 (178,700 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  8,935,000"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  95.5% Christianity, 4.5% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Port Moresby"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Hiri Motu, PNG Sign Language, Tok Pisin"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Papua New Guinean"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Kina (PGK)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +675"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SolomonIslandsScreen>
    name: "Solomon Islands"
    Image:
        source: 'solomon_islands.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  28,400 km2 (11,000 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  652,857"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  97.4% Christianity, 1.2% Folk religions, 1.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Honiara"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Solomon Islander"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Solomon Islands dollar (SBD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +677"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<VanuatuScreen>
    name: "Vanuatu"
    Image:
        source: 'vanuatu.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  12,189 km2 (4,706 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  307,815"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  93.3% Christianity, 4.1% Folk religions, 1.2% No religion, 1.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Port Vila"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Bislama, English, French"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Ni-Vanuatu and Vanuatuan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Vatu (VUV)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +678"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<FijiScreen>
    name: "Fiji"
    Image:
        source: 'fiji.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  18,274 km2 (7,056 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  926,276"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  64.4% Christianity, 23.9% No religion, 27.9% Hinduism, 6.3% Islam, 1.4% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Suva"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Fijian, English, Fiji Hindi"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Fijian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Fijian dollar (FJD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +679"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<TongaScreen>
    name: "Tonga"
    Image:
        source: 'tonga.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  748 km2 (289 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  100,209"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  98% Christianity, 1% No religion, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Nukualofa"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Tongan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Tongan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Paanga (center_y)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +676"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SamoaScreen>
    name: "Samoa"
    Image:
        source: 'samoa.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  2,842 km2 (1,097 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  202,506"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  Christianity"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Apia"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Samoan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Samoan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Taia (WST)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +685"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<TuvaluScreen>
    name: "Tuvalu"
    Image:
        source: 'tuvalu.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  26 km2 (10 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  11,646"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  67.2% Christianity"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Funafuti"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Tuvaluan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Tuvaluan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Tuvaluan dollar, Australian dollar (AUD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +688"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<KiribatiScreen>
    name: "Kiribati"
    Image:
        source: 'kiribati.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  811 km2 (313 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  119,940"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  96.2% Christianity, 2.1% Bahai, 0.5% No religion, 1.2% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  South Tarawa on Tarawa"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Gilbertese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  I-Kiribati"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Australian dollar (AUD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +686"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<NauruScreen>
    name: "Nauru"
    Image:
        source: 'nauru.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp" 
        MDLabel:
            text: "Area:  21 km2 (8.1 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  10,670"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  92.66% Christianity, 7.34% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Denigomodu District"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  Nauruan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Nauruan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  Australian dollar (AUD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +674"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<MarshallIslandsScreen>
    name: "Marshall Islands"
    Image:
        source: 'marshall_islands.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  181.43 km2 (70.05 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  58,413"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  97% Christianity, 2% No religion, 1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Marshallese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Marshallese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Marshallese"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  United States dollar (USD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +692"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<MicronesiaScreen>
    name: "Micronesia"
    Image:
        source: 'micronesia.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  702 km2 (271 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  104,468"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  95.3% Christianity, 4.1% Folk religions, 0.6% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Weno"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Micronesian"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  United States Dollar (USD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +691"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<PalauScreen>
    name: "Palau"
    Image:
        source: 'palau.png'
        opacity: 0.7
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDLabel:
            text: "Area:  459 km2 (177 sq mi)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Population:  17,907"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Religion:  89.7% Christianity, 5.7% Modekngei, 3% Islam, 2.1% Other"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Largest city:  Koror"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Official languages:  English, Palauan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Demonym:  Palauan"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Currency:  United States dollar (USD)"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "Calling code:  +680"
            font_style: "H6"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release:
                root.manager.current = "SearchCountryScreen" if app.sp else app.past_page



<SearchCountryScreen>
    name: "SearchCountryScreen"
    BoxLayout:
        orientation: 'vertical'
        padding: "12dp"
        spacing: "8dp"
        MDTextFieldRound:
            id: TextField
            hint_text: "Search country"
            normal_color: (255/255, 240/255, 0/255, 1)
            text_color: (0/255, 0/255, 0/255, 1)
            icon_right: "magnify"
            pos_hint: {"center_x": 0.5, "center_y": 0.9}
            size_hint: (0.9, 0.05)
            on_text: app.search(self.text.capitalize())
        ScrollView:
            MDList:
                id: container  
        MDFillRoundFlatButton:
            text: "Back"
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            md_bg_color: (255/255, 240/255, 0/255, 1)
            on_release:
                root.manager.current = app.past_page
                app.sp = None
                app.remove_char_from_TF(self)



<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: 'vertical'
        spacing: '8dp'
        MDToolbar:
            elevation: 25
            title: 'World countries'
            left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]  
            MDIconButton:
                icon: "magnify"
                icon_color: (255/255, 255/255, 255/255, 1)
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release:
                    root.manager.current = "SearchCountryScreen"              
        ScrollView:
            Image:
                source: 'continents.png'
                Widget:

    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'continents.png'
            MDLabel:
                text: '            Continents'
                font_style: 'H5'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineListItem:
                        text: 'North America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "North America"
                    OneLineListItem:
                        text: 'South America'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "South America"
                    OneLineListItem:
                        text: 'Europe'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Europe"
                    OneLineListItem:
                        text: 'Asia'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Asia"
                    OneLineListItem:
                        text: 'Africa'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Africa"
                    OneLineListItem:
                        text: 'Australia and Oceania'
                        on_release:
                            root.ids.nav_drawer.set_state("close")
                            root.manager.current = "Australia and Oceania"              
"""





class MainScreen(Screen):
    pass

class NorthAmericaScreen(Screen):
    pass

class SouthAmericaScreen(Screen):
    pass

class EuropeScreen(Screen):
    pass

class AsiaScreen(Screen):
    pass

class AfricaScreen(Screen):
    pass

class AustraliaandOceaniaScreen(Screen):
    pass



class SearchCountryScreen(Screen):
    pass



class CanadaScreen(MDScreen):
    pass

class USAScreen(Screen):
    pass

class MexicoScreen(Screen):
    pass

class GuatemalaScreen(Screen):
    pass

class BelizeScreen(Screen):
    pass

class SalvadorScreen(Screen):
    pass

class HondurasScreen(Screen):
    pass

class NicaraguaScreen(Screen):
    pass

class CostaRicaScreen(Screen):
    pass

class PanamaScreen(Screen):
    pass

class TheBahamasScreen(Screen):
    pass

class CubaScreen(Screen):
    pass

class JamaicaScreen(Screen):
    pass

class HaitiScreen(Screen):
    pass

class DominicanRepublicScreen(Screen):
    pass

class SaintKittsandNevisScreen(Screen):
    pass

class AntiguaandBarbudaScreen(Screen):
    pass

class DominicaScreen(Screen):
    pass

class SaintLuciaScreen(Screen):
    pass

class SaintVincentandtheGrenadinesScreen(Screen):
    pass

class BarbadosScreen(Screen):
    pass

class GrenadaScreen(Screen):
    pass

class TrinidadandTobagoScreen(Screen):
    pass





class ColombiaScreen(Screen):
    pass

class VenezuelaScreen(Screen):
    pass

class GuyanaScreen(Screen):
    pass

class SurinameScreen(Screen):
    pass

class EcuadorScreen(Screen):
    pass

class PeruScreen(Screen):
    pass

class BrazilScreen(Screen):
    pass

class BoliviaScreen(Screen):
    pass

class ChileScreen(Screen):
    pass

class ArgentinaScreen(Screen):
    pass

class ParaguayScreen(Screen):
    pass

class UruguayScreen(Screen):
    pass





class PortugalScreen(Screen):
    pass

class SpainScreen(Screen):
    pass

class AndorraScreen(Screen):
    pass

class FranceScreen(Screen):
    pass

class UKScreen(Screen):
    pass

class IrelandScreen(Screen):
    pass

class IcelandScreen(Screen):
    pass

class NetherlandsScreen(Screen):
    pass

class BelgiumScreen(Screen):
    pass

class LuxembourgScreen(Screen):
    pass

class GermanyScreen(Screen):
    pass

class DenmarkScreen(Screen):
    pass

class SwitzerlandScreen(Screen):
    pass

class LiechtensteinScreen(Screen):
    pass

class AustriaScreen(Screen):
    pass

class ItalyScreen(Screen):
    pass

class VaticanScreen(Screen):
    pass

class SanMarinoScreen(Screen):
    pass

class MonacoScreen(Screen):
    pass

class MaltaScreen(Screen):
    pass

class GreeceScreen(Screen):
    pass

class NorwayScreen(Screen):
    pass

class SwedenScreen(Screen):
    pass

class FinlandScreen(Screen):
    pass

class EstoniaScreen(Screen):
    pass

class LatviaScreen(Screen):
    pass

class LithuaniaScreen(Screen):
    pass

class PolandScreen(Screen):
    pass

class BelarusScreen(Screen):
    pass

class CzechRepublicScreen(Screen):
    pass

class SlovakiaScreen(Screen):
    pass

class UkraineScreen(Screen):
    pass

class RussiaScreen(Screen):
    pass

class KazakhstanScreen(Screen):
    pass

class GeorgiaScreen(Screen):
    pass

class AzerbaijanScreen(Screen):
    pass

class SloveniaScreen(Screen):
    pass

class HungaryScreen(Screen):
    pass

class RomaniaScreen(Screen):
    pass

class MoldovaScreen(Screen):
    pass

class CroatiaScreen(Screen):
    pass

class BosniaAndHerzegovinaScreen(Screen):
    pass

class SerbiaScreen(Screen):
    pass

class MontenegroScreen(Screen):
    pass

class KosovoScreen(Screen):
    pass

class AlbaniaScreen(Screen):
    pass

class NorthMacedoniaScreen(Screen):
    pass

class BulgariaScreen(Screen):
    pass

class TurkeyScreen(Screen):
    pass



class ArmeniaScreen(Screen):
    pass

class CyprusScreen(Screen):
    pass

class IranScreen(Screen):
    pass

class IraqScreen(Screen):
    pass

class SyriaScreen(Screen):
    pass

class LebanonScreen(Screen):
    pass

class IsraelScreen(Screen):
    pass

class PalestineScreen(Screen):
    pass

class JordanScreen(Screen):
    pass

class SaudiArabiaScreen(Screen):
    pass

class KuwaitScreen(Screen):
    pass

class QatarScreen(Screen):
    pass

class BahrainScreen(Screen):
    pass

class UnitedArabEmiratesScreen(Screen):
    pass

class OmanScreen(Screen):
    pass

class YemenScreen(Screen):
    pass

class UzbekistanScreen(Screen):
    pass

class KyrgyzstanScreen(Screen):
    pass

class TurkmenistanScreen(Screen):
    pass

class TajikistanScreen(Screen):
    pass

class AfghanistanScreen(Screen):
    pass

class PakistanScreen(Screen):
    pass

class IndiaScreen(Screen):
    pass

class SriLankaScreen(Screen):
    pass

class MaldivesScreen(Screen):
    pass

class NepalScreen(Screen):
    pass

class BhutanScreen(Screen):
    pass

class BangladeshScreen(Screen):
    pass

class ChinaScreen(Screen):
    pass

class MongoliaScreen(Screen):
    pass

class NorthKoreaScreen(Screen):
    pass

class SouthKoreaScreen(Screen):
    pass

class JapanScreen(Screen):
    pass

class TaiwanScreen(Screen):
    pass

class MyanmarScreen(Screen):
    pass

class ThailandScreen(Screen):
    pass

class LaosScreen(Screen):
    pass

class VietnamScreen(Screen):
    pass

class CambodiaScreen(Screen):
    pass

class MalaysiaScreen(Screen):
    pass

class SingaporeScreen(Screen):
    pass

class PhilippinesScreen(Screen):
    pass

class BruneiScreen(Screen):
    pass

class EastTimorScreen(Screen):
    pass



class MoroccoScreen(Screen):
    pass

class AlgeriaScreen(Screen):
    pass

class TunisiaScreen(Screen):
    pass

class LibyaScreen(Screen):
    pass

class EgyptScreen(Screen):
    pass

class MauritaniaScreen(Screen):
    pass

class MaliScreen(Screen):
    pass

class NigerScreen(Screen):
    pass

class ChadScreen(Screen):
    pass

class SudanScreen(Screen):
    pass

class EritreaScreen(Screen):
    pass

class DjiboutiScreen(Screen):
    pass

class SenegalScreen(Screen):
    pass

class TheGambiaScreen(Screen):
    pass

class GuineaBissauScreen(Screen):
    pass

class GuineaScreen(Screen):
    pass

class SierraLeoneScreen(Screen):
    pass

class LiberiaScreen(Screen):
    pass

class IvoryCoastScreen(Screen):
    pass

class BurkinaFasoScreen(Screen):
    pass

class GhanaScreen(Screen):
    pass

class TogoScreen(Screen):
    pass

class BeninScreen(Screen):
    pass

class NigeriaScreen(Screen):
    pass

class CameroonScreen(Screen):
    pass

class CentralAfricanRepublicScreen(Screen):
    pass

class SouthSudanScreen(Screen):
    pass

class EthiopiaScreen(Screen):
    pass

class SomaliaScreen(Screen):
    pass

class EquatorialGuineaScreen(Screen):
    pass

class GabonScreen(Screen):
    pass

class RepublicoftheCongoScreen(Screen):
    pass

class DemocraticRepublicoftheCongoScreen(Screen):
    pass

class RwandaScreen(Screen):
    pass

class BurundiScreen(Screen):
    pass

class UgandaScreen(Screen):
    pass

class KenyaScreen(Screen):
    pass

class AngolaScreen(Screen):
    pass

class ZambiaScreen(Screen):
    pass

class MalawiScreen(Screen):
    pass

class MozambiqueScreen(Screen):
    pass

class MadagascarScreen(Screen):
    pass

class NamibiaScreen(Screen):
    pass

class BotswanaScreen(Screen):
    pass

class ZimbabweScreen(Screen):
    pass

class RepublicofSouthAfricaScreen(Screen):
    pass

class EswatiniScreen(Screen):
    pass

class LesothoScreen(Screen):
    pass

class SeychellesScreen(Screen):
    pass

class MauritiusScreen(Screen):
    pass

class ComorosScreen(Screen):
    pass

class SaoTomeandPrincipeScreen(Screen):
    pass

class CapeVerdeScreen(Screen):
    pass





class AustraliaScreen(Screen):
    pass

class NewZealandScreen(Screen):
    pass

class IndonesiaScreen(Screen):
    pass

class PapuaNewGuineaScreen(Screen):
    pass

class SolomonIslandsScreen(Screen):
    pass

class VanuatuScreen(Screen):
    pass

class FijiScreen(Screen):
    pass

class TongaScreen(Screen):
    pass

class SamoaScreen(Screen):
    pass

class TuvaluScreen(Screen):
    pass

class KiribatiScreen(Screen):
    pass

class NauruScreen(Screen):
    pass

class MarshallIslandsScreen(Screen):
    pass

class MicronesiaScreen(Screen):
    pass

class PalauScreen(Screen):
    pass


class WorldCountries(MDApp):

    past_page = "main"
    sp = None
    search_screen = SearchCountryScreen(name = "SearchCountryScreen")


    sm = ScreenManager()
    sm.add_widget(MainScreen(name = "main"))
    sm.add_widget(NorthAmericaScreen(name = "North America"))
    sm.add_widget(SouthAmericaScreen(name = "South America"))
    sm.add_widget(EuropeScreen(name = "Europe"))
    sm.add_widget(AsiaScreen(name = "Asia"))
    sm.add_widget(AfricaScreen(name = "Africa"))
    sm.add_widget(AustraliaandOceaniaScreen(name = "Australia and Oceania"))
    sm.add_widget(search_screen)


    sm.add_widget(CanadaScreen(name = "Canada"))
    sm.add_widget(USAScreen(name = "USA"))
    sm.add_widget(MexicoScreen(name = "Mexico"))
    sm.add_widget(GuatemalaScreen(name = "Guatemala"))
    sm.add_widget(BelizeScreen(name = "Belize"))
    sm.add_widget(SalvadorScreen(name = "El Salvador"))
    sm.add_widget(HondurasScreen(name = "Honduras"))
    sm.add_widget(NicaraguaScreen(name = "Nicaragua"))
    sm.add_widget(CostaRicaScreen(name = "Costa Rica"))
    sm.add_widget(PanamaScreen(name = "Panama"))
    sm.add_widget(TheBahamasScreen(name = "The Bahamas"))
    sm.add_widget(CubaScreen(name = "Cuba"))
    sm.add_widget(JamaicaScreen(name = "Jamaica"))
    sm.add_widget(HaitiScreen(name = "Haiti"))
    sm.add_widget(DominicanRepublicScreen(name = "Dominican Republic"))
    sm.add_widget(SaintKittsandNevisScreen(name = "Saint Kitts and Nevis"))
    sm.add_widget(AntiguaandBarbudaScreen(name = "Antigua and Barbuda"))
    sm.add_widget(DominicaScreen(name = "Dominica"))
    sm.add_widget(SaintLuciaScreen(name = "Saint Lucia"))
    sm.add_widget(SaintVincentandtheGrenadinesScreen(name = "Saint Vincent and the Grenadines"))
    sm.add_widget(BarbadosScreen(name = "Barbados"))
    sm.add_widget(GrenadaScreen(name = "Grenada"))
    sm.add_widget(TrinidadandTobagoScreen(name = "TrinidadandTobago"))


    sm.add_widget(ColombiaScreen(name = "Colombia"))
    sm.add_widget(VenezuelaScreen(name = "Venezuela"))
    sm.add_widget(GuyanaScreen(name = "Guyana"))
    sm.add_widget(SurinameScreen(name = "Suriname"))
    sm.add_widget(EcuadorScreen(name = "Ecuador"))
    sm.add_widget(PeruScreen(name = "Peru"))
    sm.add_widget(BrazilScreen(name = "Brazil"))
    sm.add_widget(BoliviaScreen(name = "Bolivia"))
    sm.add_widget(ChileScreen(name = "Chile"))
    sm.add_widget(ArgentinaScreen(name = "Argentina"))
    sm.add_widget(ParaguayScreen(name = "Paraguay"))
    sm.add_widget(UruguayScreen(name = "Chile"))


    sm.add_widget(PortugalScreen(name = "Portugal"))
    sm.add_widget(SpainScreen(name = "Spain"))
    sm.add_widget(AndorraScreen(name = "Andorra"))
    sm.add_widget(FranceScreen(name = "France"))
    sm.add_widget(UKScreen(name = "UK"))
    sm.add_widget(IrelandScreen(name = "Ireland"))
    sm.add_widget(IcelandScreen(name = "Iceland"))
    sm.add_widget(NetherlandsScreen(name = "Netherlands"))
    sm.add_widget(BelgiumScreen(name = "Belgium"))
    sm.add_widget(LuxembourgScreen(name = "Luxembourg"))
    sm.add_widget(GermanyScreen(name = "Germany"))
    sm.add_widget(DenmarkScreen(name = "Denmark"))
    sm.add_widget(SwitzerlandScreen(name = "Switzerland"))
    sm.add_widget(LiechtensteinScreen(name = "Liechtenstein"))
    sm.add_widget(AustriaScreen(name = "Austria"))
    sm.add_widget(ItalyScreen(name = "Italy"))
    sm.add_widget(VaticanScreen(name = "Vatican"))
    sm.add_widget(SanMarinoScreen(name = "San Marino"))
    sm.add_widget(MonacoScreen(name = "Monaco"))
    sm.add_widget(MaltaScreen(name = "Malta"))
    sm.add_widget(GreeceScreen(name = "Greece"))
    sm.add_widget(NorwayScreen(name = "Norway"))
    sm.add_widget(SwedenScreen(name = "Sweden"))
    sm.add_widget(FinlandScreen(name = "Finland"))
    sm.add_widget(EstoniaScreen(name = "Estonia"))
    sm.add_widget(LatviaScreen(name = "Latvia"))
    sm.add_widget(LithuaniaScreen(name = "Lithuania"))
    sm.add_widget(PolandScreen(name = "Poland"))
    sm.add_widget(BelarusScreen(name = "Belarus"))
    sm.add_widget(CzechRepublicScreen(name = "Czech Republic"))
    sm.add_widget(SlovakiaScreen(name = "Slovakia"))
    sm.add_widget(UkraineScreen(name = "Ukraine"))
    sm.add_widget(RussiaScreen(name = "Russia"))
    sm.add_widget(KazakhstanScreen(name = "Kazakhstan"))
    sm.add_widget(GeorgiaScreen(name = "Georgia"))
    sm.add_widget(AzerbaijanScreen(name = "Azerbaijan"))
    sm.add_widget(SloveniaScreen(name = "Slovenia"))
    sm.add_widget(HungaryScreen(name = "Hungary"))
    sm.add_widget(RomaniaScreen(name = "Romania"))
    sm.add_widget(MoldovaScreen(name = "Moldova"))
    sm.add_widget(CroatiaScreen(name = "Croatia"))
    sm.add_widget(BosniaAndHerzegovinaScreen(name = "Bosnia And Herzegovina"))
    sm.add_widget(SerbiaScreen(name = "Serbia"))
    sm.add_widget(KiribatiScreen(name = "Kiribati"))
    sm.add_widget(MontenegroScreen(name = "Montenegro"))
    sm.add_widget(KosovoScreen(name = "Kosovo"))
    sm.add_widget(NorthMacedoniaScreen(name = "North Macedonia"))
    sm.add_widget(BulgariaScreen(name = "Bulgaria"))
    sm.add_widget(TurkeyScreen(name = "TurkeyScreen"))


    sm.add_widget(ArmeniaScreen(name = "Armenia"))
    sm.add_widget(CyprusScreen(name = "Cyprus"))
    sm.add_widget(IranScreen(name = "Iran"))
    sm.add_widget(IraqScreen(name = "Iraq"))
    sm.add_widget(SyriaScreen(name = "Syria"))
    sm.add_widget(LebanonScreen(name = "Lebanon"))
    sm.add_widget(IsraelScreen(name = "Israel"))
    sm.add_widget(PalestineScreen(name = "Palestine"))
    sm.add_widget(JordanScreen(name = "Jordan"))
    sm.add_widget(SaudiArabiaScreen(name = "Saudi Arabia"))
    sm.add_widget(KuwaitScreen(name = "Kuwait"))
    sm.add_widget(QatarScreen(name = "Qatar"))
    sm.add_widget(BahrainScreen(name = "Bahrain"))
    sm.add_widget(UnitedArabEmiratesScreen(name = "United Arab Emirates"))
    sm.add_widget(OmanScreen(name = "Oman"))
    sm.add_widget(YemenScreen(name = "Yemen"))
    sm.add_widget(UzbekistanScreen(name = "Uzbekistan"))
    sm.add_widget(KyrgyzstanScreen(name = "Kyrgyzstan"))
    sm.add_widget(TurkmenistanScreen(name = "Turkmenistan"))
    sm.add_widget(TajikistanScreen(name = "Tajikistan"))
    sm.add_widget(AfghanistanScreen(name = "Afghanistan"))
    sm.add_widget(PakistanScreen(name = "Pakistan"))
    sm.add_widget(IndiaScreen(name = "India"))
    sm.add_widget(SriLankaScreen(name = "Sri Lanka"))
    sm.add_widget(MaldivesScreen(name = "Maldives"))
    sm.add_widget(NepalScreen(name = "Nepal"))
    sm.add_widget(BhutanScreen(name = "Bhutan"))
    sm.add_widget(BangladeshScreen(name = "Bangladesh"))
    sm.add_widget(ChinaScreen(name = "China"))
    sm.add_widget(MongoliaScreen(name = "Mongolia"))
    sm.add_widget(NorthKoreaScreen(name = "NorthKorea"))
    sm.add_widget(SouthKoreaScreen(name = "SouthKorea"))
    sm.add_widget(JapanScreen(name = "Japan"))
    sm.add_widget(TaiwanScreen(name = "Taiwan"))
    sm.add_widget(MyanmarScreen(name = "Myanmar"))
    sm.add_widget(ThailandScreen(name = "Thailand"))
    sm.add_widget(LaosScreen(name = "Laos"))
    sm.add_widget(VietnamScreen(name = "Vietnam"))
    sm.add_widget(CambodiaScreen(name = "Cambodia"))
    sm.add_widget(MalaysiaScreen(name = "Malaysia"))
    sm.add_widget(SingaporeScreen(name = "Singapore"))
    sm.add_widget(PhilippinesScreen(name = "Philippines"))
    sm.add_widget(BruneiScreen(name = "Brunei"))
    sm.add_widget(EastTimorScreen(name = "Malaysia"))


    sm.add_widget(MoroccoScreen(name = "Morocco"))
    sm.add_widget(AlgeriaScreen(name = "Algeria"))
    sm.add_widget(TunisiaScreen(name = "Tunisia"))
    sm.add_widget(LibyaScreen(name = "Libya"))
    sm.add_widget(EgyptScreen(name = "Egypt"))
    sm.add_widget(MauritaniaScreen(name = "Mauritania"))
    sm.add_widget(MaliScreen(name = "Mali"))
    sm.add_widget(NigerScreen(name = "Niger"))
    sm.add_widget(ChadScreen(name = "Chad"))
    sm.add_widget(LebanonScreen(name = "Lebanon"))
    sm.add_widget(SudanScreen(name = "Sudan"))
    sm.add_widget(EritreaScreen(name = "Eritrea"))
    sm.add_widget(DjiboutiScreen(name = "Djibouti"))
    sm.add_widget(SenegalScreen(name = "Senegal"))
    sm.add_widget(TheGambiaScreen(name = "The Gambia"))
    sm.add_widget(GuineaBissauScreen(name = "Guinea Bissau"))
    sm.add_widget(GuineaScreen(name = "Guinea"))
    sm.add_widget(SierraLeoneScreen(name = "Sierra Leone"))
    sm.add_widget(LiberiaScreen(name = "Liberia"))
    sm.add_widget(IvoryCoastScreen(name = "Ivory Coast"))
    sm.add_widget(BurkinaFasoScreen(name = "Burkina Faso"))
    sm.add_widget(GhanaScreen(name = "Ghana"))
    sm.add_widget(TogoScreen(name = "Togo"))
    sm.add_widget(BeninScreen(name = "Benin"))
    sm.add_widget(NigeriaScreen(name = "Nigeria"))
    sm.add_widget(CameroonScreen(name = "Cameroon"))
    sm.add_widget(CentralAfricanRepublicScreen(name = "Central African Republic"))
    sm.add_widget(SouthSudanScreen(name = "South Sudan"))
    sm.add_widget(EthiopiaScreen(name = "Ethiopia"))
    sm.add_widget(SomaliaScreen(name = "Somalia"))
    sm.add_widget(EquatorialGuineaScreen(name = "Equatorial Guinea"))
    sm.add_widget(RepublicoftheCongoScreen(name = "Republic of the Congo"))
    sm.add_widget(DemocraticRepublicoftheCongoScreen(name = "Democratic Republic of the Congo"))
    sm.add_widget(RwandaScreen(name = "Rwanda"))
    sm.add_widget(BurundiScreen(name = "Burundi"))
    sm.add_widget(UgandaScreen(name = "Uganda"))
    sm.add_widget(KenyaScreen(name = "Kenya"))
    sm.add_widget(AngolaScreen(name = "Angola"))
    sm.add_widget(ZambiaScreen(name = "Zambia"))
    sm.add_widget(MalawiScreen(name = "Malawi"))
    sm.add_widget(MozambiqueScreen(name = "Mozambique"))
    sm.add_widget(MadagascarScreen(name = "Madagascar"))
    sm.add_widget(NamibiaScreen(name = "Namibia"))
    sm.add_widget(BotswanaScreen(name = "Botswana"))
    sm.add_widget(ZimbabweScreen(name = "Zimbabwe"))
    sm.add_widget(MalaysiaScreen(name = "Malaysia"))
    sm.add_widget(RepublicofSouthAfricaScreen(name = "Republic of South Africa"))
    sm.add_widget(LesothoScreen(name = "Lesotho"))
    sm.add_widget(SeychellesScreen(name = "Seychelles"))
    sm.add_widget(ComorosScreen(name = "Comoros"))
    sm.add_widget(SaoTomeandPrincipeScreen(name = "Sao Tome and Principe"))
    sm.add_widget(CapeVerdeScreen(name = "CapeVerde"))


    sm.add_widget(AustraliaScreen(name = "Australia"))
    sm.add_widget(NewZealandScreen(name = "New Zealand"))
    sm.add_widget(IndonesiaScreen(name = "Indonesia"))
    sm.add_widget(PapuaNewGuineaScreen(name = "Papua New Guinea"))
    sm.add_widget(SolomonIslandsScreen(name = "Solomon Islands"))
    sm.add_widget(VanuatuScreen(name = "Vanuatu"))
    sm.add_widget(FijiScreen(name = "Fiji"))
    sm.add_widget(TongaScreen(name = "Tonga"))
    sm.add_widget(SamoaScreen(name = "Samoa"))
    sm.add_widget(TuvaluScreen(name = "Tuvalu"))
    sm.add_widget(KiribatiScreen(name = "Kiribati"))
    sm.add_widget(NauruScreen(name = "Nauru"))
    sm.add_widget(MarshallIslandsScreen(name = "Marshall Islands"))
    sm.add_widget(MicronesiaScreen(name = "Micronesia"))
    sm.add_widget(PalauScreen(name = "Palau"))

    
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.screen = Builder.load_string(navigation_helper)
        return self.screen


    def search(self, text):
        North_America = [x.text[:x.text.find("  ")] for x in list(self.root.ids.NA.ids.values())[:-1]]
        North_America_dict = dict(zip(North_America, list(self.root.ids.NA.ids.values())))
        South_America = [x.text[:x.text.find("  ")] for x in list(self.root.ids.SA.ids.values())[:-1]]
        South_America_dict = dict(zip(South_America, list(self.root.ids.SA.ids.values())))
        Europe = [x.text[:x.text.find("  ")] for x in list(self.root.ids.Eu.ids.values())[:-1]]
        Europe_dict = dict(zip(Europe, list(self.root.ids.Eu.ids.values())))
        Asia = [x.text[:x.text.find("  ")] for x in list(self.root.ids.As.ids.values())[:-1]]
        Asia_dict = dict(zip(Asia, list(self.root.ids.As.ids.values())))
        Africa = [x.text[:x.text.find("  ")] for x in list(self.root.ids.Af.ids.values())[:-1]]
        Africa_dict = dict(zip(Africa, list(self.root.ids.Af.ids.values())))
        AaO = [x.text[:x.text.find("  ")] for x in list(self.root.ids.AAO.ids.values())[:-1]]
        AaO_dict = dict(zip(AaO, list(self.root.ids.AAO.ids.values())))
        all = {}
        all.update(North_America_dict)
        all.update(South_America_dict)
        all.update(Europe_dict)
        all.update(Asia_dict)
        all.update(Africa_dict)
        all.update(AaO_dict)
        all_keys = list(all.keys())
        added_items = []
        for i in all_keys:
            if text in i :
                item = OneLineAvatarListItem(text = all[i].text, on_release = self.change_screen)
                added_items.append(item)
        for i in added_items:
            if text not in i.text:
                print(text,i.text)
                added_items.remove(i)
        self.root.ids.search.ids.container.clear_widgets()
        for i in added_items:
            self.root.ids.search.ids.container.add_widget(i)
        if text == "":
            self.root.ids.search.ids.container.clear_widgets()
                

    def remove_char_from_TF(self, obj):
        self.root.current = self.past_page
        self.root.ids.search.ids.TextField.text = ""


    def change_screen(self, obj):
        if self.root.current != "SearchCountryScreen":
            self.past_page = self.root.current
            self.root.current = obj.text[:obj.text.find("  ")]
        else:
            self.sp = True
            self.root.current = obj.text[:obj.text.find("  ")]

    
WorldCountries().run()
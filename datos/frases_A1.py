# update_examples_A1.py

import sqlite3

conn = sqlite3.connect("aleman.db")
cursor = conn.cursor()

ejemplos = [

    (
	 "Haus",
	 "Das Haus ist sehr groß.",
	 "La casa es muy grande."
    ),

    (
	 "Mann",
	 "Der Mann arbeitet in Madrid.",
	 "El hombre trabaja en Madrid."
    ),

    (
	 "Frau",
	 "Die Frau spricht Deutsch.",
	 "La mujer habla alemán."
    ),

    (
	 "Kind",
	 "Das Kind spielt im Park.",
	 "El niño juega en el parque."
    ),

    (
	 "Auto",
	 "Mein Auto ist neu.",
	 "Mi coche es nuevo."
    ),

    (
	 "Wasser",
	 "Ich trinke jeden Tag Wasser.",
	 "Bebo agua todos los días."
    ),

    (
	 "Kaffee",
	 "Morgens trinke ich Kaffee.",
	 "Por las mañanas tomo café."
    ),

    (
	 "Baum",
	 "Der Baum ist sehr hoch.",
	 "El árbol es muy alto."
    ),

    (
	 "gehen",
	 "Ich gehe zur Arbeit.",
	 "Voy al trabajo."
    ),

    (
	 "kommen",
	 "Kommst du heute?",
	 "¿Vienes hoy?"
    ),

    (
	 "lernen",
	 "Ich lerne Deutsch.",
	 "Aprendo alemán."
    ),

    (
	 "arbeiten",
	 "Ich arbeite in einer Firma.",
	 "Trabajo en una empresa."
    ),

    (
	 "essen",
	 "Wir essen Pizza.",
	 "Comemos pizza."
    ),

    (
	 "trinken",
	 "Er trinkt Tee.",
	 "Él bebe té."
    ),

    (
	 "sprechen",
	 "Sie spricht sehr gut Deutsch.",
	 "Ella habla alemán muy bien."
    ),

    (
	 "groß",
	 "Mein Haus ist groß.",
	 "Mi casa es grande."
    ),

    (
	 "klein",
	 "Das Zimmer ist klein.",
	 "La habitación es pequeña."
    ),

    (
	 "gut",
	 "Das ist eine gute Idee.",
	 "Es una buena idea."
    ),

    (
	 "schlecht",
	 "Heute ist das Wetter schlecht.",
	 "Hoy hace mal tiempo."
    ),

    (
	 "wichtig",
	 "Deutsch ist wichtig für meinen Beruf.",
	 "El alemán es importante para mi profesión."
    ),

    ("Familie",
     "Meine Familie lebt in Spanien.",
     "Mi familia vive en España."),

    ("Vater",
     "Mein Vater arbeitet im Büro.",
     "Mi padre trabaja en la oficina."),

    ("Mutter",
     "Meine Mutter kocht sehr gut.",
     "Mi madre cocina muy bien."),

    ("Bruder",
     "Mein Bruder spielt Fußball.",
     "Mi hermano juega al fútbol."),

    ("Schwester",
     "Meine Schwester lernt Deutsch.",
     "Mi hermana aprende alemán."),

    ("Freund",
     "Mein Freund wohnt in Berlin.",
     "Mi amigo vive en Berlín."),

    ("Freundin",
     "Meine Freundin reist gern.",
     "A mi amiga le gusta viajar."),

    ("Zimmer",
     "Das Zimmer ist sauber.",
     "La habitación está limpia."),

    ("Küche",
     "Die Küche ist modern.",
     "La cocina es moderna."),

    ("Fenster",
     "Bitte öffne das Fenster.",
     "Por favor abre la ventana."),

    ("Tür",
     "Die Tür ist geschlossen.",
     "La puerta está cerrada."),

    ("Tisch",
     "Das Buch liegt auf dem Tisch.",
     "El libro está sobre la mesa."),

    ("Stuhl",
     "Der Stuhl ist sehr bequem.",
     "La silla es muy cómoda."),

    ("Bett",
     "Ich gehe ins Bett.",
     "Me voy a la cama."),

    ("Buch",
     "Ich lese ein interessantes Buch.",
     "Leo un libro interesante."),

    ("Schule",
     "Die Schule beginnt um acht Uhr.",
     "La escuela empieza a las ocho."),

    ("Lehrer",
     "Der Lehrer erklärt die Aufgabe.",
     "El profesor explica el ejercicio."),

    ("Student",
     "Der Student lernt jeden Tag.",
     "El estudiante estudia todos los días."),

    ("Frage",
     "Ich habe eine Frage.",
     "Tengo una pregunta."),

    ("Antwort",
     "Die Antwort ist richtig.",
     "La respuesta es correcta."),

    ("Arbeit",
     "Meine Arbeit macht mir Spaß.",
     "Mi trabajo me gusta."),

    ("Firma",
     "Die Firma wächst schnell.",
     "La empresa crece rápido."),

    ("Chef",
     "Mein Chef ist freundlich.",
     "Mi jefe es amable."),

    ("Kollege",
     "Mein Kollege spricht Englisch.",
     "Mi compañero habla inglés."),

    ("Computer",
     "Der Computer funktioniert gut.",
     "El ordenador funciona bien."),

    ("Telefon",
     "Das Telefon klingelt.",
     "El teléfono está sonando."),

    ("Zug",
     "Der Zug kommt pünktlich an.",
     "El tren llega puntual."),

    ("Bahnhof",
     "Wir treffen uns am Bahnhof.",
     "Nos encontramos en la estación."),

    ("Flugzeug",
     "Das Flugzeug landet jetzt.",
     "El avión aterriza ahora."),

    ("Reise",
     "Die Reise war sehr interessant.",
     "El viaje fue muy interesante."),

    ("Stadt",
     "Die Stadt ist sehr groß.",
     "La ciudad es muy grande."),

    ("Land",
     "Deutschland ist ein schönes Land.",
     "Alemania es un país bonito."),

    ("Park",
     "Die Kinder spielen im Park.",
     "Los niños juegan en el parque."),

    ("Hund",
     "Der Hund schläft auf dem Sofa.",
     "El perro duerme en el sofá."),

    ("Katze",
     "Die Katze trinkt Milch.",
     "El gato bebe leche."),

    ("Vogel",
     "Der Vogel sitzt auf dem Baum.",
     "El pájaro está en el árbol."),

    ("Blume",
     "Die Blume ist rot.",
     "La flor es roja."),

    ("Tag",
     "Heute ist ein schöner Tag.",
     "Hoy es un día bonito."),

    ("Woche",
     "Die Woche war lang.",
     "La semana fue larga."),

    ("Jahr",
     "Dieses Jahr lerne ich Deutsch.",
     "Este año aprendo alemán."),

    ("Morgen",
     "Morgen fahre ich nach Madrid.",
     "Mañana voy a Madrid."),

    ("Abend",
     "Am Abend sehe ich fern.",
     "Por la tarde veo la televisión."),

    ("Nacht",
     "In der Nacht ist es ruhig.",
     "Por la noche está tranquilo."),

    ("Apfel",
     "Der Apfel schmeckt gut.",
     "La manzana sabe bien."),

    ("Banane",
     "Ich esse eine Banane.",
     "Me como un plátano."),

    ("Brot",
     "Zum Frühstück esse ich Brot.",
     "Para desayunar como pan."),

    ("Milch",
     "Die Milch ist frisch.",
     "La leche está fresca."),

    ("Wasser",
     "Bitte ein Glas Wasser.",
     "Por favor, un vaso de agua."),

    ("Kaffee",
     "Ich trinke morgens Kaffee.",
     "Tomo café por las mañanas."),

    ("gehen",
     "Wir gehen heute spazieren.",
     "Hoy vamos a pasear."),

    ("kommen",
     "Wann kommst du nach Hause?",
     "¿Cuándo vienes a casa?"),

    ("machen",
     "Was machst du heute?",
     "¿Qué haces hoy?"),

    ("lernen",
     "Ich lerne Deutsch jeden Abend.",
     "Aprendo alemán cada tarde."),

    ("arbeiten",
     "Er arbeitet in einer Fabrik.",
     "Él trabaja en una fábrica."),

    ("essen",
     "Wir essen zusammen zu Mittag.",
     "Comemos juntos al mediodía."),

    ("trinken",
     "Sie trinkt einen Tee.",
     "Ella toma un té."),

    ("schlafen",
     "Das Baby schläft tief.",
     "El bebé duerme profundamente."),

    ("sprechen",
     "Sprichst du Deutsch?",
     "¿Hablas alemán?"),

    ("sehen",
     "Ich sehe einen Hund.",
     "Veo un perro."),

    ("groß",
     "Das Haus ist groß.",
     "La casa es grande."),

    ("klein",
     "Der Garten ist klein.",
     "El jardín es pequeño."),

    ("neu",
     "Mein Auto ist neu.",
     "Mi coche es nuevo."),

    ("alt",
     "Das Gebäude ist alt.",
     "El edificio es antiguo."),

    ("schnell",
     "Der Zug ist sehr schnell.",
     "El tren es muy rápido."),

    ("langsam",
     "Der Bus fährt langsam.",
     "El autobús va despacio."),

    ("schön",
     "Das Wetter ist schön.",
     "Hace buen tiempo."),

    ("teuer",
     "Das Hotel ist teuer.",
     "El hotel es caro."),

    ("Wohnung",
     "Die Wohnung ist im Stadtzentrum.",
     "El apartamento está en el centro de la ciudad."),

    ("Badezimmer",
     "Das Badezimmer ist sauber.",
     "El baño está limpio."),

    ("Lampe",
     "Die Lampe steht auf dem Tisch.",
     "La lámpara está sobre la mesa."),

    ("Straße",
     "Die Straße ist sehr lang.",
     "La calle es muy larga."),

    ("Hotel",
     "Wir schlafen heute im Hotel.",
     "Dormimos hoy en el hotel."),

    ("Restaurant",
     "Das Restaurant ist voll.",
     "El restaurante está lleno."),

    ("Supermarkt",
     "Ich gehe in den Supermarkt.",
     "Voy al supermercado."),

    ("Bank",
     "Die Bank öffnet um neun Uhr.",
     "El banco abre a las nueve."),

    ("Kirche",
     "Die Kirche ist alt.",
     "La iglesia es antigua."),

    ("Heft",
     "Das Heft liegt im Rucksack.",
     "El cuaderno está en la mochila."),

    ("Stift",
     "Der Stift ist blau.",
     "El bolígrafo es azul."),

    ("Sprache",
     "Deutsch ist eine interessante Sprache.",
     "El alemán es un idioma interesante."),

    ("Beruf",
     "Mein Beruf gefällt mir.",
     "Mi profesión me gusta."),

    ("Pause",
     "Wir machen eine Pause.",
     "Hacemos una pausa."),

    ("E-Mail",
     "Ich schreibe eine E-Mail.",
     "Escribo un correo electrónico."),

    ("Fahrrad",
     "Mein Fahrrad ist rot.",
     "Mi bicicleta es roja."),

    ("Flughafen",
     "Der Flughafen ist sehr groß.",
     "El aeropuerto es muy grande."),

    ("Ticket",
     "Ich kaufe ein Ticket.",
     "Compro un billete."),

    ("Meer",
     "Das Meer ist heute ruhig.",
     "El mar está tranquilo hoy."),

    ("Berg",
     "Der Berg ist hoch.",
     "La montaña es alta."),

    ("Sonne",
     "Die Sonne scheint.",
     "Hace sol."),

    ("Mond",
     "Der Mond ist heute hell.",
     "La luna brilla esta noche."),

    ("Himmel",
     "Der Himmel ist blau.",
     "El cielo es azul."),

    ("Stunde",
     "Die Stunde beginnt jetzt.",
     "La hora empieza ahora."),

    ("Minute",
     "Warte eine Minute.",
     "Espera un minuto."),

    ("Uhr",
     "Die Uhr zeigt zehn Uhr.",
     "El reloj marca las diez."),

    ("Hemd",
     "Das Hemd ist weiß.",
     "La camisa es blanca."),

    ("Hose",
     "Die Hose ist neu.",
     "El pantalón es nuevo."),

    ("Jacke",
     "Ich brauche eine Jacke.",
     "Necesito una chaqueta."),

    ("Schuh",
     "Der Schuh ist bequem.",
     "El zapato es cómodo."),

    ("Kleid",
     "Das Kleid gefällt mir.",
     "El vestido me gusta."),

    ("Tasche",
     "Meine Tasche ist schwer.",
     "Mi bolso pesa mucho."),

    ("Mantel",
     "Im Winter trage ich einen Mantel.",
     "En invierno llevo abrigo."),

    ("Pullover",
     "Der Pullover ist warm.",
     "El jersey es cálido."),

    ("rot",
     "Mein Auto ist rot.",
     "Mi coche es rojo."),

    ("blau",
     "Der Himmel ist blau.",
     "El cielo es azul."),

    ("grün",
     "Das Gras ist grün.",
     "La hierba es verde."),

    ("gelb",
     "Die Banane ist gelb.",
     "El plátano es amarillo."),

    ("schwarz",
     "Mein Hund ist schwarz.",
     "Mi perro es negro."),

    ("weiß",
     "Die Wand ist weiß.",
     "La pared es blanca."),

    ("freundlich",
     "Der Verkäufer ist freundlich.",
     "El vendedor es amable."),

    ("interessant",
     "Das Buch ist interessant.",
     "El libro es interesante."),

    ("gesund",
     "Obst ist gesund.",
     "La fruta es saludable."),

    ("krank",
     "Heute bin ich krank.",
     "Hoy estoy enfermo."),

    ("warm",
     "Das Wasser ist warm.",
     "El agua está caliente."),

    ("kalt",
     "Der Kaffee ist kalt.",
     "El café está frío."),

    ("stark",
     "Der Wind ist stark.",
     "El viento es fuerte."),

    ("leicht",
     "Die Prüfung war leicht.",
     "El examen fue fácil."),

    ("schwer",
     "Die Aufgabe ist schwer.",
     "El ejercicio es difícil."),

    ("immer",
     "Ich trinke immer Kaffee.",
     "Siempre tomo café."),

    ("nie",
     "Ich komme nie zu spät.",
     "Nunca llego tarde."),

    ("oft",
     "Wir gehen oft spazieren.",
     "Vamos a pasear a menudo."),

    ("manchmal",
     "Manchmal lese ich ein Buch.",
     "A veces leo un libro."),

    ("heute",
     "Heute habe ich frei.",
     "Hoy tengo libre."),

    ("gestern",
     "Gestern war ich müde.",
     "Ayer estaba cansado."),

    ("morgen",
     "Morgen arbeite ich von zu Hause.",
     "Mañana trabajaré desde casa."),

    ("jetzt",
     "Jetzt habe ich Zeit.",
     "Ahora tengo tiempo."),

    ("früh",
     "Ich stehe früh auf.",
     "Me levanto temprano."),

    ("spät",
     "Heute komme ich spät nach Hause.",
     "Hoy llego tarde a casa.")

]

for palabra, ejemplo_de, ejemplo_es in ejemplos:

    cursor.execute("""
    UPDATE vocabulario
    SET ejemplo_de = ?,
        ejemplo_es = ?
    WHERE palabra = ?
    """, (
        ejemplo_de,
        ejemplo_es,
        palabra
    ))

conn.commit()
conn.close()

print(
    f"{len(ejemplos)} ejemplos actualizados"
)
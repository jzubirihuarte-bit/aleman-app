# update_examples_A2.py

import sqlite3

conn = sqlite3.connect("aleman.db")
cursor = conn.cursor()

ejemplos_a2 = [

    ("Erfahrung",
     "Ich habe viel Erfahrung in diesem Bereich.",
     "Tengo mucha experiencia en este campo."),

    ("Bewerbung",
     "Ich habe gestern eine Bewerbung geschickt.",
     "Ayer envié una solicitud de empleo."),

    ("Lebenslauf",
     "Mein Lebenslauf ist auf Deutsch geschrieben.",
     "Mi currículum está escrito en alemán."),

    ("Gehalt",
     "Das Gehalt ist höher als erwartet.",
     "El salario es más alto de lo esperado."),

    ("Besprechung",
     "Die Besprechung beginnt um zehn Uhr.",
     "La reunión empieza a las diez."),

    ("Projekt",
     "Das Projekt dauert sechs Monate.",
     "El proyecto dura seis meses."),

    ("Vertrag",
     "Ich habe den Vertrag bereits unterschrieben.",
     "Ya he firmado el contrato."),

    ("Miete",
     "Die Miete ist in dieser Stadt sehr teuer.",
     "El alquiler es muy caro en esta ciudad."),

    ("Nachbar",
     "Meine Nachbarn sind sehr freundlich.",
     "Mis vecinos son muy amables."),

    ("Balkon",
     "Wir frühstücken oft auf dem Balkon.",
     "A menudo desayunamos en el balcón."),

    ("Ausland",
     "Nächstes Jahr möchte ich im Ausland arbeiten.",
     "El próximo año quiero trabajar en el extranjero."),

    ("Grenze",
     "Die Grenze ist nur zehn Kilometer entfernt.",
     "La frontera está a solo diez kilómetros."),

    ("Reiseführer",
     "Der Reiseführer kennt die Stadt sehr gut.",
     "El guía turístico conoce muy bien la ciudad."),

    ("Verspätung",
     "Der Zug hat zwanzig Minuten Verspätung.",
     "El tren tiene veinte minutos de retraso."),

    ("Ankunft",
     "Die Ankunft ist für 18 Uhr geplant.",
     "La llegada está prevista para las 18:00."),

    ("Rabatt",
     "Heute gibt es zehn Prozent Rabatt.",
     "Hoy hay un diez por ciento de descuento."),

    ("Kreditkarte",
     "Kann ich mit Kreditkarte bezahlen?",
     "¿Puedo pagar con tarjeta de crédito?"),

    ("Bestellung",
     "Ihre Bestellung wurde bereits versendet.",
     "Su pedido ya ha sido enviado."),

    ("Versicherung",
     "Eine gute Versicherung ist sehr wichtig.",
     "Un buen seguro es muy importante."),

    ("Gesundheit",
     "Gesundheit ist wichtiger als Geld.",
     "La salud es más importante que el dinero."),

    ("Unfall",
     "Zum Glück war der Unfall nicht schwer.",
     "Por suerte el accidente no fue grave."),

    ("Behandlung",
     "Die Behandlung dauert zwei Wochen.",
     "El tratamiento dura dos semanas."),

    ("Prüfung",
     "Morgen habe ich eine wichtige Prüfung.",
     "Mañana tengo un examen importante."),

    ("Universität",
     "Die Universität liegt im Stadtzentrum.",
     "La universidad está en el centro de la ciudad."),

    ("Zertifikat",
     "Nach dem Kurs bekomme ich ein Zertifikat.",
     "Después del curso recibiré un certificado."),

    ("Bibliothek",
     "Ich lerne oft in der Bibliothek.",
     "Estudio a menudo en la biblioteca."),

    ("Software",
     "Die Software wurde gestern aktualisiert.",
     "El software fue actualizado ayer."),

    ("Netzwerk",
     "Das Netzwerk funktioniert momentan nicht.",
     "La red no funciona actualmente."),

    ("Verbindung",
     "Die Internetverbindung ist sehr langsam.",
     "La conexión a internet es muy lenta."),

    ("Kamera",
     "Die Kamera macht sehr gute Fotos.",
     "La cámara hace muy buenas fotos."),

    ("Freizeit",
     "In meiner Freizeit spiele ich Tennis.",
     "En mi tiempo libre juego al tenis."),

    ("Einladung",
     "Vielen Dank für die Einladung.",
     "Muchas gracias por la invitación."),

    ("Konzert",
     "Das Konzert war wirklich fantastisch.",
     "El concierto fue realmente fantástico."),

    ("Museum",
     "Am Wochenende besuchten wir ein Museum.",
     "El fin de semana visitamos un museo."),

    ("Hobby",
     "Mein Hobby ist das Fotografieren.",
     "Mi afición es la fotografía."),

    ("Umwelt",
     "Wir müssen die Umwelt besser schützen.",
     "Debemos proteger mejor el medio ambiente."),

    ("Energie",
     "Windenergie wird immer wichtiger.",
     "La energía eólica es cada vez más importante."),

    ("Recycling",
     "Recycling reduziert den Abfall erheblich.",
     "El reciclaje reduce considerablemente los residuos."),

    ("Klima",
     "Das Klima verändert sich weltweit.",
     "El clima está cambiando en todo el mundo."),

    ("Formular",
     "Bitte füllen Sie dieses Formular aus.",
     "Por favor rellene este formulario."),

    ("Antrag",
     "Der Antrag wurde genehmigt.",
     "La solicitud fue aprobada."),

    ("Dokument",
     "Ich habe das Dokument per E-Mail erhalten.",
     "He recibido el documento por correo electrónico."),

    ("Unterschrift",
     "Hier fehlt noch Ihre Unterschrift.",
     "Aquí falta todavía su firma."),

    ("verbessern",
     "Ich möchte mein Deutsch verbessern.",
     "Quiero mejorar mi alemán."),

    ("erklären",
     "Kannst du mir das erklären?",
     "¿Puedes explicármelo?"),

    ("entscheiden",
     "Wir müssen uns heute entscheiden.",
     "Tenemos que decidirnos hoy."),

    ("vergleichen",
     "Vergleichen wir beide Angebote.",
     "Comparemos ambas ofertas."),

    ("organisieren",
     "Sie organisiert das Treffen.",
     "Ella organiza la reunión."),

    ("reservieren",
     "Ich möchte ein Zimmer reservieren.",
     "Quiero reservar una habitación."),

    ("einladen",
     "Wir laden unsere Freunde zum Essen ein.",
     "Invitamos a nuestros amigos a cenar."),

    ("teilnehmen",
     "Möchtest du am Kurs teilnehmen?",
     "¿Quieres participar en el curso?"),

    ("sparen",
     "Ich spare für eine Reise nach Deutschland.",
     "Estoy ahorrando para un viaje a Alemania."),

    ("gesund",
     "Eine gesunde Ernährung ist wichtig.",
     "Una alimentación saludable es importante."),

    ("attraktiv",
     "Die Stadt ist für Touristen sehr attraktiv.",
     "La ciudad es muy atractiva para los turistas."),

    ("pünktlich",
     "Er kommt immer pünktlich zur Arbeit.",
     "Siempre llega puntual al trabajo."),

    ("zufrieden",
     "Ich bin mit dem Ergebnis zufrieden.",
     "Estoy satisfecho con el resultado."),

    ("spannend",
     "Das Buch war sehr spannend.",
     "El libro fue muy emocionante."),

    ("weil",
     "Ich bleibe zu Hause, weil es regnet.",
     "Me quedo en casa porque está lloviendo."),

    ("deshalb",
     "Ich war krank, deshalb blieb ich zu Hause.",
     "Estaba enfermo, por eso me quedé en casa."),

    ("außerdem",
     "Außerdem spricht sie sehr gut Deutsch.",
     "Además habla alemán muy bien."),

    ("trotzdem",
     "Es regnet, trotzdem gehen wir spazieren.",
     "Llueve, aun así vamos a pasear."),

    ("zum Beispiel",
     "Ich mag Obst, zum Beispiel Äpfel.",
     "Me gusta la fruta, por ejemplo las manzanas."),
	 

    ("Arbeitsplatz",
     "Mein Arbeitsplatz befindet sich im Stadtzentrum.",
     "Mi puesto de trabajo se encuentra en el centro de la ciudad."),

    ("Aufgabe",
     "Die Aufgabe muss bis morgen fertig sein.",
     "La tarea debe estar terminada para mañana."),

    ("Abteilung",
     "Ich arbeite in der technischen Abteilung.",
     "Trabajo en el departamento técnico."),

    ("Vermieter",
     "Der Vermieter hat die Heizung repariert.",
     "El casero ha reparado la calefacción."),

    ("Aufzug",
     "Der Aufzug funktioniert heute nicht.",
     "El ascensor no funciona hoy."),

    ("Keller",
     "Wir lagern die Fahrräder im Keller.",
     "Guardamos las bicicletas en el sótano."),

    ("Möbel",
     "Die neuen Möbel sehen sehr modern aus.",
     "Los muebles nuevos parecen muy modernos."),

    ("Schrank",
     "Die Kleidung liegt im Schrank.",
     "La ropa está en el armario."),

    ("Teppich",
     "Der Teppich passt gut zum Zimmer.",
     "La alfombra encaja bien con la habitación."),

    ("Unterkunft",
     "Die Unterkunft war sauber und ruhig.",
     "El alojamiento era limpio y tranquilo."),

    ("Ausweis",
     "Bitte zeigen Sie Ihren Ausweis.",
     "Por favor muestre su documento de identidad."),

    ("Führung",
     "Die Führung durch die Stadt war interessant.",
     "La visita guiada por la ciudad fue interesante."),

    ("Lieferung",
     "Die Lieferung kommt morgen an.",
     "La entrega llega mañana."),

    ("Konto",
     "Ich habe ein neues Konto eröffnet.",
     "He abierto una cuenta nueva."),

    ("Überweisung",
     "Die Überweisung wurde gestern durchgeführt.",
     "La transferencia se realizó ayer."),

    ("Patientin",
     "Die Patientin wartet auf den Arzt.",
     "La paciente espera al médico."),

    ("Tablette",
     "Nimm diese Tablette zweimal täglich.",
     "Toma esta pastilla dos veces al día."),

    ("Notfall",
     "Im Notfall rufen Sie die Nummer 112 an.",
     "En caso de emergencia llame al 112."),

    ("Lektion",
     "Die heutige Lektion war nicht schwer.",
     "La lección de hoy no fue difícil."),

    ("Übung",
     "Diese Übung hilft beim Lernen.",
     "Este ejercicio ayuda a aprender."),

    ("Thema",
     "Das Thema der Präsentation war interessant.",
     "El tema de la presentación fue interesante."),

    ("Anwendung",
     "Diese Anwendung ist sehr nützlich.",
     "Esta aplicación es muy útil."),

    ("Benutzer",
     "Der Benutzer hat sein Passwort vergessen.",
     "El usuario ha olvidado su contraseña."),

    ("Drucker",
     "Der Drucker hat kein Papier mehr.",
     "La impresora ya no tiene papel."),

    ("Download",
     "Der Download dauert nur wenige Minuten.",
     "La descarga dura solo unos minutos."),

    ("Upload",
     "Der Upload der Datei war erfolgreich.",
     "La subida del archivo fue exitosa."),

    ("Veranstaltung",
     "Viele Menschen besuchten die Veranstaltung.",
     "Muchas personas asistieron al evento."),

    ("Ausstellung",
     "Die Ausstellung ist bis Sonntag geöffnet.",
     "La exposición está abierta hasta el domingo."),

    ("Mitglied",
     "Ich bin Mitglied eines Sportvereins.",
     "Soy miembro de un club deportivo."),

    ("Verein",
     "Der Verein organisiert verschiedene Aktivitäten.",
     "La asociación organiza diversas actividades."),

    ("Wettbewerb",
     "Unser Team hat den Wettbewerb gewonnen.",
     "Nuestro equipo ganó la competición."),

    ("Müll",
     "Bitte werfen Sie den Müll hier weg.",
     "Por favor tire la basura aquí."),

    ("Luft",
     "Die Luft auf dem Land ist sauber.",
     "El aire en el campo es limpio."),

    ("Strom",
     "Heute Nacht gab es keinen Strom.",
     "Anoche no hubo electricidad."),

    ("Verbrauch",
     "Der Stromverbrauch ist gestiegen.",
     "El consumo eléctrico ha aumentado."),

    ("Behörde",
     "Die Behörde bearbeitet den Antrag.",
     "La administración está tramitando la solicitud."),

    ("Genehmigung",
     "Für das Projekt brauchen wir eine Genehmigung.",
     "Para el proyecto necesitamos una autorización."),

    ("Bescheinigung",
     "Ich habe die Bescheinigung gestern erhalten.",
     "Recibí el certificado ayer."),

    ("empfehlen",
     "Kannst du mir ein gutes Restaurant empfehlen?",
     "¿Puedes recomendarme un buen restaurante?"),

    ("beschreiben",
     "Bitte beschreiben Sie das Problem genauer.",
     "Por favor describa el problema con más detalle."),

    ("anrufen",
     "Ich rufe dich später an.",
     "Te llamaré más tarde."),

    ("mitbringen",
     "Kannst du morgen das Dokument mitbringen?",
     "¿Puedes traer mañana el documento?"),

    ("abholen",
     "Ich hole dich vom Bahnhof ab.",
     "Te recogeré en la estación."),

    ("verdienen",
     "Er verdient genug Geld für seine Familie.",
     "Gana suficiente dinero para su familia."),

    ("wechseln",
     "Ich möchte die Wohnung wechseln.",
     "Quiero cambiar de vivienda."),

    ("geeignet",
     "Dieses Hotel ist für Familien geeignet.",
     "Este hotel es adecuado para familias."),

    ("geduldig",
     "Der Lehrer ist sehr geduldig.",
     "El profesor es muy paciente."),

    ("hilfreich",
     "Deine Erklärung war sehr hilfreich.",
     "Tu explicación fue muy útil."),

    ("regional",
     "Wir kaufen regionale Produkte.",
     "Compramos productos regionales."),

    ("technisch",
     "Das technische Problem wurde gelöst.",
     "El problema técnico fue resuelto."),

    ("wahrscheinlich",
     "Wahrscheinlich komme ich morgen später.",
     "Probablemente llegaré más tarde mañana."),

    ("Termin",
     "Ich habe morgen einen wichtigen Termin.",
     "Tengo una cita importante mañana."),

    ("Patient",
     "Der Patient wartet im Wartezimmer.",
     "El paciente espera en la sala de espera."),

    ("Apotheke",
     "Die Apotheke ist bis acht Uhr geöffnet.",
     "La farmacia está abierta hasta las ocho."),

    ("Krankheit",
     "Die Krankheit dauert schon eine Woche.",
     "La enfermedad dura ya una semana."),

    ("Schmerz",
     "Ich habe Schmerzen im Rücken.",
     "Tengo dolor de espalda."),

    ("Fieber",
     "Das Kind hat hohes Fieber.",
     "El niño tiene fiebre alta."),

    ("Markt",
     "Am Samstag gehen wir auf den Markt.",
     "Los sábados vamos al mercado."),

    ("Preis",
     "Der Preis ist günstiger als letztes Jahr.",
     "El precio es más barato que el año pasado."),

    ("Verkäufer",
     "Der Verkäufer hilft den Kunden.",
     "El vendedor ayuda a los clientes."),

    ("Rechnung",
     "Die Rechnung wurde per E-Mail geschickt.",
     "La factura fue enviada por correo electrónico."),

    ("Internet",
     "Ohne Internet kann ich nicht arbeiten.",
     "Sin internet no puedo trabajar."),

    ("Passwort",
     "Bitte ändern Sie Ihr Passwort regelmäßig.",
     "Por favor cambie su contraseña regularmente."),

    ("Bildschirm",
     "Der Bildschirm ist zu dunkel.",
     "La pantalla está demasiado oscura."),

    ("Datei",
     "Ich habe die Datei gespeichert.",
     "He guardado el archivo."),

    ("Handy",
     "Mein Handy hat keinen Akku mehr.",
     "Mi móvil ya no tiene batería."),

    ("Film",
     "Der Film war wirklich spannend.",
     "La película fue realmente emocionante."),

    ("Musik",
     "Ich höre gern klassische Musik.",
     "Me gusta escuchar música clásica."),

    ("Lied",
     "Dieses Lied gefällt mir sehr.",
     "Esta canción me gusta mucho."),

    ("Foto",
     "Wir haben viele Fotos gemacht.",
     "Hemos sacado muchas fotos."),

    ("Zeitung",
     "Mein Vater liest jeden Morgen die Zeitung.",
     "Mi padre lee el periódico cada mañana."),

    ("Wetter",
     "Das Wetter wird morgen besser.",
     "El tiempo mejorará mañana."),

    ("Regen",
     "Wegen des Regens bleiben wir zu Hause.",
     "Por la lluvia nos quedamos en casa."),

    ("Schnee",
     "Im Winter gibt es hier viel Schnee.",
     "En invierno hay mucha nieve aquí."),

    ("Wind",
     "Der Wind ist heute sehr stark.",
     "Hoy hace mucho viento."),

    ("Temperatur",
     "Die Temperatur liegt bei zwanzig Grad.",
     "La temperatura es de veinte grados."),

    ("Sommer",
     "Im Sommer fahren wir ans Meer.",
     "En verano vamos al mar."),

    ("Winter",
     "Im Winter fahre ich gern Ski.",
     "En invierno me gusta esquiar."),

    ("Frühling",
     "Im Frühling blühen viele Blumen.",
     "En primavera florecen muchas flores."),

    ("Herbst",
     "Im Herbst fallen die Blätter von den Bäumen.",
     "En otoño caen las hojas de los árboles."),

    ("Koffer",
     "Mein Koffer ist sehr schwer.",
     "Mi maleta pesa mucho."),

    ("Pass",
     "Vergiss deinen Pass nicht.",
     "No olvides tu pasaporte."),

    ("Tourist",
     "Viele Touristen besuchen die Stadt.",
     "Muchos turistas visitan la ciudad."),

    ("Karte",
     "Kannst du mir die Karte zeigen?",
     "¿Puedes enseñarme el mapa?"),

    ("Ausflug",
     "Der Ausflug hat allen gefallen.",
     "La excursión gustó a todos."),

    ("Ferien",
     "Wir verbringen die Ferien in Spanien.",
     "Pasamos las vacaciones en España."),

    ("Reservierung",
     "Die Reservierung wurde bestätigt.",
     "La reserva fue confirmada."),

    ("Gepäck",
     "Das Gepäck kommt später an.",
     "El equipaje llegará más tarde."),

    ("Fluss",
     "Der Fluss fließt durch die Stadt.",
     "El río atraviesa la ciudad."),

    ("See",
     "Im Sommer schwimmen wir im See.",
     "En verano nadamos en el lago."),

    ("Wald",
     "Wir gehen oft im Wald spazieren.",
     "A menudo paseamos por el bosque."),

    ("Pflanze",
     "Die Pflanze braucht mehr Wasser.",
     "La planta necesita más agua."),

    ("Tier",
     "Dieses Tier lebt in Afrika.",
     "Este animal vive en África."),

    ("Fisch",
     "Heute Abend essen wir Fisch.",
     "Esta noche cenamos pescado."),

    ("organisieren",
     "Sie organisiert die Reise für das Team.",
     "Ella organiza el viaje para el equipo."),

    ("diskutieren",
     "Wir diskutieren über das neue Projekt.",
     "Estamos debatiendo sobre el nuevo proyecto."),

    ("verbessern",
     "Ich möchte meine Aussprache verbessern.",
     "Quiero mejorar mi pronunciación."),

    ("verstehen",
     "Jetzt verstehe ich die Aufgabe besser.",
     "Ahora entiendo mejor el ejercicio."),

    ("erreichen",
     "Wir haben unser Ziel erreicht.",
     "Hemos alcanzado nuestro objetivo."),

    ("erfolgreich",
     "Die Präsentation war sehr erfolgreich.",
     "La presentación fue muy exitosa."),

    ("möglich",
     "Ist es möglich, morgen zu kommen?",
     "¿Es posible venir mañana?")

]

for palabra, ejemplo_de, ejemplo_es in ejemplos_a2:

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
    
print(
    f"{len(ejemplos_a2)} ejemplos actualizados"
)
# update_examples_B1.py

import sqlite3

conn = sqlite3.connect("aleman.db")
cursor = conn.cursor()

ejemplos_b1 = [

    ("Unternehmen",
     "Das Unternehmen plant eine Erweiterung seiner Produktion.",
     "La empresa planea una ampliación de su producción."),

    ("Besprechung",
     "In der Besprechung wurden die nächsten Schritte festgelegt.",
     "En la reunión se definieron los siguientes pasos."),

    ("Verhandlung",
     "Die Verhandlungen dauerten länger als erwartet.",
     "Las negociaciones duraron más de lo esperado."),

    ("Strategie",
     "Wir müssen eine langfristige Strategie entwickeln.",
     "Debemos desarrollar una estrategia a largo plazo."),

    ("Gewinn",
     "Das Unternehmen hat seinen Gewinn deutlich gesteigert.",
     "La empresa ha aumentado considerablemente sus beneficios."),

    ("Verlust",
     "Im letzten Quartal wurde ein Verlust verzeichnet.",
     "En el último trimestre se registró una pérdida."),

    ("Budget",
     "Das Budget für das Projekt wurde genehmigt.",
     "El presupuesto del proyecto fue aprobado."),

    ("Investition",
     "Die Investition wird sich in wenigen Jahren auszahlen.",
     "La inversión dará sus frutos en pocos años."),

    ("Lieferant",
     "Der Lieferant konnte die Ware nicht rechtzeitig liefern.",
     "El proveedor no pudo entregar la mercancía a tiempo."),

    ("Qualität",
     "Die Qualität des Produkts hat sich verbessert.",
     "La calidad del producto ha mejorado."),

    ("Zusammenarbeit",
     "Die Zusammenarbeit zwischen den Teams funktioniert gut.",
     "La colaboración entre los equipos funciona bien."),

    ("System",
     "Das neue System reduziert den Arbeitsaufwand.",
     "El nuevo sistema reduce la carga de trabajo."),

    ("Gerät",
     "Das Gerät muss regelmäßig gewartet werden.",
     "El dispositivo debe mantenerse regularmente."),

    ("Daten",
     "Die Daten wurden sorgfältig analysiert.",
     "Los datos fueron analizados cuidadosamente."),

    ("Netzwerk",
     "Das Netzwerk war für einige Minuten ausgefallen.",
     "La red estuvo caída durante algunos minutos."),

    ("Sensor",
     "Der Sensor misst die Temperatur kontinuierlich.",
     "El sensor mide la temperatura continuamente."),

    ("Signal",
     "Das Signal wurde erfolgreich übertragen.",
     "La señal fue transmitida con éxito."),

    ("Messung",
     "Die Messungen wurden gestern abgeschlossen.",
     "Las mediciones finalizaron ayer."),

    ("Analyse",
     "Die Analyse zeigte mehrere interessante Ergebnisse.",
     "El análisis mostró varios resultados interesantes."),

    ("Berechnung",
     "Die Berechnung wurde mit neuen Daten aktualisiert.",
     "El cálculo fue actualizado con nuevos datos."),

    ("Modell",
     "Das Modell liefert realistische Ergebnisse.",
     "El modelo proporciona resultados realistas."),

    ("Parameter",
     "Mehrere Parameter wurden angepasst.",
     "Se ajustaron varios parámetros."),

    ("Geschwindigkeit",
     "Die Windgeschwindigkeit nahm am Nachmittag zu.",
     "La velocidad del viento aumentó por la tarde."),

    ("Umwelt",
     "Der Schutz der Umwelt wird immer wichtiger.",
     "La protección del medio ambiente es cada vez más importante."),

    ("Windkraft",
     "Windkraft spielt eine wichtige Rolle in Europa.",
     "La energía eólica desempeña un papel importante en Europa."),

    ("Windpark",
     "Der neue Windpark soll nächstes Jahr gebaut werden.",
     "El nuevo parque eólico se construirá el próximo año."),

    ("Turbine",
     "Die Turbine wurde nach der Inspektion wieder gestartet.",
     "La turbina volvió a ponerse en marcha tras la inspección."),

    ("Standort",
     "Der Standort wurde aufgrund der Windbedingungen ausgewählt.",
     "El emplazamiento fue seleccionado debido a las condiciones de viento."),

    ("Netz",
     "Der Windpark ist an das Stromnetz angeschlossen.",
     "El parque eólico está conectado a la red eléctrica."),

    ("Klimawandel",
     "Der Klimawandel beeinflusst viele Regionen der Welt.",
     "El cambio climático afecta a muchas regiones del mundo."),

    ("Meinung",
     "Meiner Meinung nach ist diese Lösung sinnvoll.",
     "En mi opinión esta solución tiene sentido."),

    ("Argument",
     "Sein Argument war überzeugend.",
     "Su argumento fue convincente."),

    ("Diskussion",
     "Die Diskussion führte zu einem guten Ergebnis.",
     "La discusión condujo a un buen resultado."),

    ("Vorschlag",
     "Der Vorschlag wurde vom Team positiv aufgenommen.",
     "La propuesta fue bien recibida por el equipo."),

    ("Entscheidung",
     "Die endgültige Entscheidung fällt nächste Woche.",
     "La decisión final se tomará la próxima semana."),

    ("Möglichkeit",
     "Es gibt mehrere Möglichkeiten, das Problem zu lösen.",
     "Existen varias posibilidades para resolver el problema."),

    ("Vorteil",
     "Ein Vorteil der Methode ist ihre Einfachheit.",
     "Una ventaja del método es su simplicidad."),

    ("Nachteil",
     "Ein Nachteil besteht in den hohen Kosten.",
     "Una desventaja son los costes elevados."),

    ("Gesellschaft",
     "Die Gesellschaft verändert sich ständig.",
     "La sociedad cambia constantemente."),

    ("Bildung",
     "Bildung ist eine wichtige Grundlage für die Zukunft.",
     "La educación es una base importante para el futuro."),

    ("Vertrauen",
     "Vertrauen ist für eine gute Zusammenarbeit entscheidend.",
     "La confianza es fundamental para una buena colaboración."),

    ("Verantwortung",
     "Jeder Mitarbeiter trägt Verantwortung für seine Aufgaben.",
     "Cada empleado tiene responsabilidad sobre sus tareas."),

    ("Freiheit",
     "Freiheit gehört zu den wichtigsten Werten.",
     "La libertad forma parte de los valores más importantes."),

    ("Kommunikation",
     "Eine klare Kommunikation vermeidet Missverständnisse.",
     "Una comunicación clara evita malentendidos."),

    ("analysieren",
     "Wir analysieren die Ergebnisse der Messkampagne.",
     "Analizamos los resultados de la campaña de medición."),

    ("bewerten",
     "Die Daten müssen objektiv bewertet werden.",
     "Los datos deben evaluarse objetivamente."),

    ("entwickeln",
     "Das Team entwickelt eine neue Software.",
     "El equipo desarrolla un nuevo software."),

    ("verwenden",
     "Wir verwenden die neuesten Messdaten.",
     "Utilizamos los datos de medición más recientes."),

    ("verbessern",
     "Die neue Methode verbessert die Genauigkeit.",
     "El nuevo método mejora la precisión."),

    ("zuverlässig",
     "Die Ergebnisse sind sehr zuverlässig.",
     "Los resultados son muy fiables."),

    ("Anforderung",
     "Die technischen Anforderungen wurden klar definiert.",
     "Los requisitos técnicos fueron definidos claramente."),

    ("Ziel",
     "Unser Ziel ist die Verbesserung der Datenqualität.",
     "Nuestro objetivo es mejorar la calidad de los datos."),

    ("Umsatz",
     "Der Umsatz ist im Vergleich zum Vorjahr gestiegen.",
     "La facturación ha aumentado respecto al año anterior."),

    ("Nachfrage",
     "Die Nachfrage nach erneuerbaren Energien wächst.",
     "La demanda de energías renovables está creciendo."),

    ("Markt",
     "Der Markt entwickelt sich sehr dynamisch.",
     "El mercado se desarrolla de forma muy dinámica."),

    ("Produktion",
     "Die Produktion wurde vorübergehend gestoppt.",
     "La producción se detuvo temporalmente."),

    ("Bedingung",
     "Unter diesen Bedingungen ist das Projekt realisierbar.",
     "Bajo estas condiciones el proyecto es viable."),

    ("Lösung",
     "Wir suchen nach einer langfristigen Lösung.",
     "Buscamos una solución a largo plazo."),

    ("Fortschritt",
     "Der Fortschritt des Projekts wird monatlich überprüft.",
     "El avance del proyecto se revisa mensualmente."),

    ("Vergleich",
     "Der Vergleich zeigt deutliche Unterschiede.",
     "La comparación muestra diferencias significativas."),

    ("Leistung",
     "Die Leistung der Anlage wurde analysiert.",
     "El rendimiento de la instalación fue analizado."),

    ("Benutzer",
     "Die Benutzer erhalten eine neue Anleitung.",
     "Los usuarios recibirán una nueva guía."),

    ("Datei",
     "Die Datei wurde erfolgreich gespeichert.",
     "El archivo se guardó correctamente."),

    ("Speicher",
     "Der Speicherplatz reicht für die Daten aus.",
     "El espacio de almacenamiento es suficiente para los datos."),

    ("Verbindung",
     "Die Verbindung zwischen den Systemen wurde getestet.",
     "La conexión entre los sistemas fue probada."),

    ("Hardware",
     "Die Hardware muss ersetzt werden.",
     "El hardware debe ser sustituido."),

    ("Programm",
     "Das Programm läuft ohne Fehler.",
     "El programa funciona sin errores."),

    ("Einstellung",
     "Diese Einstellung verbessert die Genauigkeit.",
     "Esta configuración mejora la precisión."),

    ("Prozess",
     "Der Prozess wurde vollständig dokumentiert.",
     "El proceso fue documentado completamente."),

    ("Ergebnis",
     "Die Ergebnisse bestätigen unsere Erwartungen.",
     "Los resultados confirman nuestras expectativas."),

    ("Version",
     "Die aktuelle Version enthält neue Funktionen.",
     "La versión actual incluye nuevas funciones."),

    ("Server",
     "Der Server war gestern kurzzeitig nicht erreichbar.",
     "El servidor estuvo inaccesible durante un breve periodo."),

    ("Sicherheit",
     "Die Sicherheit der Daten hat höchste Priorität.",
     "La seguridad de los datos es una prioridad máxima."),

    ("Störung",
     "Die Störung konnte schnell behoben werden.",
     "La avería pudo resolverse rápidamente."),

    ("Entfernung",
     "Die Entfernung zum Standort beträgt 15 Kilometer.",
     "La distancia hasta el emplazamiento es de 15 kilómetros."),

    ("Technologie",
     "Neue Technologien verändern den Arbeitsmarkt.",
     "Las nuevas tecnologías transforman el mercado laboral."),

    ("Erzeugung",
     "Die Stromerzeugung war höher als erwartet.",
     "La generación eléctrica fue superior a la prevista."),

    ("Anlage",
     "Die Anlage wird regelmäßig gewartet.",
     "La instalación recibe mantenimiento regularmente."),

    ("Spannung",
     "Die Spannung wurde kontinuierlich überwacht.",
     "La tensión fue monitorizada continuamente."),

    ("Batterie",
     "Die Batterie muss vollständig geladen werden.",
     "La batería debe cargarse completamente."),

    ("Emission",
     "Die Emissionen konnten reduziert werden.",
     "Las emisiones pudieron reducirse."),

    ("Ressource",
     "Ressourcen sollten effizient genutzt werden.",
     "Los recursos deben utilizarse eficientemente."),

    ("Nachhaltigkeit",
     "Nachhaltigkeit spielt heute eine zentrale Rolle.",
     "La sostenibilidad desempeña hoy un papel central."),

    ("Validierung",
     "Die Ergebnisse wurden durch eine Validierung bestätigt.",
     "Los resultados fueron confirmados mediante una validación."),

    ("Bewertung",
     "Die Bewertung erfolgte nach internationalen Standards.",
     "La evaluación se realizó según estándares internacionales."),

    ("Beispiel",
     "Dieses Beispiel verdeutlicht das Problem.",
     "Este ejemplo ilustra el problema."),

    ("Einfluss",
     "Der Einfluss des Wetters wurde berücksichtigt.",
     "Se tuvo en cuenta la influencia del clima."),

    ("Funktion",
     "Die Funktion wurde erfolgreich getestet.",
     "La función fue probada exitosamente."),

    ("Methode",
     "Diese Methode liefert stabile Ergebnisse.",
     "Este método proporciona resultados estables."),

    ("Risiko",
     "Das Risiko wurde als gering eingestuft.",
     "El riesgo fue considerado bajo."),

    ("Struktur",
     "Die Struktur des Berichts wurde angepasst.",
     "La estructura del informe fue ajustada."),

    ("Tendenz",
     "Die Daten zeigen eine positive Tendenz.",
     "Los datos muestran una tendencia positiva."),

    ("Umsetzung",
     "Die Umsetzung beginnt im nächsten Monat.",
     "La implementación comienza el próximo mes."),

    ("Wirkung",
     "Die Maßnahme zeigte eine deutliche Wirkung.",
     "La medida mostró un efecto significativo."),

    ("feststellen",
     "Wir konnten mehrere Abweichungen feststellen.",
     "Pudimos detectar varias desviaciones."),

    ("reduzieren",
     "Das Unternehmen möchte die Kosten reduzieren.",
     "La empresa quiere reducir los costes."),

    ("untersuchen",
     "Die Experten untersuchen die Ursache des Problems.",
     "Los expertos investigan la causa del problema."),

    ("verbinden",
     "Die beiden Systeme werden miteinander verbunden.",
     "Los dos sistemas serán conectados entre sí."),

    ("vorbereiten",
     "Wir bereiten den Bericht für den Kunden vor.",
     "Estamos preparando el informe para el cliente."),

    ("zustimmen",
     "Die meisten Teilnehmer stimmten dem Vorschlag zu.",
     "La mayoría de los participantes estuvo de acuerdo con la propuesta."),

    ("Bereich",
     "Dieser Bereich benötigt weitere Untersuchungen.",
     "Esta área necesita más investigaciones."),

    ("Beitrag",
     "Sein Beitrag war für das Projekt sehr wichtig.",
     "Su contribución fue muy importante para el proyecto."),

    ("Beschreibung",
     "Die Beschreibung des Prozesses ist sehr detailliert.",
     "La descripción del proceso es muy detallada."),

    ("Bestimmung",
     "Die neuen Bestimmungen treten nächsten Monat in Kraft.",
     "Las nuevas disposiciones entrarán en vigor el próximo mes."),

    ("Chance",
     "Das Projekt bietet neue Chancen für das Unternehmen.",
     "El proyecto ofrece nuevas oportunidades para la empresa."),

    ("Definition",
     "Die Definition muss präziser formuliert werden.",
     "La definición debe formularse con más precisión."),

    ("Einheit",
     "Alle Werte werden in derselben Einheit angegeben.",
     "Todos los valores se expresan en la misma unidad."),

    ("Eigenschaft",
     "Diese Eigenschaft ist besonders wichtig.",
     "Esta propiedad es especialmente importante."),

    ("Entwurf",
     "Der erste Entwurf wurde bereits fertiggestellt.",
     "El primer borrador ya ha sido completado."),

    ("Faktor",
     "Der wichtigste Faktor ist die Datenqualität.",
     "El factor más importante es la calidad de los datos."),

    ("Fläche",
     "Die Fläche beträgt ungefähr fünf Quadratkilometer.",
     "La superficie es de aproximadamente cinco kilómetros cuadrados."),

    ("Genehmigung",
     "Die Genehmigung wird in den nächsten Wochen erwartet.",
     "La autorización se espera en las próximas semanas."),

    ("Hinweis",
     "Vielen Dank für Ihren hilfreichen Hinweis.",
     "Muchas gracias por su útil observación."),

    ("Kennzahl",
     "Diese Kennzahl wird monatlich ausgewertet.",
     "Este indicador se evalúa mensualmente."),

    ("Maßnahme",
     "Die Maßnahme führte zu besseren Ergebnissen.",
     "La medida produjo mejores resultados."),

    ("Nutzen",
     "Der Nutzen der Analyse ist offensichtlich.",
     "La utilidad del análisis es evidente."),

    ("Priorität",
     "Sicherheit hat höchste Priorität.",
     "La seguridad tiene la máxima prioridad."),

    ("Rahmen",
     "Das Projekt wurde im europäischen Rahmen entwickelt.",
     "El proyecto fue desarrollado dentro del marco europeo."),

    ("Schätzung",
     "Die Schätzung basiert auf historischen Daten.",
     "La estimación se basa en datos históricos."),

    ("Schritt",
     "Der nächste Schritt ist die Validierung.",
     "El siguiente paso es la validación."),

    ("Schwerpunkt",
     "Der Schwerpunkt liegt auf der Datenanalyse.",
     "El foco principal está en el análisis de datos."),

    ("Teilnehmer",
     "Alle Teilnehmer erhielten die Präsentation.",
     "Todos los participantes recibieron la presentación."),

    ("Umstand",
     "Unter diesen Umständen ist die Entscheidung nachvollziehbar.",
     "Bajo estas circunstancias la decisión es comprensible."),

    ("Vergütung",
     "Die Vergütung hängt von der Erfahrung ab.",
     "La remuneración depende de la experiencia."),

    ("Verhältnis",
     "Das Verhältnis zwischen Aufwand und Nutzen ist gut.",
     "La relación entre esfuerzo y beneficio es buena."),

    ("Voraussetzung",
     "Deutschkenntnisse sind eine wichtige Voraussetzung.",
     "Los conocimientos de alemán son un requisito importante."),

    ("Zusammenhang",
     "Zwischen beiden Faktoren besteht ein Zusammenhang.",
     "Existe una relación entre ambos factores."),

    ("beobachten",
     "Wir beobachten die Entwicklung des Marktes.",
     "Observamos la evolución del mercado."),

    ("berechnen",
     "Die Werte wurden automatisch berechnet.",
     "Los valores fueron calculados automáticamente."),

    ("bestätigen",
     "Die Ergebnisse bestätigen unsere Annahmen.",
     "Los resultados confirman nuestras hipótesis."),

    ("entwickeln",
     "Das Team entwickelt eine neue Lösung.",
     "El equipo desarrolla una nueva solución."),

    ("erkennen",
     "Wir konnten mehrere Probleme erkennen.",
     "Pudimos identificar varios problemas."),

    ("feststellen",
     "Die Experten stellten Abweichungen fest.",
     "Los expertos detectaron desviaciones."),

    ("fördern",
     "Das Programm fördert erneuerbare Energien.",
     "El programa fomenta las energías renovables."),

    ("gewährleisten",
     "Die Maßnahmen gewährleisten die Qualität der Daten.",
     "Las medidas garantizan la calidad de los datos."),

    ("messen",
     "Die Sensoren messen die Windgeschwindigkeit.",
     "Los sensores miden la velocidad del viento."),

    ("prüfen",
     "Alle Berechnungen wurden nochmals geprüft.",
     "Todos los cálculos fueron revisados nuevamente."),

    ("steigern",
     "Das neue Verfahren steigert die Effizienz.",
     "El nuevo procedimiento aumenta la eficiencia."),

    ("vertreten",
     "Er vertritt das Unternehmen auf der Konferenz.",
     "Representa a la empresa en la conferencia."),

    ("verwenden",
     "Wir verwenden aktuelle Messdaten.",
     "Utilizamos datos de medición actualizados."),

    ("vorschlagen",
     "Ich möchte eine Alternative vorschlagen.",
     "Me gustaría proponer una alternativa."),

    ("wachsen",
     "Der Markt für Windenergie wächst schnell.",
     "El mercado de la energía eólica crece rápidamente."),

    ("allgemein",
     "Im Allgemeinen sind die Ergebnisse positiv.",
     "En general los resultados son positivos."),

    ("effektiv",
     "Die Lösung ist einfach und effektiv.",
     "La solución es sencilla y eficaz."),

    ("effizient",
     "Das Team arbeitet sehr effizient.",
     "El equipo trabaja de forma muy eficiente."),

    ("relevant",
     "Diese Information ist für die Analyse relevant.",
     "Esta información es relevante para el análisis."),

    ("stabil",
     "Die Messwerte bleiben über Stunden stabil.",
     "Los valores medidos permanecen estables durante horas."),

    ("umfangreich",
     "Der Bericht enthält umfangreiche Informationen.",
     "El informe contiene información extensa."),

    ("zuverlässig",
     "Das System liefert zuverlässige Ergebnisse.",
     "El sistema proporciona resultados fiables."),

    ("wirtschaftlich",
     "Das Projekt ist wirtschaftlich sinnvoll.",
     "El proyecto es económicamente viable.")
]


for palabra, ejemplo_de, ejemplo_es in ejemplos_b1:

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

print(
    f"{len(ejemplos_b1)} ejemplos actualizados"
)
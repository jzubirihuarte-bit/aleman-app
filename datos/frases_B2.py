# update_examples_B2.py

import sqlite3

conn = sqlite3.connect("aleman.db")
cursor = conn.cursor()

ejemplos_b2 = [

    ("Abhängigkeit",
     "Die Ergebnisse zeigen eine starke Abhängigkeit von den Eingangsdaten.",
     "Los resultados muestran una fuerte dependencia de los datos de entrada."),

    ("Anforderung",
     "Alle Anforderungen wurden im Lastenheft dokumentiert.",
     "Todos los requisitos fueron documentados en el pliego de condiciones."),

    ("Ansatz",
     "Dieser Ansatz ermöglicht eine genauere Bewertung der Unsicherheiten.",
     "Este enfoque permite una evaluación más precisa de las incertidumbres."),

    ("Auswirkung",
     "Die Auswirkung der Änderung war größer als erwartet.",
     "El impacto del cambio fue mayor de lo esperado."),

    ("Bewertung",
     "Die Bewertung basiert auf internationalen Standards.",
     "La evaluación se basa en estándares internacionales."),

    ("Datensatz",
     "Der Datensatz wurde vor der Analyse bereinigt.",
     "El conjunto de datos fue depurado antes del análisis."),

    ("Einflussfaktor",
     "Mehrere Einflussfaktoren wurden berücksichtigt.",
     "Se tuvieron en cuenta varios factores de influencia."),

    ("Empfehlung",
     "Die Empfehlungen werden im Abschlussbericht zusammengefasst.",
     "Las recomendaciones se resumirán en el informe final."),

    ("Erkenntnis",
     "Die Untersuchung lieferte wichtige Erkenntnisse.",
     "La investigación proporcionó conclusiones importantes."),

    ("Ertrag",
     "Der erwartete Ertrag liegt über dem Durchschnitt.",
     "La producción esperada está por encima de la media."),

    ("Grundlage",
     "Diese Daten bilden die Grundlage der Analyse.",
     "Estos datos constituyen la base del análisis."),

    ("Herausforderung",
     "Die größte Herausforderung war die Datenverfügbarkeit.",
     "El mayor reto fue la disponibilidad de datos."),

    ("Konzept",
     "Das Konzept wurde erfolgreich umgesetzt.",
     "El concepto fue implementado con éxito."),

    ("Leistungsfähigkeit",
     "Die Leistungsfähigkeit des Systems wurde getestet.",
     "La capacidad de rendimiento del sistema fue probada."),

    ("Methodik",
     "Die Methodik wird ausführlich beschrieben.",
     "La metodología se describe detalladamente."),

    ("Nachweis",
     "Der Nachweis erfolgte durch mehrere Messkampagnen.",
     "La demostración se realizó mediante varias campañas de medición."),

    ("Optimierung",
     "Die Optimierung führte zu besseren Ergebnissen.",
     "La optimización produjo mejores resultados."),

    ("Potenzial",
     "Das Gebiet besitzt ein hohes Windenergiepotenzial.",
     "La zona posee un alto potencial eólico."),

    ("Prognose",
     "Die Prognose basiert auf historischen Daten.",
     "La previsión se basa en datos históricos."),

    ("Referenz",
     "Die Referenzdaten stammen aus einer Langzeitmessung.",
     "Los datos de referencia proceden de una medición a largo plazo."),

    ("Risikobewertung",
     "Die Risikobewertung wurde aktualisiert.",
     "La evaluación de riesgos fue actualizada."),

    ("Simulation",
     "Die Simulation zeigt verschiedene Szenarien.",
     "La simulación muestra distintos escenarios."),

    ("Unsicherheit",
     "Die Unsicherheit der Messung wurde quantifiziert.",
     "La incertidumbre de la medición fue cuantificada."),

    ("Verfügbarkeit",
     "Die Verfügbarkeit der Anlage lag bei 98 Prozent.",
     "La disponibilidad de la instalación fue del 98 por ciento."),

    ("Wirkungsgrad",
     "Der Wirkungsgrad der Anlage wurde verbessert.",
     "La eficiencia de la instalación fue mejorada."),

    ("Windenergie",
     "Windenergie ist ein wichtiger Bestandteil der Energiewende.",
     "La energía eólica es una parte importante de la transición energética."),

    ("Windgeschwindigkeit",
     "Die Windgeschwindigkeit wurde in zehnminütigen Intervallen gemessen.",
     "La velocidad del viento se midió en intervalos de diez minutos."),

    ("Kapazitätsfaktor",
     "Der Kapazitätsfaktor liegt über den Erwartungen.",
     "El factor de capacidad está por encima de las expectativas."),

    ("Ertragsberechnung",
     "Die Ertragsberechnung wurde mit neuen Daten aktualisiert.",
     "El cálculo de producción fue actualizado con nuevos datos."),

    ("Messkampagne",
     "Die Messkampagne dauerte insgesamt zwei Jahre.",
     "La campaña de medición duró un total de dos años."),

    ("Unsicherheitsanalyse",
     "Die Unsicherheitsanalyse bestätigte die Ergebnisse.",
     "El análisis de incertidumbre confirmó los resultados."),

    ("Verlustfaktor",
     "Der Verlustfaktor wurde konservativ angesetzt.",
     "El factor de pérdidas se estimó de forma conservadora."),

    ("Netzanschluss",
     "Der Netzanschluss ist für nächstes Jahr geplant.",
     "La conexión a red está prevista para el próximo año."),

    ("Leistungskurve",
     "Die Leistungskurve wurde anhand der Messdaten validiert.",
     "La curva de potencia fue validada mediante datos de medición."),

    ("Digitalisierung",
     "Die Digitalisierung verändert viele Geschäftsprozesse.",
     "La digitalización transforma muchos procesos empresariales."),

    ("Globalisierung",
     "Die Globalisierung erhöht den internationalen Wettbewerb.",
     "La globalización aumenta la competencia internacional."),

    ("Wettbewerbsfähigkeit",
     "Innovation stärkt die Wettbewerbsfähigkeit eines Unternehmens.",
     "La innovación fortalece la competitividad de una empresa."),

    ("Qualifikation",
     "Für diese Position ist eine technische Qualifikation erforderlich.",
     "Para este puesto se requiere una cualificación técnica."),

    ("Kommunikation",
     "Eine effektive Kommunikation verbessert die Zusammenarbeit.",
     "Una comunicación eficaz mejora la colaboración."),

    ("Führungskraft",
     "Die Führungskraft präsentierte die neue Strategie.",
     "El directivo presentó la nueva estrategia."),

    ("analysieren",
     "Die Experten analysieren die langfristigen Trends.",
     "Los expertos analizan las tendencias a largo plazo."),

    ("berücksichtigen",
     "Alle relevanten Faktoren müssen berücksichtigt werden.",
     "Todos los factores relevantes deben tenerse en cuenta."),

    ("beschleunigen",
     "Die neue Software beschleunigt die Datenverarbeitung.",
     "El nuevo software acelera el procesamiento de datos."),

    ("gewährleisten",
     "Das Verfahren gewährleistet eine hohe Qualität.",
     "El procedimiento garantiza una alta calidad."),

    ("identifizieren",
     "Die Ursache des Problems konnte identifiziert werden.",
     "Se pudo identificar la causa del problema."),

    ("optimieren",
     "Wir möchten den gesamten Prozess optimieren.",
     "Queremos optimizar todo el proceso."),

    ("reflektieren",
     "Der Bericht reflektiert die aktuelle Situation.",
     "El informe refleja la situación actual."),

    ("regulieren",
     "Die Temperatur wird automatisch reguliert.",
     "La temperatura se regula automáticamente."),

    ("voraussagen",
     "Das Modell kann zukünftige Entwicklungen voraussagen.",
     "El modelo puede predecir desarrollos futuros."),

    ("zuverlässig",
     "Die Methode liefert zuverlässige Ergebnisse.",
     "El método proporciona resultados fiables."),

    ("Priorität",
     "Die Sicherheit der Mitarbeiter bleibt unsere höchste Priorität.",
     "La seguridad de los empleados sigue siendo nuestra máxima prioridad."),

    ("Rahmenbedingung",
     "Die wirtschaftlichen Rahmenbedingungen haben sich verändert.",
     "Las condiciones marco económicas han cambiado."),

    ("Schnittstelle",
     "Die Schnittstelle zwischen beiden Systemen wurde verbessert.",
     "La interfaz entre ambos sistemas fue mejorada."),

    ("Standpunkt",
     "Er erläuterte seinen Standpunkt sehr ausführlich.",
     "Expuso su punto de vista con mucho detalle."),

    ("Verbesserung",
     "Die Verbesserung der Prozesse spart erhebliche Kosten.",
     "La mejora de los procesos ahorra costes considerables."),

    ("Voraussetzung",
     "Eine gute Planung ist die wichtigste Voraussetzung für den Erfolg.",
     "Una buena planificación es el requisito más importante para el éxito."),

    ("Digitalisierung",
     "Die Digitalisierung ermöglicht effizientere Arbeitsabläufe.",
     "La digitalización permite procesos de trabajo más eficientes."),

    ("Innovationskraft",
     "Die Innovationskraft des Unternehmens ist beeindruckend.",
     "La capacidad innovadora de la empresa es impresionante."),

    ("Arbeitsmarkt",
     "Der Arbeitsmarkt benötigt zunehmend qualifizierte Fachkräfte.",
     "El mercado laboral necesita cada vez más personal cualificado."),

    ("Weiterbildung",
     "Regelmäßige Weiterbildung verbessert die beruflichen Chancen.",
     "La formación continua mejora las oportunidades profesionales."),

    ("Lebensqualität",
     "Eine nachhaltige Entwicklung erhöht die Lebensqualität.",
     "Un desarrollo sostenible aumenta la calidad de vida."),

    ("Mobilität",
     "Die Mobilität in den Städten verändert sich rasant.",
     "La movilidad en las ciudades está cambiando rápidamente."),

    ("Verhandlung",
     "Die Verhandlung führte zu einer für beide Seiten akzeptablen Lösung.",
     "La negociación condujo a una solución aceptable para ambas partes."),

    ("Entscheidungsprozess",
     "Der Entscheidungsprozess dauerte länger als geplant.",
     "El proceso de toma de decisiones duró más de lo previsto."),

    ("Projektleiter",
     "Der Projektleiter koordinierte alle beteiligten Teams.",
     "El jefe de proyecto coordinó a todos los equipos implicados."),

    ("Meilenstein",
     "Der erste Meilenstein wurde erfolgreich erreicht.",
     "El primer hito se alcanzó con éxito."),

    ("Ressource",
     "Die verfügbaren Ressourcen müssen effizient genutzt werden.",
     "Los recursos disponibles deben utilizarse eficientemente."),

    ("Machbarkeit",
     "Die Machbarkeit des Projekts wurde untersucht.",
     "La viabilidad del proyecto fue estudiada."),

    ("Projektumfang",
     "Der Projektumfang wurde nachträglich erweitert.",
     "El alcance del proyecto fue ampliado posteriormente."),

    ("Risikomanagement",
     "Ein gutes Risikomanagement reduziert Unsicherheiten.",
     "Una buena gestión de riesgos reduce las incertidumbres."),

    ("Koordination",
     "Die Koordination zwischen den Abteilungen war entscheidend.",
     "La coordinación entre departamentos fue decisiva."),

    ("Verantwortungsbereich",
     "Jeder Mitarbeiter kennt seinen Verantwortungsbereich.",
     "Cada empleado conoce su área de responsabilidad."),

    ("Freigabe",
     "Das Dokument wartet auf die endgültige Freigabe.",
     "El documento espera la aprobación definitiva."),

    ("Dokumentation",
     "Eine vollständige Dokumentation ist unverzichtbar.",
     "Una documentación completa es imprescindible."),

    ("Tagesordnung",
     "Die Tagesordnung wurde vorab verteilt.",
     "El orden del día se distribuyó previamente."),

    ("Beschluss",
     "Der Beschluss wurde einstimmig angenommen.",
     "La resolución fue aprobada por unanimidad."),

    ("Einwand",
     "Niemand erhob einen Einwand gegen den Vorschlag.",
     "Nadie planteó una objeción contra la propuesta."),

    ("Konsens",
     "Nach einer langen Diskussion wurde ein Konsens erzielt.",
     "Tras una larga discusión se alcanzó un consenso."),

    ("Kompromiss",
     "Die Parteien fanden einen tragfähigen Kompromiss.",
     "Las partes encontraron un compromiso viable."),

    ("Moderation",
     "Die Moderation sorgte für einen strukturierten Ablauf.",
     "La moderación garantizó un desarrollo estructurado."),

    ("vielmehr",
     "Das Problem liegt nicht in den Daten, vielmehr in ihrer Interpretation.",
     "El problema no está en los datos, sino en su interpretación."),

    ("dementsprechend",
     "Die Ergebnisse waren positiv, dementsprechend wurde das Projekt fortgesetzt.",
     "Los resultados fueron positivos, por consiguiente el proyecto continuó."),

    ("angesichts",
     "Angesichts der aktuellen Situation müssen wir flexibel bleiben.",
     "Dada la situación actual debemos permanecer flexibles."),

    ("analysieren",
     "Die Fachleute analysierten große Datenmengen.",
     "Los especialistas analizaron grandes cantidades de datos."),

    ("beeinflussen",
     "Mehrere Faktoren beeinflussen die Messergebnisse.",
     "Varios factores influyen en los resultados de medición."),

    ("berücksichtigen",
     "Alle Annahmen wurden in der Berechnung berücksichtigt.",
     "Todas las hipótesis fueron consideradas en el cálculo."),

    ("darstellen",
     "Die Ergebnisse werden in einem Diagramm dargestellt.",
     "Los resultados se presentan en un gráfico."),

    ("einschätzen",
     "Die Experten schätzen das Risiko als gering ein.",
     "Los expertos consideran bajo el riesgo."),

    ("integrieren",
     "Die neue Lösung wurde erfolgreich integriert.",
     "La nueva solución fue integrada con éxito."),

    ("koordinieren",
     "Ein zentrales Team koordiniert alle Aktivitäten.",
     "Un equipo central coordina todas las actividades."),

    ("optimieren",
     "Der Algorithmus wurde weiter optimiert.",
     "El algoritmo fue optimizado aún más."),

    ("technologisch",
     "Das Unternehmen gehört zu den technologischen Marktführern.",
     "La empresa pertenece a los líderes tecnológicos del mercado."),

    ("transparent",
     "Der gesamte Prozess muss transparent bleiben.",
     "Todo el proceso debe permanecer transparente."),

    ("wissenschaftlich",
     "Die Studie basiert auf wissenschaftlichen Methoden.",
     "El estudio se basa en métodos científicos."),

    ("anspruchsvoll",
     "Das Projekt war technisch sehr anspruchsvoll.",
     "El proyecto era técnicamente muy exigente."),

    ("innovativ",
     "Das Team entwickelte eine innovative Lösung.",
     "El equipo desarrolló una solución innovadora."),

    ("wesentlich",
     "Dieser Faktor ist für das Ergebnis wesentlich.",
     "Este factor es esencial para el resultado."),

    ("verlässlich",
     "Die Daten stammen aus einer verlässlichen Quelle.",
     "Los datos proceden de una fuente fiable."),

    ("zukunftsorientiert",
     "Das Unternehmen verfolgt eine zukunftsorientierte Strategie.",
     "La empresa sigue una estrategia orientada al futuro."),

    ("reflektieren",
     "Die Ergebnisse reflektieren die tatsächlichen Bedingungen vor Ort.",
     "Los resultados reflejan las condiciones reales del emplazamiento."),

    ("voraussagen",
     "Mit diesem Modell lassen sich zukünftige Trends besser voraussagen.",
     "Con este modelo pueden predecirse mejor las tendencias futuras."),

    ("Priorität",
     "Die Reduzierung der Unsicherheit hat derzeit höchste Priorität.",
     "La reducción de la incertidumbre tiene actualmente la máxima prioridad."),

    ("Rahmenbedingung",
     "Die Rahmenbedingungen haben sich im Verlauf des Projekts geändert.",
     "Las condiciones marco han cambiado durante el desarrollo del proyecto."),

    ("Schnittstelle",
     "An der Schnittstelle zwischen beiden Systemen wurden Fehler entdeckt.",
     "Se detectaron errores en la interfaz entre ambos sistemas."),

    ("Verbesserung",
     "Die Verbesserung der Datenqualität führte zu zuverlässigeren Ergebnissen.",
     "La mejora de la calidad de los datos condujo a resultados más fiables."),

    ("Voraussetzung",
     "Eine genaue Datenerfassung ist eine wesentliche Voraussetzung.",
     "Una recopilación precisa de datos es un requisito esencial."),

    ("Digitalisierung",
     "Die Digitalisierung ermöglicht effizientere Arbeitsprozesse.",
     "La digitalización permite procesos de trabajo más eficientes."),

    ("Arbeitsmarkt",
     "Der Arbeitsmarkt verlangt zunehmend spezialisierte Fachkräfte.",
     "El mercado laboral requiere cada vez más personal especializado."),

    ("Qualifikation",
     "Für diese Stelle wird eine technische Qualifikation erwartet.",
     "Para este puesto se espera una cualificación técnica."),

    ("Führungskraft",
     "Die Führungskraft präsentierte die Ergebnisse vor dem Management.",
     "El directivo presentó los resultados ante la dirección."),

    ("Entscheidungsprozess",
     "Der Entscheidungsprozess basierte auf objektiven Daten.",
     "El proceso de toma de decisiones se basó en datos objetivos."),

    ("Koordination",
     "Die Koordination mehrerer Teams war eine große Herausforderung.",
     "La coordinación de varios equipos fue un gran desafío."),

    ("Risikomanagement",
     "Ein wirksames Risikomanagement reduziert potenzielle Probleme.",
     "Una gestión eficaz de riesgos reduce los problemas potenciales."),

    ("Dokumentation",
     "Die Dokumentation muss regelmäßig aktualisiert werden.",
     "La documentación debe actualizarse regularmente."),

    ("Verantwortungsbereich",
     "Jeder Mitarbeiter kennt seinen Verantwortungsbereich genau.",
     "Cada empleado conoce exactamente su área de responsabilidad."),

    ("Freigabe",
     "Die Freigabe des Berichts erfolgte am Freitag.",
     "La aprobación del informe se realizó el viernes."),

    ("Meilenstein",
     "Der zweite Meilenstein wurde pünktlich erreicht.",
     "El segundo hito se alcanzó puntualmente."),

    ("Projektbudget",
     "Das Projektbudget wurde vollständig ausgeschöpft.",
     "El presupuesto del proyecto fue utilizado por completo."),

    ("Arbeitsgruppe",
     "Die Arbeitsgruppe entwickelt neue Lösungsansätze.",
     "El grupo de trabajo desarrolla nuevos enfoques de solución."),

    ("Machbarkeit",
     "Die Machbarkeit des Vorhabens wurde untersucht.",
     "La viabilidad del proyecto fue estudiada."),

    ("Projektpartner",
     "Die Projektpartner arbeiten eng zusammen.",
     "Los socios del proyecto trabajan estrechamente."),

    ("Beschluss",
     "Der Beschluss wurde einstimmig verabschiedet.",
     "La resolución fue aprobada por unanimidad."),

    ("Einwand",
     "Es wurden keine Einwände gegen den Vorschlag erhoben.",
     "No se presentaron objeciones contra la propuesta."),

    ("Kompromiss",
     "Nach langen Verhandlungen wurde ein Kompromiss gefunden.",
     "Tras largas negociaciones se encontró un compromiso."),

    ("Konsens",
     "Am Ende der Sitzung wurde ein Konsens erreicht.",
     "Al final de la reunión se alcanzó un consenso."),

    ("Moderation",
     "Die Moderation sorgte für einen konstruktiven Austausch.",
     "La moderación favoreció un intercambio constructivo."),

    ("Argumentation",
     "Die Argumentation wurde mit Daten untermauert.",
     "La argumentación fue respaldada con datos."),

    ("Analyse",
     "Die Analyse ergab mehrere relevante Erkenntnisse.",
     "El análisis arrojó varios hallazgos relevantes."),

    ("Auswertung",
     "Die Auswertung der Messdaten dauert noch an.",
     "La evaluación de los datos de medición sigue en curso."),

    ("Validität",
     "Die Validität der Ergebnisse wurde überprüft.",
     "La validez de los resultados fue verificada."),

    ("Genauigkeit",
     "Die Genauigkeit der Messungen konnte verbessert werden.",
     "La precisión de las mediciones pudo mejorarse."),

    ("Transparenz",
     "Mehr Transparenz erhöht das Vertrauen der Kunden.",
     "Una mayor transparencia aumenta la confianza de los clientes."),

    ("Relevanz",
     "Die Relevanz dieser Kennzahl wurde diskutiert.",
     "Se debatió la relevancia de este indicador."),

    ("Stabilität",
     "Die Stabilität des Systems wurde erfolgreich getestet.",
     "La estabilidad del sistema fue probada con éxito."),

    ("Zuverlässigkeit",
     "Die Zuverlässigkeit der Anlage ist sehr hoch.",
     "La fiabilidad de la instalación es muy alta."),

    ("Verfahren",
     "Das Verfahren entspricht den aktuellen Standards.",
     "El procedimiento cumple con los estándares actuales."),

    ("Schwachstelle",
     "Eine Schwachstelle im Prozess wurde identifiziert.",
     "Se identificó un punto débil en el proceso."),

    ("Kapazität",
     "Die Kapazität der Anlage soll erweitert werden.",
     "La capacidad de la instalación se ampliará."),

    ("Komponente",
     "Mehrere Komponenten mussten ersetzt werden.",
     "Varias componentes tuvieron que ser sustituidas."),

    ("Effizienz",
     "Die Effizienz konnte durch Automatisierung gesteigert werden.",
     "La eficiencia pudo aumentarse mediante automatización."),

    ("Arbeitsweise",
     "Unsere Arbeitsweise hat sich deutlich verändert.",
     "Nuestra forma de trabajar ha cambiado considerablemente."),

    ("Sachverhalt",
     "Der Sachverhalt wurde ausführlich erläutert.",
     "La situación fue explicada detalladamente."),

    ("Schlussfolgerung",
     "Die Schlussfolgerung basiert auf belastbaren Daten.",
     "La conclusión se basa en datos sólidos."),

    ("Umfang",
     "Der Umfang des Projekts wurde neu definiert.",
     "El alcance del proyecto fue redefinido."),

    ("Wettbewerbsvorteil",
     "Innovationen schaffen langfristige Wettbewerbsvorteile.",
     "Las innovaciones crean ventajas competitivas a largo plazo."),

    ("abwägen",
     "Vor der Entscheidung müssen alle Optionen abgewogen werden.",
     "Antes de la decisión deben valorarse todas las opciones."),

    ("argumentieren",
     "Die Experten argumentierten auf Grundlage der Analyse.",
     "Los expertos argumentaron basándose en el análisis."),

    ("berücksichtigen",
     "Alle relevanten Faktoren wurden berücksichtigt.",
     "Se tuvieron en cuenta todos los factores relevantes."),

    ("identifizieren",
     "Die Ursache des Problems wurde schnell identifiziert.",
     "La causa del problema fue identificada rápidamente."),

    ("optimieren",
     "Das Unternehmen optimiert seine Prozesse kontinuierlich.",
     "La empresa optimiza continuamente sus procesos."),

    ("integrieren",
     "Die neue Software wurde erfolgreich integriert.",
     "El nuevo software fue integrado con éxito."),

    ("voraussagen",
     "Das Modell kann zukünftige Entwicklungen relativ genau voraussagen.",
     "El modelo puede predecir desarrollos futuros con relativa precisión.")
]


for palabra, ejemplo_de, ejemplo_es in ejemplos_b2:

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
    f"{len(ejemplos_b2)} ejemplos actualizados"
)
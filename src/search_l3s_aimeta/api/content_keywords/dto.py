from flask_restx import Model, fields

dto_content_tags_response = Model("DtoContentTagsResponse", {
    "task_id": fields.String(description='The task ID', example='10'),
    "content_tags": fields.List(fields.String, description='List of Content Tags', example=[
    "Arbeitsauftrag",
    "Ziele",
    "Funktion",
    "Bauteil",
    "Einzelteilzeichnung",
    "anspruchsvolles Werkstück",
    "Arbeitsfolge",
    "Form- und Lagetoleranzen",
    "Arbeitsplan",
    "Arbeitszeit",
    "Optimale Qualität",
    "Sicherheitsvorschriften",
    "Toleranzen",
    "Lagetoleranz",
    "Reflexion",
    "Lernbegleiter",
    "persönliche Reflexion",
    "Planung",
    "Effektivität",
    "Arbeitsplanformular",
    "Arbeitsplan",
    "Prozesse",
    "Vorgehen",
    "Sicherheitsbestimmungen",
    "Erfolgskontrolle",
    "Erfolgskontrolle Formular",
    "überfachliche Kompetenzen",
    "fachliche Kompetenzen",
    "Bewertungsbögen",
    "Lernfortschritt"
  ])
})


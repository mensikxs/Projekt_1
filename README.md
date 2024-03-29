Dokumentace k projektu č.1

Projektem č.1 je textový analyzátor:
x Program pracuje s texty, které jsou importovány
    z knihovny task_template.py
x Program vyžaduje přihlášení uživatele jménem a heslem,
    registrovaní uživatelé:
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
x Pokud je zadáno jméno neregistrovaného uživatele,
    nebo je zadáno nesprávné heslo, program je ukončen
x Pokud je zadáno správné jméno i heslo, program přivítá uživatele
    a nabídne mu k výběru čísla textů pro analýzu
x Pokud je zadán jiný znak než číselný, program je ukončen
x Pokud je zadáno číslo, které nebylo programem nabídnuto,
    program je ukončen
x Po zadání správného čísla zobrazí program analýzu
    zvoleného textu, a ta zahrnuje:
    počet slov v textu
    počet slov začínajících velkým písmenem
    počet slov zapsaných velkými písmeny
    počet slov zapsaných malými písmeny
    počet čísel
    sumu čísel
x Dále vypočítá délky jednotlivých slov a jejich četnosti,
    které zobrazí v sloupcovém grafu
    (legenda: len - délka slova, occurences - četnosti vyobrazené
    symbolem "*", NR - četnosti číselně)
x Následně je program ukončen



### Dokumentace k projektu č.1

## Projektem č.1 je textový analyzátor:
**Program pracuje s texty, které jsou importovány z knihovny task_template.py**
Program vyžaduje přihlášení uživatele jménem a heslem, registrovaní uživatelé:
**user    password**
bob       123     
ann     pass123   
mike  password123 
liz     pass123 

Pokud je zadáno jméno neregistrovaného uživatele, nebo je zadáno nesprávné heslo, program je ukončen
Pokud je zadáno správné jméno i heslo, program přivítá uživatelea nabídne mu k výběru čísla textů pro analýzu
Pokud je zadán jiný znak než číselný, program je ukončen
Pokud je zadáno číslo, které nebylo programem nabídnuto, program je ukončen
Po zadání správného čísla zobrazí program analýzu
    zvoleného textu, a ta zahrnuje:
    počet slov v textu
    počet slov začínajících velkým písmenem
    počet slov zapsaných velkými písmeny
    počet slov zapsaných malými písmeny
    počet čísel
    sumu čísel
Dále vypočítá délky jednotlivých slov a jejich četnosti,
    které zobrazí v sloupcovém grafu
    (legenda: len - délka slova, occurences - četnosti vyobrazené
    symbolem "*", NR - četnosti číselně)
Následně je program ukončen



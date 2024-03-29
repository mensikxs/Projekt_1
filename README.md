### Dokumentace k projektu č.1

## Projekt č.1 - Textový analyzátor:
**Program pracuje s texty, které jsou importovány z modulu task_template.py**</br>

Program vyžaduje přihlášení uživatele jménem a heslem, registrovaní uživatelé:</br>
**user &emsp; password**</br>
bob &emsp; 123  </br>
ann &emsp; pass123 </br>
mike &emsp; password123 </br>
liz &emsp; pass123 </br>

Pokud je zadáno jméno neregistrovaného uživatele, nebo je zadáno nesprávné heslo, program je ukončen.</br>
Pokud je zadáno správné jméno i heslo, program přivítá uživatele a nabídne mu k výběru čísla textů pro analýzu.</br>
Pokud je zadán jiný znak než číselný, program je ukončen.</br>
Pokud je zadáno číslo, které nebylo programem nabídnuto, program je ukončen.</br>
Po zadání správného čísla zobrazí program analýzu zvoleného textu, a ta zahrnuje:</br>
&emsp; 1. počet slov v textu</br>
&emsp; 2. počet slov začínajících velkým písmenem</br>
&emsp; 3. počet slov zapsaných velkými písmeny</br>
&emsp; 4. počet slov zapsaných malými písmeny</br>
&emsp; 5. počet čísel</br>
&emsp; 6. sumu čísel</br>

Dále program vypočítá délky jednotlivých slov a jejich četnosti, které zobrazí v sloupcovém grafu</br>
_(legenda: len - délka slova, occurences - četnosti vyobrazené symbolem "*", NR - četnosti)_ </br>
Následně je program ukončen.



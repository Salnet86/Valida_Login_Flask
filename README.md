# Valida_Login_Flask

# Login Form con Flask

Questo è un progetto semplice basato su **Flask** che implementa una funzionalità di login con convalida dell'email. Gli utenti possono inserire la loro email e password, e l'app verifica se l'email è valida e se i campi non sono vuoti. I messaggi di errore vengono visualizzati se necessario.

Come funziona nel codice: Nel codice, la route /login riceve i dati dal modulo di login, quindi verifica se l'email è valida con una regex e se i campi sono stati compilati. Se ci sono errori (ad esempio, email non valida o campi vuoti), restituisce un messaggio di errore. Se tutto è valido, un messaggio di successo è visualizzato.

2. Funzionalità
Descrivi le funzionalità principali implementate. Questo aiuta chi legge a capire cosa fa il progetto e cosa ci si può aspettare.









Esempio:
## Funzionalità

- **Modulo di login**: Consente agli utenti di inserire una email e una password.
- **Validazione dell'email**: Verifica che l'email inserita abbia il formato corretto.
- **Gestione degli errori**: Mostra messaggi di errore se i campi sono vuoti o l'email non è valida.
- **Messaggio di successo**: Se l'email è corretta e i campi non sono vuoti, visualizza un messaggio di conferma.

Flask: la base dell'applicazione
Flask è un micro-framework Python utilizzato per costruire applicazioni web. È progettato per essere leggero, flessibile e facile da usare. In questo caso, il tuo progetto usa Flask per gestire le richieste HTTP e mostrare pagine HTML agli utenti.

Come funziona il flusso dell'applicazione
Pagina di login ("/login")

Quando un utente visita la pagina di login, viene visualizzato un modulo dove può inserire il proprio email e password.
L'utente invia i dati (via metodo POST) cliccando un pulsante per il login.
Validazione dell'email

Quando l'utente invia i dati del modulo, l'applicazione verifica se l'indirizzo email inserito è valido, utilizzando una espressione regolare (regex). Un'email è considerata valida se segue un formato specifico, ad esempio esempio@dominio.com.
Se l'email non è valida, l'applicazione mostra un messaggio di errore che avvisa l'utente.
Verifica dei campi vuoti

Se l'utente lascia vuoti i campi dell'email o della password, viene visualizzato un messaggio che segnala l'errore, indicando che i campi sono obbligatori.
Messaggi di errore o successo

Se tutto è corretto (email valida e campi non vuoti), l'applicazione può mostrare un messaggio di successo, come "Login effettuato con successo", oppure può reindirizzare l'utente a una pagina successiva.
In caso di errori (email non valida o campi vuoti), il sistema mostrerà un messaggio di errore.
Redirect e Rendering

Se c'è un errore o il login è riuscito, l'applicazione renderizza di nuovo la pagina, mostrando i messaggi di errore o di successo.
In caso di successo, l'applicazione potrebbe anche reindirizzare l'utente a un'altra pagina, ma in questo esempio non è stato implementato un vero e proprio reindirizzamento (manca la logica di "successo" dopo il login).
Cosa succede nel codice
Raccolta dei dati del modulo

Quando l'utente invia il modulo, il codice raccoglie i dati tramite request.form, che è un oggetto che contiene tutti i valori inviati tramite il modulo HTML. Per esempio:
email = request.form['email']: raccoglie l'email che l'utente ha inserito.
password = request.form['password']: raccoglie la password dell'utente.
Controllo della validità dell'email

Viene usata una espressione regolare (regex) per verificare se l'email è nel formato corretto. Se l'email non rispetta questo formato, viene mostrato un messaggio di errore: "Email inserita non è valida".
Se l'email è vuota, viene mostrato un altro messaggio: "I campi inseriti sono vuoti".
Visualizzazione dei messaggi

Se ci sono errori, l'applicazione renderizza la pagina con i messaggi di errore.
Se l'email è valida e i campi non sono vuoti, viene visualizzato un messaggio di successo, come "Email inserita con successo".
Rendering della pagina

Dopo aver verificato l'email e i campi, la pagina viene aggiornata con i dati che l'utente ha inviato, ma mostrando eventuali errori o successi, attraverso il sistema di renderizzazione di Flask, che mostra la pagina HTML (index.html) con i messaggi appropriati.
Semplificazione della logica senza codice
Pagina iniziale: L'utente accede alla pagina di login.
Inserimento dei dati: L'utente inserisce la sua email e password.
Validazione:
Se l'email non è valida o i campi sono vuoti, l'applicazione mostra un messaggio di errore.
Se l'email è valida e i campi sono compilati, l'applicazione mostra un messaggio di successo.
Visualizzazione: La pagina viene aggiornata con il risultato della validazione.
Cosa deve fare un utente
L'utente apre la pagina di login.
Inserisce la propria email e password.
Clicca su "Login" per inviare i dati.
Se l'email è corretta e i campi non sono vuoti, riceverà un messaggio di successo.
Se c'è un errore (ad esempio, un'email non valida o i campi vuoti), l'utente vedrà un messaggio di errore.















## Installazione
pip install flask

### Prerequisiti

Assicurati di avere **Python 3.x** installato sul tuo sistema. Puoi verificarlo con il comando:

```bash
python --version




MIT License

Copyright (c) 2024 John Doe

Con la presente si concede, senza alcuna garanzia, il permesso di utilizzare, copiare, modificare, fondere, pubblicare, distribuire, sublicenziare e/o vendere copie del Software, e di permettere alle persone a cui il Software è fornito di farlo, conformemente alle seguenti condizioni:
    
La dichiarazione di copyright e questa licenza devono essere incluse in tutte le copie o in parti sostanziali del Software.

IL SOFTWARE VIENE FORNITO "COSÌ COM'È", SENZA GARANZIE DI ALCUN GENERE, ESPRESSE O IMPLICITE, INCLUSE MA NON LIMITATE A GARANZIE DI COMMERCIABILITÀ, IDONEITÀ PER UN PARTICOLARE SCOPO E NON VIOLAZIONE. IN NESSUN CASO GLI AUTORI O I DETENTORI DEL COPYRIGHT SARANNO RESPONSABILI PER QUALSIASI RECLAMO, DANNO O ALTRO, SIA IN UN'AZIONE DI CONTRATTO, TORTO O ALTRIMENTI, DERIVANTE DA, O IN CONNESSIONE CON IL SOFTWARE O L'USO O ALTRE TRATTATIVE NEL SOFTWARE.

![License: MIT](https://img.shields.io/badge/License-MIT-green)

# Mannaggia

Da un'idea originale di Pietro "Legolas" Suffritti

[https://github.com/LegolasTheElf/mannaggia](https://github.com/LegolasTheElf/mannaggia)

**mannaggia** e **cowdamn** sono utility per system administrator. Possono essere utilizzate solo da sistemisti esperti per mannaggiare automaticamente Santi e Beati. 

## Warranty
Queste utility sono fornite *as is* e senza nessuna garanzia. L'autore non potrà essere ritunuto reponsabile di eventuali punizioni e/o vendette divine come (elenco puramente esemplificativo, incompleto e non esaustivo):

* perdita di dati in sistemi di produzione il cui backup è bloccato da eoni
* richiesta di assistenza da utenti con cultura informatica paragonabile a quella di una scimmia urlante
* blocco assoluto dei sistemi la sera prima della partenza per le vacanze

## Build

Per costruire il pacchetto RPM:

* settare la variabile d'ambiente MANNAGGIA_VERS
```
$ export MANNAGGIA_VERS=1.2
```

* eseguire lo script build.sh
```
$ ./build.sh
```
Questo comando produce il il file `~/rpmbuild/RPMS/noarch/mannaggia-<MANNAGGIA_VERS>-1.noarch.rpm`

## Utilizzo

### mannaggia

Di seguito un esempio di utilizzo.

Es. 1:
```
$ mannaggia
Mannaggia Beato Giacomo Alberione!
$ 
```
Es. 2:
```
$ mannaggia "Si è esaurito lo spazio disco"
Mannaggia Beata Maria di San Giuseppe Alvarado! Si è esaurito lo spazio disco
$
```
### cowdamn

Si consiglia l'utilizzo di `cowdamn` per un'esperienza di mannaggia più autentica. 

Es. 1:
```
$ cowdamn 
 ______________________
< Mannaggia San Rocco! >
 ----------------------
      \                _
       \              (_)   <-- life
        \   ^__^       / \
         \  (oo)\_____/_\ \
            (__)\  you  ) /
                ||----w ((
                ||     ||>> 
$
```
Es. 2:
```
$ cowdamn "La CPU sta a manetta"
 ________________________________________
/ Mannaggia San Romano il Melode! La CPU \
\ sta a manetta                          /
 ----------------------------------------
      \                _
       \              (_)   <-- life
        \   ^__^       / \
         \  (oo)\_____/_\ \
            (__)\  you  ) /
                ||----w ((
                ||     ||>> 
$
```
### Eseguire comandi con *mannaggia* e *cowdamn*

*mannaggia* e *cowdamn* sono particolarmente utili per eseguire comandi e, in caso di errore, mannaggiare automaticamente prima di mostrare il messaggio d'errore del comando eseguito.

es:
```
$ mannaggia -c 'cat file-inesistente'
Mannaggia Beato Clemens August von Galen! cat: file-inesistente: No such file or directory
$
```
```
$ cowdamn -c 'cat file-inesistente'
 ________________________________________
/ Mannaggia San Rinaldo di Nocera Umbra! \
| cat: file-inesistente: No such file or |
\ directory                              /
 ----------------------------------------
      \                _
       \              (_)   <-- life
        \   ^__^       / \
         \  (oo)\_____/_\ \
            (__)\  you  ) /
                ||----w ((
                ||     ||>> 
$
```
Se il comando non genera errori allo non viene mannaggiato nessun Santo o Beato.

es:
```
$ mannaggia -c 'uname'
Linux

$ 
```
## Installazione su RedHat, CentOS e fedora

Il package rpm già buildato è disponibile [qui](http://sandrospadaro.altervista.org/repo/index.html) per il download. Per installare il pacchetto:

```
$ sudo rpm -i mannaggia-<VERSION>-1.noarch.rpm
```

I furbi lo possono invece installare tramite repository **yum** seguendo questi step:

* Configurare il repository scaricando il file `/etc/yum.repos.d/sandrospadaro.repo`
```
$ cd /etc/yum.repos.d/
$ sudo curl http://sandrospadaro.altervista.org/sandrospadaro.repo --output sandrospadaro.repo
```
* Installare il pacchetto tramite dnf lanciando il comando
```
$ sudo dnf install mannaggia -y
```

## Installazione su Debian e Ubuntu

Visto che è stato richiesto da molti, anche se ciò va oltre lo scopo per cui questo progetto è stato creato, si è provveduto ad implementare lo script `install_deb.sh` al fine di facilitare l'installazione su sistemi **Debian based** a partire dal 'codice sorgente'.

Per eseguire l'installazione è sufficiente usare il comando:
```
$ sudo install_deb.sh
```

## Installazione su altre distribuzioni

Per usare le utility su altre distribuzione basta 
1. installare `cowasy` e `python >= 3.6` con il package manager previsto dal sistema
2. copiare lo script `mannaggia` in `/usr/sbin/`
3. creare l'hard link `cowdamn` a mannaggia in `/usr/sbin/`
4. copiare i file `mannaggia.dat` e `mannaggia.cow` in `/etc/mannaggia.d/`

## Supporto multilingua

```
 _________________________________________
/ Mannaggia San Gregorio di Nissa! Non    \
| esageriamo. Se volete mannaggiare Santi |
| e Beati in altre lingue la traduzione   |
\ ve la fate da voi.                      /
 -----------------------------------------
      \                _
       \              (_)   <-- life
        \   ^__^       / \
         \  (oo)\_____/_\ \
            (__)\  you  ) /
                ||----w ((
                ||     ||>> 

```
## Credits

### Santi e beati
I santi e beati da mannaggiare sono stati estratti da [cathopedia.org](https://it.cathopedia.org/)
* [https://it.cathopedia.org/wiki/Lista_dei_Santi](https://it.cathopedia.org/wiki/Lista_dei_Santi)
* [https://it.cathopedia.org/wiki/Lista_dei_Beati](https://it.cathopedia.org/wiki/Lista_dei_Beati)

### Costruzione del pacchetto RPM

* [https://blog.prometheusproject.it/creare-pacchetti-rpm-su-centosrhel/](https://blog.prometheusproject.it/creare-pacchetti-rpm-su-centosrhel/)
* [https://fedoraproject.org/wiki/How_to_create_an_RPM_package/it](https://fedoraproject.org/wiki/How_to_create_an_RPM_package/it)
* [https://www.thegeekstuff.com/2015/02/rpm-build-package-example/](https://www.thegeekstuff.com/2015/02/rpm-build-package-example/)

### Configurazione di un repository yum

* [https://stackoverflow.com/questions/13876875/how-to-make-rpm-auto-install-dependencies](https://stackoverflow.com/questions/13876875/how-to-make-rpm-auto-install-dependencies)
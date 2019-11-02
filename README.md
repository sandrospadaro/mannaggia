# Mannaggia

Da un'idea originale di Pietro "Legolas" Suffritti

https://github.com/LegolasTheElf/mannaggia

**mannaggia** e **cowdamn** sono utility per system administrator. Possono essere solo da sistemisti esperti per mannaggiare Santi e Beati. 

## Warranty
Queste utility sono fornite *as is* e senza nessuna garanzia. L'autore non potrà essere ritunuto reponsabile di eventuali punizioni divine come (elenco puramente esemplificativo, incompleto e non esaustivo):

* perdita di dati in sistemi di produzione il cui backup è bloccato da eoni
* richiesta di assistenza da utenti con cultura informatica paragonabile a quelle di una scimmia urlante
* blocco assoluto dei sistemi la sera prima della partenza per le vacanze

## Build

Per costruire il pacchetto RPM:

* costruire l'archivio `tar.gz` con i file dell'utility
```
$ tar cvfz mannaggia-<VERSION>.tar.gz mannaggia-<VERSION>
```
* copiare nella cartella `~/rpmbuild/SOURCES/`
```
$ cp mannaggia-<VERSION>.tar.gz ~/rpmbuild/SOURCES/
```
* copiare il file `.spec` in `~/rpmbuild/SPECS/`
```
$ cp mannaggia.spec ~/rpmbuild/SPECS/
```
* spostarsi nella cartella `~/rpmbuild/SPECS/` e creare il pacchetto rpm
```
$ cd ~/rpmbuild/SPECS
$ rpmbuild -ba mannaggia.spec
```
Questo comando produce il il file `~/rpmbuild/RPMS/noarch/mannaggia-<VERSION>-1.noarch.rpm`

## Installazione

Per i pigri il package rpm già buildato è disponibile [qui](https://raw.githubusercontent.com/sandrospadaro/mannaggia/develop/bin/noarch/mannaggia-1.1-1.noarch.rpm) per il download. Per installare il pacchetto:

```
$ sudo rpm -i mannaggia-<VERSION>-1.noarch.rpm
```

I funbi possono invece installarlo tramite repository **dnf** seguendo i seguenti passi:

### Configurazione del repository

Creare il file `/etc/yum.repos.d/sandrospadaro.repo`

```
$ cd /etc/yum.repos.d/
$ sudo curl http://sandrospadaro.altervista.org/sandrospadaro.repo --output sandrospadaro.repo
```

### Installazione tramite dnf

Lanciare il comando

```
$ sudo dnf install mannaggia -y
```

## Utilizzo

### Mannaggia

Di seguito un esempio di utilizzo:

```
$ mannaggia
Mannaggia Beato Giacomo Alberione
$ 
```
### cowdamn

Si consiglia l'utilizzo di `cowdamn` per un'esperienza di mannaggia più autentica . Es:
```
$ cowdamn
 ________________________________
< Mannaggia San Filippo apostolo >
 --------------------------------
      \                _
       \              (_)   <-- TeleBEARS
        \   ^__^       / \
         \  (oo)\_____/_\ \
            (__)\  you  ) /
                ||----w ((
                ||     ||>> 
$ 
```

## Gestione del repository

Per sviluppare questo progetto ho usato `git flow`. Ad ogni nuova release viene aggiornato il change log con l'istruzione:

```
git log <last-tag>..HEAD | cat - CHANGELOG.md | sponge CHANGELOG.md
```

es:

```
git log 1.0.1..HEAD | cat - CHANGELOG.md | sponge CHANGELOG.md
```

## Credits

### Santi e beati
I santi e beati da mannaggiare sono stati estratti da [cathopedia.org](https://it.cathopedia.org/)
* https://it.cathopedia.org/wiki/Lista_dei_Santi
* https://it.cathopedia.org/wiki/Lista_dei_Beati

### Costruzione del pacchetto RPM

* https://blog.prometheusproject.it/creare-pacchetti-rpm-su-centosrhel/ 
* https://fedoraproject.org/wiki/How_to_create_an_RPM_package/it
* https://www.thegeekstuff.com/2015/02/rpm-build-package-example/

### Configurazione di un repository yum

* https://stackoverflow.com/questions/13876875/how-to-make-rpm-auto-install-dependencies
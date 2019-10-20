# Mannaggia

Da un'idea originale di Pietro "Legolas" Suffritti

https://github.com/LegolasTheElf/mannaggia

**mannaggia** è utility per system administrator. Può essere solo da sistemisti esperti
per mannaggiare Santi e Beati. 

## Warranty
L'applicazione viene fornita *as is* e senza nessuna garanzia. L'autore non potrà essere ritunuto reponsabile di eventuali vendette divine.

## Build

Per costruire il pacchetto RPM:

Costruire l'archivio `tar.gz` con i file dell'utility

```
$ tar cvfz mannaggia-1.0.tar.gz mannaggia-1.0
```

copiare nella cartella `~/rpmbuild/SOURCES/`

```
$ cp mannaggia-1.0.tar.gz ~/rpmbuild/SOURCES/
```

copiare il file `.spec` in `~/rpmbuild/SPEC/`

```
$ cp mannaggia.spec ~/rpmbuild/SPEC/
```
creare il pacchetto rpm

```
$ rpmbuild -ba mannaggia.spec
```

Questo comando produce il il file `~/rpmbuild/RPMS/noarch/mannaggia-1.0-1.noarch.rpm`

## Installazione

Il package rpm è disponibile [qui](https://raw.githubusercontent.com/sandrospadaro/mannaggia/develop/bin/noarch/mannaggia-1.0-1.noarch.rpm) per il download. Per installare il pacchetto:

```
$ sudo rpm -i mannaggia-1.0-1.noarch.rpm
```

## Utilizzo

Di seguito un esempio di utilizzo:

```
$ mannaggia
Mannaggia Beato Giacomo Alberione
$ 
```
## Suggerimenti

`mannaggia` può essere usato congiuntamente a `cowsay` per un'esperienza di mannaggia più autentica. Es:
```
$ mannaggia | cowsay -f telebears
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
Prova anche ad aggiungere un alias sul `.bashrc`; es: `alias cowdamn='mannaggia | cowsay -f telebears'`

## Credits

### Santi e beati
I santi e beati da mannaggiare sono stati estratti da [cathopedia.org](https://it.cathopedia.org/)
* https://it.cathopedia.org/wiki/Lista_dei_Santi
* https://it.cathopedia.org/wiki/Lista_dei_Beati

### Costruzione del pacchetto RPM

* https://blog.prometheusproject.it/creare-pacchetti-rpm-su-centosrhel/ 
* https://fedoraproject.org/wiki/How_to_create_an_RPM_package/it
* https://www.thegeekstuff.com/2015/02/rpm-build-package-example/
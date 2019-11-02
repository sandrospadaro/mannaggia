Name:           mannaggia
Version:        1.1
Release:        1
Summary:        Utility per mannaggiare Santi e Beati

License:        GPL
URL:            https://github.com/sandrospadaro/mannaggia
Source0:        mannaggia-1.1.tar.gz
BuildArch:	noarch

Requires: cowsay

%description
Utility per sistemisti. Può essere solo da sistemisti esperti
per mannaggiare Santi e Beati.

%prep
%setup -q
#%autosetup


%build
#%configure
#%make_build


%install
install -d -m 0755 $RPM_BUILD_ROOT/etc/mannaggia.d
install -d $RPM_BUILD_ROOT/usr/sbin
install -m 0755 mannaggia-1.1/mannaggia $RPM_BUILD_ROOT/usr/sbin/mannaggia
install -m 0755 mannaggia-1.1/cowdamn $RPM_BUILD_ROOT/usr/sbin/cowdamn
install -m 0755 mannaggia-1.1/mannaggia.dat $RPM_BUILD_ROOT/etc/mannaggia.d/mannaggia.dat
#%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/etc/mannaggia.d
/usr/sbin/mannaggia
/usr/sbin/cowdamn
/etc/mannaggia.d/mannaggia.dat
#%license add-license-file-here
#%doc add-docs-here



%changelog
* Sun Oct 20 2019 Sandro Spadaro <sandro.spadaro@gmail.com>
- 

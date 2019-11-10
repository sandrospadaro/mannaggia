%define version %{getenv:MANNAGGIA_VERS}
Name:           mannaggia
Version:        %{version}
Release:        1
Summary:        Utility per mannaggiare Santi e Beati

License:        GPL
URL:            https://github.com/sandrospadaro/mannaggia
Source0:        mannaggia-%{version}.tar.gz
BuildArch:      noarch

Requires: cowsay, python >= 3.6

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
install -m 0755 mannaggia-%{version}/mannaggia $RPM_BUILD_ROOT/usr/sbin/mannaggia
install -m 0644 mannaggia-%{version}/mannaggia.dat $RPM_BUILD_ROOT/etc/mannaggia.d/mannaggia.dat
install -m 0644 mannaggia-%{version}/mannaggia.cow $RPM_BUILD_ROOT/etc/mannaggia.d/mannaggia.cow
#%make_install

%post
ln -f /usr/sbin/mannaggia /usr/sbin/cowdamn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/etc/mannaggia.d
/usr/sbin/mannaggia
/etc/mannaggia.d/mannaggia.dat
/etc/mannaggia.d/mannaggia.cow
#%license add-license-file-here
#%doc add-docs-here



%changelog
* Sun Oct 20 2019 Sandro Spadaro <sandro.spadaro@gmail.com>
- 

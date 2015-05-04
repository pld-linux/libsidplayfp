Summary:	A library to play Commodore 64 music
Summary(pl.UTF-8):	Biblioteka do odtwarzania muzyki z Commodore 64
Name:		libsidplayfp
Version:	1.1.0
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sidplay-residfp/%{name}-%{version}.tar.gz
# Source0-md5:	21917667ce1a19a905a18e1ba073ed70
URL:		http://sourceforge.net/projects/sidplay-residfp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsidplayfp (and its console frontend sidplayfp) is a fork of
sidplay2 born with the aim to improve the quality of emulating the
6581, 8580 chips and the surrounding C64 system in order to play SID
music better.

%description -l pl.UTF-8
Libsidplayfp (i jego konsolowy interfejs sidplayfp) to odgałęzienie
sidplay2 mające na celu poprawienie jakości emulacji układów 6581 i 8580
wraz z systemem C64, aby lepiej odtwarzać muzykę SID.

%package devel
Summary:	Header files for compiling apps that use libsidplayfp
Summary(pl.UTF-8):	Pliki nagłówkowe do budowania aplikacji używających libsidplayfp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains the header files for compiling applications that
use libsidplayfp.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do budowania aplikacji używających
biblioteki libsidplayfp.

%package static
Summary:	Static libsidplayfp library
Summary(pl.UTF-8):	Statyczna biblioteka libsidplayfp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of libsidplayfp.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję libsidplayfp.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libsidplayfp.so.3
%attr(755,root,root) %{_libdir}/libsidplayfp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstilview.so.0
%attr(755,root,root) %{_libdir}/libstilview.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsidplayfp.so
%attr(755,root,root) %{_libdir}/libstilview.so
%{_includedir}/sidplayfp
%{_includedir}/stilview
%{_pkgconfigdir}/libsidplayfp.pc
%{_pkgconfigdir}/libstilview.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsidplayfp.a
%{_libdir}/libstilview.a

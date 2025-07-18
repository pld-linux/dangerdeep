Summary:	Danger from the Deep - WW2 german submarine simulation
Summary(pl.UTF-8):	Danger from the Deep - symulacja niemieckiej łodzi podwodnej
Name:		dangerdeep
Version:	0.3.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/dangerdeep/%{name}-%{version}.tar.gz
# Source0-md5:	8a1d19326a9a0bd8bb91a652bfa51bd9
Source1:	http://dl.sourceforge.net/dangerdeep/%{name}-data-%{version}.zip
# Source1-md5:	b9a2f2ff756cd7715a3b58de7504c1d0
Source2:	%{name}.desktop
Patch0:		%{name}-X11.patch
URL:		http://dangerdeep.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	fftw3-devel
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Danger from the deep (aka dangerdeep) is a Free / Open Source World
War II german submarine simulation. It is currently available for
Linux/i386 and Windows, but since it uses SDL/OpenGL it should be
portable to other operating systems or platforms. This game is planned
as tactical simulation and will be as realistic as our time and
knowledge of physics allows. It's current state is ALPHA, but it is
playable.

%description -l pl.UTF-8
Danger from the deep jest darmową (z dostępnymi źródłami) symulacją
niemieckiej łodzi podwodnej z czasów II Wojny Światowej. Gra jest
zaplanowana jako taktyczno-symulacyjna i będzie tak realistyczna jak
pozwoli na to czas twórców i ich wiedza z fizyki. Aktualny stan jest
określony jako ALPHA, ale jest grywalna.

%package utils
Summary:	Danger from the Deep - utils
Summary(pl.UTF-8):	Danger from the Deep - narzędzia
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description utils
Danger from the Deep - utils.

%description utils -l pl.UTF-8
Danger from the Deep - narzędzia.

%prep
%setup -q -a 1
%patch -P0 -p1
%{__sed} -i 's@-g -O2@%{rpmcflags}@' SConstruct
%{__sed} -i 's@/usr/local/share/dangerdeep@%{_datadir}/dangerdeep@' SConstruct

%build
# use `scons usex86sse=-1' to build dangerdeep on Ac (tested on i686)
scons usex86sse=-1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_mandir}/man6,%{_pixmapsdir}}

install build/linux/%{name} $RPM_BUILD_ROOT%{_bindir}
install doc/man/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install logo.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm
cp -r data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

install build/linux/{crosssection,damagemodel,oceantest,portal,viewmodel} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_pixmapsdir}/%{name}.xpm

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/crosssection
%attr(755,root,root) %{_bindir}/damagemodel
%attr(755,root,root) %{_bindir}/oceantest
%attr(755,root,root) %{_bindir}/portal
%attr(755,root,root) %{_bindir}/viewmodel

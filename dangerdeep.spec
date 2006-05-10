Summary:	Danger from the Deep - WW2 german submarine simulation
Summary(pl):	Danger from the Deep - symulacja niemieckiej ³odzi podwodnej
Name:		dangerdeep
Version:	0.1.1
Release:	0.2
License:	GPL v2
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/dangerdeep/%{name}-%{version}.tar.gz
# Source0-md5:	7de20b4594c0fee8d3c1a281f686f943
URL:		http://dangerdeep.sourceforge.net/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	fftw3-devel
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Danger from the deep (aka dangerdeep) is a Free / Open Source World
War II german submarine simulation. It is currently available for
Linux/i386 and Windows, but since it uses SDL/OpenGL it should be
portable to other operating systems or platforms. This game is planned
as tactical simulation and will be as realistic as our time and
knowledge of physics allows. It's current state is ALPHA, but it is
playable.

%description -l pl
Danger from the deep jest darmow± (z dostêpnymi ¼ród³ami) symulacj±
niemieckiej ³odzi podwodnej z czasów II Wojny ¦wiatowej. Gra jest
zaplanowana jako taktyczno-symulacyjna i bêdzie tak realistyczna jak
pozwoli na to czas twórców i ich wiedza z fizyki. Aktualny stan jest
okre¶lony jako ALPHA, ale jest grywalna.

%package utils
Summary:	Danger from the Deep - utils
Summary(pl):	Danger from the Deep - narzêdzia
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description utils
Danger from the Deep - utils.

%description utils -l pl
Danger from the Deep - narzêdzia.

%prep
%setup -q
sed -i 's@-g -O2@%{rpmcflags}@' SConstruct
sed -i 's@/usr/local/share/dangerdeep@%{_datadir}/dangerdeep@' SConstruct

%build
# use `scons usex86sse=-1' to build dangerdeep on Ac (tested on i686)
scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_mandir}/man6}

install build/linux/%{name} $RPM_BUILD_ROOT%{_bindir}
install doc/man/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6
cp -r data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

install build/linux/{crosssection,damagemodel,oceantest,portal,viewmodel} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/crosssection
%attr(755,root,root) %{_bindir}/damagemodel
%attr(755,root,root) %{_bindir}/oceantest
%attr(755,root,root) %{_bindir}/portal
%attr(755,root,root) %{_bindir}/viewmodel

Summary:	Danger from the Deep - WW2 german submarine simulation
Summary(pl):	Danger from the Deep - symulacja niemieckiej ³odzi podwodnej
Name:		dangerdeep
Version:	0.0.19
Release:	0.1
License:	GPL v2
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/dangerdeep/%{name}-%{version}.tar.gz
# Source0-md5:	b1dcc97066aa370a22e0ad768181590c
URL:		http://dangerdeep.sourceforge.net/
BuildRequires:	fftw3-devel
BuildRequires:	scons
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
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
Danger from the deep jest darmow± (otwartymi ¼ród³ami) symulacj± 
niemieckiej ³odzi podwodnej z czasów II Wojny ¦wiatowej. 
Gra jest zaplanowana jako taktyczno-symulacyjna i bedzie tak 
realistyczna jak pozowli na to czas twórców i ich wiedza z fizyki.
Aktualny stan jest okre¶lony jako ALPHA, ale jest grywalna.

%prep
%setup -q -c

%build
sed -i 's@-g -O2@%{rpmcflags}@' SConstruct
sed -i 's@/usr/local/share/dangerdeep@%{_datadir}/dangerdeep@' SConstruct
scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_mandir}/man6}

install build/linux/%{name} $RPM_BUILD_ROOT%{_bindir}
install doc/man/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6
cp -r data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*

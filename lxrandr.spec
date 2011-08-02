%define git 0
Summary:	Simple monitor config tool for LXDE
Name:     	lxrandr
Version:	0.1.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel intltool
Requires:	xrandr

%description
This is a very basic monitor config tool utilizing XRandR. It can let you
change the screen resolution on the fly. Besides, when you run lxrandr
with external monitor connected, its GUI will change, and show you some 
quick options to get your projector working correctly.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_mandir}/man1/*.1.*
%{_datadir}/applications/*.desktop

Summary:	Simple monitor config tool for LXDE
Name:     	lxrandr
Version:	0.3.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://wiki.lxde.org/en/LXRandR
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)

Requires:	xrandr

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

LXRandR is the standard screen manager of LXDE. It manages screen resolution
and external monitors. You can plug in another screen into LXDE or choose to
use a big screen projector. Local screen and external screen can be used at
the same time. LXRandR configures the screen solution automatically. 

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


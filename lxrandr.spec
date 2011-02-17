Summary:	Simple monitor config tool for LXDE
Name:     	lxrandr
Version:	0.1.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Patch0:		10_save_configuration.patch
Patch1:		11_gseal_migration.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel
Requires:	xrandr

%description
This is a very basic monitor config tool utilizing XRandR. It can let you
change the screen resolution on the fly. Besides, when you run lxrandr
with external monitor connected, its GUI will change, and show you some 
quick options to get your projector working correctly.

%prep
%setup -q
%patch0 -p1 -b .save_autostart_config
%patch1 -p1 -b .fix_GTK3_build

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post  
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_mandir}/man1/*.1.*
%{_datadir}/applications/*.desktop

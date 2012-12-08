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


%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 693010
- update to 0.1.2

* Wed Jun 01 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.1-6
+ Revision: 682404
- remove unused patch and add new fixes and lang.po from svn

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.1.1-5
+ Revision: 640482
- rebuild to obsolete old packages

* Thu Feb 17 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.1-4
+ Revision: 638308
+ rebuild (emptylog)

* Thu Feb 17 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.1-3
+ Revision: 638284
+ rebuild (emptylog)

* Thu Feb 17 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.1-2
+ Revision: 638273
- add save config to autostart

* Fri Jul 10 2009 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2011.0
+ Revision: 394053
- fix file list
- new version 0.1.1

* Sun Jun 22 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.0
+ Revision: 227910
- import lxrandr


